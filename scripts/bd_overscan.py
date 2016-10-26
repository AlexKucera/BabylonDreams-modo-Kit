#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

Allows setting up overscan rendering with either a known output resolution or a known
scaling factor and set up the frame format and film back of the render camera accordingly.

Release Notes:

V0.1 Initial Release

"""

import traceback
import sys
import lx


# FUNCTIONS -----------------------------------------------


def restoreSelection(listSelections):
    """
    Used together with:

    global save_selection
    save_selection = lx.evalN("query sceneservice selection ? all")

    to save and later restore a selection in modo with

    bd_utils.restoreSelection(save_selection)

    """

    try:
        # lx.out(listSelections)
        first = True
        for x in listSelections:
            lx.out("Restoring Selection: " + x)
            if first:
                lx.eval("select.item {%s} set" % x)
            else:
                lx.eval("select.item {%s} add" % x)
            first = False

    except:
        lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true '
                'open:true')
        lx.out("ERROR restoreSelection failed with ", sys.exc_info())
        return None

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------


def main():
    lx.eval("user.defNew overscan_mode integer momentary")
    lx.eval('user.def overscan_mode username "Overscan Mode"')
    lx.eval('user.def overscan_mode dialogname "Which overscan mode do you want to use?"')
    lx.eval("user.def overscan_mode list resolution;scaling")
    lx.eval("user.value overscan_mode")

    mode = lx.eval("user.value overscan_mode ?")
    lx.out(mode)

    # Get selection
    save_selection = lx.evalN("query sceneservice selection ? all")

    # Get Render Camera
    render_camera = lx.eval("render.camera ?")
    lx.eval("select.item {%s} set" % render_camera)

    # Get Film Back
    apertureX = lx.eval("item.channel apertureX ?")
    apertureY = lx.eval("item.channel apertureY ?")

    # Get Render Resolution
    lx.eval("select.item Render")
    resX = float(lx.eval("item.channel resX ?"))
    resY = float(lx.eval("item.channel resY ?"))

    if mode == "resolution":

        # Ask for new resolution
        lx.eval("user.defNew newRes.X integer momentary")
        lx.eval("user.value newRes.X")
        newResX = lx.eval("user.value newRes.X ?")

        lx.eval("user.defNew newRes.Y integer momentary")
        lx.eval("user.value newRes.Y")
        newResY = lx.eval("user.value newRes.Y ?")

    elif mode == "scaling":

        # Ask for scaling factor
        lx.eval("user.defNew newRes.scaling float momentary")
        lx.eval("user.value newRes.scaling")
        newResScaling = lx.eval("user.value newRes.scaling ?")
        newResX = resX * newResScaling
        newResY = resY * newResScaling

    # Apply Overscan formula to width and height
    newApertureX = apertureX * (newResX / resX)
    newApertureY = apertureY * (newResY / resY)

    # Fill in new render resolution
    lx.eval("render.res 0 %s" % newResX)
    lx.eval("render.res 1 %s" % newResY)

    # Fill in new film back
    lx.eval("select.item {%s} set" % render_camera)
    lx.eval("item.channel apertureX %s" % newApertureX)
    lx.eval("item.channel apertureY %s" % newApertureY)

    # Restore selection
    restoreSelection(save_selection)

    # Option to switch back to original resolution


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
