#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

Release Notes:

V0.1 Initial Release

"""
import subprocess
import traceback
import platform

import lx

import bd_utils


# FUNCTIONS -----------------------------------------------

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------


def main():
    save_selection = lx.evalN("query sceneservice selection ? all")

    filename = lx.eval("item.channel renderOutput$filename ?")

    osType = platform.system()

    if osType == "Windows":
        path = filename.rsplit("\\", 1)
        return path
    elif osType == "Darwin":
        path = filename.rsplit("/", 1)
        return path
    else:
        lx.out("ERROR no valid OS given for path transform")
        return None

    lx.out("Opening path: " + path[0])

    try:
        subprocess.Popen(['open', path[0]])
    except:
        lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true '
                'open:true')
        lx.out("ERROR Opening Render Output path failed with ", sys.exc_info())

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
