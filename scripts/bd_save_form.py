#!/usr/bin/env python
# encoding: utf-8
# Check Azure Paths
# Alexander Kucera
# babylondreams.de

"""
Saves the UI Config of the BabylonDreams UI Kit Button.
"""

import sys
import traceback

import lx


__author__ = 'alex'


# MAIN PROGRAM --------------------------------------------
def main():
    lx.out("Saving KIT UI Config…")
    try:
        lx.eval("select.attr {83740604103:sheet} set")
        lx.eval(
            "attr.save /Volumes/ProjectsRaid/x_Pipeline/x_AppPlugins/modo/content/Kits/BabylonDreams-modo-Kit/configs/babylondreams_forms.cfg")
        lx.eval("select.attr {35548411557:sheet} set")
        lx.eval(
            "attr.save /Volumes/ProjectsRaid/x_Pipeline/x_AppPlugins/modo/content/Kits/BabylonDreams-modo-Kit/configs/babylondreams_popup_form.cfg")
        lx.out("Successfully saved KIT UI Config!")
        lx.eval("select.attr {11265178910:sheet} set")
        lx.eval("attr.save /Volumes/ProjectsRaid/x_Pipeline/x_AppPlugins/modo/content/Kits/BabylonDreams-modo-Kit/configs/babylondreams_menubar_form.cfg")
    except:
        lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true')
        lx.out("ERROR Saving KIT UI Config failed with ", sys.exc_info())


# END MAIN PROGRAM -----------------------------------------------

if __name__ == '__main__':
    try:
        main()
    except:
        lx.out(traceback.format_exc())