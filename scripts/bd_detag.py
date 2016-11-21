#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

Release Notes:

A script that deletes all Part tags in a scene. Use after a CAD Item has been imported.

V0.1 Initial Release - 2016-11-21

"""

import traceback
import lx



# FUNCTIONS -----------------------------------------------

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():
    lx.out("Clearingall Part tags…")
    lx.eval("select.itemType mesh")
    lx.eval("poly.setPart name")
    lx.eval("poly.renameTag name {} PART")
    lx.out("Cleared all Part tags.")


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

        main()  # call the script with any arguments here.

    except:
        lx.out(traceback.format_exc())