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

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():
    scene = modo.Scene()

    item = scene.selected

    if len(item) > 2:
        lx.out("Please select only two items. The first one will be linked to the second one.")
    else:

        #lx.eval('user.defNew mirror_x integer')
        #lx.eval('user.def onOff list "on;off"')

        #mode = lx.eval("user.value overscan_mode ?")
        #lx.out(mode)

        # Get Item Transforms
        channelSource = item[0].position.id
        channelTarget = item[1].position.id

        # Create Math Node
        lx.eval('channelModifier.create "cmMathBasic:div"')
        lx.eval('item.name invert cmMathBasic')
        inverter = lx.eval('query sceneservice selection ? all')
        lx.eval('channel.value -1.0 channel:{%s:input2}' % inverter)

        # Link Items to Math Node
        lx.eval('channel.link add {%s:pos.Z} {%s:input1}' % (channelSource, inverter))
        lx.eval('channel.link add {%s:output} {%s:pos.Z}' % (inverter, channelTarget))

        item[0].position.x >> item[1].position.x
        item[0].position.y >> item[1].position.y

    scene.deselect()



# END MAIN PROGRAM -----------------------------------------------

if __name__ == '__main__':
    try:
        main()
    except:
        lx.out(traceback.format_exc())