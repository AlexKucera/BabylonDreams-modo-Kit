#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""
BabylonDreams-modo-Kit - bd_meshcleanup

Release Notes:

V0.1 Initial Release - 2017-01-26

"""

import lx
import traceback


# FUNCTIONS -----------------------------------------------
# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():

    # See if the user value exists
    if lx.eval("query scriptsysservice userValue.isDefined ? bd_meshcleanup_tolerance") == 0:
        lx.eval('user.defNew bd_meshcleanup_tolerance distance');
        lx.eval('user.def bd_meshcleanup_tolerance username \"merge verts closer than:\"');

    # See if a value has been set yet
    if lx.eval("query scriptsysservice userValue.isSet ? bd_meshcleanup_tolerance") == 0:
        lx.eval('user.value bd_meshcleanup_tolerance 0.001');

    lx.eval('user.value bd_meshcleanup_tolerance')
    bd_meshcleanup_tolerance = lx.eval('user.value bd_meshcleanup_tolerance ?')

    lx.eval("select.polygon add type subdiv 1")
    lx.eval("poly.convert face subdiv false")
    lx.eval("select.polygon add type psubdiv 2")
    lx.eval("poly.convert face psubdiv false")

    for i in range(3):
        lx.eval("vert.merge fixed false %s false true" % bd_meshcleanup_tolerance)
        lx.eval("mesh.cleanup true true true true true true true true true true")
        lx.eval("user.value vnormkit.angle 40.0")
        lx.eval("vertMap.hardenNormals angle")

    lx.eval("select.type item")


# END MAIN PROGRAM -----------------------------------------------

if __name__ == '__main__':
    try:
        main()
    except:
        print traceback.format_exc()
