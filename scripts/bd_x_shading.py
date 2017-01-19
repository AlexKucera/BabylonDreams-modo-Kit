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
import modo


# FUNCTIONS -----------------------------------------------

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():
    shading_scenes = ["x_shading_for_animation", "x_shading_for_rendering"]
    shading_path = "/Volumes/ProjectsRaid/WorkingProjects/peri/peri-2014_000-sharedspace/work/modo/03_shader/"
    shading_format = ".lxo"
    edit = []
    for scene in shading_scenes:
        edit.append("open~" + scene)

    scene = modo.Scene()

    # Get which shading style the user wants to apply
    lx.eval("user.defNew scene_chooser integer momentary")
    lx.eval('user.def scene_chooser username "Scene Chooser"')
    lx.eval('user.def scene_chooser dialogname "Which shading mode do you want to use?"')
    lx.eval("user.def scene_chooser list {0};{1};{2};{3};{4}".format(shading_scenes[0], shading_scenes[1], "clear", edit[0], edit[1]))
    lx.eval('user.def scene_chooser listnames "Animation;Rendering;Clear Shading;Open Animation shading for editing;Open Render shading for editing"')
    lx.eval("user.value scene_chooser")

    mode = lx.eval("user.value scene_chooser ?")

    if "open~" in mode:
        mode = mode.split("~")[1]
        print mode
        lx.eval("scene.open {0}{1}{2}".format(shading_path, mode, shading_format))

    else:

        # Check if the shading scene is already present in the scene.
        grouplocators = scene.items(itype='groupLocator', superType=True)
        masks = scene.items(itype='mask', superType=True)
        search = list(grouplocators + masks)
        items = []

        for item in search:
            if "x_shading" in item.name:
                items.append(item)

        # If items is not zero we already have a shading setup in the scene and need to delete it first.
        if len(items) != 0:
            print "Found old shading setup. Deleting it first."
            for item in items:
                try:
                    safe_item = modo.Item(item.id)
                    if safe_item:
                        lx.eval("!item.delete item:{%s}" % safe_item.id)
                except:
                    continue
            print "Cleared x_shading out of scene."
            if mode == "clear":
                modo.dialogs.alert(title="Cleaned up", message="Cleared x_shading out of scene.")

        # Now we have a clean slate and can import our new or updated shading setup.

        if mode != "clear":

            lx.eval("scene.open {0}{1}{2} import".format(shading_path, mode, shading_format))

            masks = scene.items(itype='mask', superType=True)
            for mask in masks:
                if "x_shading" in mask.name:
                    item_selection = modo.item.ItemGraph(item=mask, graphType='shadeLoc').forward()
                    modo.item.ItemGraph(item=mask, graphType='shadeLoc').disconnectInput(item_selection[0])
                    mask.name = '%s_%s' % (mask.type, mode)
            print "Imported x_shading."
            modo.dialogs.alert(title="Imported x_shading.", message="Imported {0}".format(mode))

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
