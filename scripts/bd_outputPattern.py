#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

Release Notes:

V0.1 Initial Release

"""

import traceback

import bd_utils

import lx
import pyModo


# FUNCTIONS -----------------------------------------------

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------

def main():
    save_selection = lx.evalN("query sceneservice selection ? all")

    groups = pyModo.Group_Name_All()
    passes = False

    pyModo.Render_Count_All()

    for group in groups:

        if group == "passes":
            passes = True

    if passes:
        lx.out("Setting up proper Output Pattern: '[<pass>]_[<output>][<LR>].<FFFF>'")
        lx.eval("select.Item Render")
        lx.eval('item.channel outPat "[<pass>]_[<output>][<LR>].<FFFF>"')
    else:
        lx.out("Setting up proper Output Pattern: '[<pass>][<output>][<LR>].<FFFF>'")
        lx.eval("select.Item Render")
        lx.eval('item.channel outPat "[<pass>][<output>][<LR>].<FFFF>"')

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
