#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

Release Notes:

"""
import traceback

import lx
import modo


# FUNCTIONS -----------------------------------------------
def createInversion(axis, channelSource, channelTarget, sourceName):

    # Create Math Node
    lx.eval('channelModifier.create "cmMathBasic:div"')
    lx.eval('item.name invert_%s_%s cmMathBasic' % (axis, str.lower(sourceName)))
    inverter = lx.eval('query sceneservice selection ? all')
    lx.eval('channel.value -1.0 channel:{%s:input2}' % inverter)

    # Link Items to Math Node
    lx.eval('channel.link add {%s:pos.%s} {%s:input1}' % (channelSource, str.upper(axis), inverter))
    lx.eval('channel.link add {%s:output} {%s:pos.%s}' % (inverter, channelTarget, str.upper(axis)))

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():
    scene = modo.Scene()

    item = scene.selected

    if len(item) > 2:
        lx.out("Please select only two items. The first one will be linked to the second one.")
    else:
        # Query which axis to mirror
        lx.eval('user.defNew invert_x boolean momentary')
        lx.eval('user.def invert_x username "Invert X"')

        lx.eval('user.defNew invert_y boolean momentary')
        lx.eval('user.def invert_y username "Invert Y"')

        lx.eval('user.defNew invert_z boolean momentary')
        lx.eval('user.def invert_z username "Invert Z"')

        lx.eval("user.value invert_x")
        lx.eval("user.value invert_y")
        lx.eval("user.value invert_z")

        invert_x = lx.eval("user.value invert_x ?")
        invert_y = lx.eval("user.value invert_y ?")
        invert_z = lx.eval("user.value invert_z ?")

        # Get Item Transforms
        channelSource = item[0].position.id
        channelTarget = item[1].position.id
        sourceName = item[0].name

        if invert_x:
            createInversion("x", channelSource, channelTarget, sourceName)
        else:
            item[0].position.x >> item[1].position.x

        if invert_y:
            createInversion("y", channelSource, channelTarget, sourceName)
        else:
            item[0].position.y >> item[1].position.y

        if invert_z:
            createInversion("z", channelSource, channelTarget, sourceName)
        else:
            item[0].position.z >> item[1].position.z


    scene.deselect()


# END MAIN PROGRAM -----------------------------------------------

if __name__ == '__main__':
    try:
        main()
    except:
        lx.out(traceback.format_exc())