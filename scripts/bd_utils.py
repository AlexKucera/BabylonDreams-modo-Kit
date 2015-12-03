#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

General modo utilities library.

Release Notes:

V0.1 Initial Release

"""

import os
import sys
from bs4 import BeautifulSoup
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
            try:
                os.makedirs(path)
                lx.out("Created folder: " + str(path))
            except OSError:
                if not os.path.isdir(path):
                    raise

    except:
        lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true '
                'open:true')
        lx.out("ERROR creating path for " + path, sys.exc_info())


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
        lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true '
                'open:true')
        lx.out("ERROR get_ids(" + itemtype + ") failed with ", sys.exc_info())
        return None


def fileName():
    return lx.eval('query sceneservice scene.name ? current')


def filePath():
    filePath = lx.eval('query sceneservice scene.file ? current')

    if filePath:
        return os.path.dirname(filePath)
    else:
        return False


def pathAliases():
    """
    Returns all PathAliases as dictionary pair.

    """

    lx.eval("config.save")

    config = lx.eval("query platformservice path.path ? configname")
    soup = BeautifulSoup(open(config))
    config_pathaliases = soup.find(type='PathAliases')
    config_pathaliases = config_pathaliases.find_all(type='Alias')

    pathaliases = {}

    for alias in config_pathaliases:
        alias_alias = alias['key']
        for string in alias.atom.strings:
            alias_path = string

        pathaliases[alias_alias] = alias_path

    return pathaliases

# END FUNCTIONS -----------------------------------------------
