#!/usr/bin/env python
# encoding: utf-8
# Check Azure Paths
# Alexander Kucera
# babylondreams.de

"""
Saves the modo config, but keeps the config file locked
to avoid accidental changes or corruption.
"""

import os
import traceback
import sys

import lx
import shutil


__author__ = 'alex'

# Functions -----------------------------------------------


def saveLock():
    configpath = lx.eval("query platformservice path.path ? configname")
    if os.path.isfile(configpath):
        lx.out("Found Config at: " + configpath)
        lx.out("Unlocking Config…")
        errorcode = os.system("chflags nouchg " + configpath)
        chmoderror = os.system("chmod 644 " + configpath)
        if errorcode == 0 and chmoderror == 0:
            lx.out("Saving Config…")
            try:
                lx.eval("config.save")
            except:
                lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                        'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true '
                        'open:true')
                lx.out("ERROR Saving config failed with ", sys.exc_info())

            lx.out("Locking Config…")
            chmoderror = os.system("chmod 444 " + configpath)
            errorcode = os.system("chflags uchg " + configpath)
            if errorcode != 0 and chmoderror != 0:
                lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                        'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true')
                lx.out("ERROR Locking failed with Error Codes: CHFLAGS(" + errorcode +
                       ") and CHMOD(" + chmoderror + ")")
            else:
                lx.out("Successfully saved Config!")
        else:
            lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                    'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true')
            lx.out("ERROR Unlocking failed with Error Code: CHFLAGS(" + errorcode +
                   ") and CHMOD(" + chmoderror + ")")
    else:
        lx.out("Config not found")


def saveCopy():
    configpath = lx.eval("query platformservice path.path ? configname")
    if os.path.isfile(configpath):
        lx.out("Found Config at: " + configpath)
        lx.out("Saving Config…")
        try:
            lx.eval("config.save")
            lx.out("Successfully saved Config!")
        except:
            lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                    'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true '
                    'open:true')
            lx.out("ERROR Saving config failed with ", sys.exc_info())

        lx.out("Copying Config…")
        try:
            shutil.copy2(configpath, configpath + "_backup")
        except:
            lx.eval('layout.createOrClose EventLog "Event Log_layout" '
                    'title:@macros.layouts@EventLog@ width:600 height:600 persistent:true '
                    'open:true')
            lx.out("ERROR Backup failed with ", sys.exc_info())
        lx.out("Copied backup config.")

    else:
        lx.out("Config not found")

# END Functions -------------------------------------------


# MAIN PROGRAM --------------------------------------------
def main():
    saveCopy()


# END MAIN PROGRAM -----------------------------------------------

if __name__ == '__main__':
    try:
        main()
    except:
        lx.out(traceback.format_exc())
