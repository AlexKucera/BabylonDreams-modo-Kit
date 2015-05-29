#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

Release Notes:

Enables or disables all plugins for debug purposes. Bind to a button with
"@bd_toggle_plugins.py enable" or "@bd_toggle_plugins.py disable".

Edit the exclude list for plugins you want to keep enabled/disabled (meaning keep the
state it is in when the script triggers).

Requires http://www.crummy.com/software/BeautifulSoup/

V0.1 Initial Release
V0.2 Added some smarts that finds the kits automatically. No more typing long lists.

"""
import fnmatch
import traceback
import os
from bs4 import BeautifulSoup
import lx

exclude = ['XSR', 'babylondreams', 'mecco_snap', 'lux_ffmpeg_export']

kits = []

# Grab all kits based on modo's environment
importpaths = lx.eval("query platformservice importpaths ?")
for paths in importpaths:
    for path, dirs, files in os.walk(paths):
        for filename in fnmatch.filter(files, "index.cfg"):
            config = os.path.join(path, filename)
            soup = BeautifulSoup(open(config))
            tag = soup.configuration['kit']
            kits.append(str(tag))

lx.out("Installed Kits:")
for kit in kits:
    lx.out(kit)

kits = [f for f in kits if f not in exclude]

lx.out("Excluded Kits:" + str(exclude) + "\nThese kits will not be toggled by the "
                                         "plugin.")



# FUNCTIONS -----------------------------------------------

def locate(pattern, root=os.curdir):
    """Locate all files matching supplied filename pattern in and below supplied root
    directory."""
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, pattern):
            return os.path.join(path, filename)


# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main(switch):
    if switch == "disable":
        lx.out("Disabling all Plugins")
        for kit in kits:
            if lx.eval("kit.toggleEnable " + kit + " ?"):
                lx.eval("kit.toggleEnable " + kit)
    elif switch == "enable":
        lx.out("Enabling all Plugins")
        for kit in kits:
            if not lx.eval("kit.toggleEnable " + kit + " ?"):
                lx.eval("kit.toggleEnable " + kit)
    elif switch == "debug":
        lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true '
                'open:true')
        lx.out("debug mode")
        pass

    else:
        lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true '
                'open:true')
        lx.out("Please provide either enable or disable as argument")


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

        main(argsAsString)

    except:
        lx.out(traceback.format_exc())
