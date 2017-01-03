#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

Collapses a camera hierarchy down to a single camera item for export/baking.

Release Notes:

V0.1 Initial Release

"""
import os
import traceback
import lx
import modo
import bd_utils


# FUNCTIONS -----------------------------------------------
# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():

    scene = modo.Scene()

    item = scene.selected

    if len(item) > 1:

        print "Please select only one item."

    elif len(item) == 0:

        print "Please select at least one camera."

    elif item[0].type != "camera":

        print "Please select a camera."

    else:

        cam = item[0]
        bake_cam_name = os.path.splitext(scene.name)[0] + "_bakeCam"
        bake_cam = scene.addCamera(name=bake_cam_name)

        # Parent to animated camera
        scene.select(bake_cam)
        scene.select(cam, add=True)
        lx.eval("constraintTransform type:pos")

        scene.select(bake_cam)
        scene.select(cam, add=True)
        lx.eval("constraintTransform type:rot")

        # Link relevant channels
        cam.channel("focalLen") >> bake_cam.channel("focalLen")
        cam.channel("apertureX") >> bake_cam.channel("apertureX")
        cam.channel("apertureY") >> bake_cam.channel("apertureY")
        cam.channel("offsetX") >> bake_cam.channel("offsetX")
        cam.channel("offsetY") >> bake_cam.channel("offsetY")
        cam.channel("focusDist") >> bake_cam.channel("focusDist")
        cam.channel("fStop") >> bake_cam.channel("fStop")

        scene.select(bake_cam)
        lx.eval("?item.bake 0")


        lx.eval("select.drop channel")
        lx.eval("select.channel {{{0}:focalLen}} add".format(bake_cam.id))
        lx.eval("select.channel {{{0}:apertureX}} add".format(bake_cam.id))
        lx.eval("select.channel {{{0}:apertureY}} add".format(bake_cam.id))
        lx.eval("select.channel {{{0}:offsetX}} add".format(bake_cam.id))
        lx.eval("select.channel {{{0}:offsetY}} add".format(bake_cam.id))
        lx.eval("select.channel {{{0}:focusDist}} add".format(bake_cam.id))
        lx.eval("select.channel {{{0}:fStop}} add".format(bake_cam.id))
        lx.eval("?channel.bake 0")

        lx.eval("item.selectChannels anim")
        lx.eval("channel.keyReduce")

        scene.select(bake_cam)

        export_format = bd_utils.queryDialog(listvalues=["Alembic", "FBX"], listnames=["Alembic", "FBX"], query="Choose Export Format", title="Export Format")
        if export_format == "Alembic":
            lx.eval("export.selected 3 false false true")
        elif export_format == "FBX":
            lx.eval("export.selected 11 false false true")
        else:
            print "Invalid Export Format"

        scene.removeItems(bake_cam)



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
