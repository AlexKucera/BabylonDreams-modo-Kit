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
import sys
import lx


# FUNCTIONS -----------------------------------------------

def addmask(id, name, type):
    lx.eval('select.item item:%s set' % id)
    lx.eval('shader.create renderOutput')
    lx.eval('shader.setEffect %s' % type)
    lx.eval('texture.name "%s"' % name)

    _name = lx.eval('texture.name ?')
    plaintype = type.split(".")

    if ' ' in _name:
        _name = "_".join(_name.split())

    _name = _name + "." + plaintype[1]

    lx.eval('texture.name {%s}' % _name)
    lx.eval('item.channel renderOutput$colorspace "nuke-default:linear"')
    lx.eval('item.channel renderOutput$clamp false')

    lx.eval('item.channel renderOutput$filename path')
    lx.eval('item.channel renderOutput$format openexr')

    new = lx.eval('query sceneservice selection ? renderOutput')
    outputs.append(new)


def selectnew():
    for id in outputs:
        name = lx.eval('query sceneservice item.name ? %s' % id)
        lx.out('Selecting %s' % name)
        lx.eval('select.item %s add' % id)


# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():
    global outputs

    outputs = []
    allnames = []
    selection = lx.evalN('query sceneservice selection ? mask')
    try:
        if len(selection) == 0:
            lx.out('No Groups selected!')
        else:
            for id in selection:
                name = lx.eval('query sceneservice mask.name ? %s' % id)
                children = lx.evalN('query sceneservice mask.children ? %s' % id)
                childrenstring = ''.join(children)
                if "renderOutput" in childrenstring:
                    lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                            'title:@macros.layouts@EventLog@ width:600 height:600 '
                            'persistent:true '
                            'open:true')
                    lx.out('"%s" already has one or more RenderOutputs!' % name)
                    allnames.append(name)
                else:
                    lx.out('Adding Alpha output to "%s"' % name)
                    addmask(id, name, "shade.alpha")
                    lx.out('Adding Diffuse Color output to "%s"' % name)
                    addmask(id, name, "mat.diffCol")

            # select new render outputs at the end
            selectnew()
            lx.out('Success!')

            if len(allnames) is not 0:
                lx.out('Some layers already had one or more RenderOutputs:')
                lx.out(allnames)
    except:
        lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true '
                'open:true')
        lx.out("ERROR failed with ", sys.exc_info())


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
