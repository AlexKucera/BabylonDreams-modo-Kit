#!/usr/bin/python

#Author Keith Sheppard
#April 2015
# pyModoPatterns
# to make repetitive mesh copies in formation
#patterns return  rotX, rotY, rotZ, sclX, sclY, sclZ, posX, posY, posZ   .....in that order....
#to get rotZ = yourVariable[2]

import pyModo as pm
import pyModoT as mt
import sys

def CreatePatterns():
    ssPats = []
    xCntSelSet = 0

    mID = pm.Mesh_ID_Selected()

    if len(mID) < 1:
        pm.Modo_UserMessage_Info('Mesh Selection','Please select a mesh layer and rerun the script!')
        sys.exit()

    if pm.Poly_Count_Selected(mID) < 1:
        pm.Modo_UserMessage_Info('Poly Selection','Please select polygons and rerun the script!')
        sys.exit()

    allPolys =pm.Poly_Index_Selected(mID)

    pm.Poly_DeSelect_All()
    ############################################################################################
    ############################################################################################
    ###  ADD YOU NEW PATTERNS TO THE LIST BELOW
    ############################################################################################
    ptrnFunctions = 'pattern001;pattern002;pattern003;' \
                    'pattern004;pattern005;pattern006;' \
                    'pattern007;pattern008;pattern009;' \
                    'pattern010'
    ###########################################################################################
    ############################################################################################
    ############################################################################################

    ptrnSelected = '__' + pm.Modo_UserChoice_Selection(ptrnFunctions)

    ptrnIter = pm.Modo_UserDataEntry_asInteger('How many iterations?')

    if ptrnIter < 2:
        pm.Modo_UserMessage_Info('Iteration Count','Please enter a number higher than 2!')
        sys.exit()

    fn_Pattern  = globals()[ptrnSelected]
    ptrnResults = fn_Pattern()

    #check user preferences
    uPref_CD = pm.Modo_SysPref_MeshItems_CopyDeSelection()
    uPref_PS = pm.Modo_SysPref_MeshItems_PasteSelection()
    uPref_PD = pm.Modo_SysPref_MeshItems_PasteDeSelection()
    #set user preferences for script
    pm.Modo_SysPref_MeshItems_CopyDeSelection(0)
    pm.Modo_SysPref_MeshItems_PasteSelection(1)
    pm.Modo_SysPref_MeshItems_PasteDeSelection(1)

    for polys in allPolys:

        pm.Poly_DeSelect_All()
        pm.Poly_Select(polys)
        SelSet= 'pattern_SS'
        xCntSelSet += 1
        ss = SelSet + str('%04d' % xCntSelSet)
        pm.SelectionSet_AddTo(ss)
        ssPats.append(ss)

        for x in range(1,ptrnIter,1):
            pm.Item_Select(mID)
            pm.Poly_DeSelect_All()
            pm.Poly_Mode_Set()
            pm.SelectionSet_Select(ss)
            selpoly = pm.Poly_Index_Selected(mID)

            vX = pm.Vert_Average_Position_X_Get(mID)
            vY = pm.Vert_Average_Position_Y_Get(mID)
            vZ = pm.Vert_Average_Position_Z_Get(mID)

            for poly in selpoly:
                pNrml = pm.Poly_Normal_Get(poly)

            newPosX =  (pNrml[0] + (vX * ptrnResults[6]))/x
            newPosY =  (pNrml[1] + (vY * ptrnResults[7]))/x
            newPosZ =  (pNrml[2] + (vZ * ptrnResults[8]))/x

            pm.Item_Select(mID)
            pm.Poly_DeSelect_All()
            pm.Poly_Mode_Set()
            pm.Poly_Select(poly)
            pm.Poly_Select_Connected()
            pm.Poly_Copy()
            pm.Poly_Paste()

            #data from patterns
            __SizeIt(ptrnResults[3], ptrnResults[4], ptrnResults[5])
            __SpinIt(ptrnResults[0], ptrnResults[1], ptrnResults[2])
            __MoveIt(newPosX, newPosY, newPosZ)

            pm.Poly_DeSelect_All()
            pm.Poly_Mode_Set()
            pm.Poly_Select(poly)
            pm.SelectionSet_RemoveFrom(ss)

    #finalize
    pm.Poly_Mode_Set()
    for all_ss in ssPats: pm.SelectionSet_Delete(all_ss)
    pm.Poly_DeSelect_All()
    # pm.Mesh_Cleanup(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    #return user preferences
    pm.Modo_SysPref_MeshItems_CopyDeSelection(uPref_CD)
    pm.Modo_SysPref_MeshItems_PasteSelection(uPref_PS)
    pm.Modo_SysPref_MeshItems_PasteDeSelection(uPref_PD)

def __MoveIt(posX, posY, posZ):
    mt.Move_pOnOff(1)
    mt.Tool_Reset_Set()
    mt.Move_X_Value(posX)
    mt.Move_Y_Value(posY)
    mt.Move_Z_Value(posZ)
    mt.Tool_Apply_Set()
    mt.Move_pOnOff(0)

def __SizeIt(sclX, sclY, sclZ):
    mt.Scale_pOnOff(1)
    mt.Tool_Reset_Set()
    mt.Scale_Scale_X_Value(sclX)
    mt.Scale_Scale_Y_Value(sclY)
    mt.Scale_Scale_Z_Value(sclZ)
    mt.Tool_Apply_Set()
    mt.Scale_pOnOff(0)

def __SpinIt(rotX, rotY, rotZ):
    mt.Rotate_pOnOff(1)
    mt.Tool_Reset_Set()
    mt.Rotate_X_Value(rotX)
    mt.Rotate_Y_Value(rotY)
    mt.Rotate_Z_Value(rotZ)
    mt.Tool_Apply_Set()
    mt.Rotate_pOnOff(0)

def __pattern001():
    rotX = 2.5
    rotY = 2.5
    rotZ = 0
    sclX = .95
    sclY = .95
    sclZ = .95
    posX = 0.05
    posY = 0.05
    posZ = 0.05

    return rotX, rotY, rotZ, sclX, sclY, sclZ, posX, posY, posZ

def __pattern002():
    rotX = 0
    rotY = 10
    rotZ = 22.5
    sclX = 1.05
    sclY = 1.05
    sclZ = 1.05
    posX = 0.25
    posY = 0.25
    posZ = 0.25

    return rotX, rotY, rotZ, sclX, sclY, sclZ, posX, posY, posZ

def __pattern003():
    rotX = 2.5
    rotY = 12.5
    rotZ = 2.5
    sclX = .98
    sclY = .98
    sclZ = .98
    posX = .15
    posY = .50
    posZ = .15

    return rotX, rotY, rotZ, sclX, sclY, sclZ, posX, posY, posZ

def __pattern004():
    rotX = 22.5
    rotY = 10
    rotZ = 7.5
    sclX = 1.05
    sclY = 1.05
    sclZ = 1.05
    posX = .2
    posY = .2
    posZ = .2

    return rotX, rotY, rotZ, sclX, sclY, sclZ, posX, posY, posZ

def __pattern005():
    rotX = 0
    rotY = 75
    rotZ = 0
    sclX = .99
    sclY = .99
    sclZ = .99
    posX = .025
    posY = .025
    posZ = .025

    return rotX, rotY, rotZ, sclX, sclY, sclZ, posX, posY, posZ

def __pattern006():
    rotX = 2.5
    rotY = 2.5
    rotZ = 2.5
    sclX = 1.025
    sclY = 1.025
    sclZ = 1.025
    posX = .15
    posY = .15
    posZ = .15

    return rotX, rotY, rotZ, sclX, sclY, sclZ, posX, posY, posZ

def __pattern007():
    rotX = 2.5
    rotY = 25
    rotZ = 2.5
    sclX = 1.0025
    sclY = 1.0025
    sclZ = 1.0025
    posX = 0.0002
    posY = 0.00002
    posZ = 0.0002

    return rotX, rotY, rotZ, sclX, sclY, sclZ, posX, posY, posZ

def __pattern008():
    rotX = 0.5
    rotY = 12.5
    rotZ = 0.5
    sclX = .98
    sclY = .98
    sclZ = .98
    posX = .05
    posY = .1
    posZ = .05

    return rotX, rotY, rotZ, sclX, sclY, sclZ, posX, posY, posZ

def __pattern009():
    rotX = 1.5
    rotY = 4.5
    rotZ = 2.5
    sclX = 1
    sclY = 1
    sclZ = 1
    posX = .0025
    posY = .0015
    posZ = .0025

    return rotX, rotY, rotZ, sclX, sclY, sclZ, posX, posY, posZ

def __pattern010():
    rotX = 5.15
    rotY = 5.25
    rotZ = 5.15
    sclX = .99
    sclY = .99
    sclZ = .99
    posX = .05
    posY = .25
    posZ = .05

    return rotX, rotY, rotZ, sclX, sclY, sclZ, posX, posY, posZ