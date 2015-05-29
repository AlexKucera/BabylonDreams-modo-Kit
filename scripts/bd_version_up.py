#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

Incremental Save, the BabylonDreams way. Not like modo's shoddy incremental save.

Release Notes:

V0.1 Initial Release

"""

import traceback
import sys
import os

import lx

import bd_utils


# FUNCTIONS -----------------------------------------------

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():

    save_selection = lx.evalN("query sceneservice selection ? all")

    filepath = bd_utils.filePath()
    filename = os.path.splitext(bd_utils.fileName())
    fileextension = filename[1]

    filename = filename[0]
    filename = filename.rsplit("_", 1)
    version = filename[1]
    filename = filename[0]
    lx.out('Current file "' + filename + '" is at Version ' + version + '.')

    version = version.lstrip("_v")

    created = False

    while created is False:
        version = str(int(version) + 1).zfill(2)
        newfile = filepath + "/" + filename + "_v" + version + fileextension
        if os.path.isfile(newfile):
            lx.out("Version " + version + " already exists. Increasing version count.")
            pass
        else:
            lx.out("Saving as Version " + version)
            try:
                lx.eval('scene.saveAs {%s}' % newfile)
            except:
                lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                        'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true '
                        'open:true')
                lx.out("ERROR Scene save failed with ", sys.exc_info())

            created = True

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
