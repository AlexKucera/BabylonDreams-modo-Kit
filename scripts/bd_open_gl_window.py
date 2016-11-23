#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

Allows opening an OpenGL window of defined dimensions for size accurate OpenGL Previews.

Release Notes:

V0.1 Initial Release - 2016-11-23

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

    lx.eval("user.defNew gl_viewport_size integer momentary")
    lx.eval('user.def gl_viewport_size username "Open New GL View"')
    lx.eval('user.def gl_viewport_size dialogname "Which resolution do you need to open?"')
    lx.eval("user.def gl_viewport_size list Full;Half;Quarter;Tenth")
    lx.eval("user.value gl_viewport_size")

    mode = lx.eval("user.value gl_viewport_size ?")
    lx.out(mode)

    if mode == "Full":
        percent = 1.0
    elif mode == "Half":
        percent = 0.5
    elif mode == "Quarter":
        percent = 0.25
    elif mode == "Tenth":
        percent = 0.1
    else:
        percent = 1

    lx.out(percent)

    # Get selection
    save_selection = lx.evalN("query sceneservice selection ? all")

    # Get Render Resolution
    lx.eval("select.item Render")
    resX = float(lx.eval("item.channel resX ?"))
    resY = float(lx.eval("item.channel resY ?"))

    newResX = int(resX * percent)
    newResY = int(resY * percent)

    # Restore selection
    restoreSelection(save_selection)

    # Option to switch back to original resolution

    open_window = "layout.create Camera width:{0} height:{1} " \
                  "persistent:false style:palette layout:\"BlankCamera Palette\"".format(str(newResX), str(newResY))

    lx.out(open_window)
    lx.eval(open_window)


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
