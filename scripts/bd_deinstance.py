#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""
BabylonDreams-modo-Kit - bd_deinstance

Release Notes: De-Instances any selected instances no matter the item type

V0.1 Initial Release - 2017-02-21

"""

import modo
import lx
import traceback


# FUNCTIONS -----------------------------------------------
# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():

    scene = modo.Scene()

    i = 0
    items = []
    for item in scene.selected:
        if item.isAnInstance:
            item.itemGraph(graphType='source').disconnectInput(item.itemGraph(graphType='source').forward()[0])
            i += 1
            items.append(item.name)

    print "{0} Instances de-instanced.\n{1}".format(i, items)


# END MAIN PROGRAM -----------------------------------------------

if __name__ == '__main__':
    # Argument parsing is available through the 
    # lx.arg and lx.args methods. lx.arg returns 
    # the raw argument string that was passed into 
    # the script. lx.args parses the argument string 
    # and returns an array of arguments for easier 
    # processing.

    argsAsString = lx.arg()
    argsAsTuple = lx.args()

    try:
        main()
    except:
        print traceback.format_exc()
