#!/usr/bin/env python
# encoding: utf-8
# Check Azure Paths
# Alexander Kucera
# babylondreams.de

# Description
"""

Checks if the specified Render Output path is valid (exists)
and if not creates the necessary folder structure.

Release Notes:

V0.1 Initial Release

"""

import traceback

import lx
import bd_utils


# FUNCTIONS -----------------------------------------------

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------


def main():
    global save_selection

    lx.trace(True)

    save_selection = lx.evalN("query sceneservice selection ? all")

    renderoutputs = bd_utils.get_ids("renderOutput")

    if renderoutputs:

        for x in renderoutputs:
            lx.eval(r"select.Item %s" % x)
            renderpath = lx.eval("item.channel renderOutput$filename ?")
            if renderpath:
                lx.out(renderpath)
                bd_utils.makes_path(renderpath)

        bd_utils.restoreSelection(save_selection)
    else:
        bd_utils.restoreSelection(save_selection)


# END MAIN PROGRAM -----------------------------------------------

if __name__ == '__main__':
    try:
        main()
    except:
        lx.out(traceback.format_exc())
