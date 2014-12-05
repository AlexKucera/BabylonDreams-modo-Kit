# python
# coding=utf-8

import os
import traceback

import lx


__author__ = 'alex'


# MAIN PROGRAM --------------------------------------------
def main():
    configpath = lx.eval("query platformservice path.path ? configname")
    if os.path.isfile(configpath):
        lx.out("Found Config at: " + configpath)
        lx.out("Unlocking Config…")
        errorcode = os.system("chflags nouchg " + configpath)
        chmoderror = os.system("chmod 644 " + configpath)
        if errorcode == 0 and chmoderror == 0:
            lx.out("Saving Config…")
            lx.eval("config.save")
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


# END MAIN PROGRAM -----------------------------------------------

if __name__ == '__main__':
    try:
        main()
    except:
        lx.out(traceback.format_exc())
