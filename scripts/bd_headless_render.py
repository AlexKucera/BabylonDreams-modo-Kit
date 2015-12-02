#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

Release Notes:

Grabs the first and last frame from the Render item, then writes out a basic modo
render batch into the projects TMP directory. Afterwards it will open a terminal
window and copy the required command into the systems clipboard.


V0.1 Initial Release - 2015-05-19
V0.2 2015-08-15: Added the ability to time the execution and mail a summary to an email address.
                Requires http://caspian.dotconf.net/menu/Software/SendEmail/
                Also requires a config file and the setup of the global variable
                "mail_config_path" right after the import statements.

                The config file has the following syntax:
                TO_ADDRESS="mail@server.com"
                FROM_ADDRESS="mail@server.com"
                SERVER="mail.server.com:port"
                USER="mail@server.com"
                PASS="password"

"""
from itertools import izip_longest
import os
import re
import subprocess
import traceback
import bd_utils
import lx
import pyperclip

mail_config_path = "/Volumes/ProjectsRaid/x_Pipeline/Scripting/tinkertoys/bash/mail_send.conf"


# FUNCTIONS -----------------------------------------------

def grouper(iterable, n, fillvalue=''):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
import pyModo


def main(batchsize=None):
    lx.out("Headless Rendering Triggered")

    headless_path = lx.eval("query platformservice path.path ? headless") + "_cl"
    lx.eval("select.Item Render")
    first_frame = str(lx.eval("item.channel first ?"))
    last_frame = str(lx.eval("item.channel last ?"))
    frame_step = str(lx.eval("item.channel step ?"))

    save_selection = lx.evalN("query sceneservice selection ? all")

    filepath = bd_utils.filePath()
    filename = bd_utils.fileName().split(".")
    filename = filename[0]
    fullpath = lx.eval('query sceneservice scene.file ? current')

    groups = pyModo.Group_Name_All()
    passes = False

    pyModo.Render_Count_All()

    for group in groups:

        if group == "passes":
            passes = True

    if passes:
        rendercmd = "render.animation {*} group:passes"
    else:
        rendercmd = "render.animation {*}"

    if filepath is False:
        lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true '
                'open:true')
        lx.out("ERROR Please save scene first.")
    else:
        wd_regex = re.compile("/Volumes/ProjectsRaid/WorkingProjects/[^/]*/[^/]*/")
        workingdirectory = wd_regex.match(filepath).group()

        batchdir = workingdirectory + "work/modo/05_render/_batch/"
        bd_utils.makes_path(batchdir)

        if batchsize:

            shellfile = batchdir + filename + "_batchrender.sh"
            s = open(shellfile, 'w')
            s.write("""#!/usr/bin/env bash

source """ + mail_config_path + """
SUBJECT="modo render completed"
MACHINE=$(hostname -s)


START=$(date +%s)
STARTDATE=$(date -j -f "%s" "`date +%s`" "+%A, %d.%m.%Y %T")

""")

            filesdir = workingdirectory + "work/modo/05_render/_batch/" + filename + "/"
            bd_utils.makes_path(filesdir)

            framelist = range(int(first_frame), int(last_frame) + 1, int(frame_step))
            framelist = chunker(framelist, batchsize)

            for framegroup in framelist:
                first_frame = str(min(int(minframe) for minframe in framegroup))
                last_frame = str(max(int(maxframe) for maxframe in framegroup))

                batchfile = filesdir + filename + \
                    "_batchrender_frames_" + first_frame + "-" + last_frame \
                    + ".txt"
                lx.out("Saving renderbatch at: " + batchfile)

                template = """log.toConsole true
log.toConsoleRolling true
scene.open """ + fullpath + """
pref.value render.threads auto
select.Item Render
item.channel step """ + frame_step + """
item.channel first """ + first_frame + """
item.channel last """ + last_frame + """
""" + rendercmd + """
scene.close
app.quit
"""
                f = open(batchfile, 'w')
                f.write(template)
                f.close()

                s.write(headless_path + " < " + batchfile + "\n")

            s.write("""
END=$(date +%s)
ENDDATE=$(date -j -f "%s" "`date +%s`" "+%A, %d.%m.%Y %T")
secs=$((END-START))
DURATION=$(printf '%dh:%02dm:%02ds' $(($secs/3600)) $(($secs%3600/60)) $(($secs%60)))

BODY="${MACHINE} just finished rendering """ + filename + """.
It started at ${STARTDATE}"""
 + """ and ended at ${ENDDATE} taking ${DURATION} overall."

sendemail -f ${FROM_ADDRESS} -t ${TO_ADDRESS} -m ${BODY} -u ${SUBJECT} -s ${SERVER} -xu ${USER} -xp ${PASS}""")
            s.close()
            os.chmod(shellfile, 0755)

            pyperclip.copy(shellfile)
            subprocess.Popen(['open', '-a', '/Applications/Utilities/Terminal.app', '-n'])

        else:

            batchfile = batchdir + filename + \
                    "_batchrender_frames_" + first_frame + "-" + last_frame \
                    + ".txt"
            lx.out("Saving renderbatch at: " + batchfile)

            template = """log.toConsole true
log.toConsoleRolling true
scene.open """ + fullpath + """
pref.value render.threads auto
select.Item Render
item.channel step """ + frame_step + """
item.channel first """ + first_frame + """
item.channel last """ + last_frame + """
""" + rendercmd + """
scene.close
app.quit
"""
            f = open(batchfile, 'w')
            f.write(template)
            f.close()

            renderbatch = " < " + batchfile

            # Broken at the moment. I'm resorting to simply opening a Terminal window and
            # copying the necessary command to the clipboard

            # subprocess.Popen(['open', '-a', '/Applications/Utilities/Terminal.app', '-n',
            # '--args', headless_path, '<', batchfile])

            pyperclip.copy(headless_path + " < " + batchfile)
            subprocess.Popen(['open', '-a', '/Applications/Utilities/Terminal.app', '-n'])

    bd_utils.restoreSelection(save_selection)

# END MAIN PROGRAM -----------------------------------------------

if __name__ == '__main__':
    try:
        # Argument parsing is available through the 
        # lx.arg and lx.args methods. lx.arg returns 
        # the raw argument string that was passed into 
        # the script. lx.args parses the argument string 
        # and returns an array of arguments for easier 
        # processing.

        argsAsString = lx.arg()
        argsAsTuple = lx.args()

        if not argsAsString:
            main()
        else:
            main(int(argsAsString))

    except:
        lx.out(traceback.format_exc())
