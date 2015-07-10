#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

Sets up the correct render path in relation to the BabylonDreams project structure and
automatically labels the renderOutput correctly in relation to the scene name.

Also creates the necessary folder structure.

Release Notes:

V0.1 Initial Release

"""

import traceback
import re
import os

import lx

import bd_utils
import bd_outputPattern


# FUNCTIONS -----------------------------------------------

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():

    save_selection = lx.evalN("query sceneservice selection ? all")

    filepath = bd_utils.filePath()
    if filepath is False:
        lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true '
                'open:true')
        lx.out("ERROR Please save scene first.")
    else:
        filename = os.path.splitext(bd_utils.fileName())
        fileextension = filename[1]

        filename = filename[0]
        filename = filename.rsplit("_", 1)
        version = str.lower(filename[1])
        filename = str.lower(filename[0])
        lx.out('File "' + filename + '" is at Version ' + version + '.')

        wd_regex = re.compile("/Volumes/ProjectsRaid/WorkingProjects/[^/]*/[^/]*/")
        workingdirectory = wd_regex.match(filepath).group()
        lx.out("Project is located at: " + workingdirectory)

        turntable = ""
        turntable_regex = re.compile("turntable")
        if turntable_regex.search(filepath) or turntable_regex.search(filename) is not \
                None:
            turntable = "turntables/"

        # renderpath = workingdirectory + "img/cg/" + turntable + filename + "/" + filename + "_" + version + "/"

        renderpath = workingdirectory + "img/cg/" + filename + "/" + \
                     filename + "_" + version + "/"
        lx.out("The renders will be located at: " + renderpath)

        renderoutputs = bd_utils.get_ids("renderOutput")

        if renderoutputs:

            bd_utils.makes_path(renderpath)

            for x in renderoutputs:

                lx.eval("select.Item \"%s\"" % x)
                filepath = lx.eval("item.channel renderOutput$filename ?")
                enabled = lx.eval("shader.setVisible \"%s\" ?" % x)

                if filepath is not None and enabled:

                    fileformat = lx.eval("item.channel renderOutput$format ?")

                    if fileformat is None or "$FLEX":
                        fileformat = "openexr"

                    if x == "rgba":
                        renderpasspath = renderpath
                    else:
                        renderpasspath = renderpath + x + "/"

                    renderoutputpath = renderpasspath + filename + "_" + version + "_"
                    lx.out("RenderOutput " + x + " will be located at: " +
                           renderpasspath)
                    bd_utils.makes_path(renderpasspath)
                    lx.out("Setting Render Output path to: " + renderoutputpath)
                    lx.eval("item.channel renderOutput$filename " + renderoutputpath)
                    lx.out("Setting Render Output format to: " + fileformat)
                    lx.eval("item.channel renderOutput$format " + fileformat)

                else:
                    
                    lx.out("Skipping %s as it is either disabled or has no \"PATH\" "
                           "filled in" % x)

        bd_outputPattern.main()

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
