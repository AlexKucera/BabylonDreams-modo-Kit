# python
# encoding: utf-8
# Check Azure Paths
# Alexander Kucera
# babylondreams.de

# Description
"""

Allows paths switching from OS X to Windows for Render Outputs
for the purpose of rendering on Azure or EC2.

Also checks if the specified Render Output path is valid (exists)
and if not creates the necessary folder structure.

Release Notes:

V0.1 Initial Release

"""

import os
import platform
import traceback

import lx

# FUNCTIONS -----------------------------------------------
import sys


def update_render_output(renderoutput):
    """
        Updates the Render Output path to work on Azure or OS X depending on
        the OS we are on.
    """
    try:
        lx.eval(r"select.Item %s" % renderoutput)
        oldpath = lx.eval("item.channel renderOutput$filename ?")

        if oldpath is not None:
            lx.out(renderoutput + " has a set output path: " + oldpath)
            newpath = format_filename(oldpath)
            lx.out("Turned output path it into " + osType + " Path: " + newpath)
            lx.eval(r'item.channel renderOutput$filename "%s"' % newpath)

            # MakePath
            makes_path(newpath)

        elif oldpath is None:
            lx.out(str(renderoutput) + " has no active filename.")

    except:
        lx.out("Command updateRenderOutput failed with ", sys.exc_info())
        return None


def format_filename(s):
    """
    Takes a UNIX path and turns it into a Windows path.
    """
    if osType == "Windows":
        filename = s.replace(unix_path, win_path)
        filename = filename.replace('/', '\\')
        return filename
    elif osType == "Darwin":
        filename = s.replace(win_path, unix_path)
        filename = filename.replace('\\', '/')
        return filename
    else:
        lx.out("ERROR no valid OS given for path transform")
        return None


def makes_path(pathfile):
    """
    Check to make sure destination directory exists.
    If it doesn't create the directory.
    """
    path = os.path.dirname(pathfile)

    try:
        exists = os.path.exists(path)
        if exists:
            lx.out(
                "Tried creating folder \"" + path + "\", but it already exists.")
        else:
            os.makedirs(path)
            lx.out("Created folder: " + str(path))
    except:
        lx.out("ERROR creating path for " + path)


def get_ids(itemtype):
    """
    Get a list of item IDs of type 'type'
    Returns a list of item IDs or None if there are no items of the specified
    type or if there's an error. Error printed is to Event log.
    type - the type of item to be returned (mesh, camera etc)
    """
    try:
        itemlist = []
        numitems = lx.eval('!!query sceneservice ' + itemtype + '.N ?')
        if numitems == 0:
            return None
        else:
            for x in xrange(numitems):
                itemlist.append(
                    lx.eval('query sceneservice ' + itemtype + '.ID ? %s' % x))
            lx.out("Found " + str(numitems) + " " + itemtype + "s: " + ", ".join(
                itemlist))
            return itemlist
    except:
        lx.out("ERROR get_ids")
        return None


# END FUNCTIONS -----------------------------------------------

# TODO Split into three different scripts Switch Paths, Check Paths and Base Functions
# TODO Split into Switch Paths
# TODO Split Check Paths
# TODO Split Base Functions

# MAIN PROGRAM --------------------------------------------
def main(justcreate):
    global osType
    global unix_path
    global win_path

    lx.trace(False)

    osType = platform.system()
    lx.out("TYPE OS: " + osType)

    unix_path = "/Volumes/ProjectsRaid/WorkingProjects"
    win_path = "E:\AzureSync\CloudComputing\WorkingProjects"

    renderoutputs = get_ids("renderOutput")

    if renderoutputs:

        if justcreate == "switch":
            for x in renderoutputs:
                update_render_output(x)
        else:
            for x in renderoutputs:
                lx.eval(r"select.Item %s" % x)
                renderpath = lx.eval("item.channel renderOutput$filename ?")
                if renderpath:
                    lx.out(renderpath)
                    makes_path(renderpath)


# END MAIN PROGRAM -----------------------------------------------

if __name__ == '__main__':
    try:
        args = lx.args()
        if args:
            justCreate = args[0]
            main(justCreate)
        else:
            main(None)
    except:
        lx.out(traceback.format_exc())
