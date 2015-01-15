#!/usr/bin/env python
# encoding: utf-8
# Check Azure Paths
# Alexander Kucera
# babylondreams.de

# Description
"""

Allows paths switching from OS X to Windows for Render Outputs
for the purpose of rendering on Azure or EC2.

Also checks if the specified Render Output path is valid (exists)
and if not creates the necessary folder structure.

Release Notes:

V0.1 Initial Release

"""

import platform
import traceback

import lx
import sys
import bd_utils

# FUNCTIONS -----------------------------------------------


def update_render_output(renderoutput):
    """
        Updates the Render Output path to work on Azure or OS X depending on
        the OS we are on.
    """
    try:
        lx.eval(r"select.Item %s" % renderoutput)
        oldpath = lx.eval("item.channel renderOutput$filename ?")

        if oldpath is not None:
            lx.out(renderoutput + " has a set output path: " + oldpath)
            newpath = format_filename(oldpath)
            lx.out("Turned output path it into " + osType + " Path: " + newpath)
            if oldpath is not newpath:
                lx.eval(r'item.channel renderOutput$filename "%s"' % newpath)

                # MakePath
                bd_utils.makes_path(newpath)
            else:
                lx.out("Old and new path are identical. No change necessary.")

        elif oldpath is None:
            lx.out(str(renderoutput) + " has no active filename. Not touching anything.")

    except:
        bd_utils.restoreSelection(save_selection)
        lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true')
        lx.out("ERROR Command updateRenderOutput failed with ", sys.exc_info())
        return None


def format_filename(s):
    """
    Takes a UNIX path and turns it into a Windows path.
    """
    if osType == "Windows":
        filename = s.replace(unix_path, win_path)
        filename = filename.replace('/', '\\')
        return filename
    elif osType == "Darwin":
        filename = s.replace(win_path, unix_path)
        filename = filename.replace('\\', '/')
        return filename
    else:
        lx.out("ERROR no valid OS given for path transform")
        return None


# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():
    global osType
    global unix_path
    global win_path
    global save_selection

    lx.trace(False)

    osType = platform.system()
    lx.out("TYPE OS: " + osType)

    unix_path = "/Volumes/ProjectsRaid/WorkingProjects"
    win_path = "E:\AzureSync\CloudComputing\WorkingProjects"

    save_selection = lx.evalN("query sceneservice selection ? all")

    renderoutputs = bd_utils.get_ids("renderOutput")

    if renderoutputs:
        for x in renderoutputs:
            update_render_output(x)

        bd_utils.restoreSelection(save_selection)
    else:
        bd_utils.restoreSelection(save_selection)


# END MAIN PROGRAM -----------------------------------------------

if __name__ == '__main__':
    try:
        main()
    except:
        lx.out(traceback.format_exc())
