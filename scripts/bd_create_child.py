#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""
BabylonDreams-modo-Kit - bd_create_child

Release Notes:

V0.1 Initial Release - 2017-01-23

"""

import modo
import lx
import traceback
import pyperclip

# FUNCTIONS -----------------------------------------------
# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():

    scene = modo.Scene()
    stored_selection = item = scene.selected

    # Grab last selected item and normalize output

    if len(item) > 1:

        item = item[-1]

    elif len(item) == 0:

        item = scene.sceneItem

    else:

        item = item[0]

    pyperclip.copy(item.name)

    lx.eval("user.defNew name string momentary")
    lx.eval("user.value name")

    name = lx.eval("user.value name ?")

    locator = scene.addItem("locator", name)

    locator.setParent(item, -1)

    scene.select(stored_selection)




# END MAIN PROGRAM -----------------------------------------------

if __name__ == '__main__':
    try:
        main()
    except:
        print traceback.format_exc()
