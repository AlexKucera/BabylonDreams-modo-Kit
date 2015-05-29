#!/usr/bin/env python
# encoding: utf-8
# Import x_shading
# Alexander Kucera
# babylondreams.de

# Description
"""

One click import of x_shading and setting of the Shader Mask to "all".

Release Notes:

V0.1 Initial Release

"""

import traceback

import lx

# FUNCTIONS -----------------------------------------------


# END FUNCTIONS -----------------------------------------------


# MAIN PROGRAM --------------------------------------------
def main():
    try:
        # lx.trace(True)
        lx.eval('scene.open /Volumes/ProjectsRaid/WorkingProjects/peri/peri-2014_000-sharedspace/work/modo/03_shader/x_shading_new.lxo import')
        n = lx.eval('query sceneservice mask.N ? all')
        for i in range(n):
            name = lx.eval("query sceneservice mask.name ? %s" % i)
            if name == "x_shading_new (Item)":
                maskid = lx.eval("query sceneservice mask.id ? %s" % i)
                lx.eval("select.Item %s" % maskid)
                lx.eval("mask.setMesh (all)")

    except:
        lx.out(traceback.format_exc())


# END MAIN PROGRAM -----------------------------------------------

if __name__ == '__main__':
    try:
        args = lx.args()
        main()
    except:
        lx.out(traceback.format_exc())
