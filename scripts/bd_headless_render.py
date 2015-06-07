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

"""
import os
import re
import subprocess
import traceback
import bd_utils
import lx
import pyperclip


# FUNCTIONS -----------------------------------------------

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
import pyModo


def main():
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

        batchfile = workingdirectory + "tmp/" + filename + \
                    "_batchrender_frames_" + first_frame + "-" + last_frame \
                    +".txt"
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

        main()

    except:
        lx.out(traceback.format_exc())