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
    lx.eval('select.Item x_shading_new')
    lx.eval('!item.delete')
    lx.eval('select.Item Group set textureLayer')
    lx.eval('!item.delete')
    lx.eval('scene.open /Volumes/ProjectsRaid/WorkingProjects/peri/peri-2014_000-sharedspace/work/modo/03_shader/x_shading_new.lxo import')
    n = lx.eval('query sceneservice mask.N ? all')
    for i in range(n):
        name = lx.eval("query sceneservice mask.name ? %s" % i)
        if name == "x_shading_new (Item)":
            maskid = lx.eval("query sceneservice mask.id ? %s" % i)
            lx.eval("select.Item %s" % maskid)
            lx.eval("mask.setMesh (all)")


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
