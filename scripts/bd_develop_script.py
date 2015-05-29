#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

Release Notes:

A simple wrapper that allows me to bind one button in the modo UI to.
With this setup I don't have to build a UI for a script I am still developing or playing
around with.

Simply import the script that is being currently developed and call it at the very
bottom (line 49)

V0.1 Initial Release - 2015-05-19

"""

import traceback
import lx
import bd_headless_render  # Import the script here


# FUNCTIONS -----------------------------------------------

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():
    pass

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

        bd_headless_render.main()  # call the script with any arguments here.

    except:
        lx.out(traceback.format_exc())
