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


# FUNCTIONS -----------------------------------------------

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():
    alphas = []
    ids = bd_utils.get_ids('renderOutput')
    for id in ids:
        lx.eval('select.item item:%s set' % id)
        type = lx.eval('shader.setEffect ?')

        if type == "shade.alpha":
            alphas.append(id)
            lx.out(type)

    lx.eval('select.drop item')

    for alpha in alphas:
        name = lx.eval('query sceneservice item.name ? %s' % alpha)
        lx.out('Selecting %s' % name)
        lx.eval('select.item %s add' % alpha)



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
