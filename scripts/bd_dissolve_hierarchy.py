#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""
babylondreams - bd_dissolve_group

Release Notes:

V0.1 Initial Release - 2017-02-20

"""

import modo
import lx
import traceback



# FUNCTIONS -----------------------------------------------

def get_selected(num=1):
    """

    Returns: A list of last N selected items. If the minimum number of selected items is not selected a warning dialog pops up.

    """
    scene = modo.Scene()
    selected = scene.selected

    if len(selected) < num:

        if num == 1:
            filler = "item"
        else:
            filler = "items"

        modo.dialogs.alert("Warning", "Please select at least one {0}.".format(filler), dtype='warning')

    if len(selected) > num:
        selected = selected[-num:]

    return selected

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():
    scene = modo.Scene()

    # Initialize Variables
    index = 10000000000000000000000  # Set the index to something very high so we can find the lowest index
    firstFrame = scene.renderItem.channel('first').get() / scene.fps
    chan_set_name = 'blend_channel_set'

    # Find the topmost spot below the renderOutputs
    for item in scene.renderItem.children():
        if item.type == "renderOutput":
            if index > item.parentIndex:
                index = item.parentIndex

    parentIndex = index

    # Check if we have anything selected, if so, generate the "blend_" name
    selected = get_selected(1)
    blend_name = 'blend_{0}'.format(selected[0].name)

    # Generate the complete hierarchy from the parent down and add it to a group
    hierarchy = [selected[0]]

    for item in selected[0].children(recursive=True):
        hierarchy.append(item)

    blend_group = scene.addGroup(name='{0}_grp'.format(blend_name))
    blend_group.addItems(hierarchy)

    # Create a shading group, a shader and a constant
    mask = scene.addItem('mask', name='{0}_msk'.format(blend_name))
    shader = scene.addItem('defaultShader', name='{0}_shdr'.format(blend_name))
    constant = scene.addItem('constant', name='{0}_cnstnt'.format(blend_name))

    # Parent everything to the shading group
    shader.setParent(mask)
    constant.setParent(mask, index=0)
    mask.setParent(scene.renderItem, index=parentIndex)

    # Set the correct Shading Effect
    constant.channel('effect').set('tranAmount')
    constant.channel('value').set(0.0)  # , time=firstFrame, key=True)

    # Adjust the Item dropdown in the shading group
    # (yes, it is reverse, we are actually setting the input of the group to be the shading group)
    blend_group.itemGraph('shadeLoc').connectInput(mask)

    # Check if the Channel Set exist if not create it and add our new blend channel to it
    chan_set = False
    for group in scene.getGroups(gtype='chanset'):

        if group.name == chan_set_name:
            chan_set = True

    if not chan_set:
        chan_set = scene.addGroup(name=chan_set_name, gtype='chanset')
    else:
        chan_set = scene.item(chan_set_name)

    chan_set.addChannel('value', constant)


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
