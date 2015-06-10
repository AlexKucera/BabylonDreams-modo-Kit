#!/usr/bin/python


# pyModo
#Author Keith Sheppard
#Contributors - Oleg (aka: ThirteenthGuest)
#6/8/2015 6:18:23 PM


import lx
import sys
import math
import random
import string
import glob
import os
import pyModoT as mt


def Area_Light_Count_All():
    strItemType = 'Area Light'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Area_Light_Count_Selected():
    strItemType = 'Area Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Area_Light_Count_UnSelected():
    strItemType = 'Area Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Area_Light_Name_All():
    strItemType = 'Area Light'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Area_Light_Name_Selected():
    strItemType = 'Area Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Area_Light_Name_UnSelected():
    strItemType = 'Area Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Area_Light_ID_All():
    strItemType = 'Area Light'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Area_Light_ID_Selected():
    strItemType = 'Area Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Area_Light_ID_UnSelected():
    strItemType = 'Area Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Area_Light_Add_New():
    strItemType = 'areaLight'
    lx.eval('item.create {%s}' % strItemType)


def Backdrop_Item_Count_All():
    strItemType = 'Backdrop Item'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Backdrop_Item_Count_Selected():
    strItemType = 'Backdrop Item'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Backdrop_Item_Count_UnSelected():
    strItemType = 'Backdrop Item'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Backdrop_Item_Name_All():
    strItemType = 'Backdrop Item'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Backdrop_Item_Name_Selected():
    strItemType = 'Backdrop Item'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Backdrop_Item_Name_UnSelected():
    strItemType = 'Backdrop Item'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Backdrop_Item_ID_All():
    strItemType = 'Backdrop Item'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Backdrop_Item_ID_Selected():
    strItemType = 'Backdrop Item'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Backdrop_Item_ID_UnSelected():
    strItemType = 'Backdrop Item'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Backdrop_Item_Add_New():
    strItemType = 'backdrop'
    lx.eval('item.create {%s}' % strItemType)


def Bend_Effector_Count_All():
    strItemType = 'Bend Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Bend_Effector_Count_Selected():
    strItemType = 'Bend Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Bend_Effector_Count_UnSelected():
    strItemType = 'Bend Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Bend_Effector_Name_All():
    strItemType = 'Bend Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Bend_Effector_Name_Selected():
    strItemType = 'Bend Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Bend_Effector_Name_UnSelected():
    strItemType = 'Bend Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Bend_Effector_ID_All():
    strItemType = 'Bend Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Bend_Effector_ID_Selected():
    strItemType = 'Bend Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Bend_Effector_ID_UnSelected():
    strItemType = 'Bend Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Bend_Effector_Add_New():
    strItemType = 'deform.bend'
    lx.eval('item.create {%s}' % strItemType)


def Bezier_Falloff_Count_All():
    strItemType = 'Bezier Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Bezier_Falloff_Count_Selected():
    strItemType = 'Bezier Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Bezier_Falloff_Count_UnSelected():
    strItemType = 'Bezier Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Bezier_Falloff_Name_All():
    strItemType = 'Bezier Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Bezier_Falloff_Name_Selected():
    strItemType = 'Bezier Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Bezier_Falloff_Name_UnSelected():
    strItemType = 'Bezier Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Bezier_Falloff_ID_All():
    strItemType = 'Bezier Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Bezier_Falloff_ID_Selected():
    strItemType = 'Bezier Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Bezier_Falloff_ID_UnSelected():
    strItemType = 'Bezier Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Bezier_Falloff_Add_New():
    strItemType = 'falloff.bezier'
    lx.eval('item.create {%s}' % strItemType)


def Blob_Count_All():
    strItemType = 'Blob'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Blob_Count_Selected():
    strItemType = 'Blob'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Blob_Count_UnSelected():
    strItemType = 'Blob'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Blob_Name_All():
    strItemType = 'Blob'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Blob_Name_Selected():
    strItemType = 'Blob'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Blob_Name_UnSelected():
    strItemType = 'Blob'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Blob_ID_All():
    strItemType = 'Blob'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Blob_ID_Selected():
    strItemType = 'Blob'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Blob_ID_UnSelected():
    strItemType = 'Blob'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Blob_Add_New():
    strItemType = 'blob'
    lx.eval('item.create {%s}' % strItemType)


def Camera_Count_All():
    strItemType = 'Camera'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Camera_Count_Selected():
    strItemType = 'Camera'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Camera_Count_UnSelected():
    strItemType = 'Camera'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Camera_Name_All():
    strItemType = 'Camera'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Camera_Name_Selected():
    strItemType = 'Camera'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Camera_Name_UnSelected():
    strItemType = 'Camera'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Camera_ID_All():
    strItemType = 'Camera'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Camera_ID_Selected():
    strItemType = 'Camera'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Camera_ID_UnSelected():
    strItemType = 'Camera'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Camera_Add_New():
    strItemType = 'camera'
    lx.eval('item.create {%s}' % strItemType)


def Capsule_Falloff_Count_All():
    strItemType = 'Capsule Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Capsule_Falloff_Count_Selected():
    strItemType = 'Capsule Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Capsule_Falloff_Count_UnSelected():
    strItemType = 'Capsule Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Capsule_Falloff_Name_All():
    strItemType = 'Capsule Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Capsule_Falloff_Name_Selected():
    strItemType = 'Capsule Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Capsule_Falloff_Name_UnSelected():
    strItemType = 'Capsule Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Capsule_Falloff_ID_All():
    strItemType = 'Capsule Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Capsule_Falloff_ID_Selected():
    strItemType = 'Capsule Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Capsule_Falloff_ID_UnSelected():
    strItemType = 'Capsule Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Capsule_Falloff_Add_New():
    strItemType = 'falloff.capsule'
    lx.eval('item.create {%s}' % strItemType)


def Cel_Edges_Material_Count_All():
    strItemType = 'Cel Edges Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Cel_Edges_Material_Count_Selected():
    strItemType = 'Cel Edges Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Cel_Edges_Material_Count_UnSelected():
    strItemType = 'Cel Edges Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Cel_Edges_Material_Name_All():
    strItemType = 'Cel Edges Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Cel_Edges_Material_Name_Selected():
    strItemType = 'Cel Edges Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Cel_Edges_Material_Name_UnSelected():
    strItemType = 'Cel Edges Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Cel_Edges_Material_ID_All():
    strItemType = 'Cel Edges Material'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Cel_Edges_Material_ID_Selected():
    strItemType = 'Cel Edges Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Cel_Edges_Material_ID_UnSelected():
    strItemType = 'Cel Edges Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Cel_Edges_Material_Add_New():
    strItemType = 'material.celEdges'
    lx.eval('shader.create {%s}' % strItemType)


def Cel_Material_Count_All():
    strItemType = 'Cel Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Cel_Material_Count_Selected():
    strItemType = 'Cel Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Cel_Material_Count_UnSelected():
    strItemType = 'Cel Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Cel_Material_Name_All():
    strItemType = 'Cel Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Cel_Material_Name_Selected():
    strItemType = 'Cel Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Cel_Material_Name_UnSelected():
    strItemType = 'Cel Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Cel_Material_ID_All():
    strItemType = 'Cel Material'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Cel_Material_ID_Selected():
    strItemType = 'Cel Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Cel_Material_ID_UnSelected():
    strItemType = 'Cel Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Cel_Material_Add_New():
    strItemType = 'material.celShader'
    lx.eval('shader.create {%s}' % strItemType)


def Cellular_Count_All():
    strItemType = 'Cellular'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Cellular_Count_Selected():
    strItemType = 'Cellular'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Cellular_Count_UnSelected():
    strItemType = 'Cellular'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Cellular_Name_All():
    strItemType = 'Cellular'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Cellular_Name_Selected():
    strItemType = 'Cellular'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Cellular_Name_UnSelected():
    strItemType = 'Cellular'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Cellular_ID_All():
    strItemType = 'Cellular'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Cellular_ID_Selected():
    strItemType = 'Cellular'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Cellular_ID_UnSelected():
    strItemType = 'Cellular'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Cellular_Add_New():
    strItemType = 'cellular'
    lx.eval('shader.create {%s}' % strItemType)


def Checker_Count_All():
    strItemType = 'Checker'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Checker_Count_Selected():
    strItemType = 'Checker'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Checker_Count_UnSelected():
    strItemType = 'Checker'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Checker_Name_All():
    strItemType = 'Checker'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Checker_Name_Selected():
    strItemType = 'Checker'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Checker_Name_UnSelected():
    strItemType = 'Checker'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Checker_ID_All():
    strItemType = 'Checker'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Checker_ID_Selected():
    strItemType = 'Checker'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Checker_ID_UnSelected():
    strItemType = 'Checker'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Checker_Add_New():
    strItemType = 'checker'
    lx.eval('shader.create {%s}' % strItemType)


def ClipBin_Image_Count_All():
    strItemType = 'Image'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ClipBin_Image_Count_Selected():
    strItemType = 'Image'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ClipBin_Image_Count_UnSelected():
    strItemType = 'Image'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ClipBin_Image_Name_All():
    strItemType = 'Image'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ClipBin_Image_Name_Selected():
    strItemType = 'Image'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ClipBin_Image_Name_UnSelected():
    strItemType = 'Image'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ClipBin_Image_ID_All():
    strItemType = 'Image'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ClipBin_Image_ID_Selected():
    strItemType = 'Image'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ClipBin_Image_ID_UnSelected():
    strItemType = 'Image'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Collector_Emitter_Count_All():
    strItemType = 'Collector / Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Collector_Emitter_Count_Selected():
    strItemType = 'Collector / Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Collector_Emitter_Count_UnSelected():
    strItemType = 'Collector / Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Collector_Emitter_Name_All():
    strItemType = 'Collector / Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Collector_Emitter_Name_Selected():
    strItemType = 'Collector / Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Collector_Emitter_Name_UnSelected():
    strItemType = 'Collector / Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Collector_Emitter_ID_All():
    strItemType = 'Collector / Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Collector_Emitter_ID_Selected():
    strItemType = 'Collector / Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Collector_Emitter_ID_UnSelected():
    strItemType = 'Collector / Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Collector_Emitter_Add_New():
    strItemType = 'collectorEmitter'
    lx.eval('item.create {%s}' % strItemType)


def Constant_Count_All():
    strItemType = 'Constant'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Constant_Count_Selected():
    strItemType = 'Constant'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Constant_Count_UnSelected():
    strItemType = 'Constant'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Constant_Name_All():
    strItemType = 'Constant'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Constant_Name_Selected():
    strItemType = 'Constant'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Constant_Name_UnSelected():
    strItemType = 'Constant'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Constant_ID_All():
    strItemType = 'Constant'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Constant_ID_Selected():
    strItemType = 'Constant'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Constant_ID_UnSelected():
    strItemType = 'Constant'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Constant_Add_New():
    strItemType = 'constant'
    lx.eval('shader.create {%s}' % strItemType)


def CSV_Point_Cache_Count_All():
    strItemType = 'CSV Point Cache'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def CSV_Point_Cache_Count_Selected():
    strItemType = 'CSV Point Cache'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def CSV_Point_Cache_Count_UnSelected():
    strItemType = 'CSV Point Cache'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def CSV_Point_Cache_Name_All():
    strItemType = 'CSV Point Cache'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def CSV_Point_Cache_Name_Selected():
    strItemType = 'CSV Point Cache'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def CSV_Point_Cache_Name_UnSelected():
    strItemType = 'CSV Point Cache'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def CSV_Point_Cache_ID_All():
    strItemType = 'CSV Point Cache'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def CSV_Point_Cache_ID_Selected():
    strItemType = 'CSV Point Cache'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def CSV_Point_Cache_ID_UnSelected():
    strItemType = 'CSV Point Cache'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def CSV_Point_Cache_Add_New():
    strItemType = 'csvCache'
    lx.eval('item.create {%s}' % strItemType)


def Curve_Constraint_Effector_Count_All():
    strItemType = 'Curve Constraint Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Curve_Constraint_Effector_Count_Selected():
    strItemType = 'Curve Constraint Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Curve_Constraint_Effector_Count_UnSelected():
    strItemType = 'Curve Constraint Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Curve_Constraint_Effector_Name_All():
    strItemType = 'Curve Constraint Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Curve_Constraint_Effector_Name_Selected():
    strItemType = 'Curve Constraint Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Curve_Constraint_Effector_Name_UnSelected():
    strItemType = 'Curve Constraint Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Curve_Constraint_Effector_ID_All():
    strItemType = 'Curve Constraint Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Curve_Constraint_Effector_ID_Selected():
    strItemType = 'Curve Constraint Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Curve_Constraint_Effector_ID_UnSelected():
    strItemType = 'Curve Constraint Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Curve_Constraint_Effector_Add_New():
    strItemType = 'deform.crvConst'
    lx.eval('item.create {%s}' % strItemType)


def Curve_Emitter_Count_All():
    strItemType = 'Curve Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Curve_Emitter_Count_Selected():
    strItemType = 'Curve Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Curve_Emitter_Count_UnSelected():
    strItemType = 'Curve Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Curve_Emitter_Name_All():
    strItemType = 'Curve Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Curve_Emitter_Name_Selected():
    strItemType = 'Curve Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Curve_Emitter_Name_UnSelected():
    strItemType = 'Curve Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Curve_Emitter_ID_All():
    strItemType = 'Curve Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Curve_Emitter_ID_Selected():
    strItemType = 'Curve Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Curve_Emitter_ID_UnSelected():
    strItemType = 'Curve Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Curve_Emitter_Add_New():
    strItemType = 'curveEmitter'
    lx.eval('item.create {%s}' % strItemType)


def Curve_Force_Count_All():
    strItemType = 'Curve Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Curve_Force_Count_Selected():
    strItemType = 'Curve Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Curve_Force_Count_UnSelected():
    strItemType = 'Curve Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Curve_Force_Name_All():
    strItemType = 'Curve Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Curve_Force_Name_Selected():
    strItemType = 'Curve Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Curve_Force_Name_UnSelected():
    strItemType = 'Curve Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Curve_Force_ID_All():
    strItemType = 'Curve Force'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Curve_Force_ID_Selected():
    strItemType = 'Curve Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Curve_Force_ID_UnSelected():
    strItemType = 'Curve Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Curve_Force_Add_New():
    strItemType = 'force.curve'
    lx.eval('item.create {%s}' % strItemType)


def Cylinder_Light_Count_All():
    strItemType = 'Cylinder Light'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Cylinder_Light_Count_Selected():
    strItemType = 'Cylinder Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Cylinder_Light_Count_UnSelected():
    strItemType = 'Cylinder Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Cylinder_Light_Name_All():
    strItemType = 'Cylinder Light'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Cylinder_Light_Name_Selected():
    strItemType = 'Cylinder Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Cylinder_Light_Name_UnSelected():
    strItemType = 'Cylinder Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Cylinder_Light_ID_All():
    strItemType = 'Cylinder Light'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Cylinder_Light_ID_Selected():
    strItemType = 'Cylinder Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Cylinder_Light_ID_UnSelected():
    strItemType = 'Cylinder Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Cylinder_Light_Add_New():
    strItemType = 'cylinderLight'
    lx.eval('item.create {%s}' % strItemType)


def Directional_Light_Count_All():
    strItemType = 'Directional Light'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Directional_Light_Count_Selected():
    strItemType = 'Directional Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Directional_Light_Count_UnSelected():
    strItemType = 'Directional Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Directional_Light_Name_All():
    strItemType = 'Directional Light'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Directional_Light_Name_Selected():
    strItemType = 'Directional Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Directional_Light_Name_UnSelected():
    strItemType = 'Directional Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Directional_Light_ID_All():
    strItemType = 'Directional Light'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Directional_Light_ID_Selected():
    strItemType = 'Directional Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Directional_Light_ID_UnSelected():
    strItemType = 'Directional Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Directional_Light_Add_New():
    strItemType = 'sunLight'
    lx.eval('item.create {%s}' % strItemType)


def Dome_Light_Count_All():
    strItemType = 'Dome Light'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Dome_Light_Count_Selected():
    strItemType = 'Dome Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Dome_Light_Count_UnSelected():
    strItemType = 'Dome Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Dome_Light_Name_All():
    strItemType = 'Dome Light'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Dome_Light_Name_Selected():
    strItemType = 'Dome Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Dome_Light_Name_UnSelected():
    strItemType = 'Dome Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Dome_Light_ID_All():
    strItemType = 'Dome Light'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Dome_Light_ID_Selected():
    strItemType = 'Dome Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Dome_Light_ID_UnSelected():
    strItemType = 'Dome Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Dome_Light_Add_New():
    strItemType = 'domeLight'
    lx.eval('item.create {%s}' % strItemType)


def Dots_Count_All():
    strItemType = 'Dots'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Dots_Count_Selected():
    strItemType = 'Dots'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Dots_Count_UnSelected():
    strItemType = 'Dots'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Dots_Name_All():
    strItemType = 'Dots'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Dots_Name_Selected():
    strItemType = 'Dots'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Dots_Name_UnSelected():
    strItemType = 'Dots'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Dots_ID_All():
    strItemType = 'Dots'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Dots_ID_Selected():
    strItemType = 'Dots'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Dots_ID_UnSelected():
    strItemType = 'Dots'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Dots_Add_New():
    strItemType = 'dots'
    lx.eval('shader.create {%s}' % strItemType)


def Drag_Force_Count_All():
    strItemType = 'Drag Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Drag_Force_Count_Selected():
    strItemType = 'Drag Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Drag_Force_Count_UnSelected():
    strItemType = 'Drag Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Drag_Force_Name_All():
    strItemType = 'Drag Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Drag_Force_Name_Selected():
    strItemType = 'Drag Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Drag_Force_Name_UnSelected():
    strItemType = 'Drag Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Drag_Force_ID_All():
    strItemType = 'Drag Force'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Drag_Force_ID_Selected():
    strItemType = 'Drag Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Drag_Force_ID_UnSelected():
    strItemType = 'Drag Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Drag_Force_Add_New():
    strItemType = 'force.drag'
    lx.eval('item.create {%s}' % strItemType)


def Dynamic_Collider_Count_All():
    strItemType = 'Dynamic Collider'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Dynamic_Collider_Count_Selected():
    strItemType = 'Dynamic Collider'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Dynamic_Collider_Count_UnSelected():
    strItemType = 'Dynamic Collider'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Dynamic_Collider_Name_All():
    strItemType = 'Dynamic Collider'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Dynamic_Collider_Name_Selected():
    strItemType = 'Dynamic Collider'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Dynamic_Collider_Name_UnSelected():
    strItemType = 'Dynamic Collider'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Dynamic_Collider_ID_All():
    strItemType = 'Dynamic Collider'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Dynamic_Collider_ID_Selected():
    strItemType = 'Dynamic Collider'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Dynamic_Collider_ID_UnSelected():
    strItemType = 'Dynamic Collider'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Dynamic_Collider_Add_New():
    strItemType = 'dynamicCollider'
    lx.eval('item.create {%s}' % strItemType)


def Dynamic_Fluid_Count_All():
    strItemType = 'Dynamic Fluid'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Dynamic_Fluid_Count_Selected():
    strItemType = 'Dynamic Fluid'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Dynamic_Fluid_Count_UnSelected():
    strItemType = 'Dynamic Fluid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Dynamic_Fluid_Name_All():
    strItemType = 'Dynamic Fluid'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Dynamic_Fluid_Name_Selected():
    strItemType = 'Dynamic Fluid'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Dynamic_Fluid_Name_UnSelected():
    strItemType = 'Dynamic Fluid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Dynamic_Fluid_ID_All():
    strItemType = 'Dynamic Fluid'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Dynamic_Fluid_ID_Selected():
    strItemType = 'Dynamic Fluid'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Dynamic_Fluid_ID_UnSelected():
    strItemType = 'Dynamic Fluid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Dynamic_Fluid_Add_New():
    strItemType = 'dynamicFluid'
    lx.eval('item.create {%s}' % strItemType)


def Edge_Count_All(Requires_ItemID):
    strItemType = 'Edge'
    asVariant = 'all'
    return __fn_pyModo_Component_Count(Requires_ItemID, strItemType, asVariant)


def Edge_Count_Selected(Requires_ItemID):
    strItemType = 'Edge'
    asVariant = 'selected'
    return __fn_pyModo_Component_Count(Requires_ItemID, strItemType, asVariant)


def Edge_Count_UnSelected(Requires_ItemID):
    strItemType = 'Edge'
    asVariant = 'unselected'
    return __fn_pyModo_Component_Count(Requires_ItemID, strItemType, asVariant)


def Edge_Index_All(Requires_ItemID):
    strItemType = 'Edge'
    asVariant = 'all'
    return __fn_pyModo_Component_Index(Requires_ItemID, strItemType, asVariant)


def Edge_Index_Selected(Requires_ItemID):
    strItemType = 'Edge'
    asVariant = 'selected'
    return __fn_pyModo_Component_Index(Requires_ItemID, strItemType, asVariant)


def Edge_Index_UnSelected(Requires_ItemID):
    strItemType = 'Edge'
    asVariant = 'unselected'
    return __fn_pyModo_Component_Index(Requires_ItemID, strItemType, asVariant)


def Environment_Count_All():
    strItemType = 'Environment'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Environment_Count_Selected():
    strItemType = 'Environment'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Environment_Count_UnSelected():
    strItemType = 'Environment'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Environment_Name_All():
    strItemType = 'Environment'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Environment_Name_Selected():
    strItemType = 'Environment'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Environment_Name_UnSelected():
    strItemType = 'Environment'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Environment_ID_All():
    strItemType = 'Environment'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Environment_ID_Selected():
    strItemType = 'Environment'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Environment_ID_UnSelected():
    strItemType = 'Environment'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Environment_Add_New():
    strItemType = 'environment'
    lx.eval('item.create {%s}' % strItemType)


def Environment_Material_Count_All():
    strItemType = 'Environment Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Environment_Material_Count_Selected():
    strItemType = 'Environment Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Environment_Material_Count_UnSelected():
    strItemType = 'Environment Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Environment_Material_Name_All():
    strItemType = 'Environment Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Environment_Material_Name_Selected():
    strItemType = 'Environment Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Environment_Material_Name_UnSelected():
    strItemType = 'Environment Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Environment_Material_ID_All():
    strItemType = 'Environment Material'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Environment_Material_ID_Selected():
    strItemType = 'Environment Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Environment_Material_ID_UnSelected():
    strItemType = 'Environment Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Environment_Material_Add_New():
    strItemType = 'envMaterial'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Display_Counter_1_Count_All():
    strItemType = 'Counter 1'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Display_Counter_1_Count_Selected():
    strItemType = 'Counter 1'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Display_Counter_1_Count_UnSelected():
    strItemType = 'Counter 1'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Display_Counter_1_Name_All():
    strItemType = 'Counter 1'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Display_Counter_1_Name_Selected():
    strItemType = 'Counter 1'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Display_Counter_1_Name_UnSelected():
    strItemType = 'Counter 1'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Display_Counter_1_ID_All():
    strItemType = 'Counter 1'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Display_Counter_1_ID_Selected():
    strItemType = 'Counter 1'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Display_Counter_1_ID_UnSelected():
    strItemType = 'Counter 1'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Display_Counter_1_Add_New():
    strItemType = 'val.Display_Counter1.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Display_Counter_2_Count_All():
    strItemType = 'Counter 2'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Display_Counter_2_Count_Selected():
    strItemType = 'Counter 2'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Display_Counter_2_Count_UnSelected():
    strItemType = 'Counter 2'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Display_Counter_2_Name_All():
    strItemType = 'Counter 2'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Display_Counter_2_Name_Selected():
    strItemType = 'Counter 2'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Display_Counter_2_Name_UnSelected():
    strItemType = 'Counter 2'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Display_Counter_2_ID_All():
    strItemType = 'Counter 2'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Display_Counter_2_ID_Selected():
    strItemType = 'Counter 2'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Display_Counter_2_ID_UnSelected():
    strItemType = 'Counter 2'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Display_Counter_2_Add_New():
    strItemType = 'val.Display_Counter2.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Display_UV_LEDs_Count_All():
    strItemType = 'UV LEDs'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Display_UV_LEDs_Count_Selected():
    strItemType = 'UV LEDs'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Display_UV_LEDs_Count_UnSelected():
    strItemType = 'UV LEDs'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Display_UV_LEDs_Name_All():
    strItemType = 'UV LEDs'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Display_UV_LEDs_Name_Selected():
    strItemType = 'UV LEDs'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Display_UV_LEDs_Name_UnSelected():
    strItemType = 'UV LEDs'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Display_UV_LEDs_ID_All():
    strItemType = 'UV LEDs'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Display_UV_LEDs_ID_Selected():
    strItemType = 'UV LEDs'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Display_UV_LEDs_ID_UnSelected():
    strItemType = 'UV LEDs'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Display_UV_LEDs_Add_New():
    strItemType = 'val.Display_UVLEDs.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Geometry_Box_Count_All():
    strItemType = 'Box'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Box_Count_Selected():
    strItemType = 'Box'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Box_Count_UnSelected():
    strItemType = 'Box'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Box_Name_All():
    strItemType = 'Box'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Box_Name_Selected():
    strItemType = 'Box'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Box_Name_UnSelected():
    strItemType = 'Box'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Box_ID_All():
    strItemType = 'Box'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Box_ID_Selected():
    strItemType = 'Box'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Box_ID_UnSelected():
    strItemType = 'Box'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Box_Add_New():
    strItemType = 'val.Geometric_Box.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Geometry_Circular_Count_All():
    strItemType = 'Circular'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Circular_Count_Selected():
    strItemType = 'Circular'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Circular_Count_UnSelected():
    strItemType = 'Circular'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Circular_Name_All():
    strItemType = 'Circular'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Circular_Name_Selected():
    strItemType = 'Circular'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Circular_Name_UnSelected():
    strItemType = 'Circular'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Circular_ID_All():
    strItemType = 'Circular'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Circular_ID_Selected():
    strItemType = 'Circular'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Circular_ID_UnSelected():
    strItemType = 'Circular'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Circular_Add_New():
    strItemType = 'val.Geometric_Circular.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Geometry_Corners_Count_All():
    strItemType = 'Corners'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Corners_Count_Selected():
    strItemType = 'Corners'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Corners_Count_UnSelected():
    strItemType = 'Corners'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Corners_Name_All():
    strItemType = 'Corners'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Corners_Name_Selected():
    strItemType = 'Corners'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Corners_Name_UnSelected():
    strItemType = 'Corners'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Corners_ID_All():
    strItemType = 'Corners'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Corners_ID_Selected():
    strItemType = 'Corners'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Corners_ID_UnSelected():
    strItemType = 'Corners'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Corners_Add_New():
    strItemType = 'val.Geometric_Corners.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Geometry_Cubic_Count_All():
    strItemType = 'Cubic'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Cubic_Count_Selected():
    strItemType = 'Cubic'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Cubic_Count_UnSelected():
    strItemType = 'Cubic'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Cubic_Name_All():
    strItemType = 'Cubic'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Cubic_Name_Selected():
    strItemType = 'Cubic'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Cubic_Name_UnSelected():
    strItemType = 'Cubic'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Cubic_ID_All():
    strItemType = 'Cubic'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Cubic_ID_Selected():
    strItemType = 'Cubic'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Cubic_ID_UnSelected():
    strItemType = 'Cubic'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Cubic_Add_New():
    strItemType = 'val.Geometric_Cubic.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Geometry_Dimples_Count_All():
    strItemType = 'Dimples'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Dimples_Count_Selected():
    strItemType = 'Dimples'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Dimples_Count_UnSelected():
    strItemType = 'Dimples'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Dimples_Name_All():
    strItemType = 'Dimples'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Dimples_Name_Selected():
    strItemType = 'Dimples'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Dimples_Name_UnSelected():
    strItemType = 'Dimples'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Dimples_ID_All():
    strItemType = 'Dimples'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Dimples_ID_Selected():
    strItemType = 'Dimples'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Dimples_ID_UnSelected():
    strItemType = 'Dimples'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Dimples_Add_New():
    strItemType = 'val.Geometric_Dimples.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Geometry_Grid_Count_All():
    strItemType = 'Grid'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Grid_Count_Selected():
    strItemType = 'Grid'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Grid_Count_UnSelected():
    strItemType = 'Grid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Grid_Name_All():
    strItemType = 'Grid'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Grid_Name_Selected():
    strItemType = 'Grid'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Grid_Name_UnSelected():
    strItemType = 'Grid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Grid_ID_All():
    strItemType = 'Grid'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Grid_ID_Selected():
    strItemType = 'Grid'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Grid_ID_UnSelected():
    strItemType = 'Grid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Grid_Add_New():
    strItemType = 'val.Geometric_Grid.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Geometry_Iris_Count_All():
    strItemType = 'Iris'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Iris_Count_Selected():
    strItemType = 'Iris'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Iris_Count_UnSelected():
    strItemType = 'Iris'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Iris_Name_All():
    strItemType = 'Iris'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Iris_Name_Selected():
    strItemType = 'Iris'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Iris_Name_UnSelected():
    strItemType = 'Iris'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Iris_ID_All():
    strItemType = 'Iris'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Iris_ID_Selected():
    strItemType = 'Iris'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Iris_ID_UnSelected():
    strItemType = 'Iris'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Iris_Add_New():
    strItemType = 'val.Geometric_Iris.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Geometry_Linear_Count_All():
    strItemType = 'Linear'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Linear_Count_Selected():
    strItemType = 'Linear'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Linear_Count_UnSelected():
    strItemType = 'Linear'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Linear_Name_All():
    strItemType = 'Linear'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Linear_Name_Selected():
    strItemType = 'Linear'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Linear_Name_UnSelected():
    strItemType = 'Linear'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Linear_ID_All():
    strItemType = 'Linear'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Linear_ID_Selected():
    strItemType = 'Linear'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Linear_ID_UnSelected():
    strItemType = 'Linear'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Linear_Add_New():
    strItemType = 'val.Geometric_Linear.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Geometry_Polygon_Count_All():
    strItemType = 'Polygon'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Polygon_Count_Selected():
    strItemType = 'Polygon'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Polygon_Count_UnSelected():
    strItemType = 'Polygon'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Polygon_Name_All():
    strItemType = 'Polygon'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Polygon_Name_Selected():
    strItemType = 'Polygon'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Polygon_Name_UnSelected():
    strItemType = 'Polygon'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Polygon_ID_All():
    strItemType = 'Polygon'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Polygon_ID_Selected():
    strItemType = 'Polygon'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Polygon_ID_UnSelected():
    strItemType = 'Polygon'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Polygon_Add_New():
    strItemType = 'val.Geometric_Polygon.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Geometry_Radial_Count_All():
    strItemType = 'Radial'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Radial_Count_Selected():
    strItemType = 'Radial'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Radial_Count_UnSelected():
    strItemType = 'Radial'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Radial_Name_All():
    strItemType = 'Radial'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Radial_Name_Selected():
    strItemType = 'Radial'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Radial_Name_UnSelected():
    strItemType = 'Radial'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Radial_ID_All():
    strItemType = 'Radial'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Radial_ID_Selected():
    strItemType = 'Radial'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Radial_ID_UnSelected():
    strItemType = 'Radial'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Radial_Add_New():
    strItemType = 'val.Geometric_Radial.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Geometry_Random_Linear_Count_All():
    strItemType = 'Random Linear'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Random_Linear_Count_Selected():
    strItemType = 'Random Linear'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Random_Linear_Count_UnSelected():
    strItemType = 'Random Linear'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Random_Linear_Name_All():
    strItemType = 'Random Linear'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Random_Linear_Name_Selected():
    strItemType = 'Random Linear'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Random_Linear_Name_UnSelected():
    strItemType = 'Random Linear'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Random_Linear_ID_All():
    strItemType = 'Random Linear'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Random_Linear_ID_Selected():
    strItemType = 'Random Linear'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Random_Linear_ID_UnSelected():
    strItemType = 'Random Linear'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Random_Linear_Add_New():
    strItemType = 'val.Geometric_RndLinear.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Geometry_Ring_Count_All():
    strItemType = 'Ring'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Ring_Count_Selected():
    strItemType = 'Ring'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Ring_Count_UnSelected():
    strItemType = 'Ring'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Ring_Name_All():
    strItemType = 'Ring'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Ring_Name_Selected():
    strItemType = 'Ring'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Ring_Name_UnSelected():
    strItemType = 'Ring'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Ring_ID_All():
    strItemType = 'Ring'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Ring_ID_Selected():
    strItemType = 'Ring'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Ring_ID_UnSelected():
    strItemType = 'Ring'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Ring_Add_New():
    strItemType = 'val.Geometric_Ring.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Geometry_Spiral_Count_All():
    strItemType = 'Spiral'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Spiral_Count_Selected():
    strItemType = 'Spiral'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Spiral_Count_UnSelected():
    strItemType = 'Spiral'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Spiral_Name_All():
    strItemType = 'Spiral'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Spiral_Name_Selected():
    strItemType = 'Spiral'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Spiral_Name_UnSelected():
    strItemType = 'Spiral'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Spiral_ID_All():
    strItemType = 'Spiral'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Spiral_ID_Selected():
    strItemType = 'Spiral'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Spiral_ID_UnSelected():
    strItemType = 'Spiral'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Spiral_Add_New():
    strItemType = 'val.Geometric_Spiral.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Geometry_Star_Count_All():
    strItemType = 'Star'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Star_Count_Selected():
    strItemType = 'Star'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Star_Count_UnSelected():
    strItemType = 'Star'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Geometry_Star_Name_All():
    strItemType = 'Star'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Star_Name_Selected():
    strItemType = 'Star'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Star_Name_UnSelected():
    strItemType = 'Star'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Geometry_Star_ID_All():
    strItemType = 'Star'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Star_ID_Selected():
    strItemType = 'Star'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Star_ID_UnSelected():
    strItemType = 'Star'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Geometry_Star_Add_New():
    strItemType = 'val.Geometric_Star.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Agate_Count_All():
    strItemType = 'Agate'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Agate_Count_Selected():
    strItemType = 'Agate'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Agate_Count_UnSelected():
    strItemType = 'Agate'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Agate_Name_All():
    strItemType = 'Agate'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Agate_Name_Selected():
    strItemType = 'Agate'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Agate_Name_UnSelected():
    strItemType = 'Agate'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Agate_ID_All():
    strItemType = 'Agate'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Agate_ID_Selected():
    strItemType = 'Agate'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Agate_ID_UnSelected():
    strItemType = 'Agate'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Agate_Add_New():
    strItemType = 'val.Noise_Agate.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Bozo_Count_All():
    strItemType = 'Bozo'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Bozo_Count_Selected():
    strItemType = 'Bozo'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Bozo_Count_UnSelected():
    strItemType = 'Bozo'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Bozo_Name_All():
    strItemType = 'Bozo'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Bozo_Name_Selected():
    strItemType = 'Bozo'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Bozo_Name_UnSelected():
    strItemType = 'Bozo'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Bozo_ID_All():
    strItemType = 'Bozo'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Bozo_ID_Selected():
    strItemType = 'Bozo'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Bozo_ID_UnSelected():
    strItemType = 'Bozo'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Bozo_Add_New():
    strItemType = 'val.Noise_Bozo.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Cruddy_Count_All():
    strItemType = 'Cruddy'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Cruddy_Count_Selected():
    strItemType = 'Cruddy'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Cruddy_Count_UnSelected():
    strItemType = 'Cruddy'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Cruddy_Name_All():
    strItemType = 'Cruddy'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Cruddy_Name_Selected():
    strItemType = 'Cruddy'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Cruddy_Name_UnSelected():
    strItemType = 'Cruddy'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Cruddy_ID_All():
    strItemType = 'Cruddy'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Cruddy_ID_Selected():
    strItemType = 'Cruddy'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Cruddy_ID_UnSelected():
    strItemType = 'Cruddy'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Cruddy_Add_New():
    strItemType = 'val.Noise_Cruddy.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Dented_Count_All():
    strItemType = 'Dented'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Dented_Count_Selected():
    strItemType = 'Dented'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Dented_Count_UnSelected():
    strItemType = 'Dented'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Dented_Name_All():
    strItemType = 'Dented'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Dented_Name_Selected():
    strItemType = 'Dented'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Dented_Name_UnSelected():
    strItemType = 'Dented'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Dented_ID_All():
    strItemType = 'Dented'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Dented_ID_Selected():
    strItemType = 'Dented'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Dented_ID_UnSelected():
    strItemType = 'Dented'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Dented_Add_New():
    strItemType = 'val.Noise_Dented.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Etched_Count_All():
    strItemType = 'Etched'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Etched_Count_Selected():
    strItemType = 'Etched'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Etched_Count_UnSelected():
    strItemType = 'Etched'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Etched_Name_All():
    strItemType = 'Etched'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Etched_Name_Selected():
    strItemType = 'Etched'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Etched_Name_UnSelected():
    strItemType = 'Etched'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Etched_ID_All():
    strItemType = 'Etched'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Etched_ID_Selected():
    strItemType = 'Etched'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Etched_ID_UnSelected():
    strItemType = 'Etched'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Etched_Add_New():
    strItemType = 'val.Noise_Etched.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_fBm_Count_All():
    strItemType = 'fBm'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_fBm_Count_Selected():
    strItemType = 'fBm'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_fBm_Count_UnSelected():
    strItemType = 'fBm'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_fBm_Name_All():
    strItemType = 'fBm'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_fBm_Name_Selected():
    strItemType = 'fBm'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_fBm_Name_UnSelected():
    strItemType = 'fBm'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_fBm_ID_All():
    strItemType = 'fBm'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_fBm_ID_Selected():
    strItemType = 'fBm'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_fBm_ID_UnSelected():
    strItemType = 'fBm'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_fBm_Add_New():
    strItemType = 'val.Noise_fBm.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Flow_Bozo_Count_All():
    strItemType = 'Flow Bozo'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Flow_Bozo_Count_Selected():
    strItemType = 'Flow Bozo'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Flow_Bozo_Count_UnSelected():
    strItemType = 'Flow Bozo'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Flow_Bozo_Name_All():
    strItemType = 'Flow Bozo'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Flow_Bozo_Name_Selected():
    strItemType = 'Flow Bozo'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Flow_Bozo_Name_UnSelected():
    strItemType = 'Flow Bozo'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Flow_Bozo_ID_All():
    strItemType = 'Flow Bozo'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Flow_Bozo_ID_Selected():
    strItemType = 'Flow Bozo'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Flow_Bozo_ID_UnSelected():
    strItemType = 'Flow Bozo'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Flow_Bozo_Add_New():
    strItemType = 'val.Noise_FlowBozo.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Granite_Count_All():
    strItemType = 'Granite'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Granite_Count_Selected():
    strItemType = 'Granite'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Granite_Count_UnSelected():
    strItemType = 'Granite'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Granite_Name_All():
    strItemType = 'Granite'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Granite_Name_Selected():
    strItemType = 'Granite'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Granite_Name_UnSelected():
    strItemType = 'Granite'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Granite_ID_All():
    strItemType = 'Granite'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Granite_ID_Selected():
    strItemType = 'Granite'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Granite_ID_UnSelected():
    strItemType = 'Granite'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Granite_Add_New():
    strItemType = 'val.Noise_Granite.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Hybrid_Count_All():
    strItemType = 'Hybrid'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Hybrid_Count_Selected():
    strItemType = 'Hybrid'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Hybrid_Count_UnSelected():
    strItemType = 'Hybrid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Hybrid_Name_All():
    strItemType = 'Hybrid'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Hybrid_Name_Selected():
    strItemType = 'Hybrid'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Hybrid_Name_UnSelected():
    strItemType = 'Hybrid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Hybrid_ID_All():
    strItemType = 'Hybrid'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Hybrid_ID_Selected():
    strItemType = 'Hybrid'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Hybrid_ID_UnSelected():
    strItemType = 'Hybrid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Hybrid_Add_New():
    strItemType = 'val.Noise_Hybrid.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Lump_Count_All():
    strItemType = 'Lump'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Lump_Count_Selected():
    strItemType = 'Lump'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Lump_Count_UnSelected():
    strItemType = 'Lump'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Lump_Name_All():
    strItemType = 'Lump'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Lump_Name_Selected():
    strItemType = 'Lump'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Lump_Name_UnSelected():
    strItemType = 'Lump'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Lump_ID_All():
    strItemType = 'Lump'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Lump_ID_Selected():
    strItemType = 'Lump'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Lump_ID_UnSelected():
    strItemType = 'Lump'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Lump_Add_New():
    strItemType = 'val.Noise_Lump.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Marble_Noise_Count_All():
    strItemType = 'Marble Noise'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Marble_Noise_Count_Selected():
    strItemType = 'Marble Noise'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Marble_Noise_Count_UnSelected():
    strItemType = 'Marble Noise'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Marble_Noise_Name_All():
    strItemType = 'Marble Noise'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Marble_Noise_Name_Selected():
    strItemType = 'Marble Noise'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Marble_Noise_Name_UnSelected():
    strItemType = 'Marble Noise'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Marble_Noise_ID_All():
    strItemType = 'Marble Noise'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Marble_Noise_ID_Selected():
    strItemType = 'Marble Noise'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Marble_Noise_ID_UnSelected():
    strItemType = 'Marble Noise'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Marble_Noise_Add_New():
    strItemType = 'val.Noise_MarbleNoise.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Marble_Vein_Count_All():
    strItemType = 'Marble Vein'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Marble_Vein_Count_Selected():
    strItemType = 'Marble Vein'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Marble_Vein_Count_UnSelected():
    strItemType = 'Marble Vein'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Marble_Vein_Name_All():
    strItemType = 'Marble Vein'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Marble_Vein_Name_Selected():
    strItemType = 'Marble Vein'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Marble_Vein_Name_UnSelected():
    strItemType = 'Marble Vein'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Marble_Vein_ID_All():
    strItemType = 'Marble Vein'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Marble_Vein_ID_Selected():
    strItemType = 'Marble Vein'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Marble_Vein_ID_UnSelected():
    strItemType = 'Marble Vein'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Marble_Vein_Add_New():
    strItemType = 'val.Noise_MarbleVein.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_MultiFractal_Count_All():
    strItemType = 'Multi-Fractal'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_MultiFractal_Count_Selected():
    strItemType = 'Multi-Fractal'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_MultiFractal_Count_UnSelected():
    strItemType = 'Multi-Fractal'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_MultiFractal_Name_All():
    strItemType = 'Multi-Fractal'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_MultiFractal_Name_Selected():
    strItemType = 'Multi-Fractal'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_MultiFractal_Name_UnSelected():
    strItemType = 'Multi-Fractal'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_MultiFractal_ID_All():
    strItemType = 'Multi-Fractal'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_MultiFractal_ID_Selected():
    strItemType = 'Multi-Fractal'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_MultiFractal_ID_UnSelected():
    strItemType = 'Multi-Fractal'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_MultiFractal_Add_New():
    strItemType = 'val.Noise_MultiFractal.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Pebbles_Count_All():
    strItemType = 'Pebbles'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Pebbles_Count_Selected():
    strItemType = 'Pebbles'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Pebbles_Count_UnSelected():
    strItemType = 'Pebbles'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Pebbles_Name_All():
    strItemType = 'Pebbles'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Pebbles_Name_Selected():
    strItemType = 'Pebbles'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Pebbles_Name_UnSelected():
    strItemType = 'Pebbles'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Pebbles_ID_All():
    strItemType = 'Pebbles'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Pebbles_ID_Selected():
    strItemType = 'Pebbles'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Pebbles_ID_UnSelected():
    strItemType = 'Pebbles'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Pebbles_Add_New():
    strItemType = 'val.Noise_Pebbles.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Puffy_Clouds_Count_All():
    strItemType = 'Puffy Clouds'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Puffy_Clouds_Count_Selected():
    strItemType = 'Puffy Clouds'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Puffy_Clouds_Count_UnSelected():
    strItemType = 'Puffy Clouds'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Puffy_Clouds_Name_All():
    strItemType = 'Puffy Clouds'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Puffy_Clouds_Name_Selected():
    strItemType = 'Puffy Clouds'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Puffy_Clouds_Name_UnSelected():
    strItemType = 'Puffy Clouds'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Puffy_Clouds_ID_All():
    strItemType = 'Puffy Clouds'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Puffy_Clouds_ID_Selected():
    strItemType = 'Puffy Clouds'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Puffy_Clouds_ID_UnSelected():
    strItemType = 'Puffy Clouds'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Puffy_Clouds_Add_New():
    strItemType = 'val.Noise_PuffyClouds.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Ridged_Count_All():
    strItemType = 'Ridged'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Ridged_Count_Selected():
    strItemType = 'Ridged'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Ridged_Count_UnSelected():
    strItemType = 'Ridged'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Ridged_Name_All():
    strItemType = 'Ridged'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Ridged_Name_Selected():
    strItemType = 'Ridged'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Ridged_Name_UnSelected():
    strItemType = 'Ridged'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Ridged_ID_All():
    strItemType = 'Ridged'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Ridged_ID_Selected():
    strItemType = 'Ridged'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Ridged_ID_UnSelected():
    strItemType = 'Ridged'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Ridged_Add_New():
    strItemType = 'val.Noise_Ridged.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Scar_Count_All():
    strItemType = 'Scar'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Scar_Count_Selected():
    strItemType = 'Scar'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Scar_Count_UnSelected():
    strItemType = 'Scar'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Scar_Name_All():
    strItemType = 'Scar'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Scar_Name_Selected():
    strItemType = 'Scar'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Scar_Name_UnSelected():
    strItemType = 'Scar'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Scar_ID_All():
    strItemType = 'Scar'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Scar_ID_Selected():
    strItemType = 'Scar'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Scar_ID_UnSelected():
    strItemType = 'Scar'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Scar_Add_New():
    strItemType = 'val.Noise_Scar.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Scruffed_Count_All():
    strItemType = 'Scruffed'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Scruffed_Count_Selected():
    strItemType = 'Scruffed'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Scruffed_Count_UnSelected():
    strItemType = 'Scruffed'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Scruffed_Name_All():
    strItemType = 'Scruffed'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Scruffed_Name_Selected():
    strItemType = 'Scruffed'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Scruffed_Name_UnSelected():
    strItemType = 'Scruffed'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Scruffed_ID_All():
    strItemType = 'Scruffed'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Scruffed_ID_Selected():
    strItemType = 'Scruffed'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Scruffed_ID_UnSelected():
    strItemType = 'Scruffed'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Scruffed_Add_New():
    strItemType = 'val.Noise_Scruffed.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Strata_Count_All():
    strItemType = 'Strata'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Strata_Count_Selected():
    strItemType = 'Strata'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Strata_Count_UnSelected():
    strItemType = 'Strata'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Strata_Name_All():
    strItemType = 'Strata'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Strata_Name_Selected():
    strItemType = 'Strata'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Strata_Name_UnSelected():
    strItemType = 'Strata'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Strata_ID_All():
    strItemType = 'Strata'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Strata_ID_Selected():
    strItemType = 'Strata'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Strata_ID_UnSelected():
    strItemType = 'Strata'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Strata_Add_New():
    strItemType = 'val.Noise_Strata.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Stucco_Count_All():
    strItemType = 'Stucco'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Stucco_Count_Selected():
    strItemType = 'Stucco'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Stucco_Count_UnSelected():
    strItemType = 'Stucco'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Stucco_Name_All():
    strItemType = 'Stucco'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Stucco_Name_Selected():
    strItemType = 'Stucco'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Stucco_Name_UnSelected():
    strItemType = 'Stucco'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Stucco_ID_All():
    strItemType = 'Stucco'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Stucco_ID_Selected():
    strItemType = 'Stucco'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Stucco_ID_UnSelected():
    strItemType = 'Stucco'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Stucco_Add_New():
    strItemType = 'val.Noise_Stucco.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Vector_Bozo_Count_All():
    strItemType = 'Vector Bozo'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Vector_Bozo_Count_Selected():
    strItemType = 'Vector Bozo'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Vector_Bozo_Count_UnSelected():
    strItemType = 'Vector Bozo'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Vector_Bozo_Name_All():
    strItemType = 'Vector Bozo'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Vector_Bozo_Name_Selected():
    strItemType = 'Vector Bozo'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Vector_Bozo_Name_UnSelected():
    strItemType = 'Vector Bozo'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Vector_Bozo_ID_All():
    strItemType = 'Vector Bozo'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Vector_Bozo_ID_Selected():
    strItemType = 'Vector Bozo'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Vector_Bozo_ID_UnSelected():
    strItemType = 'Vector Bozo'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Vector_Bozo_Add_New():
    strItemType = 'val.Noise_VectorBozo.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Noise_Wrapped_fBm_Count_All():
    strItemType = 'Wrapped fBm'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Wrapped_fBm_Count_Selected():
    strItemType = 'Wrapped fBm'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Wrapped_fBm_Count_UnSelected():
    strItemType = 'Wrapped fBm'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Noise_Wrapped_fBm_Name_All():
    strItemType = 'Wrapped fBm'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Wrapped_fBm_Name_Selected():
    strItemType = 'Wrapped fBm'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Wrapped_fBm_Name_UnSelected():
    strItemType = 'Wrapped fBm'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Noise_Wrapped_fBm_ID_All():
    strItemType = 'Wrapped fBm'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Wrapped_fBm_ID_Selected():
    strItemType = 'Wrapped fBm'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Wrapped_fBm_ID_UnSelected():
    strItemType = 'Wrapped fBm'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Noise_Wrapped_fBm_Add_New():
    strItemType = 'val.Noise_WrappedfBm.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Art_Deco_Count_All():
    strItemType = 'Art Deco'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Art_Deco_Count_Selected():
    strItemType = 'Art Deco'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Art_Deco_Count_UnSelected():
    strItemType = 'Art Deco'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Art_Deco_Name_All():
    strItemType = 'Art Deco'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Art_Deco_Name_Selected():
    strItemType = 'Art Deco'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Art_Deco_Name_UnSelected():
    strItemType = 'Art Deco'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Art_Deco_ID_All():
    strItemType = 'Art Deco'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Art_Deco_ID_Selected():
    strItemType = 'Art Deco'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Art_Deco_ID_UnSelected():
    strItemType = 'Art Deco'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Art_Deco_Add_New():
    strItemType = 'val.Organic_ArtDeco.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Blister_Count_All():
    strItemType = 'Blister'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Blister_Count_Selected():
    strItemType = 'Blister'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Blister_Count_UnSelected():
    strItemType = 'Blister'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Blister_Name_All():
    strItemType = 'Blister'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Blister_Name_Selected():
    strItemType = 'Blister'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Blister_Name_UnSelected():
    strItemType = 'Blister'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Blister_ID_All():
    strItemType = 'Blister'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Blister_ID_Selected():
    strItemType = 'Blister'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Blister_ID_UnSelected():
    strItemType = 'Blister'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Blister_Add_New():
    strItemType = 'val.Organic_Blister.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Branches_Count_All():
    strItemType = 'Branches'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Branches_Count_Selected():
    strItemType = 'Branches'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Branches_Count_UnSelected():
    strItemType = 'Branches'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Branches_Name_All():
    strItemType = 'Branches'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Branches_Name_Selected():
    strItemType = 'Branches'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Branches_Name_UnSelected():
    strItemType = 'Branches'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Branches_ID_All():
    strItemType = 'Branches'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Branches_ID_Selected():
    strItemType = 'Branches'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Branches_ID_UnSelected():
    strItemType = 'Branches'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Branches_Add_New():
    strItemType = 'val.Organic_Branches.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Caustic_Count_All():
    strItemType = 'Caustic'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Caustic_Count_Selected():
    strItemType = 'Caustic'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Caustic_Count_UnSelected():
    strItemType = 'Caustic'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Caustic_Name_All():
    strItemType = 'Caustic'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Caustic_Name_Selected():
    strItemType = 'Caustic'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Caustic_Name_UnSelected():
    strItemType = 'Caustic'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Caustic_ID_All():
    strItemType = 'Caustic'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Caustic_ID_Selected():
    strItemType = 'Caustic'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Caustic_ID_UnSelected():
    strItemType = 'Caustic'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Caustic_Add_New():
    strItemType = 'val.Organic_Caustic.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Cellular_Count_All():
    strItemType = 'Cellular'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Cellular_Count_Selected():
    strItemType = 'Cellular'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Cellular_Count_UnSelected():
    strItemType = 'Cellular'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Cellular_Name_All():
    strItemType = 'Cellular'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Cellular_Name_Selected():
    strItemType = 'Cellular'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Cellular_Name_UnSelected():
    strItemType = 'Cellular'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Cellular_ID_All():
    strItemType = 'Cellular'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Cellular_ID_Selected():
    strItemType = 'Cellular'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Cellular_ID_UnSelected():
    strItemType = 'Cellular'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Cellular_Add_New():
    strItemType = 'val.Organic_Cellular.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Cheesy_Count_All():
    strItemType = 'Cheesy'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Cheesy_Count_Selected():
    strItemType = 'Cheesy'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Cheesy_Count_UnSelected():
    strItemType = 'Cheesy'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Cheesy_Name_All():
    strItemType = 'Cheesy'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Cheesy_Name_Selected():
    strItemType = 'Cheesy'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Cheesy_Name_UnSelected():
    strItemType = 'Cheesy'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Cheesy_ID_All():
    strItemType = 'Cheesy'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Cheesy_ID_Selected():
    strItemType = 'Cheesy'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Cheesy_ID_UnSelected():
    strItemType = 'Cheesy'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Cheesy_Add_New():
    strItemType = 'val.Organic_Cheesy.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Concrete_Count_All():
    strItemType = 'Concrete'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Concrete_Count_Selected():
    strItemType = 'Concrete'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Concrete_Count_UnSelected():
    strItemType = 'Concrete'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Concrete_Name_All():
    strItemType = 'Concrete'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Concrete_Name_Selected():
    strItemType = 'Concrete'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Concrete_Name_UnSelected():
    strItemType = 'Concrete'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Concrete_ID_All():
    strItemType = 'Concrete'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Concrete_ID_Selected():
    strItemType = 'Concrete'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Concrete_ID_UnSelected():
    strItemType = 'Concrete'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Concrete_Add_New():
    strItemType = 'val.Organic_Concrete.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Crackle_Count_All():
    strItemType = 'Crackle'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Crackle_Count_Selected():
    strItemType = 'Crackle'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Crackle_Count_UnSelected():
    strItemType = 'Crackle'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Crackle_Name_All():
    strItemType = 'Crackle'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Crackle_Name_Selected():
    strItemType = 'Crackle'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Crackle_Name_UnSelected():
    strItemType = 'Crackle'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Crackle_ID_All():
    strItemType = 'Crackle'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Crackle_ID_Selected():
    strItemType = 'Crackle'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Crackle_ID_UnSelected():
    strItemType = 'Crackle'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Crackle_Add_New():
    strItemType = 'val.Organic_Crackle.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Dirt_Count_All():
    strItemType = 'Dirt'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Dirt_Count_Selected():
    strItemType = 'Dirt'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Dirt_Count_UnSelected():
    strItemType = 'Dirt'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Dirt_Name_All():
    strItemType = 'Dirt'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Dirt_Name_Selected():
    strItemType = 'Dirt'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Dirt_Name_UnSelected():
    strItemType = 'Dirt'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Dirt_ID_All():
    strItemType = 'Dirt'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Dirt_ID_Selected():
    strItemType = 'Dirt'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Dirt_ID_UnSelected():
    strItemType = 'Dirt'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Dirt_Add_New():
    strItemType = 'val.Organic_Dirt.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Disturbed_Count_All():
    strItemType = 'Disturbed'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Disturbed_Count_Selected():
    strItemType = 'Disturbed'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Disturbed_Count_UnSelected():
    strItemType = 'Disturbed'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Disturbed_Name_All():
    strItemType = 'Disturbed'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Disturbed_Name_Selected():
    strItemType = 'Disturbed'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Disturbed_Name_UnSelected():
    strItemType = 'Disturbed'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Disturbed_ID_All():
    strItemType = 'Disturbed'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Disturbed_ID_Selected():
    strItemType = 'Disturbed'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Disturbed_ID_UnSelected():
    strItemType = 'Disturbed'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Disturbed_Add_New():
    strItemType = 'val.Organic_Disturbed.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Easy_Wood_Count_All():
    strItemType = 'Easy Wood'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Easy_Wood_Count_Selected():
    strItemType = 'Easy Wood'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Easy_Wood_Count_UnSelected():
    strItemType = 'Easy Wood'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Easy_Wood_Name_All():
    strItemType = 'Easy Wood'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Easy_Wood_Name_Selected():
    strItemType = 'Easy Wood'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Easy_Wood_Name_UnSelected():
    strItemType = 'Easy Wood'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Easy_Wood_ID_All():
    strItemType = 'Easy Wood'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Easy_Wood_ID_Selected():
    strItemType = 'Easy Wood'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Easy_Wood_ID_UnSelected():
    strItemType = 'Easy Wood'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Easy_Wood_Add_New():
    strItemType = 'val.Organic_EasyWood.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Electric_Count_All():
    strItemType = 'Electric'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Electric_Count_Selected():
    strItemType = 'Electric'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Electric_Count_UnSelected():
    strItemType = 'Electric'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Electric_Name_All():
    strItemType = 'Electric'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Electric_Name_Selected():
    strItemType = 'Electric'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Electric_Name_UnSelected():
    strItemType = 'Electric'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Electric_ID_All():
    strItemType = 'Electric'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Electric_ID_Selected():
    strItemType = 'Electric'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Electric_ID_UnSelected():
    strItemType = 'Electric'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Electric_Add_New():
    strItemType = 'val.Organic_Electric.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Fire_Count_All():
    strItemType = 'Fire'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Fire_Count_Selected():
    strItemType = 'Fire'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Fire_Count_UnSelected():
    strItemType = 'Fire'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Fire_Name_All():
    strItemType = 'Fire'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Fire_Name_Selected():
    strItemType = 'Fire'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Fire_Name_UnSelected():
    strItemType = 'Fire'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Fire_ID_All():
    strItemType = 'Fire'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Fire_ID_Selected():
    strItemType = 'Fire'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Fire_ID_UnSelected():
    strItemType = 'Fire'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Fire_Add_New():
    strItemType = 'val.Organic_Fire.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Firewall_Count_All():
    strItemType = 'Firewall'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Firewall_Count_Selected():
    strItemType = 'Firewall'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Firewall_Count_UnSelected():
    strItemType = 'Firewall'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Firewall_Name_All():
    strItemType = 'Firewall'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Firewall_Name_Selected():
    strItemType = 'Firewall'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Firewall_Name_UnSelected():
    strItemType = 'Firewall'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Firewall_ID_All():
    strItemType = 'Firewall'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Firewall_ID_Selected():
    strItemType = 'Firewall'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Firewall_ID_UnSelected():
    strItemType = 'Firewall'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Firewall_Add_New():
    strItemType = 'val.Organic_FireWall.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Hardwood_Count_All():
    strItemType = 'Hardwood'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Hardwood_Count_Selected():
    strItemType = 'Hardwood'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Hardwood_Count_UnSelected():
    strItemType = 'Hardwood'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Hardwood_Name_All():
    strItemType = 'Hardwood'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Hardwood_Name_Selected():
    strItemType = 'Hardwood'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Hardwood_Name_UnSelected():
    strItemType = 'Hardwood'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Hardwood_ID_All():
    strItemType = 'Hardwood'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Hardwood_ID_Selected():
    strItemType = 'Hardwood'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Hardwood_ID_UnSelected():
    strItemType = 'Hardwood'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Hardwood_Add_New():
    strItemType = 'val.Organic_HardWood.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Membrane_Count_All():
    strItemType = 'Membrane'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Membrane_Count_Selected():
    strItemType = 'Membrane'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Membrane_Count_UnSelected():
    strItemType = 'Membrane'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Membrane_Name_All():
    strItemType = 'Membrane'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Membrane_Name_Selected():
    strItemType = 'Membrane'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Membrane_Name_UnSelected():
    strItemType = 'Membrane'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Membrane_ID_All():
    strItemType = 'Membrane'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Membrane_ID_Selected():
    strItemType = 'Membrane'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Membrane_ID_UnSelected():
    strItemType = 'Membrane'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Membrane_Add_New():
    strItemType = 'val.Organic_Membrane.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Minky_Count_All():
    strItemType = 'Minky'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Minky_Count_Selected():
    strItemType = 'Minky'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Minky_Count_UnSelected():
    strItemType = 'Minky'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Minky_Name_All():
    strItemType = 'Minky'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Minky_Name_Selected():
    strItemType = 'Minky'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Minky_Name_UnSelected():
    strItemType = 'Minky'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Minky_ID_All():
    strItemType = 'Minky'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Minky_ID_Selected():
    strItemType = 'Minky'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Minky_ID_UnSelected():
    strItemType = 'Minky'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Minky_Add_New():
    strItemType = 'val.Organic_Minky.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Scatter_Count_All():
    strItemType = 'Scatter'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Scatter_Count_Selected():
    strItemType = 'Scatter'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Scatter_Count_UnSelected():
    strItemType = 'Scatter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Scatter_Name_All():
    strItemType = 'Scatter'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Scatter_Name_Selected():
    strItemType = 'Scatter'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Scatter_Name_UnSelected():
    strItemType = 'Scatter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Scatter_ID_All():
    strItemType = 'Scatter'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Scatter_ID_Selected():
    strItemType = 'Scatter'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Scatter_ID_UnSelected():
    strItemType = 'Scatter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Scatter_Add_New():
    strItemType = 'val.Organic_Scatter.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Sin_Blob_Count_All():
    strItemType = 'Sin Blob'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Sin_Blob_Count_Selected():
    strItemType = 'Sin Blob'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Sin_Blob_Count_UnSelected():
    strItemType = 'Sin Blob'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Sin_Blob_Name_All():
    strItemType = 'Sin Blob'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Sin_Blob_Name_Selected():
    strItemType = 'Sin Blob'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Sin_Blob_Name_UnSelected():
    strItemType = 'Sin Blob'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Sin_Blob_ID_All():
    strItemType = 'Sin Blob'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Sin_Blob_ID_Selected():
    strItemType = 'Sin Blob'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Sin_Blob_ID_UnSelected():
    strItemType = 'Sin Blob'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Sin_Blob_Add_New():
    strItemType = 'val.Organic_SinBlob.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Veins_Count_All():
    strItemType = 'Veins'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Veins_Count_Selected():
    strItemType = 'Veins'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Veins_Count_UnSelected():
    strItemType = 'Veins'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Veins_Name_All():
    strItemType = 'Veins'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Veins_Name_Selected():
    strItemType = 'Veins'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Veins_Name_UnSelected():
    strItemType = 'Veins'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Veins_ID_All():
    strItemType = 'Veins'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Veins_ID_Selected():
    strItemType = 'Veins'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Veins_ID_UnSelected():
    strItemType = 'Veins'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Veins_Add_New():
    strItemType = 'val.Organic_Veins.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Wires_Count_All():
    strItemType = 'Wires'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Wires_Count_Selected():
    strItemType = 'Wires'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Wires_Count_UnSelected():
    strItemType = 'Wires'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Wires_Name_All():
    strItemType = 'Wires'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Wires_Name_Selected():
    strItemType = 'Wires'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Wires_Name_UnSelected():
    strItemType = 'Wires'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Wires_ID_All():
    strItemType = 'Wires'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Wires_ID_Selected():
    strItemType = 'Wires'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Wires_ID_UnSelected():
    strItemType = 'Wires'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Wires_Add_New():
    strItemType = 'val.Organic_Wires.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Organic_Worm_Vein_Count_All():
    strItemType = 'Worm Vein'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Worm_Vein_Count_Selected():
    strItemType = 'Worm Vein'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Worm_Vein_Count_UnSelected():
    strItemType = 'Worm Vein'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Organic_Worm_Vein_Name_All():
    strItemType = 'Worm Vein'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Worm_Vein_Name_Selected():
    strItemType = 'Worm Vein'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Worm_Vein_Name_UnSelected():
    strItemType = 'Worm Vein'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Organic_Worm_Vein_ID_All():
    strItemType = 'Worm Vein'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Worm_Vein_ID_Selected():
    strItemType = 'Worm Vein'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Worm_Vein_ID_UnSelected():
    strItemType = 'Worm Vein'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Organic_Worm_Vein_Add_New():
    strItemType = 'val.Organic_WormVein.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Panels_Peel_Count_All():
    strItemType = 'Peel'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Peel_Count_Selected():
    strItemType = 'Peel'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Peel_Count_UnSelected():
    strItemType = 'Peel'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Peel_Name_All():
    strItemType = 'Peel'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Peel_Name_Selected():
    strItemType = 'Peel'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Peel_Name_UnSelected():
    strItemType = 'Peel'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Peel_ID_All():
    strItemType = 'Peel'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Peel_ID_Selected():
    strItemType = 'Peel'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Peel_ID_UnSelected():
    strItemType = 'Peel'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Peel_Add_New():
    strItemType = 'val.Panels_Peel.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Panels_Plates_Count_All():
    strItemType = 'Plates'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Plates_Count_Selected():
    strItemType = 'Plates'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Plates_Count_UnSelected():
    strItemType = 'Plates'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Plates_Name_All():
    strItemType = 'Plates'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Plates_Name_Selected():
    strItemType = 'Plates'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Plates_Name_UnSelected():
    strItemType = 'Plates'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Plates_ID_All():
    strItemType = 'Plates'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Plates_ID_Selected():
    strItemType = 'Plates'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Plates_ID_UnSelected():
    strItemType = 'Plates'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Plates_Add_New():
    strItemType = 'val.Panels_Plates.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Panels_Rivet_Rust_Count_All():
    strItemType = 'Rivet Rust'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Rivet_Rust_Count_Selected():
    strItemType = 'Rivet Rust'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Rivet_Rust_Count_UnSelected():
    strItemType = 'Rivet Rust'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Rivet_Rust_Name_All():
    strItemType = 'Rivet Rust'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Rivet_Rust_Name_Selected():
    strItemType = 'Rivet Rust'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Rivet_Rust_Name_UnSelected():
    strItemType = 'Rivet Rust'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Rivet_Rust_ID_All():
    strItemType = 'Rivet Rust'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Rivet_Rust_ID_Selected():
    strItemType = 'Rivet Rust'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Rivet_Rust_ID_UnSelected():
    strItemType = 'Rivet Rust'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Rivet_Rust_Add_New():
    strItemType = 'val.Panels_RivetRust.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Panels_Rivets_Count_All():
    strItemType = 'Rivets'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Rivets_Count_Selected():
    strItemType = 'Rivets'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Rivets_Count_UnSelected():
    strItemType = 'Rivets'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Rivets_Name_All():
    strItemType = 'Rivets'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Rivets_Name_Selected():
    strItemType = 'Rivets'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Rivets_Name_UnSelected():
    strItemType = 'Rivets'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Rivets_ID_All():
    strItemType = 'Rivets'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Rivets_ID_Selected():
    strItemType = 'Rivets'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Rivets_ID_UnSelected():
    strItemType = 'Rivets'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Rivets_Add_New():
    strItemType = 'val.Panels_Rivets.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Panels_Rust_Count_All():
    strItemType = 'Rust'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Rust_Count_Selected():
    strItemType = 'Rust'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Rust_Count_UnSelected():
    strItemType = 'Rust'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Rust_Name_All():
    strItemType = 'Rust'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Rust_Name_Selected():
    strItemType = 'Rust'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Rust_Name_UnSelected():
    strItemType = 'Rust'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Rust_ID_All():
    strItemType = 'Rust'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Rust_ID_Selected():
    strItemType = 'Rust'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Rust_ID_UnSelected():
    strItemType = 'Rust'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Rust_Add_New():
    strItemType = 'val.Panels_Rust.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Panels_Smear_Count_All():
    strItemType = 'Smear'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Smear_Count_Selected():
    strItemType = 'Smear'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Smear_Count_UnSelected():
    strItemType = 'Smear'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Panels_Smear_Name_All():
    strItemType = 'Smear'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Smear_Name_Selected():
    strItemType = 'Smear'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Smear_Name_UnSelected():
    strItemType = 'Smear'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Panels_Smear_ID_All():
    strItemType = 'Smear'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Smear_ID_Selected():
    strItemType = 'Smear'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Smear_ID_UnSelected():
    strItemType = 'Smear'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Panels_Smear_Add_New():
    strItemType = 'val.Panels_Smear.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Process_Easy_Gradient_Count_All():
    strItemType = 'Easy Gradient'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Process_Easy_Gradient_Count_Selected():
    strItemType = 'Easy Gradient'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Process_Easy_Gradient_Count_UnSelected():
    strItemType = 'Easy Gradient'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Process_Easy_Gradient_Name_All():
    strItemType = 'Easy Gradient'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Process_Easy_Gradient_Name_Selected():
    strItemType = 'Easy Gradient'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Process_Easy_Gradient_Name_UnSelected():
    strItemType = 'Easy Gradient'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Process_Easy_Gradient_ID_All():
    strItemType = 'Easy Gradient'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Process_Easy_Gradient_ID_Selected():
    strItemType = 'Easy Gradient'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Process_Easy_Gradient_ID_UnSelected():
    strItemType = 'Easy Gradient'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Process_Easy_Gradient_Add_New():
    strItemType = 'val.Process_EasyGrad.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Process_Regional_HSV_Count_All():
    strItemType = 'Regional HSV'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Process_Regional_HSV_Count_Selected():
    strItemType = 'Regional HSV'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Process_Regional_HSV_Count_UnSelected():
    strItemType = 'Regional HSV'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Process_Regional_HSV_Name_All():
    strItemType = 'Regional HSV'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Process_Regional_HSV_Name_Selected():
    strItemType = 'Regional HSV'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Process_Regional_HSV_Name_UnSelected():
    strItemType = 'Regional HSV'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Process_Regional_HSV_ID_All():
    strItemType = 'Regional HSV'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Process_Regional_HSV_ID_Selected():
    strItemType = 'Regional HSV'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Process_Regional_HSV_ID_UnSelected():
    strItemType = 'Regional HSV'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Process_Regional_HSV_Add_New():
    strItemType = 'val.Process_RegionalHSV.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Skins_Camo_Count_All():
    strItemType = 'Camo'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Camo_Count_Selected():
    strItemType = 'Camo'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Camo_Count_UnSelected():
    strItemType = 'Camo'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Camo_Name_All():
    strItemType = 'Camo'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Camo_Name_Selected():
    strItemType = 'Camo'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Camo_Name_UnSelected():
    strItemType = 'Camo'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Camo_ID_All():
    strItemType = 'Camo'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Camo_ID_Selected():
    strItemType = 'Camo'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Camo_ID_UnSelected():
    strItemType = 'Camo'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Camo_Add_New():
    strItemType = 'val.Skins_Camo.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Skins_Crumpled_Count_All():
    strItemType = 'Crumpled'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Crumpled_Count_Selected():
    strItemType = 'Crumpled'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Crumpled_Count_UnSelected():
    strItemType = 'Crumpled'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Crumpled_Name_All():
    strItemType = 'Crumpled'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Crumpled_Name_Selected():
    strItemType = 'Crumpled'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Crumpled_Name_UnSelected():
    strItemType = 'Crumpled'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Crumpled_ID_All():
    strItemType = 'Crumpled'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Crumpled_ID_Selected():
    strItemType = 'Crumpled'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Crumpled_ID_UnSelected():
    strItemType = 'Crumpled'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Crumpled_Add_New():
    strItemType = 'val.Skins_Crumpled.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Skins_Dino_Skin_Count_All():
    strItemType = 'Dino Skin'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Dino_Skin_Count_Selected():
    strItemType = 'Dino Skin'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Dino_Skin_Count_UnSelected():
    strItemType = 'Dino Skin'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Dino_Skin_Name_All():
    strItemType = 'Dino Skin'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Dino_Skin_Name_Selected():
    strItemType = 'Dino Skin'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Dino_Skin_Name_UnSelected():
    strItemType = 'Dino Skin'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Dino_Skin_ID_All():
    strItemType = 'Dino Skin'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Dino_Skin_ID_Selected():
    strItemType = 'Dino Skin'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Dino_Skin_ID_UnSelected():
    strItemType = 'Dino Skin'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Dino_Skin_Add_New():
    strItemType = 'val.Skins_DinoSkin.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Skins_Disease_Count_All():
    strItemType = 'Disease'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Disease_Count_Selected():
    strItemType = 'Disease'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Disease_Count_UnSelected():
    strItemType = 'Disease'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Disease_Name_All():
    strItemType = 'Disease'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Disease_Name_Selected():
    strItemType = 'Disease'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Disease_Name_UnSelected():
    strItemType = 'Disease'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Disease_ID_All():
    strItemType = 'Disease'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Disease_ID_Selected():
    strItemType = 'Disease'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Disease_ID_UnSelected():
    strItemType = 'Disease'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Disease_Add_New():
    strItemType = 'val.Skins_Disease.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Skins_Frog_Skin_Count_All():
    strItemType = 'Frog Skin'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Frog_Skin_Count_Selected():
    strItemType = 'Frog Skin'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Frog_Skin_Count_UnSelected():
    strItemType = 'Frog Skin'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Frog_Skin_Name_All():
    strItemType = 'Frog Skin'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Frog_Skin_Name_Selected():
    strItemType = 'Frog Skin'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Frog_Skin_Name_UnSelected():
    strItemType = 'Frog Skin'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Frog_Skin_ID_All():
    strItemType = 'Frog Skin'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Frog_Skin_ID_Selected():
    strItemType = 'Frog Skin'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Frog_Skin_ID_UnSelected():
    strItemType = 'Frog Skin'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Frog_Skin_Add_New():
    strItemType = 'val.Skins_FrogSkin.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Skins_Grainy_Wood_Count_All():
    strItemType = 'Grainy Wood'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Grainy_Wood_Count_Selected():
    strItemType = 'Grainy Wood'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Grainy_Wood_Count_UnSelected():
    strItemType = 'Grainy Wood'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Grainy_Wood_Name_All():
    strItemType = 'Grainy Wood'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Grainy_Wood_Name_Selected():
    strItemType = 'Grainy Wood'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Grainy_Wood_Name_UnSelected():
    strItemType = 'Grainy Wood'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Grainy_Wood_ID_All():
    strItemType = 'Grainy Wood'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Grainy_Wood_ID_Selected():
    strItemType = 'Grainy Wood'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Grainy_Wood_ID_UnSelected():
    strItemType = 'Grainy Wood'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Grainy_Wood_Add_New():
    strItemType = 'val.Skins_GrainyWood.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Skins_Leather_Count_All():
    strItemType = 'Leather'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Leather_Count_Selected():
    strItemType = 'Leather'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Leather_Count_UnSelected():
    strItemType = 'Leather'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Leather_Name_All():
    strItemType = 'Leather'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Leather_Name_Selected():
    strItemType = 'Leather'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Leather_Name_UnSelected():
    strItemType = 'Leather'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Leather_ID_All():
    strItemType = 'Leather'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Leather_ID_Selected():
    strItemType = 'Leather'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Leather_ID_UnSelected():
    strItemType = 'Leather'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Leather_Add_New():
    strItemType = 'val.Skins_Leather.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Skins_Monster_Count_All():
    strItemType = 'Monster'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Monster_Count_Selected():
    strItemType = 'Monster'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Monster_Count_UnSelected():
    strItemType = 'Monster'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Monster_Name_All():
    strItemType = 'Monster'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Monster_Name_Selected():
    strItemType = 'Monster'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Monster_Name_UnSelected():
    strItemType = 'Monster'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Monster_ID_All():
    strItemType = 'Monster'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Monster_ID_Selected():
    strItemType = 'Monster'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Monster_ID_UnSelected():
    strItemType = 'Monster'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Monster_Add_New():
    strItemType = 'val.Skins_Monster.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Skins_Pastella_Count_All():
    strItemType = 'Pastella'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Pastella_Count_Selected():
    strItemType = 'Pastella'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Pastella_Count_UnSelected():
    strItemType = 'Pastella'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Pastella_Name_All():
    strItemType = 'Pastella'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Pastella_Name_Selected():
    strItemType = 'Pastella'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Pastella_Name_UnSelected():
    strItemType = 'Pastella'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Pastella_ID_All():
    strItemType = 'Pastella'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Pastella_ID_Selected():
    strItemType = 'Pastella'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Pastella_ID_UnSelected():
    strItemType = 'Pastella'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Pastella_Add_New():
    strItemType = 'val.Skins_Pastella.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Skins_Peened_Count_All():
    strItemType = 'Peened'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Peened_Count_Selected():
    strItemType = 'Peened'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Peened_Count_UnSelected():
    strItemType = 'Peened'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Peened_Name_All():
    strItemType = 'Peened'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Peened_Name_Selected():
    strItemType = 'Peened'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Peened_Name_UnSelected():
    strItemType = 'Peened'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Peened_ID_All():
    strItemType = 'Peened'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Peened_ID_Selected():
    strItemType = 'Peened'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Peened_ID_UnSelected():
    strItemType = 'Peened'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Peened_Add_New():
    strItemType = 'val.Skins_Peened.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Skins_Scratches_Count_All():
    strItemType = 'Scratches'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Scratches_Count_Selected():
    strItemType = 'Scratches'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Scratches_Count_UnSelected():
    strItemType = 'Scratches'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Skins_Scratches_Name_All():
    strItemType = 'Scratches'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Scratches_Name_Selected():
    strItemType = 'Scratches'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Scratches_Name_UnSelected():
    strItemType = 'Scratches'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Skins_Scratches_ID_All():
    strItemType = 'Scratches'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Scratches_ID_Selected():
    strItemType = 'Scratches'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Scratches_ID_UnSelected():
    strItemType = 'Scratches'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Skins_Scratches_Add_New():
    strItemType = 'val.Skins_Scratches.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Space_Blast_Count_All():
    strItemType = 'Blast'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Blast_Count_Selected():
    strItemType = 'Blast'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Blast_Count_UnSelected():
    strItemType = 'Blast'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Blast_Name_All():
    strItemType = 'Blast'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Blast_Name_Selected():
    strItemType = 'Blast'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Blast_Name_UnSelected():
    strItemType = 'Blast'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Blast_ID_All():
    strItemType = 'Blast'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Blast_ID_Selected():
    strItemType = 'Blast'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Blast_ID_UnSelected():
    strItemType = 'Blast'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Blast_Add_New():
    strItemType = 'val.Space_Blast.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Space_Coriolis_Count_All():
    strItemType = 'Coriolis'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Coriolis_Count_Selected():
    strItemType = 'Coriolis'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Coriolis_Count_UnSelected():
    strItemType = 'Coriolis'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Coriolis_Name_All():
    strItemType = 'Coriolis'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Coriolis_Name_Selected():
    strItemType = 'Coriolis'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Coriolis_Name_UnSelected():
    strItemType = 'Coriolis'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Coriolis_ID_All():
    strItemType = 'Coriolis'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Coriolis_ID_Selected():
    strItemType = 'Coriolis'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Coriolis_ID_UnSelected():
    strItemType = 'Coriolis'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Coriolis_Add_New():
    strItemType = 'val.Space_Coriolis.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Space_Flare_Count_All():
    strItemType = 'Flare'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Flare_Count_Selected():
    strItemType = 'Flare'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Flare_Count_UnSelected():
    strItemType = 'Flare'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Flare_Name_All():
    strItemType = 'Flare'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Flare_Name_Selected():
    strItemType = 'Flare'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Flare_Name_UnSelected():
    strItemType = 'Flare'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Flare_ID_All():
    strItemType = 'Flare'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Flare_ID_Selected():
    strItemType = 'Flare'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Flare_ID_UnSelected():
    strItemType = 'Flare'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Flare_Add_New():
    strItemType = 'val.Space_Flare.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Space_Gas_Giant_Count_All():
    strItemType = 'Gas Giant'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Gas_Giant_Count_Selected():
    strItemType = 'Gas Giant'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Gas_Giant_Count_UnSelected():
    strItemType = 'Gas Giant'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Gas_Giant_Name_All():
    strItemType = 'Gas Giant'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Gas_Giant_Name_Selected():
    strItemType = 'Gas Giant'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Gas_Giant_Name_UnSelected():
    strItemType = 'Gas Giant'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Gas_Giant_ID_All():
    strItemType = 'Gas Giant'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Gas_Giant_ID_Selected():
    strItemType = 'Gas Giant'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Gas_Giant_ID_UnSelected():
    strItemType = 'Gas Giant'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Gas_Giant_Add_New():
    strItemType = 'val.Space_GasGiant.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Space_Glint_Count_All():
    strItemType = 'Glint'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Glint_Count_Selected():
    strItemType = 'Glint'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Glint_Count_UnSelected():
    strItemType = 'Glint'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Glint_Name_All():
    strItemType = 'Glint'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Glint_Name_Selected():
    strItemType = 'Glint'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Glint_Name_UnSelected():
    strItemType = 'Glint'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Glint_ID_All():
    strItemType = 'Glint'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Glint_ID_Selected():
    strItemType = 'Glint'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Glint_ID_UnSelected():
    strItemType = 'Glint'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Glint_Add_New():
    strItemType = 'val.Space_Glint.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Space_Hurricane_Count_All():
    strItemType = 'Hurricane'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Hurricane_Count_Selected():
    strItemType = 'Hurricane'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Hurricane_Count_UnSelected():
    strItemType = 'Hurricane'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Hurricane_Name_All():
    strItemType = 'Hurricane'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Hurricane_Name_Selected():
    strItemType = 'Hurricane'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Hurricane_Name_UnSelected():
    strItemType = 'Hurricane'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Hurricane_ID_All():
    strItemType = 'Hurricane'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Hurricane_ID_Selected():
    strItemType = 'Hurricane'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Hurricane_ID_UnSelected():
    strItemType = 'Hurricane'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Hurricane_Add_New():
    strItemType = 'val.Space_Hurricane.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Space_Nurnies_Count_All():
    strItemType = 'Nurnies'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Nurnies_Count_Selected():
    strItemType = 'Nurnies'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Nurnies_Count_UnSelected():
    strItemType = 'Nurnies'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Nurnies_Name_All():
    strItemType = 'Nurnies'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Nurnies_Name_Selected():
    strItemType = 'Nurnies'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Nurnies_Name_UnSelected():
    strItemType = 'Nurnies'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Nurnies_ID_All():
    strItemType = 'Nurnies'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Nurnies_ID_Selected():
    strItemType = 'Nurnies'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Nurnies_ID_UnSelected():
    strItemType = 'Nurnies'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Nurnies_Add_New():
    strItemType = 'val.Space_Nurnies.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Space_Planet_Count_All():
    strItemType = 'Planet'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Planet_Count_Selected():
    strItemType = 'Planet'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Planet_Count_UnSelected():
    strItemType = 'Planet'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Planet_Name_All():
    strItemType = 'Planet'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Planet_Name_Selected():
    strItemType = 'Planet'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Planet_Name_UnSelected():
    strItemType = 'Planet'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Planet_ID_All():
    strItemType = 'Planet'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Planet_ID_Selected():
    strItemType = 'Planet'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Planet_ID_UnSelected():
    strItemType = 'Planet'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Planet_Add_New():
    strItemType = 'val.Space_Planet.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Space_Planet_Clouds_Count_All():
    strItemType = 'Planet Clouds'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Planet_Clouds_Count_Selected():
    strItemType = 'Planet Clouds'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Planet_Clouds_Count_UnSelected():
    strItemType = 'Planet Clouds'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Planet_Clouds_Name_All():
    strItemType = 'Planet Clouds'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Planet_Clouds_Name_Selected():
    strItemType = 'Planet Clouds'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Planet_Clouds_Name_UnSelected():
    strItemType = 'Planet Clouds'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Planet_Clouds_ID_All():
    strItemType = 'Planet Clouds'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Planet_Clouds_ID_Selected():
    strItemType = 'Planet Clouds'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Planet_Clouds_ID_UnSelected():
    strItemType = 'Planet Clouds'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Planet_Clouds_Add_New():
    strItemType = 'val.Space_PlanetClouds.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Space_Rings_Count_All():
    strItemType = 'Rings'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Rings_Count_Selected():
    strItemType = 'Rings'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Rings_Count_UnSelected():
    strItemType = 'Rings'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Rings_Name_All():
    strItemType = 'Rings'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Rings_Name_Selected():
    strItemType = 'Rings'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Rings_Name_UnSelected():
    strItemType = 'Rings'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Rings_ID_All():
    strItemType = 'Rings'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Rings_ID_Selected():
    strItemType = 'Rings'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Rings_ID_UnSelected():
    strItemType = 'Rings'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Rings_Add_New():
    strItemType = 'val.Space_Rings.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Space_Star_Field_Count_All():
    strItemType = 'Star Field'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Star_Field_Count_Selected():
    strItemType = 'Star Field'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Star_Field_Count_UnSelected():
    strItemType = 'Star Field'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Star_Field_Name_All():
    strItemType = 'Star Field'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Star_Field_Name_Selected():
    strItemType = 'Star Field'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Star_Field_Name_UnSelected():
    strItemType = 'Star Field'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Star_Field_ID_All():
    strItemType = 'Star Field'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Star_Field_ID_Selected():
    strItemType = 'Star Field'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Star_Field_ID_UnSelected():
    strItemType = 'Star Field'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Star_Field_Add_New():
    strItemType = 'val.Space_StarField.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Space_Swirl_Count_All():
    strItemType = 'Swirl'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Swirl_Count_Selected():
    strItemType = 'Swirl'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Swirl_Count_UnSelected():
    strItemType = 'Swirl'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Swirl_Name_All():
    strItemType = 'Swirl'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Swirl_Name_Selected():
    strItemType = 'Swirl'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Swirl_Name_UnSelected():
    strItemType = 'Swirl'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Swirl_ID_All():
    strItemType = 'Swirl'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Swirl_ID_Selected():
    strItemType = 'Swirl'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Swirl_ID_UnSelected():
    strItemType = 'Swirl'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Swirl_Add_New():
    strItemType = 'val.Space_Swirl.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Space_Terra_Count_All():
    strItemType = 'Terra'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Terra_Count_Selected():
    strItemType = 'Terra'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Terra_Count_UnSelected():
    strItemType = 'Terra'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Terra_Name_All():
    strItemType = 'Terra'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Terra_Name_Selected():
    strItemType = 'Terra'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Terra_Name_UnSelected():
    strItemType = 'Terra'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Terra_ID_All():
    strItemType = 'Terra'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Terra_ID_Selected():
    strItemType = 'Terra'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Terra_ID_UnSelected():
    strItemType = 'Terra'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Terra_Add_New():
    strItemType = 'val.Space_Terra.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Space_Windows_Count_All():
    strItemType = 'Windows'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Windows_Count_Selected():
    strItemType = 'Windows'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Windows_Count_UnSelected():
    strItemType = 'Windows'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Space_Windows_Name_All():
    strItemType = 'Windows'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Windows_Name_Selected():
    strItemType = 'Windows'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Windows_Name_UnSelected():
    strItemType = 'Windows'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Space_Windows_ID_All():
    strItemType = 'Windows'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Windows_ID_Selected():
    strItemType = 'Windows'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Windows_ID_UnSelected():
    strItemType = 'Windows'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Space_Windows_Add_New():
    strItemType = 'val.Space_Windows.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Basket_Count_All():
    strItemType = 'Basket'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Basket_Count_Selected():
    strItemType = 'Basket'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Basket_Count_UnSelected():
    strItemType = 'Basket'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Basket_Name_All():
    strItemType = 'Basket'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Basket_Name_Selected():
    strItemType = 'Basket'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Basket_Name_UnSelected():
    strItemType = 'Basket'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Basket_ID_All():
    strItemType = 'Basket'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Basket_ID_Selected():
    strItemType = 'Basket'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Basket_ID_UnSelected():
    strItemType = 'Basket'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Basket_Add_New():
    strItemType = 'val.Tiles_Basket.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Bath_Tile_Count_All():
    strItemType = 'Bath Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Bath_Tile_Count_Selected():
    strItemType = 'Bath Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Bath_Tile_Count_UnSelected():
    strItemType = 'Bath Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Bath_Tile_Name_All():
    strItemType = 'Bath Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Bath_Tile_Name_Selected():
    strItemType = 'Bath Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Bath_Tile_Name_UnSelected():
    strItemType = 'Bath Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Bath_Tile_ID_All():
    strItemType = 'Bath Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Bath_Tile_ID_Selected():
    strItemType = 'Bath Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Bath_Tile_ID_UnSelected():
    strItemType = 'Bath Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Bath_Tile_Add_New():
    strItemType = 'val.Tiles_BathTile.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Bricks_Count_All():
    strItemType = 'Bricks'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Bricks_Count_Selected():
    strItemType = 'Bricks'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Bricks_Count_UnSelected():
    strItemType = 'Bricks'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Bricks_Name_All():
    strItemType = 'Bricks'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Bricks_Name_Selected():
    strItemType = 'Bricks'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Bricks_Name_UnSelected():
    strItemType = 'Bricks'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Bricks_ID_All():
    strItemType = 'Bricks'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Bricks_ID_Selected():
    strItemType = 'Bricks'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Bricks_ID_UnSelected():
    strItemType = 'Bricks'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Bricks_Add_New():
    strItemType = 'val.Tiles_Bricks.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Checks_Count_All():
    strItemType = 'Checks'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Checks_Count_Selected():
    strItemType = 'Checks'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Checks_Count_UnSelected():
    strItemType = 'Checks'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Checks_Name_All():
    strItemType = 'Checks'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Checks_Name_Selected():
    strItemType = 'Checks'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Checks_Name_UnSelected():
    strItemType = 'Checks'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Checks_ID_All():
    strItemType = 'Checks'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Checks_ID_Selected():
    strItemType = 'Checks'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Checks_ID_UnSelected():
    strItemType = 'Checks'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Checks_Add_New():
    strItemType = 'val.Tiles_Checks.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Cornerless_Count_All():
    strItemType = 'Cornerless'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Cornerless_Count_Selected():
    strItemType = 'Cornerless'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Cornerless_Count_UnSelected():
    strItemType = 'Cornerless'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Cornerless_Name_All():
    strItemType = 'Cornerless'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Cornerless_Name_Selected():
    strItemType = 'Cornerless'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Cornerless_Name_UnSelected():
    strItemType = 'Cornerless'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Cornerless_ID_All():
    strItemType = 'Cornerless'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Cornerless_ID_Selected():
    strItemType = 'Cornerless'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Cornerless_ID_UnSelected():
    strItemType = 'Cornerless'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Cornerless_Add_New():
    strItemType = 'val.Tiles_Cornerless.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Cubes_Count_All():
    strItemType = 'Cubes'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Cubes_Count_Selected():
    strItemType = 'Cubes'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Cubes_Count_UnSelected():
    strItemType = 'Cubes'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Cubes_Name_All():
    strItemType = 'Cubes'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Cubes_Name_Selected():
    strItemType = 'Cubes'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Cubes_Name_UnSelected():
    strItemType = 'Cubes'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Cubes_ID_All():
    strItemType = 'Cubes'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Cubes_ID_Selected():
    strItemType = 'Cubes'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Cubes_ID_UnSelected():
    strItemType = 'Cubes'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Cubes_Add_New():
    strItemType = 'val.Tiles_Cubes.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Dash_Line_Count_All():
    strItemType = 'Dash Line'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Dash_Line_Count_Selected():
    strItemType = 'Dash Line'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Dash_Line_Count_UnSelected():
    strItemType = 'Dash Line'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Dash_Line_Name_All():
    strItemType = 'Dash Line'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Dash_Line_Name_Selected():
    strItemType = 'Dash Line'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Dash_Line_Name_UnSelected():
    strItemType = 'Dash Line'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Dash_Line_ID_All():
    strItemType = 'Dash Line'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Dash_Line_ID_Selected():
    strItemType = 'Dash Line'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Dash_Line_ID_UnSelected():
    strItemType = 'Dash Line'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Dash_Line_Add_New():
    strItemType = 'val.Tiles_DashLine.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Diamond_Deck_Count_All():
    strItemType = 'Diamond Deck'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Diamond_Deck_Count_Selected():
    strItemType = 'Diamond Deck'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Diamond_Deck_Count_UnSelected():
    strItemType = 'Diamond Deck'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Diamond_Deck_Name_All():
    strItemType = 'Diamond Deck'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Diamond_Deck_Name_Selected():
    strItemType = 'Diamond Deck'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Diamond_Deck_Name_UnSelected():
    strItemType = 'Diamond Deck'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Diamond_Deck_ID_All():
    strItemType = 'Diamond Deck'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Diamond_Deck_ID_Selected():
    strItemType = 'Diamond Deck'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Diamond_Deck_ID_UnSelected():
    strItemType = 'Diamond Deck'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Diamond_Deck_Add_New():
    strItemType = 'val.Tiles_DiamondDeck.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Fish_Scales_Count_All():
    strItemType = 'Fish Scales'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Fish_Scales_Count_Selected():
    strItemType = 'Fish Scales'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Fish_Scales_Count_UnSelected():
    strItemType = 'Fish Scales'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Fish_Scales_Name_All():
    strItemType = 'Fish Scales'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Fish_Scales_Name_Selected():
    strItemType = 'Fish Scales'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Fish_Scales_Name_UnSelected():
    strItemType = 'Fish Scales'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Fish_Scales_ID_All():
    strItemType = 'Fish Scales'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Fish_Scales_ID_Selected():
    strItemType = 'Fish Scales'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Fish_Scales_ID_UnSelected():
    strItemType = 'Fish Scales'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Fish_Scales_Add_New():
    strItemType = 'val.Tiles_FishScales.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Hex_Tile_Count_All():
    strItemType = 'Hex Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Hex_Tile_Count_Selected():
    strItemType = 'Hex Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Hex_Tile_Count_UnSelected():
    strItemType = 'Hex Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Hex_Tile_Name_All():
    strItemType = 'Hex Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Hex_Tile_Name_Selected():
    strItemType = 'Hex Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Hex_Tile_Name_UnSelected():
    strItemType = 'Hex Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Hex_Tile_ID_All():
    strItemType = 'Hex Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Hex_Tile_ID_Selected():
    strItemType = 'Hex Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Hex_Tile_ID_UnSelected():
    strItemType = 'Hex Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Hex_Tile_Add_New():
    strItemType = 'val.Tiles_HexTile.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Lattice_1_Count_All():
    strItemType = 'Lattice 1'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Lattice_1_Count_Selected():
    strItemType = 'Lattice 1'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Lattice_1_Count_UnSelected():
    strItemType = 'Lattice 1'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Lattice_1_Name_All():
    strItemType = 'Lattice 1'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Lattice_1_Name_Selected():
    strItemType = 'Lattice 1'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Lattice_1_Name_UnSelected():
    strItemType = 'Lattice 1'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Lattice_1_ID_All():
    strItemType = 'Lattice 1'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Lattice_1_ID_Selected():
    strItemType = 'Lattice 1'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Lattice_1_ID_UnSelected():
    strItemType = 'Lattice 1'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Lattice_1_Add_New():
    strItemType = 'val.Tiles_Lattice1.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Lattice_2_Count_All():
    strItemType = 'Lattice 2'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Lattice_2_Count_Selected():
    strItemType = 'Lattice 2'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Lattice_2_Count_UnSelected():
    strItemType = 'Lattice 2'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Lattice_2_Name_All():
    strItemType = 'Lattice 2'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Lattice_2_Name_Selected():
    strItemType = 'Lattice 2'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Lattice_2_Name_UnSelected():
    strItemType = 'Lattice 2'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Lattice_2_ID_All():
    strItemType = 'Lattice 2'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Lattice_2_ID_Selected():
    strItemType = 'Lattice 2'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Lattice_2_ID_UnSelected():
    strItemType = 'Lattice 2'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Lattice_2_Add_New():
    strItemType = 'val.Tiles_Lattice2.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Lattice_3_Count_All():
    strItemType = 'Lattice 3'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Lattice_3_Count_Selected():
    strItemType = 'Lattice 3'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Lattice_3_Count_UnSelected():
    strItemType = 'Lattice 3'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Lattice_3_Name_All():
    strItemType = 'Lattice 3'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Lattice_3_Name_Selected():
    strItemType = 'Lattice 3'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Lattice_3_Name_UnSelected():
    strItemType = 'Lattice 3'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Lattice_3_ID_All():
    strItemType = 'Lattice 3'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Lattice_3_ID_Selected():
    strItemType = 'Lattice 3'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Lattice_3_ID_UnSelected():
    strItemType = 'Lattice 3'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Lattice_3_Add_New():
    strItemType = 'val.Tiles_Lattice3.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Mosaic_Count_All():
    strItemType = 'Mosaic'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Mosaic_Count_Selected():
    strItemType = 'Mosaic'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Mosaic_Count_UnSelected():
    strItemType = 'Mosaic'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Mosaic_Name_All():
    strItemType = 'Mosaic'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Mosaic_Name_Selected():
    strItemType = 'Mosaic'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Mosaic_Name_UnSelected():
    strItemType = 'Mosaic'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Mosaic_ID_All():
    strItemType = 'Mosaic'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Mosaic_ID_Selected():
    strItemType = 'Mosaic'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Mosaic_ID_UnSelected():
    strItemType = 'Mosaic'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Mosaic_Add_New():
    strItemType = 'val.Tiles_Mosaic.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Oct_Tile_Count_All():
    strItemType = 'Oct Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Oct_Tile_Count_Selected():
    strItemType = 'Oct Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Oct_Tile_Count_UnSelected():
    strItemType = 'Oct Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Oct_Tile_Name_All():
    strItemType = 'Oct Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Oct_Tile_Name_Selected():
    strItemType = 'Oct Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Oct_Tile_Name_UnSelected():
    strItemType = 'Oct Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Oct_Tile_ID_All():
    strItemType = 'Oct Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Oct_Tile_ID_Selected():
    strItemType = 'Oct Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Oct_Tile_ID_UnSelected():
    strItemType = 'Oct Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Oct_Tile_Add_New():
    strItemType = 'val.Tiles_OctTile.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Parquet_Count_All():
    strItemType = 'Parquet'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Parquet_Count_Selected():
    strItemType = 'Parquet'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Parquet_Count_UnSelected():
    strItemType = 'Parquet'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Parquet_Name_All():
    strItemType = 'Parquet'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Parquet_Name_Selected():
    strItemType = 'Parquet'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Parquet_Name_UnSelected():
    strItemType = 'Parquet'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Parquet_ID_All():
    strItemType = 'Parquet'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Parquet_ID_Selected():
    strItemType = 'Parquet'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Parquet_ID_UnSelected():
    strItemType = 'Parquet'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Parquet_Add_New():
    strItemType = 'val.Tiles_Parquet.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Paving_Count_All():
    strItemType = 'Paving'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Paving_Count_Selected():
    strItemType = 'Paving'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Paving_Count_UnSelected():
    strItemType = 'Paving'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Paving_Name_All():
    strItemType = 'Paving'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Paving_Name_Selected():
    strItemType = 'Paving'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Paving_Name_UnSelected():
    strItemType = 'Paving'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Paving_ID_All():
    strItemType = 'Paving'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Paving_ID_Selected():
    strItemType = 'Paving'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Paving_ID_UnSelected():
    strItemType = 'Paving'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Paving_Add_New():
    strItemType = 'val.Tiles_Paving.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Plaid_Count_All():
    strItemType = 'Plaid'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Plaid_Count_Selected():
    strItemType = 'Plaid'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Plaid_Count_UnSelected():
    strItemType = 'Plaid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Plaid_Name_All():
    strItemType = 'Plaid'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Plaid_Name_Selected():
    strItemType = 'Plaid'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Plaid_Name_UnSelected():
    strItemType = 'Plaid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Plaid_ID_All():
    strItemType = 'Plaid'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Plaid_ID_Selected():
    strItemType = 'Plaid'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Plaid_ID_UnSelected():
    strItemType = 'Plaid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Plaid_Add_New():
    strItemType = 'val.Tiles_Plaid.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Planks_Count_All():
    strItemType = 'Planks'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Planks_Count_Selected():
    strItemType = 'Planks'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Planks_Count_UnSelected():
    strItemType = 'Planks'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Planks_Name_All():
    strItemType = 'Planks'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Planks_Name_Selected():
    strItemType = 'Planks'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Planks_Name_UnSelected():
    strItemType = 'Planks'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Planks_ID_All():
    strItemType = 'Planks'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Planks_ID_Selected():
    strItemType = 'Planks'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Planks_ID_UnSelected():
    strItemType = 'Planks'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Planks_Add_New():
    strItemType = 'val.Tiles_Planks.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Ribs_Count_All():
    strItemType = 'Ribs'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Ribs_Count_Selected():
    strItemType = 'Ribs'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Ribs_Count_UnSelected():
    strItemType = 'Ribs'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Ribs_Name_All():
    strItemType = 'Ribs'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Ribs_Name_Selected():
    strItemType = 'Ribs'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Ribs_Name_UnSelected():
    strItemType = 'Ribs'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Ribs_ID_All():
    strItemType = 'Ribs'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Ribs_ID_Selected():
    strItemType = 'Ribs'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Ribs_ID_UnSelected():
    strItemType = 'Ribs'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Ribs_Add_New():
    strItemType = 'val.Tiles_Ribs.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Rounded_Tile_Count_All():
    strItemType = 'Rounded Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Rounded_Tile_Count_Selected():
    strItemType = 'Rounded Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Rounded_Tile_Count_UnSelected():
    strItemType = 'Rounded Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Rounded_Tile_Name_All():
    strItemType = 'Rounded Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Rounded_Tile_Name_Selected():
    strItemType = 'Rounded Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Rounded_Tile_Name_UnSelected():
    strItemType = 'Rounded Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Rounded_Tile_ID_All():
    strItemType = 'Rounded Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Rounded_Tile_ID_Selected():
    strItemType = 'Rounded Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Rounded_Tile_ID_UnSelected():
    strItemType = 'Rounded Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Rounded_Tile_Add_New():
    strItemType = 'val.Tiles_RoundedTile.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Shingles_Count_All():
    strItemType = 'Shingles'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Shingles_Count_Selected():
    strItemType = 'Shingles'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Shingles_Count_UnSelected():
    strItemType = 'Shingles'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Shingles_Name_All():
    strItemType = 'Shingles'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Shingles_Name_Selected():
    strItemType = 'Shingles'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Shingles_Name_UnSelected():
    strItemType = 'Shingles'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Shingles_ID_All():
    strItemType = 'Shingles'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Shingles_ID_Selected():
    strItemType = 'Shingles'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Shingles_ID_UnSelected():
    strItemType = 'Shingles'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Shingles_Add_New():
    strItemType = 'val.Tiles_Shingles.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Spots_Count_All():
    strItemType = 'Spots'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Spots_Count_Selected():
    strItemType = 'Spots'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Spots_Count_UnSelected():
    strItemType = 'Spots'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Spots_Name_All():
    strItemType = 'Spots'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Spots_Name_Selected():
    strItemType = 'Spots'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Spots_Name_UnSelected():
    strItemType = 'Spots'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Spots_ID_All():
    strItemType = 'Spots'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Spots_ID_Selected():
    strItemType = 'Spots'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Spots_ID_UnSelected():
    strItemType = 'Spots'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Spots_Add_New():
    strItemType = 'val.Tiles_Spots.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Stamped_Count_All():
    strItemType = 'Stamped'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Stamped_Count_Selected():
    strItemType = 'Stamped'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Stamped_Count_UnSelected():
    strItemType = 'Stamped'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Stamped_Name_All():
    strItemType = 'Stamped'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Stamped_Name_Selected():
    strItemType = 'Stamped'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Stamped_Name_UnSelected():
    strItemType = 'Stamped'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Stamped_ID_All():
    strItemType = 'Stamped'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Stamped_ID_Selected():
    strItemType = 'Stamped'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Stamped_ID_UnSelected():
    strItemType = 'Stamped'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Stamped_Add_New():
    strItemType = 'val.Tiles_Stamped.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Tacos_Count_All():
    strItemType = 'Tacos'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tacos_Count_Selected():
    strItemType = 'Tacos'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tacos_Count_UnSelected():
    strItemType = 'Tacos'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tacos_Name_All():
    strItemType = 'Tacos'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tacos_Name_Selected():
    strItemType = 'Tacos'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tacos_Name_UnSelected():
    strItemType = 'Tacos'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tacos_ID_All():
    strItemType = 'Tacos'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tacos_ID_Selected():
    strItemType = 'Tacos'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tacos_ID_UnSelected():
    strItemType = 'Tacos'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tacos_Add_New():
    strItemType = 'val.Tiles_Tacos.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Tartan_Count_All():
    strItemType = 'Tartan'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tartan_Count_Selected():
    strItemType = 'Tartan'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tartan_Count_UnSelected():
    strItemType = 'Tartan'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tartan_Name_All():
    strItemType = 'Tartan'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tartan_Name_Selected():
    strItemType = 'Tartan'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tartan_Name_UnSelected():
    strItemType = 'Tartan'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tartan_ID_All():
    strItemType = 'Tartan'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tartan_ID_Selected():
    strItemType = 'Tartan'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tartan_ID_UnSelected():
    strItemType = 'Tartan'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tartan_Add_New():
    strItemType = 'val.Tiles_TarTan.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Tiler_Count_All():
    strItemType = 'Tiler'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tiler_Count_Selected():
    strItemType = 'Tiler'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tiler_Count_UnSelected():
    strItemType = 'Tiler'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tiler_Name_All():
    strItemType = 'Tiler'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tiler_Name_Selected():
    strItemType = 'Tiler'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tiler_Name_UnSelected():
    strItemType = 'Tiler'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tiler_ID_All():
    strItemType = 'Tiler'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tiler_ID_Selected():
    strItemType = 'Tiler'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tiler_ID_UnSelected():
    strItemType = 'Tiler'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tiler_Add_New():
    strItemType = 'val.Tiles_Tiler.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Tri_Checks_Count_All():
    strItemType = 'Tri Checks'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tri_Checks_Count_Selected():
    strItemType = 'Tri Checks'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tri_Checks_Count_UnSelected():
    strItemType = 'Tri Checks'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tri_Checks_Name_All():
    strItemType = 'Tri Checks'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tri_Checks_Name_Selected():
    strItemType = 'Tri Checks'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tri_Checks_Name_UnSelected():
    strItemType = 'Tri Checks'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tri_Checks_ID_All():
    strItemType = 'Tri Checks'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tri_Checks_ID_Selected():
    strItemType = 'Tri Checks'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tri_Checks_ID_UnSelected():
    strItemType = 'Tri Checks'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tri_Checks_Add_New():
    strItemType = 'val.Tiles_TriChecks.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Tri_Hexes_Count_All():
    strItemType = 'Tri Hexes'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tri_Hexes_Count_Selected():
    strItemType = 'Tri Hexes'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tri_Hexes_Count_UnSelected():
    strItemType = 'Tri Hexes'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tri_Hexes_Name_All():
    strItemType = 'Tri Hexes'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tri_Hexes_Name_Selected():
    strItemType = 'Tri Hexes'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tri_Hexes_Name_UnSelected():
    strItemType = 'Tri Hexes'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tri_Hexes_ID_All():
    strItemType = 'Tri Hexes'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tri_Hexes_ID_Selected():
    strItemType = 'Tri Hexes'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tri_Hexes_ID_UnSelected():
    strItemType = 'Tri Hexes'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tri_Hexes_Add_New():
    strItemType = 'val.Tiles_TriHexes.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Tri_Tile_Count_All():
    strItemType = 'Tri Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tri_Tile_Count_Selected():
    strItemType = 'Tri Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tri_Tile_Count_UnSelected():
    strItemType = 'Tri Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Tri_Tile_Name_All():
    strItemType = 'Tri Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tri_Tile_Name_Selected():
    strItemType = 'Tri Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tri_Tile_Name_UnSelected():
    strItemType = 'Tri Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Tri_Tile_ID_All():
    strItemType = 'Tri Tile'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tri_Tile_ID_Selected():
    strItemType = 'Tri Tile'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tri_Tile_ID_UnSelected():
    strItemType = 'Tri Tile'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Tri_Tile_Add_New():
    strItemType = 'val.Tiles_TriTile.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Tiles_Wall_Count_All():
    strItemType = 'Wall'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Wall_Count_Selected():
    strItemType = 'Wall'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Wall_Count_UnSelected():
    strItemType = 'Wall'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Tiles_Wall_Name_All():
    strItemType = 'Wall'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Wall_Name_Selected():
    strItemType = 'Wall'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Wall_Name_UnSelected():
    strItemType = 'Wall'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Tiles_Wall_ID_All():
    strItemType = 'Wall'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Wall_ID_Selected():
    strItemType = 'Wall'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Wall_ID_UnSelected():
    strItemType = 'Wall'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Tiles_Wall_Add_New():
    strItemType = 'val.Tiles_Wall.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Water_Drip_Drop_Count_All():
    strItemType = 'Drip Drop'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Drip_Drop_Count_Selected():
    strItemType = 'Drip Drop'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Drip_Drop_Count_UnSelected():
    strItemType = 'Drip Drop'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Drip_Drop_Name_All():
    strItemType = 'Drip Drop'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Drip_Drop_Name_Selected():
    strItemType = 'Drip Drop'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Drip_Drop_Name_UnSelected():
    strItemType = 'Drip Drop'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Drip_Drop_ID_All():
    strItemType = 'Drip Drop'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Drip_Drop_ID_Selected():
    strItemType = 'Drip Drop'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Drip_Drop_ID_UnSelected():
    strItemType = 'Drip Drop'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Drip_Drop_Add_New():
    strItemType = 'val.Water_DripDrop.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Water_Rain_Count_All():
    strItemType = 'Rain'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Rain_Count_Selected():
    strItemType = 'Rain'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Rain_Count_UnSelected():
    strItemType = 'Rain'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Rain_Name_All():
    strItemType = 'Rain'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Rain_Name_Selected():
    strItemType = 'Rain'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Rain_Name_UnSelected():
    strItemType = 'Rain'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Rain_ID_All():
    strItemType = 'Rain'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Rain_ID_Selected():
    strItemType = 'Rain'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Rain_ID_UnSelected():
    strItemType = 'Rain'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Rain_Add_New():
    strItemType = 'val.Water_Rain.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Water_Ripples_Count_All():
    strItemType = 'Ripples'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Ripples_Count_Selected():
    strItemType = 'Ripples'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Ripples_Count_UnSelected():
    strItemType = 'Ripples'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Ripples_Name_All():
    strItemType = 'Ripples'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Ripples_Name_Selected():
    strItemType = 'Ripples'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Ripples_Name_UnSelected():
    strItemType = 'Ripples'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Ripples_ID_All():
    strItemType = 'Ripples'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Ripples_ID_Selected():
    strItemType = 'Ripples'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Ripples_ID_UnSelected():
    strItemType = 'Ripples'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Ripples_Add_New():
    strItemType = 'val.Water_Ripples.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Water_Surf_Count_All():
    strItemType = 'Surf'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Surf_Count_Selected():
    strItemType = 'Surf'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Surf_Count_UnSelected():
    strItemType = 'Surf'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Surf_Name_All():
    strItemType = 'Surf'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Surf_Name_Selected():
    strItemType = 'Surf'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Surf_Name_UnSelected():
    strItemType = 'Surf'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Surf_ID_All():
    strItemType = 'Surf'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Surf_ID_Selected():
    strItemType = 'Surf'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Surf_ID_UnSelected():
    strItemType = 'Surf'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Surf_Add_New():
    strItemType = 'val.Water_Surf.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Water_Waves_Count_All():
    strItemType = 'Waves'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Waves_Count_Selected():
    strItemType = 'Waves'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Waves_Count_UnSelected():
    strItemType = 'Waves'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Waves_Name_All():
    strItemType = 'Waves'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Waves_Name_Selected():
    strItemType = 'Waves'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Waves_Name_UnSelected():
    strItemType = 'Waves'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Waves_ID_All():
    strItemType = 'Waves'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Waves_ID_Selected():
    strItemType = 'Waves'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Waves_ID_UnSelected():
    strItemType = 'Waves'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Waves_Add_New():
    strItemType = 'val.Water_Waves.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_Water_Windy_Waves_Count_All():
    strItemType = 'Windy Waves'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Windy_Waves_Count_Selected():
    strItemType = 'Windy Waves'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Windy_Waves_Count_UnSelected():
    strItemType = 'Windy Waves'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_Water_Windy_Waves_Name_All():
    strItemType = 'Windy Waves'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Windy_Waves_Name_Selected():
    strItemType = 'Windy Waves'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Windy_Waves_Name_UnSelected():
    strItemType = 'Windy Waves'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_Water_Windy_Waves_ID_All():
    strItemType = 'Windy Waves'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Windy_Waves_ID_Selected():
    strItemType = 'Windy Waves'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Windy_Waves_ID_UnSelected():
    strItemType = 'Windy Waves'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_Water_Windy_Waves_Add_New():
    strItemType = 'val.Water_WindyWaves.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Bias_Gain_Count_All():
    strItemType = 'Bias Gain'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Bias_Gain_Count_Selected():
    strItemType = 'Bias Gain'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Bias_Gain_Count_UnSelected():
    strItemType = 'Bias Gain'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Bias_Gain_Name_All():
    strItemType = 'Bias Gain'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Bias_Gain_Name_Selected():
    strItemType = 'Bias Gain'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Bias_Gain_Name_UnSelected():
    strItemType = 'Bias Gain'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Bias_Gain_ID_All():
    strItemType = 'Bias Gain'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Bias_Gain_ID_Selected():
    strItemType = 'Bias Gain'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Bias_Gain_ID_UnSelected():
    strItemType = 'Bias Gain'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Bias_Gain_Add_New():
    strItemType = 'val.Waveforms_BiasGain.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Fresnel_Count_All():
    strItemType = 'Fresnel'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Fresnel_Count_Selected():
    strItemType = 'Fresnel'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Fresnel_Count_UnSelected():
    strItemType = 'Fresnel'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Fresnel_Name_All():
    strItemType = 'Fresnel'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Fresnel_Name_Selected():
    strItemType = 'Fresnel'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Fresnel_Name_UnSelected():
    strItemType = 'Fresnel'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Fresnel_ID_All():
    strItemType = 'Fresnel'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Fresnel_ID_Selected():
    strItemType = 'Fresnel'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Fresnel_ID_UnSelected():
    strItemType = 'Fresnel'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Fresnel_Add_New():
    strItemType = 'val.Waveforms_Fresnel.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Gamma_Count_All():
    strItemType = 'Gamma'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Gamma_Count_Selected():
    strItemType = 'Gamma'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Gamma_Count_UnSelected():
    strItemType = 'Gamma'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Gamma_Name_All():
    strItemType = 'Gamma'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Gamma_Name_Selected():
    strItemType = 'Gamma'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Gamma_Name_UnSelected():
    strItemType = 'Gamma'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Gamma_ID_All():
    strItemType = 'Gamma'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Gamma_ID_Selected():
    strItemType = 'Gamma'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Gamma_ID_UnSelected():
    strItemType = 'Gamma'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Gamma_Add_New():
    strItemType = 'val.Waveforms_Gamma.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Gaussian_Count_All():
    strItemType = 'Gaussian'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Gaussian_Count_Selected():
    strItemType = 'Gaussian'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Gaussian_Count_UnSelected():
    strItemType = 'Gaussian'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Gaussian_Name_All():
    strItemType = 'Gaussian'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Gaussian_Name_Selected():
    strItemType = 'Gaussian'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Gaussian_Name_UnSelected():
    strItemType = 'Gaussian'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Gaussian_ID_All():
    strItemType = 'Gaussian'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Gaussian_ID_Selected():
    strItemType = 'Gaussian'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Gaussian_ID_UnSelected():
    strItemType = 'Gaussian'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Gaussian_Add_New():
    strItemType = 'val.Waveforms_Gaussian.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Impulse_Count_All():
    strItemType = 'Impulse'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Impulse_Count_Selected():
    strItemType = 'Impulse'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Impulse_Count_UnSelected():
    strItemType = 'Impulse'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Impulse_Name_All():
    strItemType = 'Impulse'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Impulse_Name_Selected():
    strItemType = 'Impulse'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Impulse_Name_UnSelected():
    strItemType = 'Impulse'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Impulse_ID_All():
    strItemType = 'Impulse'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Impulse_ID_Selected():
    strItemType = 'Impulse'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Impulse_ID_UnSelected():
    strItemType = 'Impulse'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Impulse_Add_New():
    strItemType = 'val.Waveforms_Impulse.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Noise_Count_All():
    strItemType = 'Noise'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Noise_Count_Selected():
    strItemType = 'Noise'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Noise_Count_UnSelected():
    strItemType = 'Noise'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Noise_Name_All():
    strItemType = 'Noise'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Noise_Name_Selected():
    strItemType = 'Noise'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Noise_Name_UnSelected():
    strItemType = 'Noise'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Noise_ID_All():
    strItemType = 'Noise'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Noise_ID_Selected():
    strItemType = 'Noise'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Noise_ID_UnSelected():
    strItemType = 'Noise'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Noise_Add_New():
    strItemType = 'val.Waveforms_Noise.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Ramp_Count_All():
    strItemType = 'Ramp'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Ramp_Count_Selected():
    strItemType = 'Ramp'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Ramp_Count_UnSelected():
    strItemType = 'Ramp'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Ramp_Name_All():
    strItemType = 'Ramp'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Ramp_Name_Selected():
    strItemType = 'Ramp'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Ramp_Name_UnSelected():
    strItemType = 'Ramp'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Ramp_ID_All():
    strItemType = 'Ramp'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Ramp_ID_Selected():
    strItemType = 'Ramp'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Ramp_ID_UnSelected():
    strItemType = 'Ramp'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Ramp_Add_New():
    strItemType = 'val.Waveforms_Ramp.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Rounded_Count_All():
    strItemType = 'Rounded'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Rounded_Count_Selected():
    strItemType = 'Rounded'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Rounded_Count_UnSelected():
    strItemType = 'Rounded'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Rounded_Name_All():
    strItemType = 'Rounded'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Rounded_Name_Selected():
    strItemType = 'Rounded'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Rounded_Name_UnSelected():
    strItemType = 'Rounded'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Rounded_ID_All():
    strItemType = 'Rounded'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Rounded_ID_Selected():
    strItemType = 'Rounded'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Rounded_ID_UnSelected():
    strItemType = 'Rounded'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Rounded_Add_New():
    strItemType = 'val.Waveforms_Rounded.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Sawtooth_Count_All():
    strItemType = 'Sawtooth'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Sawtooth_Count_Selected():
    strItemType = 'Sawtooth'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Sawtooth_Count_UnSelected():
    strItemType = 'Sawtooth'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Sawtooth_Name_All():
    strItemType = 'Sawtooth'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Sawtooth_Name_Selected():
    strItemType = 'Sawtooth'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Sawtooth_Name_UnSelected():
    strItemType = 'Sawtooth'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Sawtooth_ID_All():
    strItemType = 'Sawtooth'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Sawtooth_ID_Selected():
    strItemType = 'Sawtooth'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Sawtooth_ID_UnSelected():
    strItemType = 'Sawtooth'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Sawtooth_Add_New():
    strItemType = 'val.Waveforms_SawTooth.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Scallop_Count_All():
    strItemType = 'Scallop'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Scallop_Count_Selected():
    strItemType = 'Scallop'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Scallop_Count_UnSelected():
    strItemType = 'Scallop'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Scallop_Name_All():
    strItemType = 'Scallop'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Scallop_Name_Selected():
    strItemType = 'Scallop'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Scallop_Name_UnSelected():
    strItemType = 'Scallop'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Scallop_ID_All():
    strItemType = 'Scallop'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Scallop_ID_Selected():
    strItemType = 'Scallop'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Scallop_ID_UnSelected():
    strItemType = 'Scallop'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Scallop_Add_New():
    strItemType = 'val.Waveforms_Scallop.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_SCurve_Count_All():
    strItemType = 'S-Curve'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_SCurve_Count_Selected():
    strItemType = 'S-Curve'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_SCurve_Count_UnSelected():
    strItemType = 'S-Curve'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_SCurve_Name_All():
    strItemType = 'S-Curve'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_SCurve_Name_Selected():
    strItemType = 'S-Curve'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_SCurve_Name_UnSelected():
    strItemType = 'S-Curve'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_SCurve_ID_All():
    strItemType = 'S-Curve'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_SCurve_ID_Selected():
    strItemType = 'S-Curve'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_SCurve_ID_UnSelected():
    strItemType = 'S-Curve'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_SCurve_Add_New():
    strItemType = 'val.Waveforms_SCurve.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Sine_Count_All():
    strItemType = 'Sine'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Sine_Count_Selected():
    strItemType = 'Sine'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Sine_Count_UnSelected():
    strItemType = 'Sine'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Sine_Name_All():
    strItemType = 'Sine'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Sine_Name_Selected():
    strItemType = 'Sine'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Sine_Name_UnSelected():
    strItemType = 'Sine'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Sine_ID_All():
    strItemType = 'Sine'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Sine_ID_Selected():
    strItemType = 'Sine'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Sine_ID_UnSelected():
    strItemType = 'Sine'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Sine_Add_New():
    strItemType = 'val.Waveforms_Sine.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Smooth_Count_All():
    strItemType = 'Smooth'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Smooth_Count_Selected():
    strItemType = 'Smooth'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Smooth_Count_UnSelected():
    strItemType = 'Smooth'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Smooth_Name_All():
    strItemType = 'Smooth'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Smooth_Name_Selected():
    strItemType = 'Smooth'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Smooth_Name_UnSelected():
    strItemType = 'Smooth'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Smooth_ID_All():
    strItemType = 'Smooth'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Smooth_ID_Selected():
    strItemType = 'Smooth'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Smooth_ID_UnSelected():
    strItemType = 'Smooth'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Smooth_Add_New():
    strItemType = 'val.Waveforms_Smooth.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Smooth_Impulse_Count_All():
    strItemType = 'Smooth Impulse'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Smooth_Impulse_Count_Selected():
    strItemType = 'Smooth Impulse'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Smooth_Impulse_Count_UnSelected():
    strItemType = 'Smooth Impulse'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Smooth_Impulse_Name_All():
    strItemType = 'Smooth Impulse'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Smooth_Impulse_Name_Selected():
    strItemType = 'Smooth Impulse'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Smooth_Impulse_Name_UnSelected():
    strItemType = 'Smooth Impulse'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Smooth_Impulse_ID_All():
    strItemType = 'Smooth Impulse'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Smooth_Impulse_ID_Selected():
    strItemType = 'Smooth Impulse'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Smooth_Impulse_ID_UnSelected():
    strItemType = 'Smooth Impulse'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Smooth_Impulse_Add_New():
    strItemType = 'val.Waveforms_SmoothImpulse.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Smooth_Step_Count_All():
    strItemType = 'Smooth Step'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Smooth_Step_Count_Selected():
    strItemType = 'Smooth Step'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Smooth_Step_Count_UnSelected():
    strItemType = 'Smooth Step'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Smooth_Step_Name_All():
    strItemType = 'Smooth Step'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Smooth_Step_Name_Selected():
    strItemType = 'Smooth Step'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Smooth_Step_Name_UnSelected():
    strItemType = 'Smooth Step'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Smooth_Step_ID_All():
    strItemType = 'Smooth Step'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Smooth_Step_ID_Selected():
    strItemType = 'Smooth Step'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Smooth_Step_ID_UnSelected():
    strItemType = 'Smooth Step'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Smooth_Step_Add_New():
    strItemType = 'val.Waveforms_SmoothStep.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def ET_WaveForms_Staircase_Count_All():
    strItemType = 'Staircase'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Staircase_Count_Selected():
    strItemType = 'Staircase'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Staircase_Count_UnSelected():
    strItemType = 'Staircase'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ET_WaveForms_Staircase_Name_All():
    strItemType = 'Staircase'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Staircase_Name_Selected():
    strItemType = 'Staircase'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Staircase_Name_UnSelected():
    strItemType = 'Staircase'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ET_WaveForms_Staircase_ID_All():
    strItemType = 'Staircase'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Staircase_ID_Selected():
    strItemType = 'Staircase'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Staircase_ID_UnSelected():
    strItemType = 'Staircase'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ET_WaveForms_Staircase_Add_New():
    strItemType = 'val.Waveforms_Staircase.RJJ'
    lx.eval('shader.create {%s}' % strItemType)


def Fur_Material_Count_All():
    strItemType = 'Fur Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Fur_Material_Count_Selected():
    strItemType = 'Fur Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Fur_Material_Count_UnSelected():
    strItemType = 'Fur Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Fur_Material_Name_All():
    strItemType = 'Fur Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Fur_Material_Name_Selected():
    strItemType = 'Fur Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Fur_Material_Name_UnSelected():
    strItemType = 'Fur Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Fur_Material_ID_All():
    strItemType = 'Fur Material'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Fur_Material_ID_Selected():
    strItemType = 'Fur Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Fur_Material_ID_UnSelected():
    strItemType = 'Fur Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Fur_Material_Add_New():
    strItemType = 'furMaterial'
    lx.eval('shader.create {%s}' % strItemType)


def Gradient_Count_All():
    strItemType = 'Gradient'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Gradient_Count_Selected():
    strItemType = 'Gradient'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Gradient_Count_UnSelected():
    strItemType = 'Gradient'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Gradient_Name_All():
    strItemType = 'Gradient'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Gradient_Name_Selected():
    strItemType = 'Gradient'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Gradient_Name_UnSelected():
    strItemType = 'Gradient'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Gradient_ID_All():
    strItemType = 'Gradient'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Gradient_ID_Selected():
    strItemType = 'Gradient'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Gradient_ID_UnSelected():
    strItemType = 'Gradient'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Gradient_Add_New():
    strItemType = 'gradient'
    lx.eval('shader.create {%s}' % strItemType)


def Grid_Count_All():
    strItemType = 'Grid'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Grid_Count_Selected():
    strItemType = 'Grid'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Grid_Count_UnSelected():
    strItemType = 'Grid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Grid_Name_All():
    strItemType = 'Grid'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Grid_Name_Selected():
    strItemType = 'Grid'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Grid_Name_UnSelected():
    strItemType = 'Grid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Grid_ID_All():
    strItemType = 'Grid'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Grid_ID_Selected():
    strItemType = 'Grid'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Grid_ID_UnSelected():
    strItemType = 'Grid'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Grid_Add_New():
    strItemType = 'grid'
    lx.eval('shader.create {%s}' % strItemType)


def Group_Count_All():
    strItemType = 'Group'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Group_Count_Selected():
    strItemType = 'Group'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Group_Count_UnSelected():
    strItemType = 'Group'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Group_Name_All():
    strItemType = 'Group'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Group_Name_Selected():
    strItemType = 'Group'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Group_Name_UnSelected():
    strItemType = 'Group'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Group_ID_All():
    strItemType = 'Group'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Group_ID_Selected():
    strItemType = 'Group'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Group_ID_UnSelected():
    strItemType = 'Group'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Group_Add_New():
    strItemType = 'mask'
    lx.eval('shader.create {%s}' % strItemType)


def Group_Locator_Count_All():
    strItemType = 'Group Locator'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Group_Locator_Count_Selected():
    strItemType = 'Group Locator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Group_Locator_Count_UnSelected():
    strItemType = 'Group Locator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Group_Locator_Name_All():
    strItemType = 'Group Locator'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Group_Locator_Name_Selected():
    strItemType = 'Group Locator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Group_Locator_Name_UnSelected():
    strItemType = 'Group Locator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Group_Locator_ID_All():
    strItemType = 'Group Locator'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Group_Locator_ID_Selected():
    strItemType = 'Group Locator'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Group_Locator_ID_UnSelected():
    strItemType = 'Group Locator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Group_Locator_Add_New():
    strItemType = 'groupLocator'
    lx.eval('item.create {%s}' % strItemType)


def Hair_Material_Count_All():
    strItemType = 'Hair Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Hair_Material_Count_Selected():
    strItemType = 'Hair Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Hair_Material_Count_UnSelected():
    strItemType = 'Hair Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Hair_Material_Name_All():
    strItemType = 'Hair Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Hair_Material_Name_Selected():
    strItemType = 'Hair Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Hair_Material_Name_UnSelected():
    strItemType = 'Hair Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Hair_Material_ID_All():
    strItemType = 'Hair Material'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Hair_Material_ID_Selected():
    strItemType = 'Hair Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Hair_Material_ID_UnSelected():
    strItemType = 'Hair Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Hair_Material_Add_New():
    strItemType = 'material.hairMaterial'
    lx.eval('shader.create {%s}' % strItemType)


def Halftone_Material_Count_All():
    strItemType = 'Halftone Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Halftone_Material_Count_Selected():
    strItemType = 'Halftone Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Halftone_Material_Count_UnSelected():
    strItemType = 'Halftone Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Halftone_Material_Name_All():
    strItemType = 'Halftone Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Halftone_Material_Name_Selected():
    strItemType = 'Halftone Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Halftone_Material_Name_UnSelected():
    strItemType = 'Halftone Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Halftone_Material_ID_All():
    strItemType = 'Halftone Material'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Halftone_Material_ID_Selected():
    strItemType = 'Halftone Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Halftone_Material_ID_UnSelected():
    strItemType = 'Halftone Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Halftone_Material_Add_New():
    strItemType = 'material.halftone'
    lx.eval('shader.create {%s}' % strItemType)


def Hinge_Count_All():
    strItemType = 'Hinge'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Hinge_Count_Selected():
    strItemType = 'Hinge'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Hinge_Count_UnSelected():
    strItemType = 'Hinge'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Hinge_Name_All():
    strItemType = 'Hinge'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Hinge_Name_Selected():
    strItemType = 'Hinge'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Hinge_Name_UnSelected():
    strItemType = 'Hinge'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Hinge_ID_All():
    strItemType = 'Hinge'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Hinge_ID_Selected():
    strItemType = 'Hinge'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Hinge_ID_UnSelected():
    strItemType = 'Hinge'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Hinge_Add_New():
    strItemType = 'consHinge'
    lx.eval('item.create {%s}' % strItemType)


def Image_Map_Count_All():
    strItemType = 'Image Map'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Image_Map_Count_Selected():
    strItemType = 'Image Map'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Image_Map_Count_UnSelected():
    strItemType = 'Image Map'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Image_Map_Name_All():
    strItemType = 'Image Map'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Image_Map_Name_Selected():
    strItemType = 'Image Map'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Image_Map_Name_UnSelected():
    strItemType = 'Image Map'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Image_Map_ID_All():
    strItemType = 'Image Map'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Image_Map_ID_Selected():
    strItemType = 'Image Map'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Image_Map_ID_UnSelected():
    strItemType = 'Image Map'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Image_Map_Add_New():
    strItemType = 'imageMap'
    lx.eval('shader.create {%s}' % strItemType)


def Iridescence_Material_Count_All():
    strItemType = 'Iridescence Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Iridescence_Material_Count_Selected():
    strItemType = 'Iridescence Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Iridescence_Material_Count_UnSelected():
    strItemType = 'Iridescence Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Iridescence_Material_Name_All():
    strItemType = 'Iridescence Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Iridescence_Material_Name_Selected():
    strItemType = 'Iridescence Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Iridescence_Material_Name_UnSelected():
    strItemType = 'Iridescence Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Iridescence_Material_ID_All():
    strItemType = 'Iridescence Material'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Iridescence_Material_ID_Selected():
    strItemType = 'Iridescence Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Iridescence_Material_ID_UnSelected():
    strItemType = 'Iridescence Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Iridescence_Material_Add_New():
    strItemType = 'material.iridescence'
    lx.eval('shader.create {%s}' % strItemType)


def Lag_Effector_Count_All():
    strItemType = 'Lag Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Lag_Effector_Count_Selected():
    strItemType = 'Lag Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Lag_Effector_Count_UnSelected():
    strItemType = 'Lag Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Lag_Effector_Name_All():
    strItemType = 'Lag Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Lag_Effector_Name_Selected():
    strItemType = 'Lag Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Lag_Effector_Name_UnSelected():
    strItemType = 'Lag Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Lag_Effector_ID_All():
    strItemType = 'Lag Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Lag_Effector_ID_Selected():
    strItemType = 'Lag Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Lag_Effector_ID_UnSelected():
    strItemType = 'Lag Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Lag_Effector_Add_New():
    strItemType = 'deform.lag'
    lx.eval('item.create {%s}' % strItemType)


def Lattice_Effector_Count_All():
    strItemType = 'Lattice Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Lattice_Effector_Count_Selected():
    strItemType = 'Lattice Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Lattice_Effector_Count_UnSelected():
    strItemType = 'Lattice Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Lattice_Effector_Name_All():
    strItemType = 'Lattice Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Lattice_Effector_Name_Selected():
    strItemType = 'Lattice Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Lattice_Effector_Name_UnSelected():
    strItemType = 'Lattice Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Lattice_Effector_ID_All():
    strItemType = 'Lattice Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Lattice_Effector_ID_Selected():
    strItemType = 'Lattice Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Lattice_Effector_ID_UnSelected():
    strItemType = 'Lattice Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Lattice_Effector_Add_New():
    strItemType = 'deform.lattice'
    lx.eval('item.create {%s}' % strItemType)


def Light_Material_Count_All():
    strItemType = 'Light Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Light_Material_Count_Selected():
    strItemType = 'Light Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Light_Material_Count_UnSelected():
    strItemType = 'Light Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Light_Material_Name_All():
    strItemType = 'Light Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Light_Material_Name_Selected():
    strItemType = 'Light Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Light_Material_Name_UnSelected():
    strItemType = 'Light Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Light_Material_ID_All():
    strItemType = 'Light Material'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Light_Material_ID_Selected():
    strItemType = 'Light Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Light_Material_ID_UnSelected():
    strItemType = 'Light Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Light_Material_Add_New():
    strItemType = 'lightMaterial'
    lx.eval('shader.create {%s}' % strItemType)


def Linear_Falloff_Count_All():
    strItemType = 'Linear Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Linear_Falloff_Count_Selected():
    strItemType = 'Linear Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Linear_Falloff_Count_UnSelected():
    strItemType = 'Linear Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Linear_Falloff_Name_All():
    strItemType = 'Linear Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Linear_Falloff_Name_Selected():
    strItemType = 'Linear Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Linear_Falloff_Name_UnSelected():
    strItemType = 'Linear Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Linear_Falloff_ID_All():
    strItemType = 'Linear Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Linear_Falloff_ID_Selected():
    strItemType = 'Linear Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Linear_Falloff_ID_UnSelected():
    strItemType = 'Linear Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Linear_Falloff_Add_New():
    strItemType = 'falloff.linear'
    lx.eval('item.create {%s}' % strItemType)


def Linear_Force_Count_All():
    strItemType = 'Linear Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Linear_Force_Count_Selected():
    strItemType = 'Linear Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Linear_Force_Count_UnSelected():
    strItemType = 'Linear Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Linear_Force_Name_All():
    strItemType = 'Linear Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Linear_Force_Name_Selected():
    strItemType = 'Linear Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Linear_Force_Name_UnSelected():
    strItemType = 'Linear Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Linear_Force_ID_All():
    strItemType = 'Linear Force'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Linear_Force_ID_Selected():
    strItemType = 'Linear Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Linear_Force_ID_UnSelected():
    strItemType = 'Linear Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Linear_Force_Add_New():
    strItemType = 'force.linear'
    lx.eval('item.create {%s}' % strItemType)


def Locator_Count_All():
    strItemType = 'Locator'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Locator_Count_Selected():
    strItemType = 'Locator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Locator_Count_UnSelected():
    strItemType = 'Locator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Locator_Name_All():
    strItemType = 'Locator'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Locator_Name_Selected():
    strItemType = 'Locator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Locator_Name_UnSelected():
    strItemType = 'Locator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Locator_ID_All():
    strItemType = 'Locator'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Locator_ID_Selected():
    strItemType = 'Locator'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Locator_ID_UnSelected():
    strItemType = 'Locator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Locator_Add_New():
    strItemType = 'locator'
    lx.eval('item.create {%s}' % strItemType)


def Magnet_Effector_Count_All():
    strItemType = 'Magnet Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Magnet_Effector_Count_Selected():
    strItemType = 'Magnet Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Magnet_Effector_Count_UnSelected():
    strItemType = 'Magnet Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Magnet_Effector_Name_All():
    strItemType = 'Magnet Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Magnet_Effector_Name_Selected():
    strItemType = 'Magnet Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Magnet_Effector_Name_UnSelected():
    strItemType = 'Magnet Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Magnet_Effector_ID_All():
    strItemType = 'Magnet Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Magnet_Effector_ID_Selected():
    strItemType = 'Magnet Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Magnet_Effector_ID_UnSelected():
    strItemType = 'Magnet Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Magnet_Effector_Add_New():
    strItemType = 'deform.magnet'
    lx.eval('item.create {%s}' % strItemType)


def Material_Count_All():
    strItemType = 'Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Material_Count_Selected():
    strItemType = 'Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Material_Count_UnSelected():
    strItemType = 'Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Material_Name_All():
    strItemType = 'Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Material_Name_Selected():
    strItemType = 'Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Material_Name_UnSelected():
    strItemType = 'Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Material_ID_All():
    strItemType = 'Material'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Material_ID_Selected():
    strItemType = 'Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Material_ID_UnSelected():
    strItemType = 'Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Material_Add_New():
    strItemType = 'advancedMaterial'
    lx.eval('shader.create {%s}' % strItemType)


def Mesh_Count_All():
    strItemType = 'Mesh'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Mesh_Count_Selected():
    strItemType = 'Mesh'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Mesh_Count_UnSelected():
    strItemType = 'Mesh'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Mesh_Name_All():
    strItemType = 'Mesh'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Mesh_Name_Selected():
    strItemType = 'Mesh'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Mesh_Name_UnSelected():
    strItemType = 'Mesh'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Mesh_ID_All():
    strItemType = 'Mesh'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Mesh_ID_Selected():
    strItemType = 'Mesh'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Mesh_ID_UnSelected():
    strItemType = 'Mesh'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Mesh_Add_New():
    strItemType = 'mesh'
    lx.eval('item.create {%s}' % strItemType)


def Morph_Influence_Count_All():
    strItemType = 'Morph Influence'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Morph_Influence_Count_Selected():
    strItemType = 'Morph Influence'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Morph_Influence_Count_UnSelected():
    strItemType = 'Morph Influence'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Morph_Influence_Name_All():
    strItemType = 'Morph Influence'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Morph_Influence_Name_Selected():
    strItemType = 'Morph Influence'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Morph_Influence_Name_UnSelected():
    strItemType = 'Morph Influence'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Morph_Influence_ID_All():
    strItemType = 'Morph Influence'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Morph_Influence_ID_Selected():
    strItemType = 'Morph Influence'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Morph_Influence_ID_UnSelected():
    strItemType = 'Morph Influence'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Morph_Influence_Add_New():
    strItemType = 'morphDeform'
    lx.eval('item.create {%s}' % strItemType)


def Newton_Force_Count_All():
    strItemType = 'Newton Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Newton_Force_Count_Selected():
    strItemType = 'Newton Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Newton_Force_Count_UnSelected():
    strItemType = 'Newton Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Newton_Force_Name_All():
    strItemType = 'Newton Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Newton_Force_Name_Selected():
    strItemType = 'Newton Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Newton_Force_Name_UnSelected():
    strItemType = 'Newton Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Newton_Force_ID_All():
    strItemType = 'Newton Force'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Newton_Force_ID_Selected():
    strItemType = 'Newton Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Newton_Force_ID_UnSelected():
    strItemType = 'Newton Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Newton_Force_Add_New():
    strItemType = 'force.newton'
    lx.eval('item.create {%s}' % strItemType)


def Noise_Count_All():
    strItemType = 'Noise'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Noise_Count_Selected():
    strItemType = 'Noise'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Noise_Count_UnSelected():
    strItemType = 'Noise'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Noise_Name_All():
    strItemType = 'Noise'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Noise_Name_Selected():
    strItemType = 'Noise'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Noise_Name_UnSelected():
    strItemType = 'Noise'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Noise_ID_All():
    strItemType = 'Noise'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Noise_ID_Selected():
    strItemType = 'Noise'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Noise_ID_UnSelected():
    strItemType = 'Noise'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Noise_Add_New():
    strItemType = 'noise'
    lx.eval('shader.create {%s}' % strItemType)


def Occlusion_Count_All():
    strItemType = 'Occlusion'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Occlusion_Count_Selected():
    strItemType = 'Occlusion'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Occlusion_Count_UnSelected():
    strItemType = 'Occlusion'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Occlusion_Name_All():
    strItemType = 'Occlusion'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Occlusion_Name_Selected():
    strItemType = 'Occlusion'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Occlusion_Name_UnSelected():
    strItemType = 'Occlusion'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Occlusion_ID_All():
    strItemType = 'Occlusion'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Occlusion_ID_Selected():
    strItemType = 'Occlusion'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Occlusion_ID_UnSelected():
    strItemType = 'Occlusion'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Occlusion_Add_New():
    strItemType = 'occlusion'
    lx.eval('shader.create {%s}' % strItemType)


def Particle_Audio_Modifier_Count_All():
    strItemType = 'Particle Audio Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Audio_Modifier_Count_Selected():
    strItemType = 'Particle Audio Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Audio_Modifier_Count_UnSelected():
    strItemType = 'Particle Audio Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Audio_Modifier_Name_All():
    strItemType = 'Particle Audio Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Audio_Modifier_Name_Selected():
    strItemType = 'Particle Audio Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Audio_Modifier_Name_UnSelected():
    strItemType = 'Particle Audio Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Audio_Modifier_ID_All():
    strItemType = 'Particle Audio Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Audio_Modifier_ID_Selected():
    strItemType = 'Particle Audio Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Audio_Modifier_ID_UnSelected():
    strItemType = 'Particle Audio Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Audio_Modifier_Add_New():
    strItemType = 'pMod.audio'
    lx.eval('item.create {%s}' % strItemType)


def Particle_Cloud_Count_All():
    strItemType = 'Particle Cloud'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Cloud_Count_Selected():
    strItemType = 'Particle Cloud'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Cloud_Count_UnSelected():
    strItemType = 'Particle Cloud'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Cloud_Name_All():
    strItemType = 'Particle Cloud'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Cloud_Name_Selected():
    strItemType = 'Particle Cloud'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Cloud_Name_UnSelected():
    strItemType = 'Particle Cloud'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Cloud_ID_All():
    strItemType = 'Particle Cloud'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Cloud_ID_Selected():
    strItemType = 'Particle Cloud'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Cloud_ID_UnSelected():
    strItemType = 'Particle Cloud'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Cloud_Add_New():
    strItemType = 'pcloud'
    lx.eval('item.create {%s}' % strItemType)


def Particle_Expression_Modifier_Count_All():
    strItemType = 'Particle Expression Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Expression_Modifier_Count_Selected():
    strItemType = 'Particle Expression Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Expression_Modifier_Count_UnSelected():
    strItemType = 'Particle Expression Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Expression_Modifier_Name_All():
    strItemType = 'Particle Expression Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Expression_Modifier_Name_Selected():
    strItemType = 'Particle Expression Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Expression_Modifier_Name_UnSelected():
    strItemType = 'Particle Expression Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Expression_Modifier_ID_All():
    strItemType = 'Particle Expression Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Expression_Modifier_ID_Selected():
    strItemType = 'Particle Expression Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Expression_Modifier_ID_UnSelected():
    strItemType = 'Particle Expression Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Expression_Modifier_Add_New():
    strItemType = 'pMod.expression'
    lx.eval('item.create {%s}' % strItemType)


def Particle_Flocking_Count_All():
    strItemType = 'Particle Flocking'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Flocking_Count_Selected():
    strItemType = 'Particle Flocking'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Flocking_Count_UnSelected():
    strItemType = 'Particle Flocking'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Flocking_Name_All():
    strItemType = 'Particle Flocking'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Flocking_Name_Selected():
    strItemType = 'Particle Flocking'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Flocking_Name_UnSelected():
    strItemType = 'Particle Flocking'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Flocking_ID_All():
    strItemType = 'Particle Flocking'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Flocking_ID_Selected():
    strItemType = 'Particle Flocking'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Flocking_ID_UnSelected():
    strItemType = 'Particle Flocking'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Flocking_Add_New():
    strItemType = 'flockingOp'
    lx.eval('item.create {%s}' % strItemType)


def Particle_Generator_Count_All():
    strItemType = 'Particle Generator'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Generator_Count_Selected():
    strItemType = 'Particle Generator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Generator_Count_UnSelected():
    strItemType = 'Particle Generator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Generator_Name_All():
    strItemType = 'Particle Generator'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Generator_Name_Selected():
    strItemType = 'Particle Generator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Generator_Name_UnSelected():
    strItemType = 'Particle Generator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Generator_ID_All():
    strItemType = 'Particle Generator'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Generator_ID_Selected():
    strItemType = 'Particle Generator'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Generator_ID_UnSelected():
    strItemType = 'Particle Generator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Generator_Add_New():
    strItemType = 'pMod.generator'
    lx.eval('item.create {%s}' % strItemType)


def Particle_Look_At_Modifier_Count_All():
    strItemType = 'Particle Look At Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Look_At_Modifier_Count_Selected():
    strItemType = 'Particle Look At Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Look_At_Modifier_Count_UnSelected():
    strItemType = 'Particle Look At Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Look_At_Modifier_Name_All():
    strItemType = 'Particle Look At Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Look_At_Modifier_Name_Selected():
    strItemType = 'Particle Look At Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Look_At_Modifier_Name_UnSelected():
    strItemType = 'Particle Look At Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Look_At_Modifier_ID_All():
    strItemType = 'Particle Look At Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Look_At_Modifier_ID_Selected():
    strItemType = 'Particle Look At Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Look_At_Modifier_ID_UnSelected():
    strItemType = 'Particle Look At Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Look_At_Modifier_Add_New():
    strItemType = 'pMod.lookat'
    lx.eval('item.create {%s}' % strItemType)


def Particle_Modifier_Count_All():
    strItemType = 'Particle Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Modifier_Count_Selected():
    strItemType = 'Particle Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Modifier_Count_UnSelected():
    strItemType = 'Particle Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Modifier_Name_All():
    strItemType = 'Particle Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Modifier_Name_Selected():
    strItemType = 'Particle Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Modifier_Name_UnSelected():
    strItemType = 'Particle Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Modifier_ID_All():
    strItemType = 'Particle Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Modifier_ID_Selected():
    strItemType = 'Particle Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Modifier_ID_UnSelected():
    strItemType = 'Particle Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Modifier_Add_New():
    strItemType = 'pMod.basic'
    lx.eval('item.create {%s}' % strItemType)


def Particle_Operator_Count_All():
    strItemType = 'Particle Operator'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Operator_Count_Selected():
    strItemType = 'Particle Operator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Operator_Count_UnSelected():
    strItemType = 'Particle Operator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Operator_Name_All():
    strItemType = 'Particle Operator'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Operator_Name_Selected():
    strItemType = 'Particle Operator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Operator_Name_UnSelected():
    strItemType = 'Particle Operator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Operator_ID_All():
    strItemType = 'Particle Operator'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Operator_ID_Selected():
    strItemType = 'Particle Operator'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Operator_ID_UnSelected():
    strItemType = 'Particle Operator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Operator_Add_New():
    strItemType = 'particleOp'
    lx.eval('item.create {%s}' % strItemType)


def Particle_Random_Modifier_Count_All():
    strItemType = 'Particle Random Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Random_Modifier_Count_Selected():
    strItemType = 'Particle Random Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Random_Modifier_Count_UnSelected():
    strItemType = 'Particle Random Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Random_Modifier_Name_All():
    strItemType = 'Particle Random Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Random_Modifier_Name_Selected():
    strItemType = 'Particle Random Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Random_Modifier_Name_UnSelected():
    strItemType = 'Particle Random Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Random_Modifier_ID_All():
    strItemType = 'Particle Random Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Random_Modifier_ID_Selected():
    strItemType = 'Particle Random Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Random_Modifier_ID_UnSelected():
    strItemType = 'Particle Random Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Random_Modifier_Add_New():
    strItemType = 'pMod.random'
    lx.eval('item.create {%s}' % strItemType)


def Particle_Sieve_Modifier_Count_All():
    strItemType = 'Particle Sieve Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Sieve_Modifier_Count_Selected():
    strItemType = 'Particle Sieve Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Sieve_Modifier_Count_UnSelected():
    strItemType = 'Particle Sieve Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Sieve_Modifier_Name_All():
    strItemType = 'Particle Sieve Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Sieve_Modifier_Name_Selected():
    strItemType = 'Particle Sieve Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Sieve_Modifier_Name_UnSelected():
    strItemType = 'Particle Sieve Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Sieve_Modifier_ID_All():
    strItemType = 'Particle Sieve Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Sieve_Modifier_ID_Selected():
    strItemType = 'Particle Sieve Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Sieve_Modifier_ID_UnSelected():
    strItemType = 'Particle Sieve Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Sieve_Modifier_Add_New():
    strItemType = 'pMod.sieve'
    lx.eval('item.create {%s}' % strItemType)


def Particle_Simulation_Count_All():
    strItemType = 'Particle Simulation'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Simulation_Count_Selected():
    strItemType = 'Particle Simulation'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Simulation_Count_UnSelected():
    strItemType = 'Particle Simulation'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Simulation_Name_All():
    strItemType = 'Particle Simulation'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Simulation_Name_Selected():
    strItemType = 'Particle Simulation'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Simulation_Name_UnSelected():
    strItemType = 'Particle Simulation'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Simulation_ID_All():
    strItemType = 'Particle Simulation'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Simulation_ID_Selected():
    strItemType = 'Particle Simulation'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Simulation_ID_UnSelected():
    strItemType = 'Particle Simulation'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Simulation_Add_New():
    strItemType = 'particleSim'
    lx.eval('item.create {%s}' % strItemType)


def Particle_Step_Modifier_Count_All():
    strItemType = 'Particle Step Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Step_Modifier_Count_Selected():
    strItemType = 'Particle Step Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Step_Modifier_Count_UnSelected():
    strItemType = 'Particle Step Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Particle_Step_Modifier_Name_All():
    strItemType = 'Particle Step Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Step_Modifier_Name_Selected():
    strItemType = 'Particle Step Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Step_Modifier_Name_UnSelected():
    strItemType = 'Particle Step Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Particle_Step_Modifier_ID_All():
    strItemType = 'Particle Step Modifier'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Step_Modifier_ID_Selected():
    strItemType = 'Particle Step Modifier'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Step_Modifier_ID_UnSelected():
    strItemType = 'Particle Step Modifier'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Particle_Step_Modifier_Add_New():
    strItemType = 'pMod.step'
    lx.eval('item.create {%s}' % strItemType)


def Photometric_Light_Count_All():
    strItemType = 'Photometric Light'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Photometric_Light_Count_Selected():
    strItemType = 'Photometric Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Photometric_Light_Count_UnSelected():
    strItemType = 'Photometric Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Photometric_Light_Name_All():
    strItemType = 'Photometric Light'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Photometric_Light_Name_Selected():
    strItemType = 'Photometric Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Photometric_Light_Name_UnSelected():
    strItemType = 'Photometric Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Photometric_Light_ID_All():
    strItemType = 'Photometric Light'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Photometric_Light_ID_Selected():
    strItemType = 'Photometric Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Photometric_Light_ID_UnSelected():
    strItemType = 'Photometric Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Photometric_Light_Add_New():
    strItemType = 'photometryLight'
    lx.eval('item.create {%s}' % strItemType)


def Pin_Count_All():
    strItemType = 'Pin'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Pin_Count_Selected():
    strItemType = 'Pin'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Pin_Count_UnSelected():
    strItemType = 'Pin'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Pin_Name_All():
    strItemType = 'Pin'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Pin_Name_Selected():
    strItemType = 'Pin'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Pin_Name_UnSelected():
    strItemType = 'Pin'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Pin_ID_All():
    strItemType = 'Pin'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Pin_ID_Selected():
    strItemType = 'Pin'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Pin_ID_UnSelected():
    strItemType = 'Pin'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Pin_Add_New():
    strItemType = 'consPin'
    lx.eval('item.create {%s}' % strItemType)


def Point_Count_All():
    strItemType = 'Point'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Point_Count_Selected():
    strItemType = 'Point'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Point_Count_UnSelected():
    strItemType = 'Point'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Point_Name_All():
    strItemType = 'Point'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Point_Name_Selected():
    strItemType = 'Point'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Point_Name_UnSelected():
    strItemType = 'Point'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Point_ID_All():
    strItemType = 'Point'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Point_ID_Selected():
    strItemType = 'Point'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Point_ID_UnSelected():
    strItemType = 'Point'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Point_Add_New():
    strItemType = 'consPoint'
    lx.eval('item.create {%s}' % strItemType)


def Point_Light_Count_All():
    strItemType = 'Point Light'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Point_Light_Count_Selected():
    strItemType = 'Point Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Point_Light_Count_UnSelected():
    strItemType = 'Point Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Point_Light_Name_All():
    strItemType = 'Point Light'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Point_Light_Name_Selected():
    strItemType = 'Point Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Point_Light_Name_UnSelected():
    strItemType = 'Point Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Point_Light_ID_All():
    strItemType = 'Point Light'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Point_Light_ID_Selected():
    strItemType = 'Point Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Point_Light_ID_UnSelected():
    strItemType = 'Point Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Point_Light_Add_New():
    strItemType = 'pointLight'
    lx.eval('item.create {%s}' % strItemType)


def Poisson_Cells_Count_All():
    strItemType = 'Poisson Cells'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Poisson_Cells_Count_Selected():
    strItemType = 'Poisson Cells'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Poisson_Cells_Count_UnSelected():
    strItemType = 'Poisson Cells'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Poisson_Cells_Name_All():
    strItemType = 'Poisson Cells'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Poisson_Cells_Name_Selected():
    strItemType = 'Poisson Cells'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Poisson_Cells_Name_UnSelected():
    strItemType = 'Poisson Cells'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Poisson_Cells_ID_All():
    strItemType = 'Poisson Cells'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Poisson_Cells_ID_Selected():
    strItemType = 'Poisson Cells'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Poisson_Cells_ID_UnSelected():
    strItemType = 'Poisson Cells'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Poisson_Cells_Add_New():
    strItemType = 'val.noise.poisson'
    lx.eval('shader.create {%s}' % strItemType)


def Poly_Count_All(Requires_ItemID):
    strItemType = 'Poly'
    asVariant = 'all'
    return __fn_pyModo_Component_Count(Requires_ItemID, strItemType, asVariant)


def Poly_Count_Selected(Requires_ItemID):
    strItemType = 'Poly'
    asVariant = 'selected'
    return __fn_pyModo_Component_Count(Requires_ItemID, strItemType, asVariant)


def Poly_Count_UnSelected(Requires_ItemID):
    strItemType = 'Poly'
    asVariant = 'unselected'
    return __fn_pyModo_Component_Count(Requires_ItemID, strItemType, asVariant)


def Poly_Index_All(Requires_ItemID):
    strItemType = 'Poly'
    asVariant = 'all'
    return __fn_pyModo_Component_Index(Requires_ItemID, strItemType, asVariant)


def Poly_Index_Selected(Requires_ItemID):
    strItemType = 'Poly'
    asVariant = 'selected'
    return __fn_pyModo_Component_Index(Requires_ItemID, strItemType, asVariant)


def Poly_Index_UnSelected(Requires_ItemID):
    strItemType = 'Poly'
    asVariant = 'unselected'
    return __fn_pyModo_Component_Index(Requires_ItemID, strItemType, asVariant)


def Portal_Count_All():
    strItemType = 'Portal'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Portal_Count_Selected():
    strItemType = 'Portal'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Portal_Count_UnSelected():
    strItemType = 'Portal'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Portal_Name_All():
    strItemType = 'Portal'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Portal_Name_Selected():
    strItemType = 'Portal'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Portal_Name_UnSelected():
    strItemType = 'Portal'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Portal_ID_All():
    strItemType = 'Portal'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Portal_ID_Selected():
    strItemType = 'Portal'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Portal_ID_UnSelected():
    strItemType = 'Portal'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Portal_Add_New():
    strItemType = 'portal'
    lx.eval('item.create {%s}' % strItemType)


def Position_Count_All():
    strItemType = 'Position'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Position_Count_Selected():
    strItemType = 'Position'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Position_Count_UnSelected():
    strItemType = 'Position'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Position_Name_All():
    strItemType = 'Position'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Position_Name_Selected():
    strItemType = 'Position'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Position_Name_UnSelected():
    strItemType = 'Position'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Position_ID_All():
    strItemType = 'Position'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Position_ID_Selected():
    strItemType = 'Position'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Position_ID_UnSelected():
    strItemType = 'Position'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Radial_Emitter_Count_All():
    strItemType = 'Radial Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Radial_Emitter_Count_Selected():
    strItemType = 'Radial Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Radial_Emitter_Count_UnSelected():
    strItemType = 'Radial Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Radial_Emitter_Name_All():
    strItemType = 'Radial Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Radial_Emitter_Name_Selected():
    strItemType = 'Radial Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Radial_Emitter_Name_UnSelected():
    strItemType = 'Radial Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Radial_Emitter_ID_All():
    strItemType = 'Radial Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Radial_Emitter_ID_Selected():
    strItemType = 'Radial Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Radial_Emitter_ID_UnSelected():
    strItemType = 'Radial Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Radial_Emitter_Add_New():
    strItemType = 'radialEmitter'
    lx.eval('item.create {%s}' % strItemType)


def Radial_Falloff_Count_All():
    strItemType = 'Radial Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Radial_Falloff_Count_Selected():
    strItemType = 'Radial Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Radial_Falloff_Count_UnSelected():
    strItemType = 'Radial Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Radial_Falloff_Name_All():
    strItemType = 'Radial Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Radial_Falloff_Name_Selected():
    strItemType = 'Radial Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Radial_Falloff_Name_UnSelected():
    strItemType = 'Radial Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Radial_Falloff_ID_All():
    strItemType = 'Radial Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Radial_Falloff_ID_Selected():
    strItemType = 'Radial Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Radial_Falloff_ID_UnSelected():
    strItemType = 'Radial Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Radial_Falloff_Add_New():
    strItemType = 'falloff.radial'
    lx.eval('item.create {%s}' % strItemType)


def Radial_Force_Count_All():
    strItemType = 'Radial Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Radial_Force_Count_Selected():
    strItemType = 'Radial Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Radial_Force_Count_UnSelected():
    strItemType = 'Radial Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Radial_Force_Name_All():
    strItemType = 'Radial Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Radial_Force_Name_Selected():
    strItemType = 'Radial Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Radial_Force_Name_UnSelected():
    strItemType = 'Radial Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Radial_Force_ID_All():
    strItemType = 'Radial Force'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Radial_Force_ID_Selected():
    strItemType = 'Radial Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Radial_Force_ID_UnSelected():
    strItemType = 'Radial Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Radial_Force_Add_New():
    strItemType = 'force.radial'
    lx.eval('item.create {%s}' % strItemType)


def Realflow_Particles_Count_All():
    strItemType = 'Realflow Particles'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Realflow_Particles_Count_Selected():
    strItemType = 'Realflow Particles'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Realflow_Particles_Count_UnSelected():
    strItemType = 'Realflow Particles'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Realflow_Particles_Name_All():
    strItemType = 'Realflow Particles'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Realflow_Particles_Name_Selected():
    strItemType = 'Realflow Particles'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Realflow_Particles_Name_UnSelected():
    strItemType = 'Realflow Particles'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Realflow_Particles_ID_All():
    strItemType = 'Realflow Particles'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Realflow_Particles_ID_Selected():
    strItemType = 'Realflow Particles'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Realflow_Particles_ID_UnSelected():
    strItemType = 'Realflow Particles'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Realflow_Particles_Add_New():
    strItemType = 'realParticle'
    lx.eval('item.create {%s}' % strItemType)


def Render_Count_All():
    strItemType = 'Render'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Render_Count_Selected():
    strItemType = 'Render'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Render_Count_UnSelected():
    strItemType = 'Render'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Render_Name_All():
    strItemType = 'Render'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Render_Name_Selected():
    strItemType = 'Render'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Render_Name_UnSelected():
    strItemType = 'Render'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Render_ID_All():
    strItemType = 'Render'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Render_ID_Selected():
    strItemType = 'Render'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Render_ID_UnSelected():
    strItemType = 'Render'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Render_Output_Count_All():
    strItemType = 'Render Output'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Render_Output_Count_Selected():
    strItemType = 'Render Output'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Render_Output_Count_UnSelected():
    strItemType = 'Render Output'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Render_Output_Name_All():
    strItemType = 'Render Output'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Render_Output_Name_Selected():
    strItemType = 'Render Output'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Render_Output_Name_UnSelected():
    strItemType = 'Render Output'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Render_Output_ID_All():
    strItemType = 'Render Output'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Render_Output_ID_Selected():
    strItemType = 'Render Output'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Render_Output_ID_UnSelected():
    strItemType = 'Render Output'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Render_Output_Add_New():
    strItemType = 'renderOutput'
    lx.eval('item.create {%s}' % strItemType)


def Replicator_Count_All():
    strItemType = 'Replicator'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Replicator_Count_Selected():
    strItemType = 'Replicator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Replicator_Count_UnSelected():
    strItemType = 'Replicator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Replicator_Name_All():
    strItemType = 'Replicator'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Replicator_Name_Selected():
    strItemType = 'Replicator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Replicator_Name_UnSelected():
    strItemType = 'Replicator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Replicator_ID_All():
    strItemType = 'Replicator'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Replicator_ID_Selected():
    strItemType = 'Replicator'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Replicator_ID_UnSelected():
    strItemType = 'Replicator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Replicator_Add_New():
    strItemType = 'replicator'
    lx.eval('item.create {%s}' % strItemType)


def Ripples_Count_All():
    strItemType = 'Ripples'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Ripples_Count_Selected():
    strItemType = 'Ripples'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Ripples_Count_UnSelected():
    strItemType = 'Ripples'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Ripples_Name_All():
    strItemType = 'Ripples'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Ripples_Name_Selected():
    strItemType = 'Ripples'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Ripples_Name_UnSelected():
    strItemType = 'Ripples'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Ripples_ID_All():
    strItemType = 'Ripples'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Ripples_ID_Selected():
    strItemType = 'Ripples'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Ripples_ID_UnSelected():
    strItemType = 'Ripples'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Ripples_Add_New():
    strItemType = 'ripples'
    lx.eval('shader.create {%s}' % strItemType)


def Rotation_Count_All():
    strItemType = 'Rotation'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Rotation_Count_Selected():
    strItemType = 'Rotation'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Rotation_Count_UnSelected():
    strItemType = 'Rotation'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Rotation_Name_All():
    strItemType = 'Rotation'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Rotation_Name_Selected():
    strItemType = 'Rotation'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Rotation_Name_UnSelected():
    strItemType = 'Rotation'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Rotation_ID_All():
    strItemType = 'Rotation'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Rotation_ID_Selected():
    strItemType = 'Rotation'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Rotation_ID_UnSelected():
    strItemType = 'Rotation'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def RPC_Texture_Count_All():
    strItemType = 'RPC Texture'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def RPC_Texture_Count_Selected():
    strItemType = 'RPC Texture'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def RPC_Texture_Count_UnSelected():
    strItemType = 'RPC Texture'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def RPC_Texture_Name_All():
    strItemType = 'RPC Texture'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def RPC_Texture_Name_Selected():
    strItemType = 'RPC Texture'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def RPC_Texture_Name_UnSelected():
    strItemType = 'RPC Texture'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def RPC_Texture_ID_All():
    strItemType = 'RPC Texture'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def RPC_Texture_ID_Selected():
    strItemType = 'RPC Texture'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def RPC_Texture_ID_UnSelected():
    strItemType = 'RPC Texture'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def RPC_Texture_Add_New():
    strItemType = 'val.RpcTexture'
    lx.eval('shader.create {%s}' % strItemType)


def RT_Curvature_Count_All():
    strItemType = 'RT Curvature'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def RT_Curvature_Count_Selected():
    strItemType = 'RT Curvature'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def RT_Curvature_Count_UnSelected():
    strItemType = 'RT Curvature'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def RT_Curvature_Name_All():
    strItemType = 'RT Curvature'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def RT_Curvature_Name_Selected():
    strItemType = 'RT Curvature'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def RT_Curvature_Name_UnSelected():
    strItemType = 'RT Curvature'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def RT_Curvature_ID_All():
    strItemType = 'RT Curvature'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def RT_Curvature_ID_Selected():
    strItemType = 'RT Curvature'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def RT_Curvature_ID_UnSelected():
    strItemType = 'RT Curvature'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def RT_Curvature_Add_New():
    strItemType = 'val.RTCurvature'
    lx.eval('shader.create {%s}' % strItemType)


def Scale_Count_All():
    strItemType = 'Scale'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Scale_Count_Selected():
    strItemType = 'Scale'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Scale_Count_UnSelected():
    strItemType = 'Scale'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Scale_Name_All():
    strItemType = 'Scale'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Scale_Name_Selected():
    strItemType = 'Scale'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Scale_Name_UnSelected():
    strItemType = 'Scale'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Scale_ID_All():
    strItemType = 'Scale'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Scale_ID_Selected():
    strItemType = 'Scale'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Scale_ID_UnSelected():
    strItemType = 'Scale'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def BaseShader_Count_All():
    strItemType = 'Shader'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def BaseShader_Count_Selected():
    strItemType = 'Shader'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def BaseShader_Count_UnSelected():
    strItemType = 'Shader'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def BaseShader_Name_All():
    strItemType = 'Shader'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def BaseShader_Name_Selected():
    strItemType = 'Shader'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def BaseShader_Name_UnSelected():
    strItemType = 'Shader'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def BaseShader_ID_All():
    strItemType = 'Shader'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def BaseShader_ID_Selected():
    strItemType = 'Shader'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def BaseShader_ID_UnSelected():
    strItemType = 'Shader'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def BaseShader_Add_New():
    strItemType = 'defaultShader'
    lx.eval('shader.create {%s}' % strItemType)


def Skin_Material_Count_All():
    strItemType = 'Skin Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Skin_Material_Count_Selected():
    strItemType = 'Skin Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Skin_Material_Count_UnSelected():
    strItemType = 'Skin Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Skin_Material_Name_All():
    strItemType = 'Skin Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Skin_Material_Name_Selected():
    strItemType = 'Skin Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Skin_Material_Name_UnSelected():
    strItemType = 'Skin Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Skin_Material_ID_All():
    strItemType = 'Skin Material'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Skin_Material_ID_Selected():
    strItemType = 'Skin Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Skin_Material_ID_UnSelected():
    strItemType = 'Skin Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Skin_Material_Add_New():
    strItemType = 'material.skinMateria'
    lx.eval('shader.create {%s}' % strItemType)


def Slide_Hinge_Count_All():
    strItemType = 'Slide Hinge'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Slide_Hinge_Count_Selected():
    strItemType = 'Slide Hinge'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Slide_Hinge_Count_UnSelected():
    strItemType = 'Slide Hinge'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Slide_Hinge_Name_All():
    strItemType = 'Slide Hinge'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Slide_Hinge_Name_Selected():
    strItemType = 'Slide Hinge'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Slide_Hinge_Name_UnSelected():
    strItemType = 'Slide Hinge'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Slide_Hinge_ID_All():
    strItemType = 'Slide Hinge'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Slide_Hinge_ID_Selected():
    strItemType = 'Slide Hinge'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Slide_Hinge_ID_UnSelected():
    strItemType = 'Slide Hinge'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Slide_Hinge_Add_New():
    strItemType = 'consSlideHinge'
    lx.eval('item.create {%s}' % strItemType)


def Soft_Lag_Count_All():
    strItemType = 'Soft Lag'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Soft_Lag_Count_Selected():
    strItemType = 'Soft Lag'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Soft_Lag_Count_UnSelected():
    strItemType = 'Soft Lag'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Soft_Lag_Name_All():
    strItemType = 'Soft Lag'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Soft_Lag_Name_Selected():
    strItemType = 'Soft Lag'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Soft_Lag_Name_UnSelected():
    strItemType = 'Soft Lag'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Soft_Lag_ID_All():
    strItemType = 'Soft Lag'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Soft_Lag_ID_Selected():
    strItemType = 'Soft Lag'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Soft_Lag_ID_UnSelected():
    strItemType = 'Soft Lag'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Soft_Lag_Add_New():
    strItemType = 'softLag'
    lx.eval('item.create {%s}' % strItemType)


def Source_Emitter_Count_All():
    strItemType = 'Source Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Source_Emitter_Count_Selected():
    strItemType = 'Source Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Source_Emitter_Count_UnSelected():
    strItemType = 'Source Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Source_Emitter_Name_All():
    strItemType = 'Source Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Source_Emitter_Name_Selected():
    strItemType = 'Source Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Source_Emitter_Name_UnSelected():
    strItemType = 'Source Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Source_Emitter_ID_All():
    strItemType = 'Source Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Source_Emitter_ID_Selected():
    strItemType = 'Source Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Source_Emitter_ID_UnSelected():
    strItemType = 'Source Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Source_Emitter_Add_New():
    strItemType = 'sourceEmitter'
    lx.eval('item.create {%s}' % strItemType)


def Spline_Falloff_Count_All():
    strItemType = 'Spline Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Spline_Falloff_Count_Selected():
    strItemType = 'Spline Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Spline_Falloff_Count_UnSelected():
    strItemType = 'Spline Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Spline_Falloff_Name_All():
    strItemType = 'Spline Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Spline_Falloff_Name_Selected():
    strItemType = 'Spline Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Spline_Falloff_Name_UnSelected():
    strItemType = 'Spline Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Spline_Falloff_ID_All():
    strItemType = 'Spline Falloff'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Spline_Falloff_ID_Selected():
    strItemType = 'Spline Falloff'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Spline_Falloff_ID_UnSelected():
    strItemType = 'Spline Falloff'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Spline_Falloff_Add_New():
    strItemType = 'falloff.spline'
    lx.eval('item.create {%s}' % strItemType)


def Spot_Light_Count_All():
    strItemType = 'Spot Light'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Spot_Light_Count_Selected():
    strItemType = 'Spot Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Spot_Light_Count_UnSelected():
    strItemType = 'Spot Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Spot_Light_Name_All():
    strItemType = 'Spot Light'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Spot_Light_Name_Selected():
    strItemType = 'Spot Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Spot_Light_Name_UnSelected():
    strItemType = 'Spot Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Spot_Light_ID_All():
    strItemType = 'Spot Light'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Spot_Light_ID_Selected():
    strItemType = 'Spot Light'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Spot_Light_ID_UnSelected():
    strItemType = 'Spot Light'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Spot_Light_Add_New():
    strItemType = 'spotLight'
    lx.eval('item.create {%s}' % strItemType)


def Spring_Count_All():
    strItemType = 'Spring'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Spring_Count_Selected():
    strItemType = 'Spring'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Spring_Count_UnSelected():
    strItemType = 'Spring'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Spring_Name_All():
    strItemType = 'Spring'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Spring_Name_Selected():
    strItemType = 'Spring'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Spring_Name_UnSelected():
    strItemType = 'Spring'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Spring_ID_All():
    strItemType = 'Spring'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Spring_ID_Selected():
    strItemType = 'Spring'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Spring_ID_UnSelected():
    strItemType = 'Spring'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Spring_Add_New():
    strItemType = 'consSpring'
    lx.eval('item.create {%s}' % strItemType)


def Surface_Emitter_Count_All():
    strItemType = 'Surface Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Surface_Emitter_Count_Selected():
    strItemType = 'Surface Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Surface_Emitter_Count_UnSelected():
    strItemType = 'Surface Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Surface_Emitter_Name_All():
    strItemType = 'Surface Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Surface_Emitter_Name_Selected():
    strItemType = 'Surface Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Surface_Emitter_Name_UnSelected():
    strItemType = 'Surface Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Surface_Emitter_ID_All():
    strItemType = 'Surface Emitter'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Surface_Emitter_ID_Selected():
    strItemType = 'Surface Emitter'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Surface_Emitter_ID_UnSelected():
    strItemType = 'Surface Emitter'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Surface_Emitter_Add_New():
    strItemType = 'surfEmitter'
    lx.eval('item.create {%s}' % strItemType)


def Surface_Generator_Count_All():
    strItemType = 'Surface Generator'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Surface_Generator_Count_Selected():
    strItemType = 'Surface Generator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Surface_Generator_Count_UnSelected():
    strItemType = 'Surface Generator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Surface_Generator_Name_All():
    strItemType = 'Surface Generator'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Surface_Generator_Name_Selected():
    strItemType = 'Surface Generator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Surface_Generator_Name_UnSelected():
    strItemType = 'Surface Generator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Surface_Generator_ID_All():
    strItemType = 'Surface Generator'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Surface_Generator_ID_Selected():
    strItemType = 'Surface Generator'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Surface_Generator_ID_UnSelected():
    strItemType = 'Surface Generator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Surface_Generator_Add_New():
    strItemType = 'surfGen'
    lx.eval('shader.create {%s}' % strItemType)


def Surface_Particle_Generator_Count_All():
    strItemType = 'Surface Particle Generator'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Surface_Particle_Generator_Count_Selected():
    strItemType = 'Surface Particle Generator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Surface_Particle_Generator_Count_UnSelected():
    strItemType = 'Surface Particle Generator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Surface_Particle_Generator_Name_All():
    strItemType = 'Surface Particle Generator'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Surface_Particle_Generator_Name_Selected():
    strItemType = 'Surface Particle Generator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Surface_Particle_Generator_Name_UnSelected():
    strItemType = 'Surface Particle Generator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Surface_Particle_Generator_ID_All():
    strItemType = 'Surface Particle Generator'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Surface_Particle_Generator_ID_Selected():
    strItemType = 'Surface Particle Generator'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Surface_Particle_Generator_ID_UnSelected():
    strItemType = 'Surface Particle Generator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Surface_Particle_Generator_Add_New():
    strItemType = 'surfGenLoc'
    lx.eval('item.create {%s}' % strItemType)


def Terminator_Count_All():
    strItemType = 'Terminator'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Terminator_Count_Selected():
    strItemType = 'Terminator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Terminator_Count_UnSelected():
    strItemType = 'Terminator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Terminator_Name_All():
    strItemType = 'Terminator'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Terminator_Name_Selected():
    strItemType = 'Terminator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Terminator_Name_UnSelected():
    strItemType = 'Terminator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Terminator_ID_All():
    strItemType = 'Terminator'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Terminator_ID_Selected():
    strItemType = 'Terminator'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Terminator_ID_UnSelected():
    strItemType = 'Terminator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Terminator_Add_New():
    strItemType = 'particleTerminator'
    lx.eval('item.create {%s}' % strItemType)


def Texture_Locator_Count_All():
    strItemType = 'Texture Locator'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Texture_Locator_Count_Selected():
    strItemType = 'Texture Locator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Texture_Locator_Count_UnSelected():
    strItemType = 'Texture Locator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Texture_Locator_Name_All():
    strItemType = 'Texture Locator'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Texture_Locator_Name_Selected():
    strItemType = 'Texture Locator'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Texture_Locator_Name_UnSelected():
    strItemType = 'Texture Locator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Texture_Locator_ID_All():
    strItemType = 'Texture Locator'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Texture_Locator_ID_Selected():
    strItemType = 'Texture Locator'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Texture_Locator_ID_UnSelected():
    strItemType = 'Texture Locator'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Texture_Locator_Add_New():
    strItemType = 'txtrLocator'
    lx.eval('item.create {%s}' % strItemType)


def ThinFilm_Material_Count_All():
    strItemType = 'ThinFilm Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ThinFilm_Material_Count_Selected():
    strItemType = 'ThinFilm Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ThinFilm_Material_Count_UnSelected():
    strItemType = 'ThinFilm Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def ThinFilm_Material_Name_All():
    strItemType = 'ThinFilm Material'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ThinFilm_Material_Name_Selected():
    strItemType = 'ThinFilm Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ThinFilm_Material_Name_UnSelected():
    strItemType = 'ThinFilm Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def ThinFilm_Material_ID_All():
    strItemType = 'ThinFilm Material'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ThinFilm_Material_ID_Selected():
    strItemType = 'ThinFilm Material'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ThinFilm_Material_ID_UnSelected():
    strItemType = 'ThinFilm Material'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def ThinFilm_Material_Add_New():
    strItemType = 'material.thinfilm'
    lx.eval('shader.create {%s}' % strItemType)


def Turbulence_Force_Count_All():
    strItemType = 'Turbulence Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Turbulence_Force_Count_Selected():
    strItemType = 'Turbulence Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Turbulence_Force_Count_UnSelected():
    strItemType = 'Turbulence Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Turbulence_Force_Name_All():
    strItemType = 'Turbulence Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Turbulence_Force_Name_Selected():
    strItemType = 'Turbulence Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Turbulence_Force_Name_UnSelected():
    strItemType = 'Turbulence Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Turbulence_Force_ID_All():
    strItemType = 'Turbulence Force'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Turbulence_Force_ID_Selected():
    strItemType = 'Turbulence Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Turbulence_Force_ID_UnSelected():
    strItemType = 'Turbulence Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Turbulence_Force_Add_New():
    strItemType = 'force.turbulence'
    lx.eval('item.create {%s}' % strItemType)


def Vert_Count_All(Requires_ItemID):
    strItemType = 'Vert'
    asVariant = 'all'
    return __fn_pyModo_Component_Count(Requires_ItemID, strItemType, asVariant)


def Vert_Count_Selected(Requires_ItemID):
    strItemType = 'Vert'
    asVariant = 'selected'
    return __fn_pyModo_Component_Count(Requires_ItemID, strItemType, asVariant)


def Vert_Count_UnSelected(Requires_ItemID):
    strItemType = 'Vert'
    asVariant = 'unselected'
    return __fn_pyModo_Component_Count(Requires_ItemID, strItemType, asVariant)


def Vert_Index_All(Requires_ItemID):
    strItemType = 'Vert'
    asVariant = 'all'
    return __fn_pyModo_Component_Index(Requires_ItemID, strItemType, asVariant)


def Vert_Index_Selected(Requires_ItemID):
    strItemType = 'Vert'
    asVariant = 'selected'
    return __fn_pyModo_Component_Index(Requires_ItemID, strItemType, asVariant)


def Vert_Index_UnSelected(Requires_ItemID):
    strItemType = 'Vert'
    asVariant = 'unselected'
    return __fn_pyModo_Component_Index(Requires_ItemID, strItemType, asVariant)


def Volume_Count_All():
    strItemType = 'Volume'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Volume_Count_Selected():
    strItemType = 'Volume'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Volume_Count_UnSelected():
    strItemType = 'Volume'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Volume_Name_All():
    strItemType = 'Volume'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Volume_Name_Selected():
    strItemType = 'Volume'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Volume_Name_UnSelected():
    strItemType = 'Volume'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Volume_ID_All():
    strItemType = 'Volume'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Volume_ID_Selected():
    strItemType = 'Volume'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Volume_ID_UnSelected():
    strItemType = 'Volume'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Volume_Add_New():
    strItemType = 'volume'
    lx.eval('item.create {%s}' % strItemType)


def Vortex_Effector_Count_All():
    strItemType = 'Vortex Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Vortex_Effector_Count_Selected():
    strItemType = 'Vortex Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Vortex_Effector_Count_UnSelected():
    strItemType = 'Vortex Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Vortex_Effector_Name_All():
    strItemType = 'Vortex Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Vortex_Effector_Name_Selected():
    strItemType = 'Vortex Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Vortex_Effector_Name_UnSelected():
    strItemType = 'Vortex Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Vortex_Effector_ID_All():
    strItemType = 'Vortex Effector'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Vortex_Effector_ID_Selected():
    strItemType = 'Vortex Effector'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Vortex_Effector_ID_UnSelected():
    strItemType = 'Vortex Effector'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Vortex_Effector_Add_New():
    strItemType = 'deform.vortex'
    lx.eval('item.create {%s}' % strItemType)


def Vortex_Force_Count_All():
    strItemType = 'Vortex Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Vortex_Force_Count_Selected():
    strItemType = 'Vortex Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Vortex_Force_Count_UnSelected():
    strItemType = 'Vortex Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Vortex_Force_Name_All():
    strItemType = 'Vortex Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Vortex_Force_Name_Selected():
    strItemType = 'Vortex Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Vortex_Force_Name_UnSelected():
    strItemType = 'Vortex Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Vortex_Force_ID_All():
    strItemType = 'Vortex Force'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Vortex_Force_ID_Selected():
    strItemType = 'Vortex Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Vortex_Force_ID_UnSelected():
    strItemType = 'Vortex Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Vortex_Force_Add_New():
    strItemType = 'force.vortex'
    lx.eval('item.create {%s}' % strItemType)


def Weave_Count_All():
    strItemType = 'Weave'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Weave_Count_Selected():
    strItemType = 'Weave'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Weave_Count_UnSelected():
    strItemType = 'Weave'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Weave_Name_All():
    strItemType = 'Weave'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Weave_Name_Selected():
    strItemType = 'Weave'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Weave_Name_UnSelected():
    strItemType = 'Weave'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Weave_ID_All():
    strItemType = 'Weave'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Weave_ID_Selected():
    strItemType = 'Weave'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Weave_ID_UnSelected():
    strItemType = 'Weave'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Weave_Add_New():
    strItemType = 'weave'
    lx.eval('shader.create {%s}' % strItemType)


def Weight_Container_Count_All():
    strItemType = 'Weight Container'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Weight_Container_Count_Selected():
    strItemType = 'Weight Container'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Weight_Container_Count_UnSelected():
    strItemType = 'Weight Container'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Weight_Container_Name_All():
    strItemType = 'Weight Container'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Weight_Container_Name_Selected():
    strItemType = 'Weight Container'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Weight_Container_Name_UnSelected():
    strItemType = 'Weight Container'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Weight_Container_ID_All():
    strItemType = 'Weight Container'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Weight_Container_ID_Selected():
    strItemType = 'Weight Container'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Weight_Container_ID_UnSelected():
    strItemType = 'Weight Container'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Weight_Container_Add_New():
    strItemType = 'weightContainer'
    lx.eval('item.create {%s}' % strItemType)


def Weight_Map_Texture_Count_All():
    strItemType = 'Weight Map Texture'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Weight_Map_Texture_Count_Selected():
    strItemType = 'Weight Map Texture'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Weight_Map_Texture_Count_UnSelected():
    strItemType = 'Weight Map Texture'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Weight_Map_Texture_Name_All():
    strItemType = 'Weight Map Texture'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Weight_Map_Texture_Name_Selected():
    strItemType = 'Weight Map Texture'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Weight_Map_Texture_Name_UnSelected():
    strItemType = 'Weight Map Texture'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Weight_Map_Texture_ID_All():
    strItemType = 'Weight Map Texture'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Weight_Map_Texture_ID_Selected():
    strItemType = 'Weight Map Texture'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Weight_Map_Texture_ID_UnSelected():
    strItemType = 'Weight Map Texture'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Weight_Map_Texture_Add_New():
    strItemType = 'vmapTexture'
    lx.eval('shader.create {%s}' % strItemType)


def Wind_Force_Count_All():
    strItemType = 'Wind Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Wind_Force_Count_Selected():
    strItemType = 'Wind Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Wind_Force_Count_UnSelected():
    strItemType = 'Wind Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Wind_Force_Name_All():
    strItemType = 'Wind Force'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Wind_Force_Name_Selected():
    strItemType = 'Wind Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Wind_Force_Name_UnSelected():
    strItemType = 'Wind Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Wind_Force_ID_All():
    strItemType = 'Wind Force'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Wind_Force_ID_Selected():
    strItemType = 'Wind Force'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Wind_Force_ID_UnSelected():
    strItemType = 'Wind Force'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Wind_Force_Add_New():
    strItemType = 'force.wind'
    lx.eval('item.create {%s}' % strItemType)


def Wood_Count_All():
    strItemType = 'Wood'
    asVariant = 'all'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Wood_Count_Selected():
    strItemType = 'Wood'
    asVariant = 'selected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Wood_Count_UnSelected():
    strItemType = 'Wood'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Count(strItemType, asVariant)


def Wood_Name_All():
    strItemType = 'Wood'
    asVariant = 'all'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Wood_Name_Selected():
    strItemType = 'Wood'
    asVariant = 'selected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Wood_Name_UnSelected():
    strItemType = 'Wood'
    asVariant = 'unselected'
    return __fn_pyModo_Item_Name(strItemType, asVariant)


def Wood_ID_All():
    strItemType = 'Wood'
    asVariant = 'all'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Wood_ID_Selected():
    strItemType = 'Wood'
    asVariant = 'selected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Wood_ID_UnSelected():
    strItemType = 'Wood'
    asVariant = 'unselected'
    return __fn_pyModo_Item_ID(strItemType, asVariant)


def Wood_Add_New():
    strItemType = 'wood'
    lx.eval('shader.create {%s}' % strItemType)


####################################################
####################################################

def Scene_SaveAs_LXO(Requires_FullPath):
    lx.eval('!scene.saveas {%s} $LXOB 0' % (Requires_FullPath))


def Scene_SaveAs_FBX(Requires_FullPath):
    lx.eval('!scene.saveas {%s} fbx 0' % (Requires_FullPath))


def Scene_SaveAs_DAE(Requires_FullPath):
    lx.eval('!scene.saveas {%s} COLLADA_141 0' % (Requires_FullPath))


def Scene_SaveAs_LWO(Requires_FullPath):
    lx.eval('!scene.saveas {%s} $NLWO2 0' % (Requires_FullPath))


def Scene_SaveAs_3DM(Requires_FullPath):
    lx.eval('!scene.saveas {%s} 3DM 0' % (Requires_FullPath))


def Scene_SaveAs_ALEMBIC(Requires_FullPath):
    lx.eval('!scene.saveas {%s} Alembic 0' % (Requires_FullPath))


def Scene_SaveAs_DXF(Requires_FullPath):
    lx.eval('!scene.saveas {%s} DXF 0' % (Requires_FullPath))


def Scene_SaveAs_OBJ(Requires_FullPath):
    lx.eval('!scene.saveas {%s} wf_OBJ 0' % (Requires_FullPath))


def Scene_Current_Set(Requires_ScnIndx):
    lx.eval('!scene.set {%s}' % Requires_ScnIndx)


def Scene_Current_Index_Get():
    return lx.eval('scene.current ?')


def Scene_Open(Requires_FullPath):
    lx.eval('!scene.open {%s}' % Requires_FullPath)


def Scene_New():
    lx.eval('scene.new')


def Scene_Close():
    lx.eval('!scene.close')


def Scene_Count_All():
    return lx.eval('query sceneservice scene.N ?')


def Scene_Name(Requires_SceneIndex):
    return __fn_pyModo_Scene_Main('name', Requires_SceneIndex)


def Scene_Name_Get_All():
    return __fn_pyModo_Scene_Main('name')


def Scene_Index_Get_All():
    return __fn_pyModo_Scene_Main('index')


def Scene_FilePath(Requires_SceneIndex):
    return __fn_pyModo_Scene_Main('file', Requires_SceneIndex)


def Scene_FilePath_Get_All():
    return __fn_pyModo_Scene_Main('file')


def Scene_Format(Requires_SceneIndex):
    return __fn_pyModo_Scene_Main('format', Requires_SceneIndex)


def Scene_Format_Get_All():
    return __fn_pyModo_Scene_Main('format')


def __fn_pyModo_Scene_Main(varCheck, *args):
    Scene_Check_List = []

    TotalScenes = Scene_Count_All()

    if not args:
        for EachScene in range(0, TotalScenes):
            lx.eval('!scene.set {%s}' % EachScene)
            Scene_Check_List.append(lx.eval('query sceneservice scene.%s ? {%s}' % (varCheck, EachScene)))
    if args:
        EachScene = args
        lx.eval('!scene.set {%s}' % EachScene)
        Scene_Check_List.append(lx.eval('query sceneservice scene.%s ? {%s}' % (varCheck, EachScene)))

    return Scene_Check_List


####################################################
####################################################

def Batch_File_Conversion():
    strSelect = ''
    batchChoice = ''

    extList = ['OBJ', 'LXO', 'LWO', 'FBX', 'DAE', 'ABC']

    for extFrom in extList:
        for extTo in extList:
            if extTo != extFrom:
                strSelect = strSelect + extFrom + '<TO>' + extTo + ';'

    strSelect = strSelect[:len(strSelect) - 1]
    batchChoice = Modo_UserChoice_Selection(strSelect)
    fileType_From = batchChoice[:batchChoice.index('<')]
    fileType_To = batchChoice[batchChoice.index('>') - len(batchChoice) + 1:]

    strPath = Modo_UserDataEntry_asString('Paste Your Directory Path!')

    if not strPath[-2:] == '\*':
        strPathDir = strPath + '\*'

    for eachFile in glob.glob(strPathDir):
        #get the filename
        f = os.path.basename(eachFile)
        fileExt = '.' + str(fileType_From.lower())
        if str(f[-4:].lower()) == fileExt:
            Scene_Open(eachFile)

            #FINALIZE....
            #get the file name...
            newFileName = str(Scene_Name(0)[0]).split('.')[0]

            #Save as obj file
            if fileType_To == 'OBJ':
                fldr_OBJ = '_OBJ'
                objPath = strPath + '/' + fldr_OBJ
                if not os.path.exists(objPath): os.makedirs(objPath)
                strSaveAs = objPath + '/' + newFileName + '.obj'
                Scene_SaveAs_OBJ(strSaveAs)

            #Save as lxo file
            if fileType_To == 'LXO':
                fldr_LXO = '_LXO'
                lxoPath = strPath + '/' + fldr_LXO
                if not os.path.exists(lxoPath): os.makedirs(lxoPath)
                strSaveAs = lxoPath + '/' + newFileName + '.lxo'
                Scene_SaveAs_LXO(strSaveAs)

            #Save as lightwave file
            if fileType_To == 'LWO':
                fldr_LWO = '_LWO'
                lwoPath = strPath + '/' + fldr_LWO
                if not os.path.exists(lwoPath): os.makedirs(lwoPath)
                strSaveAs = lwoPath + '/' + newFileName + '.lwo'
                Scene_SaveAs_LWO(strSaveAs)

            #Save as fbx file
            if fileType_To == 'FBX':
                fldr_FBX = '_FBX'
                fbxPath = strPath + '/' + fldr_FBX
                if not os.path.exists(fbxPath): os.makedirs(fbxPath)
                strSaveAs = fbxPath + '/' + newFileName + '.fbx'
                Scene_SaveAs_FBX(strSaveAs)

            #Save as dae collada file
            if fileType_To == 'DAE':
                fldr_DAE = '_DAE'
                daePath = strPath + '/' + fldr_DAE
                if not os.path.exists(daePath): os.makedirs(daePath)
                strSaveAs = daePath + '/' + newFileName + '.dae'
                Scene_SaveAs_DAE(strSaveAs)

            #Save as alembic file
            if fileType_To == 'ABC':
                fldr_ABC = '_ABC'
                abcPath = strPath + '/' + fldr_ABC
                if not os.path.exists(abcPath): os.makedirs(abcPath)
                strSaveAs = abcPath + '/' + newFileName + '.abc'
                Scene_SaveAs_ALEMBIC(strSaveAs)

            #close the scene file
            Scene_Close()
        #done


####################################################
####################################################
#ITEM START


def Item_Name_Get(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        return __fn_pyModo_Scene_ItemName(EachItem)


####################################################
####################################################

def Item_ID_Get(Requires_ItemName):
    if type(Requires_ItemName) is list:
        TheList = Requires_ItemName
    else:
        TheList = str.split(Requires_ItemName, ',')
    for EachItem in TheList:
        return __fn_pyModo_Scene_ItemID(EachItem)


def Item_Type_Get(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        return __fn_pyModo_Scene_ItemType(EachItem)


####################################################
####################################################

def Item_Name_Set(Requires_ItemID, RequiresNameAsString):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        lx.eval('select.Item item:{%s} mode: set' % EachItem)
        lx.eval('!item.name {%s}' % RequiresNameAsString)


####################################################
####################################################

def Item_Delete(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        lx.eval('select.Item item:{%s} mode: set' % EachItem)
        lx.eval('!item.delete')


####################################################
####################################################

def Item_Duplicate(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        lx.eval('select.Item item:{%s} mode: set' % EachItem)
        lx.eval('!item.duplicate false locator false true')


def Item_Duplicate_No_Hierarchy(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        lx.eval('select.Item item:{%s} mode: set' % EachItem)
        lx.eval('!item.duplicate mods:false')


def Item_Duplicate_fromSelected():
    toDupe = Item_ID_fromSelected_Get()
    for eachID in toDupe:
        Item_Duplicate(eachID)


def Item_Duplicate_fromSelected_No_Hierarchy():
    toDupe = Item_ID_fromSelected_Get()
    for eachID in toDupe:
        Item_Duplicate_No_Hierarchy(eachID)


def Item_ID_fromSelected_Get():
    ItemID_fromSelected = []
    IDs = Scene_Get_Item_IDs_All()
    for id in IDs:
        iSel = __fn_pyModo_Scene_ItemsSelected(id)
        if iSel:
            ItemID_fromSelected.append(id)
    return ItemID_fromSelected


####################################################
####################################################

def Item_Instance(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        lx.eval('select.Item item:{%s} mode: set' % EachItem)
        lx.eval('!item.duplicate true locator false true')


####################################################
####################################################

def Item_Select(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    intTotalMeshes = 0

    for EachItem in TheList:
        if intTotalMeshes == 0:
            lx.eval('select.Item item:{%s} mode: set' % EachItem)
            lx.eval('query layerservice layer.name ? current')
        else:
            lx.eval('select.subItem item:{%s} mode: add' % EachItem)

        intTotalMeshes += 1


####################################################
####################################################

def Item_DeSelect(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        lx.eval('select.Item item:{%s} mode: remove' % EachItem)


####################################################
####################################################

def Item_Channel_Get_Value(Requires_Channel_Name):
    return __fn_pyModo_Item_Channel_Main(Requires_Channel_Name)


def Item_Channel_Select(RequiresOneItemID, RequiresOneChannelName):
    if type(RequiresOneItemID) is list:
        TheList = RequiresOneItemID
    else:
        TheList = str.split(RequiresOneItemID, ',')

    for EachItem in TheList:
        lx.eval('select.channel {%s:%s} set' % (EachItem, RequiresOneChannelName))


####################################################
####################################################

def Item_Channel_Set_Value(Requires_ChannelName, Requires_ChannelValue):
    lx.eval('item.channel {%s} {%s}' % (Requires_ChannelName, Requires_ChannelValue))


####################################################
####################################################

def Item_Channel_Get_Names(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    Item_Select(TheList)
    return __fn_pyModo_Item_Channel_Main('chan_name')


####################################################
####################################################

def Item_Parent_To_RenderRoot(Requires_ItemID, RootIndexPos):
    rndrRoot = Render_ID_All()
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        Item_Select(EachItem)
        lx.eval('texture.parent %s %s' % (rndrRoot[0], RootIndexPos))


def Item_Parent_in_Place(Requires_OneChildID, Requires_OneParentID):
    if type(Requires_OneChildID) is list:
        Child = Requires_OneChildID[0]
    else:
        Child = str.split(Requires_OneChildID, ',')[0]

    if type(Requires_OneParentID) is list:
        Parent = Requires_OneParentID[0]
    else:
        Parent = str.split(Requires_OneParentID, ',')[0]
    lx.eval('select.Item item:{%s} mode: add' % Child)
    lx.eval('select.subItem item:{%s} mode:add' % Parent)
    lx.eval('item.parent {%s} {%s} inPlace:1' % (Child, Parent))


def Item_ChildrenID_Get(Requires_ParentItemID):
    Kid_List = []
    if type(Requires_ParentItemID) is list:
        TheList = Requires_ParentItemID
    else:
        TheList = str.split(Requires_ParentItemID, ',')

    for EachItem in TheList:
        All_Kids = lx.evalN('query sceneservice item.children ? {%s}' % EachItem)
        for eachKid in All_Kids:
            Kid_List.append(eachKid)

    return Kid_List


def Item_ParentID_Get(Requires_ChildItemID):
    Mama_List = []
    if type(Requires_ChildItemID) is list:
        TheList = Requires_ChildItemID
    else:
        TheList = str.split(Requires_ChildItemID, ',')

    for EachItem in TheList:
        BigMamas = lx.evalN('query sceneservice item.parent ? {%s}' % EachItem)
        for eachMum in BigMamas:
            Mama_List.append(eachMum)

    return Mama_List


####################################################
####################################################

def Mesh_Transform_ID_Get(Requires_ItemID):
    Transform_ID_List = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        TransID = lx.eval('query sceneservice item.xfrmItems ? {%s}' % EachItem)
        if TransID != None:
            for eachTrID in TransID:
                Transform_ID_List.append(eachTrID)
    return Transform_ID_List


####################################################
####################################################

def Scene_Get_Item_Names_All():
    return __fn_pyModo_Scene_ItemList('name')


def Scene_Get_Item_IDs_All():
    return __fn_pyModo_Scene_ItemList('id')


def Scene_Get_Item_Labels_All():
    return __fn_pyModo_Scene_ItemList('typeLabel')


def Scene_Get_Item_Types_All():
    return __fn_pyModo_Scene_ItemList('type')


def Scene_Get_Item_Tags_All():
    return __fn_pyModo_Scene_ItemList('tags')


def __fn_pyModo_Scene_ItemList(ItemCheck):
    SceneItems = lx.eval('query sceneservice item.N ? ')

    ItemCheckList = []

    for EachItem in range(SceneItems):
        if ItemCheck == 'name':
            retVal = lx.eval('query sceneservice item.name ? {%s}' % EachItem)
        if ItemCheck == 'id':
            retVal = lx.eval('query sceneservice item.id ? {%s}' % EachItem)
        if ItemCheck == 'typeLabel':
            retVal = lx.eval('query sceneservice item.typeLabel ? {%s}' % EachItem)
        if ItemCheck == 'type':
            retVal = lx.eval('query sceneservice item.type ? {%s}' % EachItem)
        if ItemCheck == 'tags':
            retVal = lx.eval('query sceneservice item.tags ? {%s}' % EachItem)

        ItemCheckList.append(retVal)

    return ItemCheckList


def AfterItem_Create_or_Select_GetItemName(): return lx.eval('item.name ?')


def AfterItem_Create_or_Select_SetItemName(RequiresNewName): return lx.eval('item.name {%s}' % RequiresNewName)


####################################################
####################################################

def Modo_Path_Directory_Scripts():
    return lx.eval('query platformservice path.path ? scripts')


def Modo_Path_Directory_Config():
    return lx.eval('query platformservice path.path ? configs')


def Modo_Path_Directory_Kits():
    return lx.eval('query platformservice path.path ? kits')


def Modo_Path_Directory_User():
    return lx.eval('query platformservice path.path ? user')


def Modo_Path_Directory_Content():
    return lx.eval('query platformservice path.path ? content')


def Modo_Path_Directory_Asset():
    return lx.eval('query platformservice path.path ? asset')


def Modo_Path_Directory_Prefs():
    return lx.eval('query platformservice path.path ? prefs')


def Modo_Path_Directory_Temp():
    return lx.eval('query platformservice path.path ? temp')


def Modo_Path_Directory_Project():
    return lx.eval('query platformservice path.path ? project')


def Modo_Path_Directory_Documents():
    return lx.eval('query platformservice path.path ? documents')


def Modo_Path_Directory_Headless():
    return lx.eval('query platformservice path.path ? headless')


def Modo_Path_Directory_ConfigName():
    return lx.eval('query platformservice path.path ? configname')


####################################################
####################################################



def Modo_SysPref_AutoSave_Enable(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value autosave.enable %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value autosave.enable %s' % Pref)


def Modo_SysPref_AutoSave_Time(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value autosave.time %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value autosave.time %s' % Pref)


def Modo_SysPref_AutoSave_Path(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value autosave.directory %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value autosave.directory %s' % Pref)


def Modo_SysPref_AutoSave_Revisions(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value autosave.versions %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value autosave.versions %s' % Pref)


def Modo_SysPref_ColorManagement_OCIO(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value colormanagement.default_ocio_config %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value colormanagement.default_ocio_config %s' % Pref)


def Modo_SysPref_ColorManagement_8bit(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value colormanagement.8bit_default_colorspace %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value colormanagement.8bit_default_colorspace %s' % Pref)


def Modo_SysPref_ColorManagement_16bit(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value colormanagement.16bit_default_colorspace %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value colormanagement.16bit_default_colorspace %s' % Pref)


def Modo_SysPref_ColorManagement_Float(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value colormanagement.float_default_colorspace %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value colormanagement.float_default_colorspace %s' % Pref)


def Modo_SysPref_ColorManagement_View(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value colormanagement.view_default_colorspace %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value colormanagement.view_default_colorspace %s' % Pref)


def Modo_SysPref_ColorManagement_AffectModoColorPicker(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value colormanagement.colorMappingApplyToColorSwatches %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value colormanagement.colorMappingApplyToColorSwatches %s' % Pref)


def Modo_SysPref_ColorManagement_AffectSystemColorDialog(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value colormanagement.colorMappingApplyToSystemDialog %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value colormanagement.colorMappingApplyToSystemDialog %s' % Pref)


def Modo_SysPref_FinalRendering_AutoRenderThreads(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.autoThreads %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.autoThreads %s' % Pref)


def Modo_SysPref_FinalRendering_RenderThreads(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.numThread %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.numThreads %s' % Pref)


def Modo_SysPref_FinalRendering_GeometryCache(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.cacheSize %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.cacheSize %s' % Pref)


def Modo_SysPref_FinalRendering_UseNetWorkNodes(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.useNetwork %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.useNetwork %s' % Pref)


def Modo_SysPref_FinalRendering_NetWorkRenderGroup(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value lanservices.networkRenderGroup %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value lanservices.networkRenderGroup %s' % Pref)


def Modo_SysPref_FinalRendering_NetWorkJobSize(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.netJobSize %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.netJobSize %s' % Pref)


def Modo_SysPref_FinalRendering_SendAcceptAssets(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value lanservices.sendAssetsForNetworkJob %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value lanservices.sendAssetsForNetworkJob %s' % Pref)


def Modo_SysPref_FinalRendering_NetWorkSharedDirectory(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value lanservices.netPath %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value lanservices.netPath %s' % Pref)


def Modo_SysPref_FinalRendering_NodesViaBonjour(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value lanservices.discoverWithBonjour %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value lanservices.discoverWithBonjour %s' % Pref)


def Modo_SysPref_FinalRendering_NodesViaHostList(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value lanservices.discoverWithHostlist %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value lanservices.discoverWithHostlist %s' % Pref)


def Modo_SysPref_FinalRendering_OutPutGamma(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.outputGamma %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.outputGamma %s' % Pref)


def Modo_SysPref_FinalRendering_ColorPickerStops(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.colorPickerStops %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.colorPickerStops %s' % Pref)


def Modo_SysPref_FinalRendering_AffectColorControlSwatches(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.applyColorPickerStopsToColorSwatches %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.applyColorPickerStopsToColorSwatches %s' % Pref)


def Modo_SysPref_FinalRendering_DefaultFieldRendering(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.fieldRendering %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.fieldRendering %s' % Pref)


def Modo_SysPref_FinalRendering_BakeUV_BorderSize(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.bakeBorder %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.bakeBorder %s' % Pref)


def Modo_SysPref_FinalRendering_FrameCacheSize(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.frameCacheSize  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.frameCacheSize  %s' % Pref)


def Modo_SysPref_FinalRendering_WriteBucketsDirectory(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.bucketDir  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.bucketDir  %s' % Pref)


def Modo_SysPref_FinalRendering_RecentFramesDirectory(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.frameDir  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.frameDir  %s' % Pref)


def Modo_SysPref_FinalRendering_DefaultOutPutPattern(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.outputPattern  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.outputPattern  %s' % Pref)


def Modo_SysPref_FinalRendering_BlockSystemSleep(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.allowInsomnia  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.allowInsomnia  %s' % Pref)


def Modo_SysPref_FinalRendering_AutoAdd(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value render.autoAdd %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value render.autoAdd  %s' % Pref)


def Modo_SysPref_MeshItems_AutoMask(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value application.autoMask %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value application.autoMask  %s' % Pref)


def Modo_SysPref_MeshItems_PresetMask(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value application.presetMask %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value application.presetMask  %s' % Pref)


def Modo_SysPref_MeshItems_AutoXfrm(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value application.autoXfrm %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value application.autoXfrm  %s' % Pref)


def Modo_SysPref_MeshItems_AutoHide(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value application.autoHide %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value application.autoHide  %s' % Pref)


def Modo_SysPref_MeshItems_InstanceBBox(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value application.instBBox %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value application.instBBox  %s' % Pref)


def Modo_SysPref_MeshItems_SaveVMapSelection(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value application.saveVMapSelection %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value application.saveVMapSelection  %s' % Pref)


def Modo_SysPref_MeshItems_PatchDivDraw(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value editing.patchDivDraw %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value editing.patchDivDraw  %s' % Pref)


def Modo_SysPref_MeshItems_CurveDivDraw(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value editing.curveDivDraw %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value editing.curveDivDraw  %s' % Pref)


def Modo_SysPref_MeshItems_CurveAngDraw(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value editing.curveAngDraw %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value editing.curveAngDraw  %s' % Pref)


def Modo_SysPref_MeshItems_SpatchDivDraw(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value editing.spatchDivDraw %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value editing.spatchDivDraw  %s' % Pref)


def Modo_SysPref_MeshItems_PsubDivDraw(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value editing.psubDivDraw %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value editing.psubDivDraw  %s' % Pref)


def Modo_SysPref_MeshItems_DefaultSubdivs(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value application.defaultSubdivs %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value application.defaultSubdivs  %s' % Pref)


def Modo_SysPref_MeshItems_SymmetricPrimitive(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value application.symmetricPrimitive %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value application.symmetricPrimitive  %s' % Pref)


def Modo_SysPref_MeshItems_FlatLimit(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value application.flatLimit %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value application.flatLimit  %s' % Pref)


def Modo_SysPref_MeshItems_DeleteMode(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value application.deleteMode %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value application.deleteMode  %s' % Pref)


def Modo_SysPref_MeshItems_CopyDeSelection(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value application.copyDeSelection %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value application.copyDeSelection  %s' % Pref)


def Modo_SysPref_MeshItems_PasteSelection(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value application.pasteSelection %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value application.pasteSelection  %s' % Pref)


def Modo_SysPref_MeshItems_PasteDeSelection(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value application.pasteDeSelection %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value application.pasteDeSelection  %s' % Pref)


def Modo_SysPref_MeshItems_SlipUVState(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value application.slipUVState %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value application.slipUVState  %s' % Pref)


def Modo_SysPref_ToolStacks_DefaultComp_ActionCenter(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value tool.actionCenter %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value tool.actionCenter  %s' % Pref)


def Modo_SysPref_ToolStacks_DefaultComp_ActionAxis(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value tool.actionAxis %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value tool.actionAxis  %s' % Pref)


def Modo_SysPref_ToolStacks_DefaultComp_Brush(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value tool.brush %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value tool.brush  %s' % Pref)


def Modo_SysPref_ToolStacks_DefaultComp_Constraint(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value tool.const %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value tool.const  %s' % Pref)


def Modo_SysPref_ToolStacks_DefaultItem_ActionCenterItem(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value tool.actionCenterItem %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value tool.actionCenterItem  %s' % Pref)


def Modo_SysPref_ToolStacks_DefaultItem_ActionAxisItem(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value tool.actionAxisItem %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value tool.actionAxisItem  %s' % Pref)


def Modo_SysPref_ToolStacks_DefaultItem_BrushItem(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value tool.brushItem %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value tool.brushItem  %s' % Pref)


def Modo_SysPref_ToolStacks_DefaultItem_Constraint(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value tool.constItem %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value tool.constItem  %s' % Pref)


def Modo_SysPref_ColladaExport_AbsPath(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value export.absPath %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value export.absPath  %s' % Pref)


def Modo_SysPref_ColladaExport_MergsRefs(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value export.mergsRefs %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value export.mergsRefs  %s' % Pref)


def Modo_SysPref_ColladaExport_Units_System(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value units.system %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value units.system %s' % Pref)


def Modo_SysPref_ColladaExport_Units_Default(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value units.default %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value units.default %s' % Pref)


def Modo_SysPref_ColladaExport_Units_GameScale(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value units.gameScale %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value units.gameScale %s' % Pref)


def Modo_SysPref_ColladaExport_Units_UpAxis(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value units.upAxis %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value units.upAxis %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_SaveHiddenItems(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.hidden.items %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.hidden.items %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_Cameras(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.cameras %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.cameras %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_Lights(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.lights %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.lights %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_Locators(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.locators %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.locators %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_TrisAsTris(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.triangles.as.triangles %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.triangles.as.triangles %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_OrderVmaps(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.order.vmaps.alphabetically %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.order.vmaps.alphabetically %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_BakeMatrices(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.bake.matrices %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.bake.matrices %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_SaveNormals(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.normals %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.normals %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_SaveTextureCoOrds(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.texcoords %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.texcoords %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_SaveColors(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.colors %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.colors %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_SaveWeights(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.weights %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.weights %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_SaveAnimation(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.animation %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.animation %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_SampleAnimation(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.sample.animation %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.sample.animation %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_SampleAnimationStart(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.sample.animation.start %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.sample.animation.start %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_SampleAnimationEnd(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.sample.animation.end %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.sample.animation.end %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_Z_Near(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.z.near %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.z.near %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_Z_Far(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.z.far %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.z.far %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_Modo_Profile(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.modo.profile %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.modo.profile %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_Maya_Profile(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.maya.profile %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.maya.profile %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_3DSMax_Profile(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.max3d.profile %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.max3d.profile %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_Okino_Profile(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.okino.profile %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.okino.profile %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_XSI_Profile(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.save.xsi.profile %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.save.xsi.profile %s' % Pref)


def Modo_SysPref_ColladaExport_SceneIO_Formatted_Arrays(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.formatted.arrays %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.formatted.arrays %s' % Pref)


def Modo_SysPref_ColladaImport_SceneIO_Units(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.import.units %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.import.units %s' % Pref)


def Modo_SysPref_ColladaImport_SceneIO_UpAxis(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.collada.import.up.axis %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.collada.import.up.axis %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveFormat(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.format  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.format  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveExportType(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.exportType  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.exportType  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveExportToASCII(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.exportToASCII  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.exportToASCII  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveAnimationOnly(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.animationOnly  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.animationOnly  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveGeometry(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.geometry  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.geometry  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveCameras(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.cameras  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.cameras  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveLights(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.lights  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.lights  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveMaterials(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.materials  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.materials  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SavePolygonParts(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.polygonParts  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.polygonParts  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveSelectionSets(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.selectionSets  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.selectionSets  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveMeshSmoothing(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.meshSmoothing  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.meshSmoothing  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveSmoothingGroups(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.smoothingGroups  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.smoothingGroups  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveMorphMaps(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.morphMaps  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.morphMaps  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveAnimation(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.animation  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.animation  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveSampleAnimation(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.sampleAnimation  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.sampleAnimation  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveSampleAnimFpsMultiplier(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.sampleAnimFpsMultiplier  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.sampleAnimFpsMultiplier  %s' % Pref)


def Modo_SysPref_FBX_SceneIO_SaveExportActionType(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('user.value sceneio.fbx.save.exportActionType  %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('user.value sceneio.fbx.save.exportActionType  %s' % Pref)


def Modo_SysPref_RGB_Colors_Scheme_LoadPreset(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('scheme.loadPreset %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('scheme.loadPreset %s' % Pref)


def Modo_SysPref_RGB_Colors_Scheme_SavePreset(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('scheme.savePreset %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('scheme.savePreset %s' % Pref)


def Modo_SysPref_RGB_Colors_HELP_SeeModoLog():
    Modo_Log('FOR ALL COLOR CHANGES')
    Modo_Log('IN THE pyMODO modules Modo_SysPref_RGB* ')
    Modo_Log('SEND THE RGB VALUES AS A STRING IN QUOTES LIKE THIS...')
    Modo_Log(''' '0.43 0.35 0.37' ''')
    Modo_Log('WITH A SINGLE SPACE IN BETWEEN EACH VALUE!')
    Modo_Log('ie: R_Value SPACE G_Value SPACE B_Value')


def Modo_SysPref_RGB_Colors_BackGround(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.backdrop %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.backdrop {%s}' % Pref)


def Modo_SysPref_RGB_Colors_DeformersActive(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.deformers %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.deformers {%s}' % Pref)


def Modo_SysPref_RGB_Colors_SetupMode(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.setup %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.setup {%s}' % Pref)


def Modo_SysPref_RGB_Colors_Grid(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.axes %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.axes {%s}' % Pref)


def Modo_SysPref_RGB_Colors_WorkPlane(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.grid %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.grid {%s}' % Pref)


def Modo_SysPref_RGB_Colors_Wireframe(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.wireframe %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.wireframe {%s}' % Pref)


def Modo_SysPref_RGB_Colors_ColorWireFrame(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.colorWire %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.colorWire {%s}' % Pref)


def Modo_SysPref_RGB_Colors_BackGroundItem(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.bLayer %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.bLayer {%s}' % Pref)


def Modo_SysPref_RGB_Colors_Instances(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.instance %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.instance {%s}' % Pref)


def Modo_SysPref_RGB_Colors_Solid(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.sketch %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.sketch {%s}' % Pref)


def Modo_SysPref_RGB_Colors_PatchCage(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.patchCage %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.patchCage {%s}' % Pref)


def Modo_SysPref_RGB_Colors_DiscontuousPair(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.discoPair %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.discoPair {%s}' % Pref)


def Modo_SysPref_RGB_Colors_Selection(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.selection %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.selection {%s}' % Pref)


def Modo_SysPref_RGB_Colors_SelectionFill(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.selectionFill %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.selectionFill {%s}' % Pref)


def Modo_SysPref_RGB_Colors_ChildHighlight(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.childHighlight %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.childHighlight {%s}' % Pref)


def Modo_SysPref_RGB_Colors_AssemblyHighlight(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.assemHighlight %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.assemHighlight {%s}' % Pref)


def Modo_SysPref_RGB_Colors_Lasso(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.lasso %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.lasso {%s}' % Pref)


def Modo_SysPref_RGB_Handles_Handle(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.handle %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.handle {%s}' % Pref)


def Modo_SysPref_RGB_Handles_Active(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.handleHot %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.handleHot {%s}' % Pref)


def Modo_SysPref_RGB_Handles_AxisX(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.axisX %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.axisX {%s}' % Pref)


def Modo_SysPref_RGB_Handles_AxisY(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.axisY %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.axisY {%s}' % Pref)


def Modo_SysPref_RGB_Handles_AxisZ(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.axisZ %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.axisZ {%s}' % Pref)


def Modo_SysPref_RGB_Handles_Guide(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.handleGuide %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.handleGuide {%s}' % Pref)


def Modo_SysPref_RGB_Handles_Cage(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.handleCage %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.handleCage {%s}' % Pref)


def Modo_SysPref_RGB_Handles_Label(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.handleLabel %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.handleLabel {%s}' % Pref)


def Modo_SysPref_RGB_Handles_RangeCool(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.cool %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.cool {%s}' % Pref)


def Modo_SysPref_RGB_Handles_RangeWarm(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.warm %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.warm {%s}' % Pref)


def Modo_SysPref_RGB_Handles_UnSnapped(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.handleUnsnap %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.handleUnsnap {%s}' % Pref)


def Modo_SysPref_RGB_Text_Selection(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.hudSelect %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.hudSelect {%s}' % Pref)


def Modo_SysPref_RGB_Text_Info(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.hudAction %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.hudAction {%s}' % Pref)


def Modo_SysPref_RGB_Text_Weights(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.weightValues %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.weightValues {%s}' % Pref)


def Modo_SysPref_RGB_SelectionRollOver_Generic(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.rollover %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.rollover {%s}' % Pref)


def Modo_SysPref_RGB_SelectionRollOver_Face(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.rolloverFace %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.rolloverFace {%s}' % Pref)


def Modo_SysPref_RGB_SelectionRollOver_SubDivision(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.rolloverSubD %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.rolloverSubD {%s}' % Pref)


def Modo_SysPref_RGB_SelectionRollOver_CatMullClark(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.rolloverPSub %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.rolloverPSub {%s}' % Pref)


def Modo_SysPref_RGB_Topo_Face(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.topoFace %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.topoFace {%s}' % Pref)


def Modo_SysPref_RGB_Topo_Vert(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.topoVert %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.topoVert {%s}' % Pref)


def Modo_SysPref_RGB_Topo_Edge(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.topoEdge %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.topoEdge {%s}' % Pref)


def Modo_SysPref_RGB_Topo_BackEdge(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.topoBackEdge %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.topoBackEdge {%s}' % Pref)


def Modo_SysPref_RGB_PSUBS_Mask(*BlankValueHereWillGetElseSet):
    if not BlankValueHereWillGetElseSet:
        Pref = '?'
        return lx.eval('pref.value color.psubMask %s' % Pref)
    else:
        Pref = BlankValueHereWillGetElseSet
        lx.eval('pref.value color.psubMask {%s}' % Pref)


####################################################
####################################################

def Image_Load():
    try:
        lx.eval('clip.load')
    except:
        sys.exit()


def Image_Map_SetToShader(Requires_ImageName):
    if type(Requires_ImageName) is list:
        TheList = Requires_ImageName
    else:
        TheList = str.split(Requires_ImageName, ',')

    for EachItem in TheList:
        strImapSet = 'texture.setIMap {' + EachItem + ':videoStill001}'
        lx.eval(strImapSet)


####################################################
####################################################
#MODO START

def Modo_Log(RequiresVariableNameHere):
    lx.out(RequiresVariableNameHere)


####################################################
####################################################

def Modo_UserMessage_Info(strMsgTitle, strMsgToUser):
    return __fn_pyModo_MsgBox('info', strMsgTitle, strMsgToUser)


####################################################
####################################################

def Modo_UserMessage_OkCancel(strMsgTitle, strMsgToUser):
    return __fn_pyModo_MsgBox('OkCancel', strMsgTitle, strMsgToUser)


####################################################
####################################################

def Modo_UserMessage_YesNo(strMsgTitle, strMsgToUser):
    return __fn_pyModo_MsgBox('YesNo', strMsgTitle, strMsgToUser)


####################################################
####################################################

def Vert_Select(Requires_Vert_Index):
    Layer_Index = lx.eval('query layerservice layer.index ? current')
    Vert_Mode_Set()
    lx.eval('select.element layer:{%s} type:vertex mode:add index:{%s}' % (Layer_Index, Requires_Vert_Index))


def Vert_DeSelect(Requires_Vert_Index):
    Layer_Index = lx.eval('query layerservice layer.index ? current')
    Vert_Mode_Set()
    lx.eval('select.element layer:{%s} type:vertex mode:remove index:{%s}' % (Layer_Index, Requires_Vert_Index))


def Vert_Delete(): lx.eval('delete')


def Vert_Copy(): lx.eval('copy')


def Vert_Paste(): lx.eval('paste')


def Vert_Invert_Selection(): lx.eval('select.invert')


def Edge_Select(Requires_Edge_Index):
    Layer_Index = lx.eval('query layerservice layer.index ? current')
    Edge_Mode_Set()
    EdgeIndex = Requires_Edge_Index[1:-1]
    EdgeIndex = EdgeIndex.split(',')
    FirstEdgeIndex = EdgeIndex[0]
    LastEdgeIndex = EdgeIndex[1]
    lx.eval('select.element layer:{%s} type:edge mode:add index:{%s} index2:{%s}' % (Layer_Index, FirstEdgeIndex, LastEdgeIndex))


def Edge_DeSelect(Requires_Edge_Index):
    Layer_Index = lx.eval('query layerservice layer.index ? current')
    Edge_Mode_Set()
    EdgeIndex = Requires_Edge_Index[1:-1]
    EdgeIndex = EdgeIndex.split(',')
    FirstEdgeIndex = EdgeIndex[0]
    LastEdgeIndex = EdgeIndex[1]
    lx.eval('select.element layer:{%s} type:edge mode:remove index:{%s} index2:{%s}' % (Layer_Index, FirstEdgeIndex, LastEdgeIndex))


def Edge_Delete(): lx.eval('delete')


def Edge_Copy(): lx.eval('copy')


def Edge_Paste(): lx.eval('paste')


def Edge_Invert_Selection(): lx.eval('select.invert')


def Poly_Select(Requires_Poly_Index):
    Layer_Index = lx.eval('query layerservice layer.index ? current')
    lx.eval('select.element layer:{%s} type:polygon mode:add index:{%s}' % (Layer_Index, Requires_Poly_Index))


def Poly_DeSelect(Requires_Poly_Index):
    Layer_Index = lx.eval('query layerservice layer.index ? current')
    lx.eval('select.element layer:{%s} type:polygon mode:remove index:{%s}' % (Layer_Index, Requires_Poly_Index))


def Poly_Delete(): lx.eval('delete')


def Poly_Copy(): lx.eval('copy')


def Poly_Paste(): lx.eval('paste')


def Poly_Invert_Selection(): lx.eval('select.invert')


def Vert_Center_Selected_All():
    Vert_Mode_Set()
    lx.eval('vert.center all')


def Vert_Center_Selected_X():
    Vert_Mode_Set()
    lx.eval('vert.center x')


def Vert_Center_Selected_Y():
    Vert_Mode_Set()
    lx.eval('vert.center y')


def Vert_Center_Selected_Z():
    Vert_Mode_Set()
    lx.eval('vert.center z')


def Vert_Center_Selected_XY():
    Vert_Mode_Set()
    lx.eval('vert.center xy')


def Vert_Center_Selected_YZ():
    Vert_Mode_Set()
    lx.eval('vert.center yz')


def Vert_Center_Selected_ZX():
    Vert_Mode_Set()
    lx.eval('vert.center zx')


def Vert_Create_New(xPos, yPos, zPos):
    lx.eval('vert.new %s %s %s' % (xPos, yPos, zPos))


####################################################
####################################################

def Convert_To_Verts(): lx.eval('select.convert vertex')


def Convert_To_Edges(): lx.eval('select.convert edge')


def Convert_To_Polygons(): lx.eval('select.convert polygon')


def Vert_Mode_Set(): lx.eval('select.type vertex')


def Edge_Mode_Set(): lx.eval('select.type edge')


def Poly_Mode_Set(): lx.eval('select.type polygon')


def Vert_DeSelect_All(): lx.eval('select.drop vertex')


def Edge_DeSelect_All(): lx.eval('select.drop edge')


def Poly_DeSelect_All(): lx.eval('select.drop polygon')


def Center_DeSelect(): lx.eval('select.drop center')


def Pivot_DeSelect(): lx.eval('select.drop pivot')


def Item_DeSelect(): lx.eval('select.drop item')


def Poly_Create_FromVertsSelected(): lx.eval('poly.make auto')


####################################################
####################################################

def Mesh_Merge(Requires_ItemID):
    Item_Select(Requires_ItemID)
    lx.eval('layer.mergeMeshes true')


def Mesh_Merge(Requires_ItemID):
    Item_Select(Requires_ItemID)
    lx.eval('!layer.unmergeMeshes')


####################################################
####################################################

def Mesh_Export(Requires_ItemID, Full_File_Path):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    Convert_To_Polygons()
    SelSetName = 'pyModoSS_MeshExport'
    SelectionSet_AddTo(SelSetName)

    for EachItem in TheList:
        Item_Select(EachItem)
        Poly_Mode_Set()
        SelectionSet_Select(SelSetName)
        PolyCnt = Poly_Count_Selected(EachItem)
        if PolyCnt < 1:
            Item_Select(EachItem)
            Poly_Invert_Selection()
        Poly_Copy()
        Scene_New()
        M_Cnt = Mesh_Count_All()
        if M_Cnt < 1: Mesh_Add_New()
        M_ID = Mesh_ID_All()
        Item_Select(M_ID)
        Poly_Paste()
        Scene_SaveAs_OBJ(Full_File_Path)
        Scene_Close()
        Poly_Mode_Set()
        SelectionSet_Delete(SelSetName)


####################################################
####################################################

def Material_Rename_Set(RequiresMaterialName, RequiresNewMaterialName):
    lx.eval('poly.renameMaterial {%s} {%s}' % (RequiresMaterialName, RequiresNewMaterialName))


def Poly_Set_Material(MaterialName, Rcolor_Value, Gcolor_Value, Bcolor_Value, DiffuseValue, SpecularValue, Smoothing=1, Default=0, Library=0):
    lx.eval('!poly.setMaterial {%s} {%s %s %s} %s %s %s %s %s' % ( MaterialName, Rcolor_Value, Gcolor_Value, Bcolor_Value, DiffuseValue, SpecularValue, Smoothing, Default, Library))


####################################################
####################################################

def Mesh_Cleanup(RFV, ROPP, RTPP, FDPiP, RCV, FFNV, MV, MDV, UP, FU):
    strMC = '!mesh.cleanup ' + str(RFV) + ' ' + str(ROPP) + ' ' + str(RTPP) + ' ' + str(FDPiP) + ' ' + str(RCV) + ' ' + str(FFNV) + ' ' + str(MV) + ' ' + str(MDV) + ' ' + str(UP) + ' ' + str(FU)
    lx.eval(strMC)


####################################################
####################################################

def Radians_To_Degrees(radians):
    pi = math.pi
    degrees = 180 * radians / pi
    return degrees


def Degrees_To_Radians(degrees):
    pi = math.pi
    radians = pi * degrees / 180
    return radians


####################################################
####################################################

def Transform_Freeze_Position():
    lx.eval('transform.freeze translation')


def Transform_Freeze_Rotation():
    lx.eval('transform.freeze rotation')


def Transform_Freeze_Scale():
    lx.eval('transform.freeze scale')


def Transform_Freeze_Shear():
    lx.eval('transform.freeze shear')


def Transform_Freeze_All():
    lx.eval('transform.freeze all')


def Transform_Reset_Position():
    lx.eval('transform.reset translation')


def Transform_Reset_Rotation():
    lx.eval('transform.reset rotation')


def Transform_Reset_Scale():
    lx.eval('transform.reset scale')


def Transform_Reset_Shear():
    lx.eval('transform.reset shear')


def Transform_Reset_All():
    lx.eval('transform.reset all')


def Transform_Zero_Position():
    lx.eval('transform.zero translation')


def Transform_Zero_Rotation():
    lx.eval('transform.zero rotation')


def Transform_Zero_Scale():
    lx.eval('transform.zero scale')


def Transform_Zero_All():
    lx.eval('transform.zero all')


def Transform_Add_Position():
    lx.eval('transform.add pos')


def Transform_Add_Rotation():
    lx.eval('transform.add rot')


def Transform_Add_Scale():
    lx.eval('transform.add scl')


####################################################
####################################################

def VertList_WorldPos_X_(Requires_ItemID):
    V_Wpos_X_List = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        V_Indx_List = Vert_Index_Selected(EachItem)
        if not V_Indx_List: V_Indx_List = Vert_Index_All(EachItem)

        for eachV_Indx in V_Indx_List:
            V_Wpos_X = lx.eval('query layerservice vert.wpos ? {%s}' % eachV_Indx)[0]
            V_Wpos_X_List.append(V_Wpos_X)
    return V_Wpos_X_List


def VertList_WorldPos_Y_(Requires_ItemID):
    V_Wpos_Y_List = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        V_Indx_List = Vert_Index_Selected(EachItem)
        if not V_Indx_List: V_Indx_List = Vert_Index_All(EachItem)

        for eachV_Indx in V_Indx_List:
            V_Wpos_Y = lx.eval('query layerservice vert.wpos ? {%s}' % eachV_Indx)[1]
            V_Wpos_Y_List.append(V_Wpos_Y)
    return V_Wpos_Y_List


def VertList_WorldPos_Z_(Requires_ItemID):
    V_Wpos_Z_List = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        V_Indx_List = Vert_Index_Selected(EachItem)
        if not V_Indx_List: V_Indx_List = Vert_Index_All(EachItem)

        for eachV_Indx in V_Indx_List:
            V_Wpos_Z = lx.eval('query layerservice vert.wpos ? {%s}' % eachV_Indx)[2]
            V_Wpos_Z_List.append(V_Wpos_Z)
    return V_Wpos_Z_List


def Lattice_Effector_Reset(int_X, int_Y, int_Z, AutoFit_OnOff, Reset_Transform_OnOff, Reset_Positions_OnOff):
    lx.eval('!deform.lattice.reset {%s} {%s} {%s} {%s} {%s} {%s}' % (int_X, int_Y, int_Z, AutoFit_OnOff, Reset_Transform_OnOff, Reset_Positions_OnOff))


####################################################
####################################################

def Vert_Average_Position_X_Get(Requires_ItemID):
    return __fn_pyModo_Vert_Average_Position_Get(Requires_ItemID, 'X')


def Vert_Average_Position_Y_Get(Requires_ItemID):
    return __fn_pyModo_Vert_Average_Position_Get(Requires_ItemID, 'Y')


def Vert_Average_Position_Z_Get(Requires_ItemID):
    return __fn_pyModo_Vert_Average_Position_Get(Requires_ItemID, 'Z')


def __fn_pyModo_Vert_Average_Position_Get(Requires_ItemID, Enter_X_Y_Z_or_ALL):
    if not __fn_pyModo_Check_if_String(Enter_X_Y_Z_or_ALL): Enter_X_Y_Z_or_ALL = str(Enter_X_Y_Z_or_ALL)
    AXIS_mod = Enter_X_Y_Z_or_ALL.upper()

    AveXVertPos = 0  #
    AveYVertPos = 0  #
    AveZVertPos = 0  #

    xVerts = []
    yVerts = []
    zVerts = []
    AvgPos_XYZ = []

    #convert selection to verts
    strSelectionMode = Modo_Component_Mode_Get()
    Convert_To_Verts()
    Vert_Mode_Set()

    VertList = Vert_Index_Selected(Requires_ItemID)

    if not VertList: VertList = Vert_Index_All(Requires_ItemID)

    for EachVert in VertList:
        allVerts = lx.eval('query layerservice vert.wpos ? {%s}' % EachVert)
        xVerts.append(allVerts[0])
        yVerts.append(allVerts[1])
        zVerts.append(allVerts[2])

    AveXVertPos = sum(xVerts) / len(xVerts)
    AveYVertPos = sum(yVerts) / len(yVerts)
    AveZVertPos = sum(zVerts) / len(zVerts)

    lx.eval('select.type {%s}' % strSelectionMode)

    if AXIS_mod == 'X': return AveXVertPos
    if AXIS_mod == 'Y': return AveYVertPos
    if AXIS_mod == 'Z': return AveZVertPos

    if AXIS_mod == 'ALL':
        AvgPos_XYZ.append(AveXVertPos)
        AvgPos_XYZ.append(AveYVertPos)
        AvgPos_XYZ.append(AveZVertPos)
        return AvgPos_XYZ


####################################################
####################################################

def SelectionSet_AddTo(RequiresName):
    if not __fn_pyModo_Check_if_String(RequiresName): RequiresName = str(RequiresName)
    try:
        lx.eval('select.editSet {%s} add' % RequiresName)
    except:
        pass


def SelectionSet_RemoveFrom(RequiresName):
    if not __fn_pyModo_Check_if_String(RequiresName): RequiresName = str(RequiresName)
    try:
        lx.eval('select.editSet {%s} remove' % RequiresName)
    except:
        pass


def SelectionSet_Select(RequiresName):
    if not __fn_pyModo_Check_if_String(RequiresName): RequiresName = str(RequiresName)
    try:
        lx.eval('!select.useSet {%s} select' % RequiresName)
    except:
        pass


def SelectionSet_DeSelect(RequiresName):
    if not __fn_pyModo_Check_if_String(RequiresName): RequiresName = str(RequiresName)
    try:
        lx.eval('!select.useSet {%s} deselect' % RequiresName)
    except:
        pass


def SelectionSet_Delete(RequiresName):
    if not __fn_pyModo_Check_if_String(RequiresName): RequiresName = str(RequiresName)
    try:
        lx.eval('!select.deleteSet {%s}' % RequiresName)
    except:
        pass


def __fn_pyModo_Check_if_String(RequiresName):
    return isinstance(RequiresName, str)


def Vert_Select_UnderMouse():
    Vert_Mode_Set()
    lx.eval('!!select.3DElementUnderMouse set')


def Edge_Select_UnderMouse():
    Edge_Mode_Set()
    lx.eval('!!select.3DElementUnderMouse set')


def Poly_Select_UnderMouse():
    Poly_Mode_Set()
    lx.eval('!!select.3DElementUnderMouse set')


def SelectionSet_UnderMouse():
    PolySS = []
    EdgeSS = []
    VertSS = []

    m_ID = Mesh_ID_Selected()

    if not m_ID:
        Modo_UserMessage_Info('Mesh Selection', 'A selected mesh item is required!!')
        sys.exit()

    if len(m_ID) > 1:
        Modo_UserMessage_Info('Mesh Selection', 'Please select one mesh layer only!!')
        sys.exit()

    mComp = Modo_Component_Mode_Get()

    if mComp == 'polygon':
        PolySS = Poly_SelectionSetNames_Get(m_ID)
        Poly_Select_UnderMouse()
        if Poly_Count_Selected(m_ID) < 1:
            Modo_UserMessage_Info('Polygon Detection', 'Unable to detect a polygon under the mouse!!')
            sys.exit()

        Comp_ID = Poly_Index_Selected(m_ID)

        SelSets = []

        for eachSS in PolySS:
            Poly_DeSelect_All()
            SelectionSet_Select(eachSS)

            for eachPoly in Poly_Index_Selected(m_ID):
                if Comp_ID[0] == eachPoly:
                    SelSets.append(eachSS)
                    break

        Poly_DeSelect_All()
        for ss in SelSets:
            SelectionSet_Select(ss)

    if mComp == 'edge':
        EdgeSS = Edge_SelectionSetNames_Get(m_ID)
        Edge_Select_UnderMouse()
        if Edge_Count_Selected(m_ID) < 1:
            Modo_UserMessage_Info('Edge Detection', 'Unable to detect an edge under the mouse!!')
            sys.exit()

        Comp_ID = Edge_Index_Selected(m_ID)

        SelSets = []

        for eachSS in EdgeSS:
            Edge_DeSelect_All()
            SelectionSet_Select(eachSS)

            for eachEdge in Edge_Index_Selected(m_ID):
                if Comp_ID[0] == eachEdge:
                    SelSets.append(eachSS)
                    break

        Edge_DeSelect_All()
        for ss in SelSets:
            SelectionSet_Select(ss)

    if mComp == 'vertex':
        VertSS = Vert_SelectionSetNames_Get(m_ID)
        Vert_Select_UnderMouse()
        if Vert_Count_Selected(m_ID) < 1:
            Modo_UserMessage_Info('Vertex Detection', 'Unable to detect a vertex under the mouse!!')
            sys.exit()

        Comp_ID = Vert_Index_Selected(m_ID)

        SelSets = []

        for eachSS in VertSS:
            Vert_DeSelect_All()
            SelectionSet_Select(eachSS)
            for eachVert in Vert_Index_Selected(m_ID):
                if Comp_ID[0] == eachVert:
                    SelSets.append(eachSS)
                    break

        Vert_DeSelect_All()
        for ss in SelSets:
            SelectionSet_Select(ss)


####################################################
####################################################

def Vert_SelectionSetNames_Get(Requires_ItemID):
    return __pyModo_SelectionSetInfo(Requires_ItemID, 'V', 'NAME')


def Edge_SelectionSetNames_Get(Requires_ItemID):
    return __pyModo_SelectionSetInfo(Requires_ItemID, 'E', 'NAME')


def Poly_SelectionSetNames_Get(Requires_ItemID):
    return __pyModo_SelectionSetInfo(Requires_ItemID, 'P', 'NAME')


def Vert_SelectionSets_Count_All(Requires_ItemID):
    return __pyModo_SelectionSetInfo(Requires_ItemID, 'V', 'COUNT')


def Edge_SelectionSets_Count_All(Requires_ItemID):
    return __pyModo_SelectionSetInfo(Requires_ItemID, 'E', 'COUNT')


def Poly_SelectionSets_Count_All(Requires_ItemID):
    return __pyModo_SelectionSetInfo(Requires_ItemID, 'P', 'COUNT')


def __pyModo_SelectionSetInfo(Requires_ItemID, V_E_P, SS_INFO):
    SelSetCount = 0
    SelSetNameList = []

    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:

        Item_Select(EachItem)

        if V_E_P == 'V':
            Vert_Mode_Set()
            EachSSCnt = lx.eval('query layerservice vrtset.N ?')
            SelSetCount += EachSSCnt
            for EachSSName in range(0, EachSSCnt):
                SS_Name = lx.eval('query layerservice vrtset.name ? {%s}' % EachSSName)
                SelSetNameList.append(SS_Name)

        if V_E_P == 'E':
            ESS_Name = __pyModo_VMAPS(EachItem, 'name', 'edgepick')
            Edge_Mode_Set()
            for EachESS in ESS_Name:
                SelectionSet_Select(EachESS)
                ECnt = Edge_Count_Selected(EachItem)
                if ECnt > 0:
                    SelSetCount += 1
                    SelSetNameList.append(EachESS)
                    Edge_DeSelect_All()

        if V_E_P == 'P':
            Poly_Mode_Set()
            EachSSCnt = lx.eval('query layerservice polset.N ?')
            SelSetCount += EachSSCnt
            for EachSSName in range(0, EachSSCnt):
                SS_Name = lx.eval('query layerservice polset.name ? {%s}' % EachSSName)
                SelSetNameList.append(SS_Name)

    if SS_INFO == 'NAME': return SelSetNameList
    if SS_INFO == 'COUNT': return SelSetCount


####################################################
####################################################

def Poly_Invert_Selection():
    Convert_To_Polygons()
    lx.eval('select.invert')


def Edge_Invert_Selection():
    Convert_To_Edges()
    lx.eval('select.invert')


def Vert_Invert_Selection():
    Convert_To_Verts()
    lx.eval('select.invert')


def Poly_Select_Connected():
    Convert_To_Polygons()
    lx.eval('select.connect')


def Edge_Select_Connected():
    Convert_To_Edges()
    lx.eval('select.connect')


def Vert_Select_Connected():
    Convert_To_Verts()
    lx.eval('select.connect ')


def Vert_Hide_AdjacentPoly():
    Convert_To_Verts()
    lx.eval('hide.sel')


def Edge_Hide_AdjacentPoly():
    Convert_To_Edges()
    lx.eval('hide.sel')


def Poly_Hide():
    Convert_To_Polygons()
    lx.eval('hide.sel')


def Poly_UnHide():
    Convert_To_Polygons()
    lx.eval('unhide')


def Vert_Select_Expand(): lx.eval('select.expand')


def Vert_Select_Contract(): lx.eval('select.contract')


def Edge_Select_Expand(): lx.eval('select.expand')


def Edge_Select_Contract(): lx.eval('select.contract')


def Poly_Select_Expand(): lx.eval('select.expand')


def Poly_Select_Contract(): lx.eval('select.contract')


def Poly_Triple_Set(): lx.eval('poly.triple')


def Poly_VertList_Get(Requires_PolyIndex): return lx.eval('query layerservice poly.vertList ? %s' % Requires_PolyIndex)


def Deform_Add_Deform_Folder():
    lx.eval('deformer.create deformFolder')


def Deform_Add_Normalizing_Folder():
    lx.eval('deformer.create deformGroup')


def Deform_Add_Spline_Deformer(Requires_MeshID):
    Item_Select(Requires_MeshID)
    lx.eval('item.addDeformer deform.spline')


def Deform_Add_Slack_Deformer(Requires_MeshID):
    Item_Select(Requires_MeshID)
    lx.eval('item.addDeformer deform.slack')


def Deform_Add_Rotation_Deformer():
    lx.eval('item.addDeformer rotation')


def Deform_Add_Locator_Deformer():
    lx.eval('item.addDeformer locator')


####################################################
####################################################

def Poly_Hidden_Count(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        PolyHiddenCnt = Poly_Count_All(EachItem)
        PolyIndx = Poly_Index_All(EachItem)
        for EachIndx in PolyIndx:
            if not lx.eval('query layerservice poly.hidden ? {%s}' % EachIndx):
                PolyHiddenCnt -= 1

    return PolyHiddenCnt


def Poly_UnHidden_Index_All(Requires_ItemID):
    Poly_UnHidden_List = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        PolyIndx = Poly_Index_All(EachItem)
        for EachIndx in PolyIndx:
            if not lx.eval('query layerservice poly.hidden ? {%s}' % EachIndx):
                Poly_UnHidden_List.append(EachIndx)
    return Poly_UnHidden_List


def Poly_Hidden_Index_All(Requires_ItemID):
    Poly_Hidden_List = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        PolyIndx = Poly_Index_All(EachItem)
        for EachIndx in PolyIndx:
            if lx.eval('query layerservice poly.hidden ? {%s}' % EachIndx):
                Poly_Hidden_List.append(EachIndx)

    return Poly_Hidden_List


####################################################
####################################################

def Poly_Islands_To_SelectionSets(Requires_ItemID):
    __pyModo_Poly_Islands(Requires_ItemID)


def Poly_Islands_SymmetryX_To_SelectionSets(Requires_ItemID):
    __pyModo_Poly_Islands(Requires_ItemID, 'x')


def Poly_Islands_SymmetryY_To_SelectionSets(Requires_ItemID):
    __pyModo_Poly_Islands(Requires_ItemID, 'y')


def Poly_Islands_SymmetryZ_To_SelectionSets(Requires_ItemID):
    __pyModo_Poly_Islands(Requires_ItemID, 'z')


def __pyModo_Poly_Islands(Requires_ItemID, *SymInfo):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    SelSetName = 'pyModoSS_PI_SS'
    SelectionSet_AddTo(SelSetName)

    for EachItem in TheList:

        xCntSelSet = 0

        SSet = Item_Name_Get(EachItem)
        strSS = SSet + str('%04d' % xCntSelSet)
        Item_Select(EachItem)
        Poly_Mode_Set()
        SelectionSet_Select(SelSetName)
        PolyCnt = Poly_Count_All(EachItem)

        if xCntSelSet == 0:
            strSS_First = strSS
            Poly_Invert_Selection()
            SelectionSet_AddTo(strSS_First)
            Poly_Hide()

        Poly_HdnCnt = Poly_Hidden_Count(EachItem)

        while PolyCnt > Poly_HdnCnt:

            xCntSelSet += 1
            strSS = SSet + str('%04d' % xCntSelSet)
            Poly_UnHdn = Poly_UnHidden_Index_All(EachItem)
            Poly_DeSelect_All()
            Poly_Select(Poly_UnHdn[0])

            while True:
                PolySelCnt = Poly_Count_Selected(EachItem)
                Poly_Select_Expand()
                PolySelCntAgain = Poly_Count_Selected(EachItem)
                if PolySelCnt == PolySelCntAgain:

                    if SymInfo:
                        if SymInfo[0] == 'x': Poly_SymX_ReSelect(EachItem)
                        if SymInfo[0] == 'y': Poly_SymY_ReSelect(EachItem)
                        if SymInfo[0] == 'z': Poly_SymZ_ReSelect(EachItem)

                    NextCntrName = Poly_SelectionSetNames_Get(EachItem)

                    while True:
                        strSS = SSet + str('%04d' % xCntSelSet)
                        if strSS in NextCntrName:
                            xCntSelSet += 1
                        if strSS not in NextCntrName:
                            break

                    SelectionSet_AddTo(strSS)
                    Poly_Hide()
                    Poly_HdnCnt = Poly_Hidden_Count(EachItem)

                    break

        Poly_UnHide()
        Poly_Mode_Set()
        SelectionSet_Delete(strSS_First)
        SelectionSet_Delete(SelSetName)


####################################################
####################################################

def Component_Flatten_On_Y():
    #Verts Edges Polygon flattening
    lx.eval('tool.set TransformScale on')
    lx.eval('tool.setAttr xfrm.transform SX 1.0')
    lx.eval('tool.setAttr xfrm.transform SY 0.0')
    lx.eval('tool.setAttr xfrm.transform SZ 1.0')
    lx.eval('tool.apply')
    lx.eval('tool.set TransformScale off')


def Component_Flatten_On_X():
    #Verts Edges Polygon flattening
    lx.eval('tool.set TransformScale on')
    lx.eval('tool.setAttr xfrm.transform SX 0.0')
    lx.eval('tool.setAttr xfrm.transform SY 1.0')
    lx.eval('tool.setAttr xfrm.transform SZ 1.0')
    lx.eval('tool.apply')
    lx.eval('tool.set TransformScale off')


def Component_Flatten_On_Z():
    #Verts Edges Polygon flattening
    lx.eval('tool.set TransformScale on')
    lx.eval('tool.setAttr xfrm.transform SX 1.0')
    lx.eval('tool.setAttr xfrm.transform SY 1.0')
    lx.eval('tool.setAttr xfrm.transform SZ 0.0')
    lx.eval('tool.apply')
    lx.eval('tool.set TransformScale off')


####################################################
####################################################

def Vert_SymX_ReSelect(Requires_ItemID):
    __pyModo_SymReSelect(Requires_ItemID, 'V', 'X')


def Vert_SymY_ReSelect(Requires_ItemID):
    __pyModo_SymReSelect(Requires_ItemID, 'V', 'Y')


def Vert_SymZ_ReSelect(Requires_ItemID):
    __pyModo_SymReSelect(Requires_ItemID, 'V', 'Z')


def Edge_SymX_ReSelect(Requires_ItemID):
    __pyModo_SymReSelect(Requires_ItemID, 'E', 'X')


def Edge_SymY_ReSelect(Requires_ItemID):
    __pyModo_SymReSelect(Requires_ItemID, 'E', 'Y')


def Edge_SymZ_ReSelect(Requires_ItemID):
    __pyModo_SymReSelect(Requires_ItemID, 'E', 'Z')


def Poly_SymX_ReSelect(Requires_ItemID):
    __pyModo_SymReSelect(Requires_ItemID, 'P', 'X')


def Poly_SymY_ReSelect(Requires_ItemID):
    __pyModo_SymReSelect(Requires_ItemID, 'P', 'Y')


def Poly_SymZ_ReSelect(Requires_ItemID):
    __pyModo_SymReSelect(Requires_ItemID, 'P', 'Z')


def __pyModo_SymReSelect(Requires_ItemID, V_E_P, X_Y_Z):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:

        if V_E_P == 'V':
            Vert_Mode_Set()
            CompCnt = Vert_Count_Selected(EachItem)
            if CompCnt < 1: continue

            VertSel = Vert_Index_Selected(EachItem)

            for eachVS in VertSel:

                if X_Y_Z == 'X':
                    SymV = Vert_Get_SymX_Equivalenet(eachVS)
                    if SymV: Vert_Select(SymV)
                if X_Y_Z == 'Y':
                    SymV = Vert_Get_SymY_Equivalenet(eachVS)
                    if SymV: Vert_Select(SymV)
                if X_Y_Z == 'Z':
                    SymV = Vert_Get_SymZ_Equivalenet(eachVS)
                    if SymV: Vert_Select(SymV)

        if V_E_P == 'E':
            Edge_Mode_Set()
            CompCnt = Edge_Count_Selected(EachItem)
            if CompCnt < 1: continue

            EdgeSel = Edge_Index_Selected(EachItem)

            for eachES in EdgeSel:

                if X_Y_Z == 'X':
                    SymE = Edge_Get_SymX_Equivalenet(eachES)
                    if SymE: Edge_Select(SymE)
                if X_Y_Z == 'Y':
                    SymE = Edge_Get_SymY_Equivalenet(eachES)
                    if SymE: Edge_Select(SymE)
                if X_Y_Z == 'Z':
                    SymE = Edge_Get_SymZ_Equivalenet(eachES)
                    if SymE: Edge_Select(SymE)

        if V_E_P == 'P':
            Poly_Mode_Set()
            CompCnt = Poly_Count_Selected(EachItem)
            if CompCnt < 1: continue

            PolySel = Poly_Index_Selected(EachItem)

            for eachPS in PolySel:

                if X_Y_Z == 'X':
                    SymP = Poly_Get_SymX_Equivalenet(eachPS)
                    if SymP: Poly_Select(SymP)
                if X_Y_Z == 'Y':
                    SymP = Poly_Get_SymY_Equivalenet(eachPS)
                    if SymP: Poly_Select(SymP)
                if X_Y_Z == 'Z':
                    SymP = Poly_Get_SymZ_Equivalenet(eachPS)
                    if SymP: Poly_Select(SymP)


def Vert_WorldPosX_Get(Requires_VertIndex):
    return lx.eval('query layerservice vert.wpos ? {%s}' % Requires_VertIndex)[0]


def Vert_WorldPosY_Get(Requires_VertIndex):
    return lx.eval('query layerservice vert.wpos ? {%s}' % Requires_VertIndex)[1]


def Vert_WorldPosZ_Get(Requires_VertIndex):
    return lx.eval('query layerservice vert.wpos ? {%s}' % Requires_VertIndex)[2]


def Vert_Get_SymX_Equivalenet(Requires_VertIndex):
    return __pyModo_Get_SymEqual(Requires_VertIndex, 'V', 'X')


def Vert_Get_SymY_Equivalenet(Requires_VertIndex):
    return __pyModo_Get_SymEqual(Requires_VertIndex, 'V', 'Y')


def Vert_Get_SymZ_Equivalenet(Requires_VertIndex):
    return __pyModo_Get_SymEqual(Requires_VertIndex, 'V', 'Z')


def Edge_Get_SymX_Equivalenet(Requires_EdgeIndex):
    return __pyModo_Get_SymEqual(Requires_EdgeIndex, 'E', 'X')


def Edge_Get_SymY_Equivalenet(Requires_EdgeIndex):
    return __pyModo_Get_SymEqual(Requires_EdgeIndex, 'E', 'Y')


def Edge_Get_SymZ_Equivalenet(Requires_EdgeIndex):
    return __pyModo_Get_SymEqual(Requires_EdgeIndex, 'E', 'Z')


def Poly_Get_SymX_Equivalenet(Requires_PolyIndex):
    return __pyModo_Get_SymEqual(Requires_PolyIndex, 'P', 'X')


def Poly_Get_SymY_Equivalenet(Requires_PolyIndex):
    return __pyModo_Get_SymEqual(Requires_PolyIndex, 'P', 'Y')


def Poly_Get_SymZ_Equivalenet(Requires_PolyIndex):
    return __pyModo_Get_SymEqual(Requires_PolyIndex, 'P', 'Z')


def __pyModo_Get_SymEqual(Requires_CompIndex, CompSel, SymAxis):
    if SymAxis == 'X':
        Symmetry_X_On()
    if SymAxis == 'Y':
        Symmetry_Y_On()
    if SymAxis == 'Z':
        Symmetry_Z_On()

    if CompSel == 'V':
        CompIndx = lx.eval('query layerservice vert.symmetric ? {%s}' % Requires_CompIndex)

    if CompSel == 'E':
        CompIndx = lx.eval('query layerservice edge.symmetric ? {%s}' % Requires_CompIndex)

    if CompSel == 'P':
        CompIndx = lx.eval('query layerservice poly.symmetric ? {%s}' % Requires_CompIndex)

    Symmetry_Off()

    return CompIndx


####################################################
####################################################

def VMAP_Names_Weight_Get(Requires_ItemID):
    return __pyModo_VMAP_Names(Requires_ItemID, 'weight')


def VMAP_Names_Texture_Get(Requires_ItemID):
    return __pyModo_VMAP_Names(Requires_ItemID, 'texture')


def VMAP_Names_Morph_Get(Requires_ItemID):
    return __pyModo_VMAP_Names(Requires_ItemID, 'morph')


def VMAP_Names_SubWeight_Get(Requires_ItemID):
    return __pyModo_VMAP_Names(Requires_ItemID, 'subweight')


def VMAP_Names_Normal_Get(Requires_ItemID):
    return __pyModo_VMAP_Names(Requires_ItemID, 'normal')


def VMAP_Names_RGB_Get(Requires_ItemID):
    return __pyModo_VMAP_Names(Requires_ItemID, 'rgb')


def VMAP_Names_RGBA_Get(Requires_ItemID):
    return __pyModo_VMAP_Names(Requires_ItemID, 'rgba')


def __pyModo_VMAPS(Requires_ItemID, strVMapQuery, *VMAP):
    VMap_List = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:

        Item_Select(EachItem)

        All_Vmaps = lx.evalN('query layerservice vmaps ? all')

        for eachVM in All_Vmaps:
            VmapType = lx.eval('query layerservice vmap.type ? {%s}' % eachVM)

            if VMAP:
                if VmapType == VMAP[0]:
                    VmapName = lx.eval('query layerservice vmap.name ? {%s}' % eachVM)
                    VmapIndex = lx.eval('query layerservice vmap.index ?')

                    if strVMapQuery == 'type':
                        if VmapType not in VMap_List:
                            VMap_List.append(VmapType)
                    if strVMapQuery == 'name':
                        if VmapName not in VMap_List:
                            VMap_List.append(VmapName)
                    if strVMapQuery == 'index':
                        if VmapIndex not in VMap_List:
                            VMap_List.append(VmapIndex)

            else:
                if strVMapQuery == 'type':
                    if VmapType not in VMap_List:
                        VMap_List.append(VmapType)
                if strVMapQuery == 'name':
                    if VmapName not in VMap_List:
                        VMap_List.append(VmapName)
                if strVMapQuery == 'index':
                    if VmapIndex not in VMap_List:
                        VMap_List.append(VmapIndex)

    return VMap_List


def __pyModo_VMAP_Names(Requires_ItemID, *vmapType):
    VMAP_Name_List = []

    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    VMAP_Name_PreSelect = __pyModo_VMAPS(TheList, 'name', vmapType)

    for EachItem in TheList:

        Item_Select(EachItem)

        for EachVmap in VMAP_Name_PreSelect:
            if EachVmap != None:
                Vert_Mode_Set()
                Vert_DeSelect_All()
                VMAP_Vert_Selection(EachVmap)
                VertSelCnt = Vert_Count_Selected(EachItem)
                if VertSelCnt > 0:
                    VMAP_Name_List.append(EachVmap)

    return VMAP_Name_List


def __pyModo_VMAP_ReMAP(Requires_VMAP_Type):
    if Requires_VMAP_Type == 'weight':
        RemapVmap = 'wght'
    elif Requires_VMAP_Type == 'texture':
        RemapVmap = 'txuv'
    elif Requires_VMAP_Type == 'subweight':
        RemapVmap = 'subd'
    elif Requires_VMAP_Type == 'morph':
        RemapVmap = 'morf'
    elif Requires_VMAP_Type == 'absMorph':
        RemapVmap = 'spot'
    elif Requires_VMAP_Type == 'rgb':
        RemapVmap = 'rgb'
    elif Requires_VMAP_Type == 'rgba':
        RemapVmap = 'rgba'
    elif Requires_VMAP_Type == 'normal':
        RemapVmap = 'norm'
    else:
        RemapVmap = 'unknown'

    # spot
    # pick
    # epck
    # psiz
    # pdis
    # xfrm
    # vect

    return RemapVmap


def VMAP_Vert_Selection(Requires_VmapName):
    if type(Requires_VmapName) is list:
        TheList = Requires_VmapName
    else:
        TheList = str.split(Requires_VmapName, ',')

    for EachItem in TheList:
        lx.eval('select.vertex add 3 0 {%s}' % EachItem)


def VMAP_Morph_Set(Requires_MorphVmapName, MorphValue):
    lx.eval('!vertMap.applyMorph {%s} {%s}' % (Requires_MorphVmapName, MorphValue))


def VMAP_Add_New_MorphMap(Requires_ItemID, strVmapName):
    if not __fn_pyModo_Check_if_String(strVmapName): strVmapName = str(strVmapName)
    __pyModo_VMAP_Add_New(Requires_ItemID, strVmapName, 'morph')


def VMAP_Add_New_WeightMap(Requires_ItemID, strVmapName):
    if not __fn_pyModo_Check_if_String(strVmapName): strVmapName = str(strVmapName)
    __pyModo_VMAP_Add_New(Requires_ItemID, strVmapName, 'weight')


def VMAP_Add_New_TextureMap(Requires_ItemID, strVmapName):
    if not __fn_pyModo_Check_if_String(strVmapName): strVmapName = str(strVmapName)
    __pyModo_VMAP_Add_New(Requires_ItemID, strVmapName, 'texture')


def VMAP_Add_New_SubWeightMap(Requires_ItemID, strVmapName):
    if not __fn_pyModo_Check_if_String(strVmapName): strVmapName = str(strVmapName)
    __pyModo_VMAP_Add_New(Requires_ItemID, strVmapName, 'subweight')


def VMAP_Add_New_RgbMap(Requires_ItemID, strVmapName):
    if not __fn_pyModo_Check_if_String(strVmapName): strVmapName = str(strVmapName)
    __pyModo_VMAP_Add_New(Requires_ItemID, strVmapName, 'rgb')


def VMAP_Add_New_RgbaMap(Requires_ItemID, strVmapName):
    if not __fn_pyModo_Check_if_String(strVmapName): strVmapName = str(strVmapName)
    __pyModo_VMAP_Add_New(Requires_ItemID, strVmapName, 'rgba')


def VMAP_Add_New_NormalMap(Requires_ItemID, strVmapName):
    if not __fn_pyModo_Check_if_String(strVmapName): strVmapName = str(strVmapName)
    __pyModo_VMAP_Add_New(Requires_ItemID, strVmapName, 'normal')


def VMAP_Add_New_AbsoluteMorphMap(Requires_ItemID, strVmapName):
    if not __fn_pyModo_Check_if_String(strVmapName): strVmapName = str(strVmapName)
    __pyModo_VMAP_Add_New(Requires_ItemID, strVmapName, 'absMorph')


def __pyModo_VMAP_Add_New(Requires_ItemID, strVmapName, vmapType):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    ModoInternalVmapName = __pyModo_VMAP_ReMAP(vmapType)

    for EachItem in TheList:
        Item_Select(EachItem)
        lx.eval('vertMap.new {%s} {%s}' % (strVmapName, ModoInternalVmapName))


####################################################
####################################################

def Animate_Frames_Total_Get():
    TimeRange = lx.eval('time.range scene out:?')
    FramesPerSecond = lx.eval('time.fpsCustom ?')
    TotalFrames = TimeRange * FramesPerSecond
    return TotalFrames


def Animate_Frames_Range_Set_Scene(EnterStartFrame, EnterEndFrame):
    FramesPerSecond = lx.eval('time.fpsCustom ?')
    StartTimeRange = EnterStartFrame / FramesPerSecond
    EndTimeRange = EnterEndFrame / FramesPerSecond
    lx.eval('time.range scene in:{%s} out:{%s}' % (StartTimeRange, EndTimeRange))


def Animate_Frames_Range_Set_Current(EnterStartFrame, EnterEndFrame):
    FramesPerSecond = lx.eval('time.fpsCustom ?')
    StartTimeRange = EnterStartFrame / FramesPerSecond
    EndTimeRange = EnterEndFrame / FramesPerSecond
    lx.eval('time.range current in:{%s} out:{%s}' % (StartTimeRange, EndTimeRange))


def Animate_TimeAtFrame_Calc(EnterFrame):
    FramesPerSecond = lx.eval('time.fpsCustom ?')
    Time = EnterFrame / FramesPerSecond
    return Time


def Animate_FrameAtKey_Calc(EnterKeyTime):
    FramesPerSecond = lx.eval('time.fpsCustom ?')
    Frame = FramesPerSecond * EnterKeyTime
    return Frame


def Animate_Goto_Next_Frame():
    lx.eval('time.step frame next')


def Animate_Goto_Prev_Frame():
    lx.eval('time.step frame prev')


def Animate_Goto_First_Frame():
    lx.eval('time.step frame first')


def Animate_Goto_Last_Frame():
    lx.eval('time.step frame last')


def Animate_Play():
    lx.eval('anim.play start forward')


def Animate_Stop():
    lx.eval('anim.play stop forward')


def Animate_Goto_FrameNumber(EnterFrameNumber):
    frame = Animate_TimeAtFrame_Calc(EnterFrameNumber)
    lx.eval('select.time %s 0 ' % frame)


####################################################
####################################################

def Key_Count_All(Requires_OneItemID, Requires_OneChannelName):
    return __pyModo_Keys(Requires_OneItemID, Requires_OneChannelName, 'count')


def Key_Time_Get(Requires_OneItemID, Requires_OneChannelName):
    return __pyModo_Keys(Requires_OneItemID, Requires_OneChannelName, 'time')


def Key_Value_Get(Requires_OneItemID, Requires_OneChannelName):
    return __pyModo_Keys(Requires_OneItemID, Requires_OneChannelName, 'value')


def Key_DataType_Get(Requires_OneItemID, Requires_OneChannelName):
    return __pyModo_Keys(Requires_OneItemID, Requires_OneChannelName, 'type')


def Key_Index_Get(Requires_OneItemID, Requires_OneChannelName):
    return __pyModo_Keys(Requires_OneItemID, Requires_OneChannelName, 'index')


def __pyModo_Keys(Requires_OneItemID, Requires_OneChannelName, KeyQuery):
    if not __fn_pyModo_Check_if_String(Requires_OneItemID):
        Requires_OneItemID = str(Requires_OneItemID[0])
    if not __fn_pyModo_Check_if_String(Requires_OneChannelName):
        Requires_OneChannelName = str(Requires_OneChannelName[0])

    lx.eval('query sceneservice item.name ? {%s}' % Requires_OneItemID)
    ChannelIndex = lx.eval('query sceneservice channel.index ? {%s}' % Requires_OneChannelName)
    ChannelSubType = lx.eval('query sceneservice channel.subType ? {%s}' % Requires_OneChannelName)
    lx.eval('query sceneservice channel.name ? {%s}' % ChannelIndex)

    KeyResult_List = []

    TotalKeys = lx.eval('query sceneservice key.N ? ')

    if KeyQuery == 'count':
        return TotalKeys

    else:

        for eachKey in range(0, TotalKeys):
            keyVal = lx.eval('query sceneservice key.%s ? {%s}' % (KeyQuery, eachKey))

            if ChannelSubType == 'angle' and KeyQuery == 'value':
                keyVal = math.degrees(float(keyVal))

            KeyResult_List.append(keyVal)

        return KeyResult_List


def Key_Create(Requires_OneItemID, Requires_OneChannelName, EnterKeyTime, EnterKeyValue):
    if not __fn_pyModo_Check_if_String(Requires_OneItemID):
        Requires_OneItemID = str(Requires_OneItemID[0])
    if not __fn_pyModo_Check_if_String(Requires_OneChannelName):
        Requires_OneChannelName = str(Requires_OneChannelName[0])
    lx.eval('channel.key time:{%s} value:{%s} mode:add insert:false channel:{%s:%s}' % (EnterKeyTime, EnterKeyValue, Requires_OneItemID, Requires_OneChannelName))


def Key_Select(Requires_OneItemID, Requires_OneChannelName, EnterKeyTime):
    if not __fn_pyModo_Check_if_String(Requires_OneItemID):
        Requires_OneItemID = str(Requires_OneItemID[0])
    if not __fn_pyModo_Check_if_String(Requires_OneChannelName):
        Requires_OneChannelName = str(Requires_OneChannelName[0])
    ChannelIndex = lx.eval('query sceneservice channel.index ? {%s}' % Requires_OneChannelName)
    lx.eval('select.key item:{%s} channel:{%s} time:{%s} mode:set' % (Requires_OneItemID, ChannelIndex, EnterKeyTime))


def Key_Value_Set_ToKeysSelected(EnterKeyValue):
    lx.eval('key.value {%s} set ' % EnterKeyValue)


def Key_Copy_FromKeysSelected():
    lx.eval('key.copy')


def Key_Paste_ToKeysSelected():
    lx.eval('key.paste')


def Key_Delete_KeysSelected():
    lx.eval('key.delete')


def Key_Delete_All_Item_Transform_Keys(Requires_ItemID):
    Transform_ID = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        Totkeys = 0

        Pos_ID = Item_Position_ID_Get(EachItem)
        for p in Pos_ID:
            Transform_ID.append(p)

        Rot_ID = Item_Rotation_ID_Get(EachItem)
        for r in Rot_ID:
            Transform_ID.append(r)

        Scl_ID = Item_Scale_ID_Get(EachItem)
        for s in Scl_ID:
            Transform_ID.append(s)

        for eachTransID in Transform_ID:

            if eachTransID != None:

                Ch_Names = Item_Channel_Get_Names(eachTransID)

                for eachCh in Ch_Names:

                    if eachCh == 'rot.X':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'rot.Y':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'rot.Z':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'pos.X':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'pos.Y':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'pos.Z':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'scl.X':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'scl.Y':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'scl.Z':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if Totkeys > 0:
                        kTime = Key_Time_Get(eachTransID, eachCh)
                        for eachKey in kTime:
                            Key_Select(eachTransID, eachCh, eachKey)
                            Key_Delete_KeysSelected()


def Key_Navigate_Time_Select(EnterTime):
    lx.eval('select.time {%s}' % EnterTime)


def Key_Navigate_Next():
    lx.eval('time.step key next')


def Key_Navigate_Previous():
    lx.eval('time.step key prev')


def Key_Navigate_First():
    lx.eval('time.step key first')


def Key_Navigate_Last():
    lx.eval('time.step key last')


def Key_Frames_Get(Requires_OneItemID):
    FrameList = []
    Transform_ID = []

    if type(Requires_OneItemID) is list:
        TheList = Requires_OneItemID
    else:
        TheList = str.split(Requires_OneItemID, ',')

    for EachItem in TheList:
        Totkeys = 0

        Pos_ID = Item_Position_ID_Get(EachItem)
        for p in Pos_ID:
            Transform_ID.append(p)

        Rot_ID = Item_Rotation_ID_Get(EachItem)
        for r in Rot_ID:
            Transform_ID.append(r)

        Scl_ID = Item_Scale_ID_Get(EachItem)
        for s in Scl_ID:
            Transform_ID.append(s)

        for eachTransID in Transform_ID:

            if eachTransID != None:

                Ch_Names = Item_Channel_Get_Names(eachTransID)

                for eachCh in Ch_Names:

                    if eachCh == 'rot.X':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'rot.Y':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'rot.Z':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'pos.X':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'pos.Y':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'pos.Z':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'scl.X':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'scl.Y':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if eachCh == 'scl.Z':
                        Totkeys = Key_Count_All(eachTransID, eachCh)

                    if Totkeys > 0:

                        kTime = Key_Time_Get(eachTransID, eachCh)
                        for eachKey in kTime:
                            f = Animate_FrameAtKey_Calc(eachKey)
                            if f not in FrameList:
                                FrameList.append(f)

        return FrameList


def Key_Type_Linear_FromSelected():
    lx.eval('key.type linear')


def Key_Type_Auto_FromSelected():
    lx.eval('key.type auto')


def Key_Type_Manual_FromSelected():
    lx.eval('key.type manual')


def Key_Type_AutoFlat_FromSelected():
    lx.eval('key.type autoFlat')


def Key_Type_Flat_FromSelected():
    lx.eval('key.type flat')


def Key_Type_Stepped_FromSelected():
    lx.eval('key.type stepped')


def Key_DeleteAll_inChannel(Requires_ItemID, Requires_ChannelName):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        Totkeys = Key_Count_All(EachItem, Requires_ChannelName)

        if Totkeys > 0:
            kTime = Key_Time_Get(EachItem, Requires_ChannelName)

            for eachKey in kTime:
                Key_Select(EachItem, Requires_ChannelName, eachKey)
                try:
                    Key_Delete_KeysSelected()
                except:
                    pass


####################################################
####################################################

def Morph_Set(Requires_OneItemID, MrphName):
    Item_Select(Requires_OneItemID)
    lx.eval('morphDeform.mapName %s' % MrphName)


def Morph_Get(Requires_OneItemID):
    Item_Select(Requires_OneItemID)
    return lx.eval('morphDeform.mapName ?')


####################################################
####################################################

def OnFrame_Key_Morph(Frame, Requires_ItemID, MorphMapName, MorphStrength):
    kTime = Animate_TimeAtFrame_Calc(Frame)
    Morph_Set(Requires_ItemID, MorphMapName)
    Key_Create(Requires_ItemID, 'strength', kTime, MorphStrength)


def OnFrame_Key_Rotate(FrameNmbr, Requires_ItemID, xRot, yRot, zRot):
    kTime = Animate_TimeAtFrame_Calc(FrameNmbr)
    Key_Create(Requires_ItemID, 'rot.X', kTime, float(xRot))
    Key_Create(Requires_ItemID, 'rot.Y', kTime, float(yRot))
    Key_Create(Requires_ItemID, 'rot.Z', kTime, float(zRot))


def OnFrame_Key_Scale(FrameNmbr, Requires_ItemID, xScale, yScale, zScale):
    kTime = Animate_TimeAtFrame_Calc(FrameNmbr)
    Key_Create(Requires_ItemID, 'scl.X', kTime, float(xScale))
    Key_Create(Requires_ItemID, 'scl.Y', kTime, float(yScale))
    Key_Create(Requires_ItemID, 'scl.Z', kTime, float(zScale))


def OnFrame_Key_Position(FrameNmbr, Requires_ItemID, xPos, yPos, zPos):
    kTime = Animate_TimeAtFrame_Calc(FrameNmbr)
    Key_Create(Requires_ItemID, 'pos.X', kTime, float(xPos))
    Key_Create(Requires_ItemID, 'pos.Y', kTime, float(yPos))
    Key_Create(Requires_ItemID, 'pos.Z', kTime, float(zPos))


####################################################
####################################################

def VertSel_byEdge_equal0_ADD(): lx.eval('select.vertex add edge equal 0')


def VertSel_byEdge_equal1_ADD(): lx.eval('select.vertex add edge equal 1')


def VertSel_byEdge_equal2_ADD(): lx.eval('select.vertex add edge equal 2')


def VertSel_byEdge_equal3_ADD(): lx.eval('select.vertex add edge equal 3')


def VertSel_byEdge_equal4_ADD(): lx.eval('select.vertex add edge equal 4')


def VertSel_byEdge_more4_ADD(): lx.eval('select.vertex add edge more 4')


def VertSel_byEdge_equal0_REMV(): lx.eval('select.vertex remove edge equal 0')


def VertSel_byEdge_equal1_REMV(): lx.eval('select.vertex remove edge equal 1')


def VertSel_byEdge_equal2_REMV(): lx.eval('select.vertex remove edge equal 2')


def VertSel_byEdge_equal3_REMV(): lx.eval('select.vertex remove edge equal 3')


def VertSel_byEdge_equal4_REMV(): lx.eval('select.vertex remove edge equal 4')


def VertSel_byEdge_more4_REMV(): lx.eval('select.vertex remove edge more 4')


def VertSel_byPoly_equal0_ADD(): lx.eval('select.vertex add poly equal 0')


def VertSel_byPoly_equal1_ADD(): lx.eval('select.vertex add poly equal 1')


def VertSel_byPoly_equal2_ADD(): lx.eval('select.vertex add poly equal 2')


def VertSel_byPoly_equal3_ADD(): lx.eval('select.vertex add poly equal 3')


def VertSel_byPoly_equal4_ADD(): lx.eval('select.vertex add poly equal 4')


def VertSel_byPoly_more4_ADD(): lx.eval('select.vertex add poly more 4')


def VertSel_byPoly_equal0_REMV(): lx.eval('select.vertex remove poly equal 0')


def VertSel_byPoly_equal1_REMV(): lx.eval('select.vertex remove poly equal 1')


def VertSel_byPoly_equal2_REMV(): lx.eval('select.vertex remove poly equal 2')


def VertSel_byPoly_equal3_REMV(): lx.eval('select.vertex remove poly equal 3')


def VertSel_byPoly_equal4_REMV(): lx.eval('select.vertex remove poly equal 4')


def VertSel_byPoly_more4_REMV(): lx.eval('select.vertex remove poly more 4')


def VertSel_byBoundary_Colinear_ADD(): lx.eval('select.vertex add 4 0 (none)')


def VertSel_byBoundary_Colinear_REMV(): lx.eval('select.vertex remove 4 0 (none)')


def VertSel_byVMap_Subdivision_ADD(): lx.eval('select.vertex add 3 0 Subdivision')


def VertSel_byVMap_Subdivision_REMV(): lx.eval('select.vertex remove 3 0 Subdivision')


def VertSel_byVMap_Texture_ADD(RequiresVmapName): lx.eval('select.vertex add 3 0  %s' % RequiresVmapName)


def VertSel_byVMap_Texture_REMV(RequiresVmapName): lx.eval('select.vertex remove 3 0  %s' % RequiresVmapName)


def EdgeSel_byPoly_equal0_ADD(): lx.eval('select.edge add poly equal 1')


def EdgeSel_byPoly_equal1_ADD(): lx.eval('select.edge add poly equal 2')


def EdgeSel_byPoly_equal2_ADD(): lx.eval('select.edge add poly equal 3')


def EdgeSel_byPoly_equal3_ADD(): lx.eval('select.edge add poly equal 4')


def EdgeSel_byPoly_more4_ADD(): lx.eval('select.edge add poly more 4')


def EdgeSel_byPoly_equal0_REMV(): lx.eval('select.edge remove poly equal 1')


def EdgeSel_byPoly_equal1_REMV(): lx.eval('select.edge remove poly equal 2')


def EdgeSel_byPoly_equal2_REMV(): lx.eval('select.edge remove poly equal 3')


def EdgeSel_byPoly_equal3_REMV(): lx.eval('select.edge remove poly equal 4')


def EdgeSel_byPoly_more4_REMV(): lx.eval('select.edge remove poly more 4')


def EdgeSel_byVMap_Subdivision_ADD(): lx.eval('select.edge add 3 0 Subdivision')


def EdgeSel_byVMap_Subdivision_REMV(): lx.eval('select.edge remove 3 0 Subdivision')


def PolySel_byType_Material_ADD(RequiresMaterialName): lx.eval('select.polygon add material face {%s}' % RequiresMaterialName)


def PolySel_byType_Material_REMV(RequiresMaterialName): lx.eval('select.polygon remove material face {%s}' % RequiresMaterialName)


def PolySel_byType_Face_ADD(): lx.eval('select.polygon add type face 0')


def PolySel_byType_Face_REMV(): lx.eval('select.polygon remove type face 0')


def PolySel_byType_SubDiv_ADD(): lx.eval('select.polygon add type subdiv 1')


def PolySel_byType_SubDiv_REMV(): lx.eval('select.polygon remove type subdiv 1')


def PolySel_byType_Psub_ADD(): lx.eval('select.polygon add type psubdiv 2')


def PolySel_byType_Psub_REMV(): lx.eval('select.polygon remove type psubdiv 2')


def PolySel_byType_Curve_ADD(): lx.eval('select.polygon add type curve 3')


def PolySel_byType_Curve_REMV(): lx.eval('select.polygon remove type curve 3')


def PolySel_byType_Bezier_ADD(): lx.eval('select.polygon add type bezier 4')


def PolySel_byType_Bezier_REMV(): lx.eval('select.polygon remove type bezier 4')


def PolySel_byType_SplinePatch_ADD(): lx.eval('select.polygon add type spatch 5')


def PolySel_byType_SplinePatch_REMV(): lx.eval('select.polygon remove type spatch 5')


def PolySel_byType_Text_ADD(): lx.eval('select.polygon add type text 6')


def PolySel_byType_Text_REMV(): lx.eval('select.polygon remove type text 6')


def PolySel_byType_PolyLine_ADD(): lx.eval('select.polygon add type line 7')


def PolySel_byType_PolyLine_REMV(): lx.eval('select.polygon remove type line 7')


def PolySel_byType_NonPlanar_ADD(): lx.eval('select.polygon add type nonplanar 8')


def PolySel_byType_NonPlanar_REMV(): lx.eval('select.polygon remove type nonplanar 8')


def PolySel_byType_CoLocated_ADD(): lx.eval('select.polygon add type colocated 9')


def PolySel_byType_CoLocated_REMV(): lx.eval('select.polygon remove type colocated 9')


def PolySel_byType_CoPlanar_ADD(): lx.eval('select.polygon add type coplanar 10')


def PolySel_byType_CoPlanar_REMV(): lx.eval('select.polygon remove type coplanar 10')


def PolySel_byType_Angle_ADD(): lx.eval('select.polygon add type angle 11')


def PolySel_byType_Angle_REMV(): lx.eval('select.polygon remove type angle 11')


def PolySel_byType_Convex_ADD(): lx.eval('select.polygon add type convex 12')


def PolySel_byType_Convex_REMV(): lx.eval('select.polygon remove type convex 12')


def PolySel_byType_Concave_ADD(): lx.eval('select.polygon add type concave 13')


def PolySel_byType_Concave_REMV(): lx.eval('select.polygon remove type concave 13')


def PolySel_byVertex_PSubDiv1_ADD(): lx.eval('select.polygon add vertex psubdiv 1')


def PolySel_byVertex_PSubDiv2_ADD(): lx.eval('select.polygon add vertex psubdiv 2')


def PolySel_byVertex_PSubDiv3_ADD(): lx.eval('select.polygon add vertex psubdiv 3')


def PolySel_byVertex_PSubDiv4_ADD(): lx.eval('select.polygon add vertex psubdiv 4')


def PolySel_byVertex_PSubDiv_more4_ADD(): lx.eval('select.polygon add vertex bezier 4')


def PolySel_byVertex_PSubDiv1_REMV(): lx.eval('select.polygon remove vertex psubdiv 1')


def PolySel_byVertex_PSubDiv2_REMV(): lx.eval('select.polygon remove vertex psubdiv 2')


def PolySel_byVertex_PSubDiv3_REMV(): lx.eval('select.polygon remove vertex psubdiv 3')


def PolySel_byVertex_PSubDiv4_REMV(): lx.eval('select.polygon remove vertex psubdiv 4')


def PolySel_byVertex_PSubDiv_more4_REMV(): lx.eval('select.polygon remove vertex bezier 4')


####################################################
####################################################

def PolyShapeMaker(PolySize, VertCount, SetSpikey=False):
    lx.eval('item.create pMod.generator')
    PGenName = lx.eval('item.name ?')
    lx.eval('item.channel pMod.generator$type radial')
    lx.eval('item.channel pMod.generator$pidOrder sequential')
    lx.eval('item.channel pMod.generator$count {%s}' % VertCount)
    lx.eval('item.channel pMod.generator$radius {%s}' % PolySize)
    lx.eval('particle.freezeCloud')
    lx.eval('select.item {Point Cloud} set')
    lx.eval('item.name {PolyShapeMaker}')
    lx.eval('select.item {%s} set' % PGenName)
    lx.eval('item.delete')
    lx.eval('select.type vertex')
    lx.eval('select.vertex add 0 all 0')
    lx.eval('poly.make auto')
    if SetSpikey != 0:
        mt.Spikey_pOnOff(1)
        mt.Tool_Apply_Set()
        mt.Spikey_pOnOff(0)
    lx.eval('select.item {PolyShapeMaker} set')


####################################################
####################################################

def CleanStart():
    lx.eval('tool.set Transform 0')
    lx.eval('tool.set TransformScale 0')
    lx.eval('tool.set TransformMove 0')
    lx.eval('tool.set TransformRotate 0')
    lx.eval('select.drop center')
    lx.eval('select.drop pivot')
    lx.eval('select.drop item')
    lx.eval('select.drop polygon')
    lx.eval('select.drop edge')
    lx.eval('select.drop vertex')
    if lx.eval('tool.clearTask ? ') != '':
        strClearTask = lx.eval('tool.clearTask ?')
        lx.eval('tool.clearTask {%s}' % strClearTask)


####################################################
####################################################

def Group_Mask_Item_Set(Requires_ItemID, Requires_Name):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        Item_Select(EachItem)
        lx.eval('mask.setMesh {%s}' % Requires_Name)


def Group_Mask_PolyTagType_Set(Requires_ItemID, Requires_Name):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        Item_Select(EachItem)
        lx.eval('mask.setPTagType {%s}' % Requires_Name)


def Group_Mask_PolyTag_Set(Requires_ItemID, Requires_Name):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        Item_Select(EachItem)
        lx.eval('mask.setPTag {%s}' % Requires_Name)


def Group_Mask_Item_Get(Requires_ItemID):
    ItemVal = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        Item_Select(EachItem)
        ItemVal.append(lx.eval('mask.setMesh ?'))

    return ItemVal


def Group_Mask_PolyTagType_Get(Requires_ItemID):
    pTagTypeVal = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        Item_Select(EachItem)
        pTagTypeVal.append(lx.eval('mask.setPTagType ?'))

    return pTagTypeVal


def Group_Mask_PolyTag_Get(Requires_ItemID):
    pTagVal = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        Item_Select(EachItem)
        pTagVal.append(lx.eval('mask.setPTag ?'))

    return pTagVal


####################################################
####################################################

def Vert_X_Position_Set(xValue):
    lx.eval('vert.set x %s' % xValue)


def Vert_Y_Position_Set(yValue):
    lx.eval('vert.set y %s' % yValue)


def Vert_Z_Position_Set(zValue):
    lx.eval('vert.set z %s' % zValue)


def Vert_Merge():
    lx.eval('!vert.merge auto')


def Convert_To_SubD_Poly():
    lx.eval('poly.convert face subpatch true')


def Convert_To_Raw_Poly():
    lx.eval('poly.convert face subpatch false')


def Edge_Length_Get(Requires_Edge_Index):
    return lx.eval('query layerservice edge.length ? {%s}' % Requires_Edge_Index)


def Replicator_Prototype(RequiresReplicatorID, RequiresProtoTypeID):
    Item_Select(RequiresReplicatorID)
    itemName = Item_Name_Get(RequiresProtoTypeID)
    lx.eval('replicator.source {%s}' % itemName)


def Replicator_PointSource(RequiresReplicatorID, RequiresPointSourceID):
    Item_Select(RequiresReplicatorID)
    itemName = Item_Name_Get(RequiresPointSourceID)
    lx.eval('replicator.particle {%s}' % itemName)


def Poly_Normal_Get(RequiresOnePolyIndex):
    return lx.eval('query layerservice poly.normal ? {%s}' % RequiresOnePolyIndex)


def Poly_Flip():
    lx.eval('poly.flip')


def Item_Display_Draw_Set():
    lx.eval('item.draw add locator')


def Item_Display_Help_Label_Set(RequiresLabelText):
    lx.eval('item.help add label {%s}' % RequiresLabelText)


def Render_Root_Select():
    lx.eval('select.Item polyRender006 set')


####################################################
####################################################

def WorkPlane_FitSelect():
    lx.eval('workPlane.fitSelect')


def WorkPlane_Reset():
    lx.eval('workPlane.Reset')


def WorkPlane_Edit_Rotation_X_Get():
    return lx.eval('workPlane.edit rotX:?')


def WorkPlane_Edit_Rotation_Y_Get():
    return lx.eval('workPlane.edit rotY:?')


def WorkPlane_Edit_Rotation_Z_Get():
    return lx.eval('workPlane.edit rotZ:?')


def WorkPlane_Edit_Center_X_Get():
    return lx.eval('workPlane.edit cenX:?')


def WorkPlane_Edit_Center_Y_Get():
    return lx.eval('workPlane.edit cenY:?')


def WorkPlane_Edit_Center_Z_Get():
    return lx.eval('workPlane.edit cenZ:?')


def WorkPlane_Edit_Rotation_X_Set(EnterValueHere):
    lx.eval('workPlane.edit rotX: %s' % EnterValueHere)


def WorkPlane_Edit_Rotation_Y_Set(EnterValueHere):
    lx.eval('workPlane.edit rotY: %s' % EnterValueHere)


def WorkPlane_Edit_Rotation_Z_Set(EnterValueHere):
    lx.eval('workPlane.edit rotZ: %s' % EnterValueHere)


def WorkPlane_Edit_Center_X_Set(EnterValueHere):
    lx.eval('workPlane.edit cenX: %s' % EnterValueHere)


def WorkPlane_Edit_Center_Y_Set(EnterValueHere):
    lx.eval('workPlane.edit cenY: %s' % EnterValueHere)


def WorkPlane_Edit_Center_Z_Set(EnterValueHere):
    lx.eval('workPlane.edit cenZ: %s' % EnterValueHere)


def WorkPlane_Offset_X_Set(EnterValueHere):
    lx.eval('workPlane.offset 0 %s' % EnterValueHere)


def WorkPlane_Offset_Y_Set(EnterValueHere):
    lx.eval('workPlane.offset 1 %s' % EnterValueHere)


def WorkPlane_Offset_Z_Set(EnterValueHere):
    lx.eval('workPlane.offset 2 %s' % EnterValueHere)


def WorkPlane_Rotation_X_Set(EnterValueHere):
    lx.eval('workPlane.rotate 0 %s' % EnterValueHere)


def WorkPlane_Rotation_Y_Set(EnterValueHere):
    lx.eval('workPlane.rotate 1 %s' % EnterValueHere)


def WorkPlane_Rotation_Z_Set(EnterValueHere):
    lx.eval('workPlane.rotate 2 %s' % EnterValueHere)


def Center_Item_Match_WorkPlane_Rotation():
    lx.eval('center.matchWorkplaneRot')


def Center_Item_Match_WorkPlane_Position():
    lx.eval('center.matchWorkplanePos')


####################################################
####################################################

def ViewPort_View_Left_Set():
    lx.eval('view3d.projection lft')


def ViewPort_View_Right_Set():
    lx.eval('view3d.projection rgt')


def ViewPort_View_Front_Set():
    lx.eval('view3d.projection fnt')


def ViewPort_View_Back_Set():
    lx.eval('view3d.projection bck')


def ViewPort_View_Top_Set():
    lx.eval('view3d.projection top')


def ViewPort_View_Perspective_Set():
    lx.eval('view3d.projection psp')


def ViewPort_View_Camera_Set():
    lx.eval('view3d.projection cam')


def ViewPort_View_RenderCamera_Set():
    lx.eval('view3d.renderCamera')


def ViewPort_View_Camera_Specific_Set(RequiresItemID):
    lx.eval('view3d.cameraItem {%s}' % RequiresItemID)


def ViewPort_View_Light_Set():
    lx.eval('view3d.projection lgt')


def ViewPort_View_Light_Specific_Set(RequiresItemID):
    lx.eval('view3d.lightItem {%s}' % RequiresItemID)


def ViewPort_View_GetView():
    vview = lx.eval('view3d.projection ?')
    if vview == 'fnt':
        return 'front'
    elif vview == 'bck':
        return 'back'
    elif vview == 'lft':
        return 'left'
    elif vview == 'rgt':
        return 'right'
    elif vview == 'top':
        return 'top'
    elif vview == 'bot':
        return 'bottom'
    elif vview == 'psp':
        return 'perspective'
    elif vview == 'cam':
        return 'camera'
    elif vview == 'lgt':
        return 'light'
    else:
        return vview


def ViewPort_FitSelected():
    lx.eval('viewport.fitSelected')


def ViewPort_Fit():
    lx.eval('viewport.fit')


def ViewPort_View_GoTo():
    lx.eval('viewport.goto')


def Item_Poly_Normal_Get(RequiresOnePolyIndex):
    args = lx.args()  # edit

    if len(args) > 0:
        upVector = args[0]  # edit
    else:
        upVector = 'y'  # edit

    polygonNormal = lx.evalN('query layerservice poly.normal ? {%s}' % RequiresOnePolyIndex)

    polyNormRotZ = 0

    polyNormRotX = __fn_GetAngle_byVectors((0, 1, 0), polygonNormal)
    if (polygonNormal[2] < 0):
        polyNormRotX = -polyNormRotX
        polyNormRotY = __fn_GetAngle_byVectors((0, 0, -1), (polygonNormal[0], 0, polygonNormal[2]))
    else:
        polyNormRotY = __fn_GetAngle_byVectors((0, 0, 1), (polygonNormal[0], 0, polygonNormal[2]))
    if (polygonNormal[0] >= 0 and polygonNormal[2] < 0) or (polygonNormal[0] < 0 and polygonNormal[2] >= 0):
        polyNormRotY = -polyNormRotY
    if upVector == 'z':
        polyNormRotX = polyNormRotX - 90
    elif upVector == 'x':
        polyNormRotZ = 90

    return polyNormRotX, polyNormRotY, polyNormRotZ


def __fn_GetAngle_byVectors(vect1, vect2):  # edit
    cos1 = (vect1[0] * vect2[0] + vect1[1] * vect2[1] + vect1[2] * vect2[2])
    cos2 = (math.sqrt(math.pow(vect1[0], 2) + math.pow(vect1[1], 2) + math.pow(vect1[2], 2)) * math.sqrt(math.pow(vect2[0], 2) + math.pow(vect2[1], 2) + math.pow(vect2[2], 2)))
    if cos2 != 0:
        cos = cos1 / cos2
    else:
        cos = cos1
    angle = math.atan2(math.sqrt(abs(1 - (math.pow(cos, 2)))), (cos)) * (180 / math.pi)
    return angle


def Item_Scale_Value_Get(Requires_ItemID, Enter_X_Y_or_Z):
    if not __fn_pyModo_Check_if_String(Enter_X_Y_or_Z): Enter_X_Y_or_Z = str(Enter_X_Y_or_Z)
    AXIS = Enter_X_Y_or_Z.upper()

    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        Item_Select(EachItem)
        if AXIS == 'X':
            return lx.eval('transform.channel scl.X ?')
        if AXIS == 'Y':
            return lx.eval('transform.channel scl.Y ?')
        if AXIS == 'Z':
            return lx.eval('transform.channel scl.Z ?')


def Item_Rotation_Value_Get(Requires_ItemID, Enter_X_Y_or_Z):
    if not __fn_pyModo_Check_if_String(Enter_X_Y_or_Z): Enter_X_Y_or_Z = str(Enter_X_Y_or_Z)
    AXIS = Enter_X_Y_or_Z.upper()

    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        Item_Select(EachItem)
        if AXIS == 'X':
            return lx.eval('transform.channel rot.X ?')
        if AXIS == 'Y':
            return lx.eval('transform.channel rot.Y ?')
        if AXIS == 'Z':
            return lx.eval('transform.channel rot.Z ?')


def Item_Position_Value_Get(Requires_ItemID, Enter_X_Y_or_Z):
    if not __fn_pyModo_Check_if_String(Enter_X_Y_or_Z): Enter_X_Y_or_Z = str(Enter_X_Y_or_Z)
    AXIS = Enter_X_Y_or_Z.upper()

    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        Item_Select(EachItem)
        if AXIS == 'X':
            return lx.eval('transform.channel pos.X ?')
        if AXIS == 'Y':
            return lx.eval('transform.channel pos.Y ?')
        if AXIS == 'Z':
            return lx.eval('transform.channel pos.Z ?')


####################################################
####################################################

def Item_Constrain_Direction(Requires_FromItemID, Requires_ToItemID):
    __pyModo_Item_Constrain(Requires_FromItemID, Requires_ToItemID, 'Direction')


def Item_Constrain_Position(Requires_FromItemID, Requires_ToItemID):
    __pyModo_Item_Constrain(Requires_FromItemID, Requires_ToItemID, 'Position')


def Item_Constrain_Rotation(Requires_FromItemID, Requires_ToItemID, ):
    __pyModo_Item_Constrain(Requires_FromItemID, Requires_ToItemID, 'Rotation')


def Item_Constrain_Scale(Requires_FromItemID, Requires_ToItemID):
    __pyModo_Item_Constrain(Requires_FromItemID, Requires_ToItemID, 'Scale')


def __pyModo_Item_Constrain(Requires_FromItemID, Requires_ToItemID, ConsType):
    lx.eval('select.Item item:{%s} mode: add' % Requires_FromItemID)
    lx.eval('select.subItem item:{%s} mode:add' % Requires_ToItemID)

    if ConsType == 'Direction':
        lx.eval('constraintDirection')

    if ConsType == 'Position':
        lx.eval('constraintTransform type:pos')

    if ConsType == 'Rotation':
        lx.eval('constraintTransform type:rot')

    if ConsType == 'Scale':
        lx.eval('constraintTransform type:scl')


####################################################
####################################################

def Symmetry_X_On():
    lx.eval('select.symmetryState x')


def Symmetry_Y_On():
    lx.eval('select.symmetryState y')


def Symmetry_Z_On():
    lx.eval('select.symmetryState z')


def Symmetry_Off():
    lx.eval('select.symmetryState none')


####################################################
####################################################

def Center_ToBoundingBox_Center(Requires_ItemID):
    __pyModo_ToBoundingBox(Requires_ItemID, 'center', 'center')


def Center_ToBoundingBox_Top(Requires_ItemID):
    __pyModo_ToBoundingBox(Requires_ItemID, 'top', 'center')


def Center_ToBoundingBox_Bottom(Requires_ItemID):
    __pyModo_ToBoundingBox(Requires_ItemID, 'bottom', 'center')


def Center_ToBoundingBox_Front(Requires_ItemID):
    __pyModo_ToBoundingBox(Requires_ItemID, 'front', 'center')


def Center_ToBoundingBox_Back(Requires_ItemID):
    __pyModo_ToBoundingBox(Requires_ItemID, 'back', 'center')


def Center_ToBoundingBox_Left(Requires_ItemID):
    __pyModo_ToBoundingBox(Requires_ItemID, 'left', 'center')


def Center_ToBoundingBox_Right(Requires_ItemID):
    __pyModo_ToBoundingBox(Requires_ItemID, 'right', 'center')


def Pivot_ToBoundingBox_Center(Requires_ItemID):
    __pyModo_ToBoundingBox(Requires_ItemID, 'center', 'pivot')


def Pivot_ToBoundingBox_Top(Requires_ItemID):
    __pyModo_ToBoundingBox(Requires_ItemID, 'top', 'pivot')


def Pivot_ToBoundingBox_Bottom(Requires_ItemID):
    __pyModo_ToBoundingBox(Requires_ItemID, 'bottom', 'pivot')


def Pivot_ToBoundingBox_Front(Requires_ItemID):
    __pyModo_ToBoundingBox(Requires_ItemID, 'front', 'pivot')


def Pivot_ToBoundingBox_Back(Requires_ItemID):
    __pyModo_ToBoundingBox(Requires_ItemID, 'back', 'pivot')


def Pivot_ToBoundingBox_Left(Requires_ItemID):
    __pyModo_ToBoundingBox(Requires_ItemID, 'left', 'pivot')


def Pivot_ToBoundingBox_Right(Requires_ItemID):
    __pyModo_ToBoundingBox(Requires_ItemID, 'right', 'pivot')


def Center_Position_Set(Requires_ItemID, xPos, yPos, zPos):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        Item_Select(EachItem)
        Center_Mode_Set()
        Center_Item_Select(EachItem)
        lx.eval('center.setPosition {%s} {%s} {%s} world ' % (xPos, yPos, zPos))


def Center_Item_Select(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        lx.eval('select.center {%s} set' % EachItem)


def Pivot_Position_Set(Requires_ItemID, xPos, yPos, zPos):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        Item_Select(EachItem)
        Pivot_Mode_Set()
        Pivot_Item_Select(EachItem)
        lx.eval('pivot.setPosition {%s} {%s} {%s} world ' % (xPos, yPos, zPos))


def Pivot_Item_Select(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        lx.eval('select.pivot {%s} set' % EachItem)


def __pyModo_ToBoundingBox(Requires_ItemID, strPos, ItemTo):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    Item_Mode_Set()

    for EachItem in TheList:
        Item_Select(EachItem)
        lx.eval('%s.bbox {%s}' % (ItemTo, strPos))


def Item_Mode_Set(): lx.eval('select.type item')


def Center_Mode_Set(): lx.eval('select.type center')


def Pivot_Mode_Set(): lx.eval('select.type pivot')


def UnParent(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        Item_Select(EachItem)
        lx.eval('item.parent parent:{} inPlace:0')


def Convert_To_Mesh(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        Item_Select(EachItem)
        lx.eval('item.setType mesh locator')


####################################################
####################################################

def Item_Distance_Measure(Requires_OneFromID, Requires_OneToID):
    if type(Requires_OneFromID) is list:
        fromID = Requires_OneFromID[0]
    else:
        fromID = str.split(Requires_OneFromID, ',')[0]

    if type(Requires_OneToID) is list:
        toID = Requires_OneToID[0]
    else:
        toID = str.split(Requires_OneToID, ',')[0]

    FromItem = lx.eval('query sceneservice item.worldPos ? %s' % fromID)
    ToItem = lx.eval('query sceneservice item.worldPos ? %s' % toID)
    ItemDistance = math.sqrt(math.pow(round(FromItem[0], 2) - round(ToItem[0], 2), 2) + math.pow(round(FromItem[1], 2) - round(ToItem[1], 2), 2) + math.pow(round(FromItem[2], 2) - round(ToItem[2], 2), 2))
    return ItemDistance


def Item_Distance_MidPoint_XYZ_Get(Requires_OneFromID, Requires_OneToID):
    ItemMidPointXYZ = []
    if type(Requires_OneFromID) is list:
        fromID = Requires_OneFromID[0]
    else:
        fromID = str.split(Requires_OneFromID, ',')[0]

    if type(Requires_OneToID) is list:
        toID = Requires_OneToID[0]
    else:
        toID = str.split(Requires_OneToID, ',')[0]

    FromItem = lx.eval('query sceneservice item.worldPos ? %s' % fromID)
    ToItem = lx.eval('query sceneservice item.worldPos ? %s' % toID)
    ItemMidPointX = (FromItem[0] + ToItem[0]) / 2
    ItemMidPointXYZ.append(ItemMidPointX)
    ItemMidPointY = (FromItem[1] + ToItem[1]) / 2
    ItemMidPointXYZ.append(ItemMidPointY)
    ItemMidPointZ = (FromItem[2] + ToItem[2]) / 2
    ItemMidPointXYZ.append(ItemMidPointZ)
    return ItemMidPointXYZ


####################################################
####################################################

def Item_Locking_Set_On(Requires_ItemID):
    __fn_pyModo_Item_Lock_State(Requires_ItemID, 1)


def Item_Locking_Set_Off(Requires_ItemID):
    __fn_pyModo_Item_Lock_State(Requires_ItemID, 0)


def __fn_pyModo_Item_Lock_State(Requires_ItemID, blnState):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        Item_Select(EachItem)
        lx.eval('item.channel lock {%s}' % blnState)


def Item_Visibility_Set_On(Requires_ItemID):
    __fn_pyModo_Item_Visibility_State(Requires_ItemID, 1)


def Item_Visibility_Set_Off(Requires_ItemID):
    __fn_pyModo_Item_Visibility_State(Requires_ItemID, 0)


def __fn_pyModo_Item_Visibility_State(Requires_ItemID, blnState):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        lx.eval('layer.setVisibility {%s} {%s}' % (EachItem, blnState))


def Vert_Locking_Set_On(Requires_ItemID):
    __fn_pyModo_Vert_Lock_State(Requires_ItemID, 1)


def Vert_Locking_Set_Off(Requires_ItemID):
    __fn_pyModo_Vert_Lock_State(Requires_ItemID, 0)


def __fn_pyModo_Vert_Lock_State(Requires_ItemID, blnState):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    if blnState == 1: SelSetName = 'pyModoSS_VertLocking_Add'
    if blnState == 0: SelSetName = 'pyModoSS_VertLocking_Remove'

    SelectionSet_AddTo(SelSetName)

    for EachItem in TheList:
        Item_Select(EachItem)
        Vert_Mode_Set()
        SelectionSet_Select(SelSetName)
        if blnState == 1: lx.eval('lock.sel')
        if blnState == 0: lx.eval('unlock')
        SelectionSet_Delete(SelSetName)


####################################################
####################################################

def Item_Scale_Set(Requires_ItemID, SclX, SclY, SclZ):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        Item_Select(EachItem)
        lx.eval('transform.channel scl.X {%s}' % SclX)
        lx.eval('transform.channel scl.Y {%s}' % SclY)
        lx.eval('transform.channel scl.Z {%s}' % SclZ)


def Item_Rotation_Set(Requires_ItemID, RotX, RotY, RotZ):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        Item_Select(EachItem)
        lx.eval('transform.channel rot.X {%s}' % RotX)
        lx.eval('transform.channel rot.Y {%s}' % RotY)
        lx.eval('transform.channel rot.Z {%s}' % RotZ)


def Item_Position_Set(Requires_ItemID, PosX, PosY, PosZ):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        Item_Select(EachItem)
        lx.eval('transform.channel pos.X {%s}' % PosX)
        lx.eval('transform.channel pos.Y {%s}' % PosY)
        lx.eval('transform.channel pos.Z {%s}' % PosZ)


def Item_Match_Position(Requires_From_ID, Requires_To_ID, Enter_X_Y_Z_or_ALL):
    if not __fn_pyModo_Check_if_String(Enter_X_Y_Z_or_ALL): Enter_X_Y_Z_or_ALL = str(Enter_X_Y_Z_or_ALL)
    AXIS_mod = Enter_X_Y_Z_or_ALL.lower()
    lx.eval('select.Item item:{%s} add' % Requires_From_ID)
    lx.eval('select.subItem item:{%s} add' % Requires_To_ID)
    lx.eval('item.match item pos axis:{%s}' % AXIS_mod)


def Item_Match_Rotation(Requires_From_ID, Requires_To_ID, Enter_X_Y_Z_or_ALL):
    if not __fn_pyModo_Check_if_String(Enter_X_Y_Z_or_ALL): Enter_X_Y_Z_or_ALL = str(Enter_X_Y_Z_or_ALL)
    AXIS_mod = Enter_X_Y_Z_or_ALL.lower()
    lx.eval('select.Item item:{%s} add' % Requires_From_ID)
    lx.eval('select.subItem item:{%s} add' % Requires_To_ID)
    lx.eval('item.match item rot axis:{%s}' % AXIS_mod)


def Item_Match_Scale(Requires_From_ID, Requires_To_ID, Enter_X_Y_Z_or_ALL):
    if not __fn_pyModo_Check_if_String(Enter_X_Y_Z_or_ALL): Enter_X_Y_Z_or_ALL = str(Enter_X_Y_Z_or_ALL)
    AXIS_mod = Enter_X_Y_Z_or_ALL.lower()
    lx.eval('select.Item item:{%s} add' % Requires_From_ID)
    lx.eval('select.subItem item:{%s} add' % Requires_To_ID)
    lx.eval('item.match item scl axis:{%s}' % AXIS_mod)


def Item_Match_Size(Requires_From_ID, Requires_To_ID, Enter_X_Y_Z_or_ALL):
    if not __fn_pyModo_Check_if_String(Enter_X_Y_Z_or_ALL): Enter_X_Y_Z_or_ALL = str(Enter_X_Y_Z_or_ALL)
    AXIS_mod = Enter_X_Y_Z_or_ALL.upper()

    From_ItemDimX = Mesh_Dimension_X_(Requires_From_ID)
    From_ItemDimY = Mesh_Dimension_Y_(Requires_From_ID)
    From_ItemDimZ = Mesh_Dimension_Z_(Requires_From_ID)

    To_ItemDimX = Mesh_Dimension_X_(Requires_To_ID)
    To_ItemDimY = Mesh_Dimension_Y_(Requires_To_ID)
    To_ItemDimZ = Mesh_Dimension_Z_(Requires_To_ID)

    #check compare size difference

    SizeX_ratio = To_ItemDimX / From_ItemDimX
    SizeY_ratio = To_ItemDimY / From_ItemDimY
    SizeZ_ratio = To_ItemDimZ / From_ItemDimZ

    #Get the scale channel values
    ItemScaleID = Item_Scale_ID_Get(Requires_From_ID)

    for eachScl_ID in ItemScaleID:
        Item_Select(eachScl_ID)
    SclX_Val = round(float(Item_Channel_Get_Value('scl.X')), 12)
    SclY_Val = round(float(Item_Channel_Get_Value('scl.Y')), 12)
    SclZ_Val = round(float(Item_Channel_Get_Value('scl.Z')), 12)

    NewSize_X = SclX_Val * SizeX_ratio
    NewSize_Y = SclY_Val * SizeY_ratio
    NewSize_Z = SclZ_Val * SizeZ_ratio

    Item_Select(Requires_From_ID)

    if AXIS_mod == 'X': Modo_Transform_Channel_Edit(eachScl_ID, 'scl.X', NewSize_X)
    if AXIS_mod == 'Y': Modo_Transform_Channel_Edit(eachScl_ID, 'scl.Y', NewSize_Y)
    if AXIS_mod == 'Z': Modo_Transform_Channel_Edit(eachScl_ID, 'scl.Z', NewSize_Z)

    if AXIS_mod == 'ALL':
        Modo_Transform_Channel_Edit(eachScl_ID, 'scl.X', NewSize_X)
        Modo_Transform_Channel_Edit(eachScl_ID, 'scl.Y', NewSize_Y)
        Modo_Transform_Channel_Edit(eachScl_ID, 'scl.Z', NewSize_Z)


def Modo_Transform_Channel_Edit(Requires_Channel_ID, Requires_Channel_Name, Requires_NewValue):
    lx.eval('select.channel {%s:%s} set ' % (Requires_Channel_ID, Requires_Channel_Name))
    lx.eval('channel.value {%s} channel:{%s:%s}' % (Requires_NewValue, Requires_Channel_ID, Requires_Channel_Name))


def Item_Scale_ID_Get(Requires_ItemID):
    Scale_ID_List = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        SclID = lx.eval('query sceneservice item.xfrmScl ? {%s}' % EachItem)
        Scale_ID_List.append(SclID)
    return Scale_ID_List


def Item_Rotation_ID_Get(Requires_ItemID):
    Rotate_ID_List = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        RotID = lx.eval('query sceneservice item.xfrmRot ? {%s}' % EachItem)
        Rotate_ID_List.append(RotID)
    return Rotate_ID_List


def Item_Position_ID_Get(Requires_ItemID):
    Position_ID_List = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        PosID = lx.eval('query sceneservice item.xfrmPos ? {%s}' % EachItem)
        Position_ID_List.append(PosID)
    return Position_ID_List


def Item_Add_Scale_Channel(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        lx.eval('transform.add scl {%s} adv:1' % EachItem)


def Item_Add_Rotation_Channel(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        lx.eval('transform.add rot {%s} adv:1' % EachItem)


def Item_Add_Position_Channel(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        lx.eval('transform.add pos {%s} adv:1' % EachItem)


####################################################
####################################################

def Shader_Effect_Set(Requires_ItemID, Requires_EffectName):
    if not __fn_pyModo_Check_if_String(Requires_EffectName): Requires_EffectName = str(Requires_EffectName)
    EffectName = Requires_EffectName.lower()

    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:
        Item_Select(EachItem)
        lx.eval('shader.setEffect {%s}' % EffectName)


####################################################
####################################################

def Item_ReSizeX_MaintainAspect(Requires_ItemID, EnterNewSize):
    __fn_pyModo_Item_ReSize_Main(Requires_ItemID, EnterNewSize, 'X', 1)


def Item_ReSizeY_MaintainAspect(Requires_ItemID, EnterNewSize):
    __fn_pyModo_Item_ReSize_Main(Requires_ItemID, EnterNewSize, 'Y', 1)


def Item_ReSizeZ_MaintainAspect(Requires_ItemID, EnterNewSize):
    __fn_pyModo_Item_ReSize_Main(Requires_ItemID, EnterNewSize, 'Z', 1)


def Item_ReSize(Requires_ItemID, EnterNewSize, Enter_X_Y_Z_or_ALL):
    __fn_pyModo_Item_ReSize_Main(Requires_ItemID, EnterNewSize, Enter_X_Y_Z_or_ALL, 0)


def __fn_pyModo_Item_ReSize_Main(Requires_ItemID, EnterNewSize, Enter_X_Y_Z_or_ALL, blnAspectRatio):
    if not __fn_pyModo_Check_if_String(Enter_X_Y_Z_or_ALL): Enter_X_Y_Z_or_ALL = str(Enter_X_Y_Z_or_ALL)
    AXIS_mod = Enter_X_Y_Z_or_ALL.upper()

    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')
    for EachItem in TheList:

        Item_Select(EachItem)

        ItemDimX = Mesh_Dimension_X_(EachItem)
        ItemDimY = Mesh_Dimension_Y_(EachItem)
        ItemDimZ = Mesh_Dimension_Z_(EachItem)

        #check compare size difference

        SizeX_ratio = EnterNewSize / ItemDimX
        SizeY_ratio = EnterNewSize / ItemDimY
        SizeZ_ratio = EnterNewSize / ItemDimZ

        #Get the scale channel values
        ItemScaleID = Item_Scale_ID_Get(EachItem)

        for eachScl_ID in ItemScaleID:

            if eachScl_ID == None:
                Item_Add_Scale_Channel(EachItem)
                eachScl_ID = Item_Scale_ID_Get(EachItem)[0]

        Item_Select(eachScl_ID)

        SclX_Val = round(float(Item_Channel_Get_Value('scl.X')), 12)
        SclY_Val = round(float(Item_Channel_Get_Value('scl.Y')), 12)
        SclZ_Val = round(float(Item_Channel_Get_Value('scl.Z')), 12)

        if blnAspectRatio == 0:

            NewSize_X = SclX_Val * SizeX_ratio
            NewSize_Y = SclY_Val * SizeY_ratio
            NewSize_Z = SclZ_Val * SizeZ_ratio

            if AXIS_mod == 'X': Modo_Transform_Channel_Edit(eachScl_ID, 'scl.X', NewSize_X)
            if AXIS_mod == 'Y': Modo_Transform_Channel_Edit(eachScl_ID, 'scl.Y', NewSize_Y)
            if AXIS_mod == 'Z': Modo_Transform_Channel_Edit(eachScl_ID, 'scl.Z', NewSize_Z)

            if AXIS_mod == 'ALL':
                Modo_Transform_Channel_Edit(eachScl_ID, 'scl.X', NewSize_X)
                Modo_Transform_Channel_Edit(eachScl_ID, 'scl.Y', NewSize_Y)
                Modo_Transform_Channel_Edit(eachScl_ID, 'scl.Z', NewSize_Z)

        if blnAspectRatio == 1:

            if AXIS_mod == 'X':
                NewSize_X = SclX_Val * SizeX_ratio
                NewSize_Y = SclY_Val * SizeX_ratio
                NewSize_Z = SclZ_Val * SizeX_ratio
                Modo_Transform_Channel_Edit(eachScl_ID, 'scl.X', NewSize_X)
                Modo_Transform_Channel_Edit(eachScl_ID, 'scl.Y', NewSize_Y)
                Modo_Transform_Channel_Edit(eachScl_ID, 'scl.Z', NewSize_Z)
            if AXIS_mod == 'Y':
                NewSize_X = SclX_Val * SizeY_ratio
                NewSize_Y = SclY_Val * SizeY_ratio
                NewSize_Z = SclZ_Val * SizeY_ratio
                Modo_Transform_Channel_Edit(eachScl_ID, 'scl.X', NewSize_X)
                Modo_Transform_Channel_Edit(eachScl_ID, 'scl.Y', NewSize_Y)
                Modo_Transform_Channel_Edit(eachScl_ID, 'scl.Z', NewSize_Z)
            if AXIS_mod == 'Z':
                NewSize_X = SclX_Val * SizeZ_ratio
                NewSize_Y = SclY_Val * SizeZ_ratio
                NewSize_Z = SclZ_Val * SizeZ_ratio
                Modo_Transform_Channel_Edit(eachScl_ID, 'scl.X', NewSize_X)
                Modo_Transform_Channel_Edit(eachScl_ID, 'scl.Y', NewSize_Y)
                Modo_Transform_Channel_Edit(eachScl_ID, 'scl.Z', NewSize_Z)


####################################################
####################################################

def Mesh_Layer_Index_Get(Requires_ItemID):
    Layer_Index_List = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        LayerIndex = lx.eval('query layerservice layer.index ? %s ' % EachItem)
        Layer_Index_List.append(LayerIndex)

    return Layer_Index_List


####################################################
####################################################

def __AreaTri(vert1X, vert1Y, vert1Z, vert2X, vert2Y, vert2Z, vert3X, vert3Y, vert3Z):
    ax = vert2X - vert1X
    ay = vert2Y - vert1Y
    az = vert2Z - vert1Z
    bx = vert3X - vert1X
    by = vert3Y - vert1Y
    bz = vert3Z - vert1Z
    cx = ay * bz - az * by
    cy = az * bx - ax * bz
    cz = ax * by - ay * bx
    return 0.5 * math.sqrt(cx * cx + cy * cy + cz * cz)


def Calc_Mesh_Area_Get():
    if Mesh_Count_Selected() > 1:
        Modo_UserMessage_Info('Mesh Selection!', 'Please select only one mesh')

    M_ID = Mesh_ID_Selected()

    Poly_Triple_Set()

    if Poly_Count_Selected(M_ID) < 1:
        PolyIndxList = Poly_Index_All(M_ID)
    else:
        PolyIndxList = Poly_Index_Selected(M_ID)

    MeshArea = 0.0

    for eachPoly in PolyIndxList:
        Verts = Poly_VertList_Get(eachPoly)

        vert1X = Vert_WorldPosX_Get(Verts[0])
        vert1Y = Vert_WorldPosY_Get(Verts[0])
        vert1Z = Vert_WorldPosZ_Get(Verts[0])

        vert2X = Vert_WorldPosX_Get(Verts[1])
        vert2Y = Vert_WorldPosY_Get(Verts[1])
        vert2Z = Vert_WorldPosZ_Get(Verts[1])

        vert3X = Vert_WorldPosX_Get(Verts[2])
        vert3Y = Vert_WorldPosY_Get(Verts[2])
        vert3Z = Vert_WorldPosZ_Get(Verts[2])

        MeshArea += __AreaTri(vert1X, vert1Y, vert1Z, vert2X, vert2Y, vert2Z, vert3X, vert3Y, vert3Z)

    return MeshArea


####################################################
####################################################

def Mesh_Delete_withZeroPolyCount():
    M_ID = Mesh_ID_All()
    for mesh in M_ID:
        PolyCnt = Poly_Count_All(mesh)
        if PolyCnt == 0:
            Item_Delete(mesh)


####################################################
####################################################

def Modo_UserDataEntry_asFloat(UserInstructions_asString):
    return __fn_pyModo_UserDataEntry_Main(UserInstructions_asString, 'float')


def Modo_UserDataEntry_asInteger(UserInstructions_asString):
    return __fn_pyModo_UserDataEntry_Main(UserInstructions_asString, 'integer')


def Modo_UserDataEntry_asString(UserInstructions_asString):
    return __fn_pyModo_UserDataEntry_Main(UserInstructions_asString, 'string')


def __fn_pyModo_UserDataEntry_Main(strUserInstructions, DataType):
    try:
        uVar = __Modo_RandomWord(5)
        lx.eval('!user.defNew {%s} type:%s life:momentary' % (uVar, DataType))
        lx.eval('!user.def {%s} username {%s}' % (uVar, strUserInstructions))
        lx.eval('?user.value {%s} ' % uVar)

        UserVal = lx.eval('user.value {%s} ?' % uVar)

        return UserVal

    except:
        sys.exit()


def __Modo_RandomWord(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


####################################################
####################################################

def Modo_UserChoice_Selection(List_SeparateBySemiColon):
    try:
        strChoice = 'Choices'
        strType = 'list'
        if not lx.eval('query scriptsysservice userValue.isDefined ? {%s}' % strChoice):
            lx.eval('!user.defNew {%s} type:integer life:momentary ' % strChoice)
        lx.eval('!user.def {%s} {%s} {%s}' % (strChoice, strType, List_SeparateBySemiColon))
        lx.eval('?user.value {%s}' % strChoice)
        Choice_UserAnswer = lx.eval('user.value {%s} ?' % strChoice)

        return Choice_UserAnswer
    except:
        sys.exit()


####################################################
####################################################

def Mesh_Dimension_X_(Requires_ItemID): return __fn_pyModo_Mesh_Dimension(Requires_ItemID, 'X')


def Mesh_Dimension_X_highVal(Requires_ItemID): return __fn_pyModo_Mesh_Dimension(Requires_ItemID, 'Xhi')


def Mesh_Dimension_X_lowVal(Requires_ItemID): return __fn_pyModo_Mesh_Dimension(Requires_ItemID, 'Xlo')


def Mesh_Dimension_Y_(Requires_ItemID): return __fn_pyModo_Mesh_Dimension(Requires_ItemID, 'Y')


def Mesh_Dimension_Y_highVal(Requires_ItemID): return __fn_pyModo_Mesh_Dimension(Requires_ItemID, 'Yhi')


def Mesh_Dimension_Y_lowVal(Requires_ItemID): return __fn_pyModo_Mesh_Dimension(Requires_ItemID, 'Ylo')


def Mesh_Dimension_Z_(Requires_ItemID): return __fn_pyModo_Mesh_Dimension(Requires_ItemID, 'Z')


def Mesh_Dimension_Z_highVal(Requires_ItemID): return __fn_pyModo_Mesh_Dimension(Requires_ItemID, 'Zhi')


def Mesh_Dimension_Z_lowVal(Requires_ItemID): return __fn_pyModo_Mesh_Dimension(Requires_ItemID, 'Zlo')


def __fn_pyModo_Mesh_Dimension(Requires_ItemID, strAxis):
    strSelectionMode = Modo_Component_Mode_Get()
    Convert_To_Verts()

    int_Rounder = 25
    #get the dimensions of the mesh
    dbl_X_hi = max(VertList_WorldPos_X_(Requires_ItemID))
    dbl_X_lo = min(VertList_WorldPos_X_(Requires_ItemID))
    dbl_Y_hi = max(VertList_WorldPos_Y_(Requires_ItemID))
    dbl_Y_lo = min(VertList_WorldPos_Y_(Requires_ItemID))
    dbl_Z_hi = max(VertList_WorldPos_Z_(Requires_ItemID))
    dbl_Z_lo = min(VertList_WorldPos_Z_(Requires_ItemID))

    dbl_X_Dimension = round(dbl_X_hi - dbl_X_lo, int_Rounder)
    dbl_Y_Dimension = round(dbl_Y_hi - dbl_Y_lo, int_Rounder)
    dbl_Z_Dimension = round(dbl_Z_hi - dbl_Z_lo, int_Rounder)

    lx.eval('select.type {%s}' % strSelectionMode)

    if strAxis == 'X': return dbl_X_Dimension
    if strAxis == 'Y': return dbl_Y_Dimension
    if strAxis == 'Z': return dbl_Z_Dimension
    if strAxis == 'Xhi': return dbl_X_hi
    if strAxis == 'Yhi': return dbl_Y_hi
    if strAxis == 'Zhi': return dbl_Z_hi
    if strAxis == 'Xlo': return dbl_X_lo
    if strAxis == 'Ylo': return dbl_Y_lo
    if strAxis == 'Zlo': return dbl_Z_lo


####################################################
####################################################

def Modo_Component_Mode_Get():
    bln_True = 1
    # convert to component in case in item mode
    if lx.eval('select.typeFrom vertex;edge;polygon ?') == bln_True: strSelectionMode = 'vertex'
    if lx.eval('select.typeFrom edge;vertex;polygon ?') == bln_True: strSelectionMode = 'edge'
    if lx.eval('select.typeFrom polygon;edge;vertex ?') == bln_True: strSelectionMode = 'polygon'

    return strSelectionMode


####################################################
####################################################

def pyModo_Export_Data_ToFile(Requires_DataList, FullFilePath):
    if not __fn_pyModo_Check_if_String(FullFilePath): FullFilePath = str(FullFilePath)
    file_FullPath = open(FullFilePath, 'a')
    if type(Requires_DataList) is list:
        TheList = Requires_DataList
    else:
        TheList = str.split(Requires_DataList, ',')
    for EachItem in TheList:
        file_FullPath.write(EachItem + '\n')

    file_FullPath.close()


####################################################
####################################################

def Curve_Make_Open():
    lx.eval('poly.makeCurveOpen')


####################################################
####################################################

def Curve_Make_Closed():
    lx.eval('poly.makeCurveClosed')


####################################################
####################################################

def Curve_Count(Requires_ItemID):
    Curve_Select(Requires_ItemID)
    Total_CurveCount = Poly_Count_Selected(Requires_ItemID)
    Curve_DeSelect(Requires_ItemID)
    return Total_CurveCount


def Curve_Select(Requires_ItemID):
    Item_Select(Requires_ItemID)
    lx.eval('select.polygon add type curve 3')


def Curve_DeSelect(Requires_ItemID):
    Item_Select(Requires_ItemID)
    lx.eval('select.polygon remove type curve 3')


def Curve_Get_Length(Requires_ItemID):
    CurveLengthList = []
    CurveLength = 0.0
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        if Poly_Count_All(EachItem) > 0:
            Item_Select(EachItem)
            lx.eval('select.polygon add type curve 3')
            PolyCurves = Poly_Index_Selected(EachItem)
            for EachCurve in PolyCurves:
                Poly_DeSelect_All()
                Poly_Mode_Set()
                Poly_Select(EachCurve)
                Convert_To_Edges()
                CurveEdges = lx.evalN('query layerservice edges ? selected')
                CurveLength = 0.0
                for EachEdge in CurveEdges:
                    EdgeIndex = lx.eval('query layerservice edge.index ? {%s}' % EachEdge)
                    CurveLength += lx.eval('query layerservice edge.length ? {%s}' % EdgeIndex)

                CurveLengthList.append(CurveLength)

    return CurveLengthList


####################################################
####################################################
#below are the private parts.... :)
####################################################
####################################################

#Credit goes to Dongju for this piece !!
#kept necessary code only and added modifications
#http://community.thefoundry.co.uk/discussion/topic.aspx?f=37&t=57087
def __fn_pyModo_Item_Channel_Main(Channel):
    chName_List = []
    #chValue_List = []
    #chType_List = []

    s = lx.Service('sceneservice')
    s.select('scene.index', 'current')  #select current scene

    s.select('selection', 'all')
    selitems = s.queryN('selection')

    for item in selitems:
        s.select('item.id', item)
        item_channelN = s.query('channel.N')

        for channel in range(item_channelN):
            s.select('channel.index', str(channel))
            chan_name = s.query('channel.name')

            if chan_name == Channel:
                chan_value = s.query('channel.value')

            #chan_type  = s.query('channel.type')

            chName_List.append(chan_name)
        #chValue_List.append(chan_value)
        #chType_List.append(chan_type)

    if Channel == 'chan_name':
        return chName_List
    elif Channel != 'chan_name':
        return chan_value
    #elif Channel == 'chan_type':
    #return chType_List


####################################################
####################################################

def __fn_pyModo_Component_Count(Requires_OneItemID, strItemType, asVariant):
    V_TOT_ALL = []
    V_TOT_SEL = []
    V_TOT_UNS = []
    E_TOT_ALL = []
    E_TOT_SEL = []
    E_TOT_UNS = []
    P_TOT_ALL = []
    P_TOT_SEL = []
    P_TOT_UNS = []

    if type(Requires_OneItemID) is list:
        TheList = Requires_OneItemID
    else:
        TheList = str.split(Requires_OneItemID, ',')

    if strItemType == 'Vert':
        Vert_Mode_Set()

    if strItemType == 'Edge':
        Edge_Mode_Set()

    if strItemType == 'Poly':
        Poly_Mode_Set()

    for EachItem in TheList:

        Item_Select(EachItem)
        lx.eval('query layerservice layer.name ? current')

        if strItemType == 'Vert':
            Vert_Mode_Set()
            VertCount_All = lx.eval('query layerservice vert.N ? all')
            V_TOT_ALL.append(VertCount_All)
            VertCount_Selected = lx.eval('query layerservice vert.N ? selected')
            V_TOT_SEL.append(VertCount_Selected)
            VertCount_UnSelected = VertCount_All - VertCount_Selected
            V_TOT_UNS.append(VertCount_UnSelected)

        if strItemType == 'Edge':
            Edge_Mode_Set()
            EdgeCount_All = lx.eval('query layerservice edge.N ? all')
            E_TOT_ALL.append(EdgeCount_All)
            EdgeCount_Selected = lx.eval('query layerservice edge.N ? selected')
            E_TOT_SEL.append(EdgeCount_Selected)
            EdgeCount_UnSelected = EdgeCount_All - EdgeCount_Selected
            E_TOT_UNS.append(EdgeCount_UnSelected)

        if strItemType == 'Poly':
            Poly_Mode_Set()
            PolyCount_All = lx.eval('query layerservice poly.N ? all')
            P_TOT_ALL.append(PolyCount_All)
            PolyCount_Selected = lx.eval('query layerservice poly.N ? selected')
            P_TOT_SEL.append(PolyCount_Selected)
            PolyCount_UnSelected = PolyCount_All - PolyCount_Selected
            P_TOT_UNS.append(PolyCount_UnSelected)

    if strItemType == 'Vert':
        if asVariant == 'all':
            return sum(V_TOT_ALL)
        elif asVariant == 'selected':
            return sum(V_TOT_SEL)
        elif asVariant == 'unselected':
            return sum(V_TOT_UNS)
    if strItemType == 'Edge':
        if asVariant == 'all':
            return sum(E_TOT_ALL)
        elif asVariant == 'selected':
            return sum(E_TOT_SEL)
        elif asVariant == 'unselected':
            return sum(E_TOT_UNS)
    if strItemType == 'Poly':
        if asVariant == 'all':
            return sum(P_TOT_ALL)
        elif asVariant == 'selected':
            return sum(P_TOT_SEL)
        elif asVariant == 'unselected':
            return sum(P_TOT_UNS)


####################################################
####################################################

def __fn_pyModo_Component_Index(Requires_ItemID, strItemType, asVariant):
    V_TOT_ALL_LIST = []
    V_TOT_SEL_LIST = []
    V_TOT_UNS_LIST = []
    E_TOT_ALL_LIST = []
    E_TOT_SEL_LIST = []
    E_TOT_UNS_LIST = []
    P_TOT_ALL_LIST = []
    P_TOT_SEL_LIST = []
    P_TOT_UNS_LIST = []

    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    if asVariant == 'unselected':
        lx.eval('select.invert')

    for EachItem in TheList:

        lx.eval('select.Item item:{%s} mode: set' % EachItem)
        lx.eval('query layerservice layer.name ? current')

        if strItemType == 'Vert':
            Vert_Mode_Set()
            if asVariant == 'all':
                VertCount_All = lx.evalN('query layerservice verts ? all')
                for EachVert in VertCount_All:
                    EachVertIndex = lx.eval('query layerservice vert.index ? {%s}' % EachVert)
                    V_TOT_ALL_LIST.append(EachVertIndex)

            elif asVariant == 'selected':
                VertCount_Selected = lx.evalN('query layerservice verts ? selected')
                for EachVert in VertCount_Selected:
                    EachVertIndex = lx.eval('query layerservice vert.index ? {%s}' % EachVert)
                    V_TOT_SEL_LIST.append(EachVertIndex)

            elif asVariant == 'unselected':
                VertCount_UnSelected = lx.evalN('query layerservice verts ? selected')
                for EachVert in VertCount_UnSelected:
                    EachVertIndex = lx.eval('query layerservice vert.index ? {%s}' % EachVert)
                    V_TOT_UNS_LIST.append(EachVertIndex)

        if strItemType == 'Edge':
            Edge_Mode_Set()
            if asVariant == 'all':
                EdgeCount_All = lx.evalN('query layerservice edges ? all')
                for EachEdge in EdgeCount_All:
                    EachEdgeIndex = lx.eval('query layerservice edge.index ? {%s}' % EachEdge)
                    E_TOT_ALL_LIST.append(EachEdgeIndex)

            elif asVariant == 'selected':
                EdgeCount_Selected = lx.evalN('query layerservice edges ? selected')
                for EachEdge in EdgeCount_Selected:
                    EachEdgeIndex = lx.eval('query layerservice edge.index ? {%s}' % EachEdge)
                    E_TOT_SEL_LIST.append(EachEdgeIndex)

            elif asVariant == 'unselected':
                EdgeCount_UnSelected = lx.evalN('query layerservice edges ? selected')
                for EachEdge in EdgeCount_UnSelected:
                    EachEdgeIndex = lx.eval('query layerservice edge.index ? {%s}' % EachEdge)
                    E_TOT_UNS_LIST.append(EachEdgeIndex)

        if strItemType == 'Poly':
            Poly_Mode_Set()
            if asVariant == 'all':
                PolyCount_All = lx.evalN('query layerservice polys ? all')
                for EachPoly in PolyCount_All:
                    EachPolyIndex = lx.eval('query layerservice poly.index ? {%s}' % EachPoly)
                    P_TOT_ALL_LIST.append(EachPolyIndex)

            elif asVariant == 'selected':
                PolyCount_Selected = lx.evalN('query layerservice polys ? selected')
                for EachPoly in PolyCount_Selected:
                    EachPolyIndex = lx.eval('query layerservice poly.index ? {%s}' % EachPoly)
                    P_TOT_SEL_LIST.append(EachPolyIndex)

            elif asVariant == 'unselected':
                PolyCount_UnSelected = lx.evalN('query layerservice polys ? selected')
                for EachPoly in PolyCount_UnSelected:
                    EachPolyIndex = lx.eval('query layerservice poly.index ? {%s}' % EachPoly)
                    P_TOT_UNS_LIST.append(EachPolyIndex)

    if strItemType == 'Vert':
        if asVariant == 'all':
            return V_TOT_ALL_LIST
        elif asVariant == 'selected':
            return V_TOT_SEL_LIST
        elif asVariant == 'unselected':
            return V_TOT_UNS_LIST
    if strItemType == 'Edge':
        if asVariant == 'all':
            return E_TOT_ALL_LIST
        elif asVariant == 'selected':
            return E_TOT_SEL_LIST
        elif asVariant == 'unselected':
            return E_TOT_UNS_LIST
    if strItemType == 'Poly':
        if asVariant == 'all':
            return P_TOT_ALL_LIST
        elif asVariant == 'selected':
            return P_TOT_SEL_LIST
        elif asVariant == 'unselected':
            return P_TOT_UNS_LIST


####################################################
####################################################

def __fn_pyModo_MsgBox(strMsgType, strMsgTitle, strMsgToUser):
    lx.eval('dialog.setup {%s}' % strMsgType)
    lx.eval('dialog.title {%s}' % strMsgTitle)
    lx.eval('dialog.msg {%s}' % strMsgToUser)

    try:
        lx.eval('dialog.Open')

    except:
        pass

    return lx.eval('dialog.result ?')


####################################################
####################################################

def __fn_pyModo_Scene_Items():
    return lx.eval('query sceneservice item.N ?')


####################################################
####################################################

def __fn_pyModo_Scene_ItemType(EachItem):
    return lx.eval('query sceneservice item.typeLabel ? {%s}' % EachItem)


####################################################
####################################################

def __fn_pyModo_Scene_ItemID(EachItem):
    return lx.eval('query sceneservice item.id ? {%s}' % EachItem)


####################################################
####################################################

def __fn_pyModo_Scene_ItemsSelected(Requires_ItemID):
    return lx.eval('query sceneservice item.isSelected ? {%s}' % Requires_ItemID)


####################################################
####################################################

def __fn_pyModo_Scene_ItemName(EachItem):
    return lx.eval('query sceneservice item.name ? {%s}' % EachItem)


####################################################
####################################################

def __fn_pyModo_Item_Count(strItemType, asVariant):
    intTotal = 0
    blnTrue = 1
    blnFalse = 0

    SceneItemCount = __fn_pyModo_Scene_Items()

    for EachItem in range(0, SceneItemCount):

        ItemType = __fn_pyModo_Scene_ItemType(EachItem)
        ItemID = __fn_pyModo_Scene_ItemID(EachItem)

        if ItemType == strItemType:

            if asVariant == 'all':
                intTotal += 1

            if asVariant == 'selected':
                blnSelected = __fn_pyModo_Scene_ItemsSelected(ItemID)
                if blnSelected == blnTrue:
                    intTotal += 1

            if asVariant == 'unselected':
                blnUnSelected = __fn_pyModo_Scene_ItemsSelected(ItemID)
                if blnUnSelected == blnFalse:
                    intTotal += 1

    return intTotal


####################################################
####################################################

def __fn_pyModo_Item_Name(strItemType, asVariant):
    Name_List = []
    blnTrue = 1
    blnFalse = 0

    SceneItemCount = __fn_pyModo_Scene_Items()

    for EachItem in range(0, SceneItemCount):

        ItemType = __fn_pyModo_Scene_ItemType(EachItem)
        ItemID = __fn_pyModo_Scene_ItemID(EachItem)
        ItemName = __fn_pyModo_Scene_ItemName(EachItem)

        if ItemType == strItemType:

            if asVariant == 'all':
                Name_List.append(ItemName)

            if asVariant == 'selected':
                blnSelected = __fn_pyModo_Scene_ItemsSelected(ItemID)
                if blnSelected == blnTrue:
                    Name_List.append(ItemName)

            if asVariant == 'unselected':
                blnUnSelected = __fn_pyModo_Scene_ItemsSelected(ItemID)
                if blnUnSelected == blnFalse:
                    Name_List.append(ItemName)

    return Name_List


####################################################
####################################################

def __fn_pyModo_Item_ID(strItemType, asVariant):
    ID_List = []
    blnTrue = 1
    blnFalse = 0

    SceneItemCount = __fn_pyModo_Scene_Items()

    for EachItem in range(0, SceneItemCount):

        ItemType = __fn_pyModo_Scene_ItemType(EachItem)
        ItemID = __fn_pyModo_Scene_ItemID(EachItem)

        if ItemType == strItemType:

            if asVariant == 'all':
                ID_List.append(ItemID)

            if asVariant == 'selected':
                blnSelected = __fn_pyModo_Scene_ItemsSelected(ItemID)
                if blnSelected == blnTrue:
                    ID_List.append(ItemID)

            if asVariant == 'unselected':
                blnUnSelected = __fn_pyModo_Scene_ItemsSelected(ItemID)
                if blnUnSelected == blnFalse:
                    ID_List.append(ItemID)

    return ID_List

#above are the private parts.... :)
####################################################
####################################################
