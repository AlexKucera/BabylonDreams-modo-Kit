#!/usr/bin/python


#pyModo
#Author Keith Sheppard
#1/7/2015 7:52:52 PM


import lx
import sys

def Area_Light_Count_All():
	strItemType = 'Area Light'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Area_Light_Count_Selected():
	strItemType = 'Area Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Area_Light_Count_UnSelected():
	strItemType = 'Area Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Area_Light_Name_All():
	strItemType = 'Area Light'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Area_Light_Name_Selected():
	strItemType = 'Area Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Area_Light_Name_UnSelected():
	strItemType = 'Area Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Area_Light_ID_All():
	strItemType = 'Area Light'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Area_Light_ID_Selected():
	strItemType = 'Area Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Area_Light_ID_UnSelected():
	strItemType = 'Area Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Area_Light_Add_New():
	strItemType = 'areaLight'
	lx.eval('item.create {%s}' % strItemType)
def Backdrop_Item_Count_All():
	strItemType = 'Backdrop Item'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Backdrop_Item_Count_Selected():
	strItemType = 'Backdrop Item'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Backdrop_Item_Count_UnSelected():
	strItemType = 'Backdrop Item'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Backdrop_Item_Name_All():
	strItemType = 'Backdrop Item'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Backdrop_Item_Name_Selected():
	strItemType = 'Backdrop Item'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Backdrop_Item_Name_UnSelected():
	strItemType = 'Backdrop Item'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Backdrop_Item_ID_All():
	strItemType = 'Backdrop Item'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Backdrop_Item_ID_Selected():
	strItemType = 'Backdrop Item'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Backdrop_Item_ID_UnSelected():
	strItemType = 'Backdrop Item'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Backdrop_Item_Add_New():
	strItemType = 'backdrop'
	lx.eval('item.create {%s}' % strItemType)
def Bend_Effector_Count_All():
	strItemType = 'Bend Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Bend_Effector_Count_Selected():
	strItemType = 'Bend Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Bend_Effector_Count_UnSelected():
	strItemType = 'Bend Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Bend_Effector_Name_All():
	strItemType = 'Bend Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Bend_Effector_Name_Selected():
	strItemType = 'Bend Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Bend_Effector_Name_UnSelected():
	strItemType = 'Bend Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Bend_Effector_ID_All():
	strItemType = 'Bend Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Bend_Effector_ID_Selected():
	strItemType = 'Bend Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Bend_Effector_ID_UnSelected():
	strItemType = 'Bend Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Bend_Effector_Add_New():
	strItemType = 'deform.bend'
	lx.eval('item.create {%s}' % strItemType)
def Bezier_Falloff_Count_All():
	strItemType = 'Bezier Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Bezier_Falloff_Count_Selected():
	strItemType = 'Bezier Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Bezier_Falloff_Count_UnSelected():
	strItemType = 'Bezier Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Bezier_Falloff_Name_All():
	strItemType = 'Bezier Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Bezier_Falloff_Name_Selected():
	strItemType = 'Bezier Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Bezier_Falloff_Name_UnSelected():
	strItemType = 'Bezier Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Bezier_Falloff_ID_All():
	strItemType = 'Bezier Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Bezier_Falloff_ID_Selected():
	strItemType = 'Bezier Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Bezier_Falloff_ID_UnSelected():
	strItemType = 'Bezier Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Bezier_Falloff_Add_New():
	strItemType = 'falloff.bezier'
	lx.eval('item.create {%s}' % strItemType)
def Blob_Count_All():
	strItemType = 'Blob'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Blob_Count_Selected():
	strItemType = 'Blob'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Blob_Count_UnSelected():
	strItemType = 'Blob'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Blob_Name_All():
	strItemType = 'Blob'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Blob_Name_Selected():
	strItemType = 'Blob'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Blob_Name_UnSelected():
	strItemType = 'Blob'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Blob_ID_All():
	strItemType = 'Blob'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Blob_ID_Selected():
	strItemType = 'Blob'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Blob_ID_UnSelected():
	strItemType = 'Blob'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Blob_Add_New():
	strItemType = 'blob'
	lx.eval('item.create {%s}' % strItemType)
def Camera_Count_All():
	strItemType = 'Camera'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Camera_Count_Selected():
	strItemType = 'Camera'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Camera_Count_UnSelected():
	strItemType = 'Camera'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Camera_Name_All():
	strItemType = 'Camera'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Camera_Name_Selected():
	strItemType = 'Camera'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Camera_Name_UnSelected():
	strItemType = 'Camera'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Camera_ID_All():
	strItemType = 'Camera'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Camera_ID_Selected():
	strItemType = 'Camera'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Camera_ID_UnSelected():
	strItemType = 'Camera'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Camera_Add_New():
	strItemType = 'camera'
	lx.eval('item.create {%s}' % strItemType)
def Capsule_Falloff_Count_All():
	strItemType = 'Capsule Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Capsule_Falloff_Count_Selected():
	strItemType = 'Capsule Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Capsule_Falloff_Count_UnSelected():
	strItemType = 'Capsule Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Capsule_Falloff_Name_All():
	strItemType = 'Capsule Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Capsule_Falloff_Name_Selected():
	strItemType = 'Capsule Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Capsule_Falloff_Name_UnSelected():
	strItemType = 'Capsule Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Capsule_Falloff_ID_All():
	strItemType = 'Capsule Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Capsule_Falloff_ID_Selected():
	strItemType = 'Capsule Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Capsule_Falloff_ID_UnSelected():
	strItemType = 'Capsule Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Capsule_Falloff_Add_New():
	strItemType = 'falloff.capsule'
	lx.eval('item.create {%s}' % strItemType)
def Cel_Edges_Material_Count_All():
	strItemType = 'Cel Edges Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Cel_Edges_Material_Count_Selected():
	strItemType = 'Cel Edges Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Cel_Edges_Material_Count_UnSelected():
	strItemType = 'Cel Edges Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Cel_Edges_Material_Name_All():
	strItemType = 'Cel Edges Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Cel_Edges_Material_Name_Selected():
	strItemType = 'Cel Edges Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Cel_Edges_Material_Name_UnSelected():
	strItemType = 'Cel Edges Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Cel_Edges_Material_ID_All():
	strItemType = 'Cel Edges Material'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Cel_Edges_Material_ID_Selected():
	strItemType = 'Cel Edges Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Cel_Edges_Material_ID_UnSelected():
	strItemType = 'Cel Edges Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Cel_Edges_Material_Add_New():
	strItemType = 'material.celEdges'
	lx.eval('shader.create {%s}' % strItemType)
def Cel_Material_Count_All():
	strItemType = 'Cel Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Cel_Material_Count_Selected():
	strItemType = 'Cel Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Cel_Material_Count_UnSelected():
	strItemType = 'Cel Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Cel_Material_Name_All():
	strItemType = 'Cel Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Cel_Material_Name_Selected():
	strItemType = 'Cel Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Cel_Material_Name_UnSelected():
	strItemType = 'Cel Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Cel_Material_ID_All():
	strItemType = 'Cel Material'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Cel_Material_ID_Selected():
	strItemType = 'Cel Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Cel_Material_ID_UnSelected():
	strItemType = 'Cel Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Cel_Material_Add_New():
	strItemType = 'material.celShader'
	lx.eval('shader.create {%s}' % strItemType)
def Cellular_Count_All():
	strItemType = 'Cellular'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Cellular_Count_Selected():
	strItemType = 'Cellular'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Cellular_Count_UnSelected():
	strItemType = 'Cellular'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Cellular_Name_All():
	strItemType = 'Cellular'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Cellular_Name_Selected():
	strItemType = 'Cellular'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Cellular_Name_UnSelected():
	strItemType = 'Cellular'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Cellular_ID_All():
	strItemType = 'Cellular'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Cellular_ID_Selected():
	strItemType = 'Cellular'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Cellular_ID_UnSelected():
	strItemType = 'Cellular'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Cellular_Add_New():
	strItemType = 'cellular'
	lx.eval('shader.create {%s}' % strItemType)
def Checker_Count_All():
	strItemType = 'Checker'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Checker_Count_Selected():
	strItemType = 'Checker'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Checker_Count_UnSelected():
	strItemType = 'Checker'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Checker_Name_All():
	strItemType = 'Checker'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Checker_Name_Selected():
	strItemType = 'Checker'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Checker_Name_UnSelected():
	strItemType = 'Checker'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Checker_ID_All():
	strItemType = 'Checker'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Checker_ID_Selected():
	strItemType = 'Checker'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Checker_ID_UnSelected():
	strItemType = 'Checker'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Checker_Add_New():
	strItemType = 'checker'
	lx.eval('shader.create {%s}' % strItemType)
def Constant_Count_All():
	strItemType = 'Constant'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Constant_Count_Selected():
	strItemType = 'Constant'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Constant_Count_UnSelected():
	strItemType = 'Constant'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Constant_Name_All():
	strItemType = 'Constant'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Constant_Name_Selected():
	strItemType = 'Constant'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Constant_Name_UnSelected():
	strItemType = 'Constant'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Constant_ID_All():
	strItemType = 'Constant'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Constant_ID_Selected():
	strItemType = 'Constant'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Constant_ID_UnSelected():
	strItemType = 'Constant'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Constant_Add_New():
	strItemType = 'constant'
	lx.eval('shader.create {%s}' % strItemType)
def Curve_Constraint_Effector_Count_All():
	strItemType = 'Curve Constraint Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Curve_Constraint_Effector_Count_Selected():
	strItemType = 'Curve Constraint Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Curve_Constraint_Effector_Count_UnSelected():
	strItemType = 'Curve Constraint Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Curve_Constraint_Effector_Name_All():
	strItemType = 'Curve Constraint Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Curve_Constraint_Effector_Name_Selected():
	strItemType = 'Curve Constraint Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Curve_Constraint_Effector_Name_UnSelected():
	strItemType = 'Curve Constraint Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Curve_Constraint_Effector_ID_All():
	strItemType = 'Curve Constraint Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Curve_Constraint_Effector_ID_Selected():
	strItemType = 'Curve Constraint Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Curve_Constraint_Effector_ID_UnSelected():
	strItemType = 'Curve Constraint Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Curve_Constraint_Effector_Add_New():
	strItemType = 'deform.crvConst'
	lx.eval('item.create {%s}' % strItemType)
def Curve_Force_Count_All():
	strItemType = 'Curve Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Curve_Force_Count_Selected():
	strItemType = 'Curve Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Curve_Force_Count_UnSelected():
	strItemType = 'Curve Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Curve_Force_Name_All():
	strItemType = 'Curve Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Curve_Force_Name_Selected():
	strItemType = 'Curve Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Curve_Force_Name_UnSelected():
	strItemType = 'Curve Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Curve_Force_ID_All():
	strItemType = 'Curve Force'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Curve_Force_ID_Selected():
	strItemType = 'Curve Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Curve_Force_ID_UnSelected():
	strItemType = 'Curve Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Curve_Force_Add_New():
	strItemType = 'force.curve'
	lx.eval('item.create {%s}' % strItemType)
def Cylinder_Light_Count_All():
	strItemType = 'Cylinder Light'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Cylinder_Light_Count_Selected():
	strItemType = 'Cylinder Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Cylinder_Light_Count_UnSelected():
	strItemType = 'Cylinder Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Cylinder_Light_Name_All():
	strItemType = 'Cylinder Light'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Cylinder_Light_Name_Selected():
	strItemType = 'Cylinder Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Cylinder_Light_Name_UnSelected():
	strItemType = 'Cylinder Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Cylinder_Light_ID_All():
	strItemType = 'Cylinder Light'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Cylinder_Light_ID_Selected():
	strItemType = 'Cylinder Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Cylinder_Light_ID_UnSelected():
	strItemType = 'Cylinder Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Cylinder_Light_Add_New():
	strItemType = 'cylinderLight'
	lx.eval('item.create {%s}' % strItemType)
def Directional_Light_Count_All():
	strItemType = 'Directional Light'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Directional_Light_Count_Selected():
	strItemType = 'Directional Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Directional_Light_Count_UnSelected():
	strItemType = 'Directional Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Directional_Light_Name_All():
	strItemType = 'Directional Light'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Directional_Light_Name_Selected():
	strItemType = 'Directional Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Directional_Light_Name_UnSelected():
	strItemType = 'Directional Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Directional_Light_ID_All():
	strItemType = 'Directional Light'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Directional_Light_ID_Selected():
	strItemType = 'Directional Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Directional_Light_ID_UnSelected():
	strItemType = 'Directional Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Directional_Light_Add_New():
	strItemType = 'sunLight'
	lx.eval('item.create {%s}' % strItemType)
def Dome_Light_Count_All():
	strItemType = 'Dome Light'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Dome_Light_Count_Selected():
	strItemType = 'Dome Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Dome_Light_Count_UnSelected():
	strItemType = 'Dome Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Dome_Light_Name_All():
	strItemType = 'Dome Light'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Dome_Light_Name_Selected():
	strItemType = 'Dome Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Dome_Light_Name_UnSelected():
	strItemType = 'Dome Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Dome_Light_ID_All():
	strItemType = 'Dome Light'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Dome_Light_ID_Selected():
	strItemType = 'Dome Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Dome_Light_ID_UnSelected():
	strItemType = 'Dome Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Dome_Light_Add_New():
	strItemType = 'domeLight'
	lx.eval('item.create {%s}' % strItemType)
def Dots_Count_All():
	strItemType = 'Dots'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Dots_Count_Selected():
	strItemType = 'Dots'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Dots_Count_UnSelected():
	strItemType = 'Dots'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Dots_Name_All():
	strItemType = 'Dots'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Dots_Name_Selected():
	strItemType = 'Dots'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Dots_Name_UnSelected():
	strItemType = 'Dots'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Dots_ID_All():
	strItemType = 'Dots'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Dots_ID_Selected():
	strItemType = 'Dots'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Dots_ID_UnSelected():
	strItemType = 'Dots'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Dots_Add_New():
	strItemType = 'dots'
	lx.eval('shader.create {%s}' % strItemType)
def Drag_Force_Count_All():
	strItemType = 'Drag Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Drag_Force_Count_Selected():
	strItemType = 'Drag Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Drag_Force_Count_UnSelected():
	strItemType = 'Drag Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Drag_Force_Name_All():
	strItemType = 'Drag Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Drag_Force_Name_Selected():
	strItemType = 'Drag Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Drag_Force_Name_UnSelected():
	strItemType = 'Drag Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Drag_Force_ID_All():
	strItemType = 'Drag Force'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Drag_Force_ID_Selected():
	strItemType = 'Drag Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Drag_Force_ID_UnSelected():
	strItemType = 'Drag Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Drag_Force_Add_New():
	strItemType = 'force.drag'
	lx.eval('item.create {%s}' % strItemType)
def Edge_Count_All(Requires_ItemID):
	strItemType = 'Edge'
	asVariant = 'all'
	return __fn_pyModo_Component_Count(Requires_ItemID,strItemType,asVariant)
def Edge_Count_Selected(Requires_ItemID):
	strItemType = 'Edge'
	asVariant = 'selected'
	return __fn_pyModo_Component_Count(Requires_ItemID,strItemType,asVariant)
def Edge_Count_UnSelected(Requires_ItemID):
	strItemType = 'Edge'
	asVariant = 'unselected'
	return __fn_pyModo_Component_Count(Requires_ItemID,strItemType,asVariant)
def Edge_Index_All(Requires_ItemID):
	strItemType = 'Edge'
	asVariant = 'all'
	return __fn_pyModo_Component_Index(Requires_ItemID,strItemType,asVariant)
def Edge_Index_Selected(Requires_ItemID):
	strItemType = 'Edge'
	asVariant = 'selected'
	return __fn_pyModo_Component_Index(Requires_ItemID,strItemType,asVariant)
def Edge_Index_UnSelected(Requires_ItemID):
	strItemType = 'Edge'
	asVariant = 'unselected'
	return __fn_pyModo_Component_Index(Requires_ItemID,strItemType,asVariant)
def Environment_Count_All():
	strItemType = 'Environment'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Environment_Count_Selected():
	strItemType = 'Environment'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Environment_Count_UnSelected():
	strItemType = 'Environment'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Environment_Name_All():
	strItemType = 'Environment'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Environment_Name_Selected():
	strItemType = 'Environment'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Environment_Name_UnSelected():
	strItemType = 'Environment'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Environment_ID_All():
	strItemType = 'Environment'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Environment_ID_Selected():
	strItemType = 'Environment'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Environment_ID_UnSelected():
	strItemType = 'Environment'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Environment_Add_New():
	strItemType = 'environment'
	lx.eval('item.create {%s}' % strItemType)
def Environment_Material_Count_All():
	strItemType = 'Environment Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Environment_Material_Count_Selected():
	strItemType = 'Environment Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Environment_Material_Count_UnSelected():
	strItemType = 'Environment Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Environment_Material_Name_All():
	strItemType = 'Environment Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Environment_Material_Name_Selected():
	strItemType = 'Environment Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Environment_Material_Name_UnSelected():
	strItemType = 'Environment Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Environment_Material_ID_All():
	strItemType = 'Environment Material'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Environment_Material_ID_Selected():
	strItemType = 'Environment Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Environment_Material_ID_UnSelected():
	strItemType = 'Environment Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Environment_Material_Add_New():
	strItemType = 'envMaterial'
	lx.eval('shader.create {%s}' % strItemType)
def Fur_Material_Count_All():
	strItemType = 'Fur Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Fur_Material_Count_Selected():
	strItemType = 'Fur Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Fur_Material_Count_UnSelected():
	strItemType = 'Fur Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Fur_Material_Name_All():
	strItemType = 'Fur Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Fur_Material_Name_Selected():
	strItemType = 'Fur Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Fur_Material_Name_UnSelected():
	strItemType = 'Fur Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Fur_Material_ID_All():
	strItemType = 'Fur Material'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Fur_Material_ID_Selected():
	strItemType = 'Fur Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Fur_Material_ID_UnSelected():
	strItemType = 'Fur Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Fur_Material_Add_New():
	strItemType = 'furMaterial'
	lx.eval('shader.create {%s}' % strItemType)
def Gradient_Count_All():
	strItemType = 'Gradient'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Gradient_Count_Selected():
	strItemType = 'Gradient'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Gradient_Count_UnSelected():
	strItemType = 'Gradient'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Gradient_Name_All():
	strItemType = 'Gradient'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Gradient_Name_Selected():
	strItemType = 'Gradient'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Gradient_Name_UnSelected():
	strItemType = 'Gradient'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Gradient_ID_All():
	strItemType = 'Gradient'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Gradient_ID_Selected():
	strItemType = 'Gradient'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Gradient_ID_UnSelected():
	strItemType = 'Gradient'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Gradient_Add_New():
	strItemType = 'gradient'
	lx.eval('shader.create {%s}' % strItemType)
def Grid_Count_All():
	strItemType = 'Grid'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Grid_Count_Selected():
	strItemType = 'Grid'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Grid_Count_UnSelected():
	strItemType = 'Grid'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Grid_Name_All():
	strItemType = 'Grid'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Grid_Name_Selected():
	strItemType = 'Grid'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Grid_Name_UnSelected():
	strItemType = 'Grid'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Grid_ID_All():
	strItemType = 'Grid'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Grid_ID_Selected():
	strItemType = 'Grid'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Grid_ID_UnSelected():
	strItemType = 'Grid'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Grid_Add_New():
	strItemType = 'grid'
	lx.eval('shader.create {%s}' % strItemType)
def Group_Count_All():
	strItemType = 'Group'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Group_Count_Selected():
	strItemType = 'Group'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Group_Count_UnSelected():
	strItemType = 'Group'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Group_Name_All():
	strItemType = 'Group'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Group_Name_Selected():
	strItemType = 'Group'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Group_Name_UnSelected():
	strItemType = 'Group'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Group_ID_All():
	strItemType = 'Group'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Group_ID_Selected():
	strItemType = 'Group'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Group_ID_UnSelected():
	strItemType = 'Group'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Group_Add_New():
	strItemType = 'mask'
	lx.eval('shader.create {%s}' % strItemType)
def Group_Locator_Count_All():
	strItemType = 'Group Locator'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Group_Locator_Count_Selected():
	strItemType = 'Group Locator'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Group_Locator_Count_UnSelected():
	strItemType = 'Group Locator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Group_Locator_Name_All():
	strItemType = 'Group Locator'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Group_Locator_Name_Selected():
	strItemType = 'Group Locator'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Group_Locator_Name_UnSelected():
	strItemType = 'Group Locator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Group_Locator_ID_All():
	strItemType = 'Group Locator'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Group_Locator_ID_Selected():
	strItemType = 'Group Locator'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Group_Locator_ID_UnSelected():
	strItemType = 'Group Locator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Group_Locator_Add_New():
	strItemType = 'groupLocator'
	lx.eval('item.create {%s}' % strItemType)
def Hair_Material_Count_All():
	strItemType = 'Hair Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Hair_Material_Count_Selected():
	strItemType = 'Hair Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Hair_Material_Count_UnSelected():
	strItemType = 'Hair Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Hair_Material_Name_All():
	strItemType = 'Hair Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Hair_Material_Name_Selected():
	strItemType = 'Hair Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Hair_Material_Name_UnSelected():
	strItemType = 'Hair Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Hair_Material_ID_All():
	strItemType = 'Hair Material'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Hair_Material_ID_Selected():
	strItemType = 'Hair Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Hair_Material_ID_UnSelected():
	strItemType = 'Hair Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Hair_Material_Add_New():
	strItemType = 'material.hairMaterial'
	lx.eval('shader.create {%s}' % strItemType)
def Halftone_Material_Count_All():
	strItemType = 'Halftone Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Halftone_Material_Count_Selected():
	strItemType = 'Halftone Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Halftone_Material_Count_UnSelected():
	strItemType = 'Halftone Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Halftone_Material_Name_All():
	strItemType = 'Halftone Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Halftone_Material_Name_Selected():
	strItemType = 'Halftone Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Halftone_Material_Name_UnSelected():
	strItemType = 'Halftone Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Halftone_Material_ID_All():
	strItemType = 'Halftone Material'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Halftone_Material_ID_Selected():
	strItemType = 'Halftone Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Halftone_Material_ID_UnSelected():
	strItemType = 'Halftone Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Halftone_Material_Add_New():
	strItemType = 'material.halftone'
	lx.eval('shader.create {%s}' % strItemType)
def Hinge_Count_All():
	strItemType = 'Hinge'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Hinge_Count_Selected():
	strItemType = 'Hinge'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Hinge_Count_UnSelected():
	strItemType = 'Hinge'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Hinge_Name_All():
	strItemType = 'Hinge'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Hinge_Name_Selected():
	strItemType = 'Hinge'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Hinge_Name_UnSelected():
	strItemType = 'Hinge'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Hinge_ID_All():
	strItemType = 'Hinge'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Hinge_ID_Selected():
	strItemType = 'Hinge'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Hinge_ID_UnSelected():
	strItemType = 'Hinge'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Hinge_Add_New():
	strItemType = 'consHinge'
	lx.eval('item.create {%s}' % strItemType)
def Image_Map_Count_All():
	strItemType = 'Image Map'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Image_Map_Count_Selected():
	strItemType = 'Image Map'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Image_Map_Count_UnSelected():
	strItemType = 'Image Map'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Image_Map_Name_All():
	strItemType = 'Image Map'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Image_Map_Name_Selected():
	strItemType = 'Image Map'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Image_Map_Name_UnSelected():
	strItemType = 'Image Map'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Image_Map_ID_All():
	strItemType = 'Image Map'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Image_Map_ID_Selected():
	strItemType = 'Image Map'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Image_Map_ID_UnSelected():
	strItemType = 'Image Map'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Iridescence_Material_Count_All():
	strItemType = 'Iridescence Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Iridescence_Material_Count_Selected():
	strItemType = 'Iridescence Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Iridescence_Material_Count_UnSelected():
	strItemType = 'Iridescence Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Iridescence_Material_Name_All():
	strItemType = 'Iridescence Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Iridescence_Material_Name_Selected():
	strItemType = 'Iridescence Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Iridescence_Material_Name_UnSelected():
	strItemType = 'Iridescence Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Iridescence_Material_ID_All():
	strItemType = 'Iridescence Material'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Iridescence_Material_ID_Selected():
	strItemType = 'Iridescence Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Iridescence_Material_ID_UnSelected():
	strItemType = 'Iridescence Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Iridescence_Material_Add_New():
	strItemType = 'material.iridescence'
	lx.eval('shader.create {%s}' % strItemType)
def Lag_Effector_Count_All():
	strItemType = 'Lag Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Lag_Effector_Count_Selected():
	strItemType = 'Lag Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Lag_Effector_Count_UnSelected():
	strItemType = 'Lag Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Lag_Effector_Name_All():
	strItemType = 'Lag Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Lag_Effector_Name_Selected():
	strItemType = 'Lag Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Lag_Effector_Name_UnSelected():
	strItemType = 'Lag Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Lag_Effector_ID_All():
	strItemType = 'Lag Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Lag_Effector_ID_Selected():
	strItemType = 'Lag Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Lag_Effector_ID_UnSelected():
	strItemType = 'Lag Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Lag_Effector_Add_New():
	strItemType = 'deform.lag'
	lx.eval('item.create {%s}' % strItemType)
def Lattice_Effector_Count_All():
	strItemType = 'Lattice Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Lattice_Effector_Count_Selected():
	strItemType = 'Lattice Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Lattice_Effector_Count_UnSelected():
	strItemType = 'Lattice Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Lattice_Effector_Name_All():
	strItemType = 'Lattice Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Lattice_Effector_Name_Selected():
	strItemType = 'Lattice Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Lattice_Effector_Name_UnSelected():
	strItemType = 'Lattice Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Lattice_Effector_ID_All():
	strItemType = 'Lattice Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Lattice_Effector_ID_Selected():
	strItemType = 'Lattice Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Lattice_Effector_ID_UnSelected():
	strItemType = 'Lattice Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Lattice_Effector_Add_New():
	strItemType = 'deform.lattice'
	lx.eval('item.create {%s}' % strItemType)
def Light_Material_Count_All():
	strItemType = 'Light Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Light_Material_Count_Selected():
	strItemType = 'Light Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Light_Material_Count_UnSelected():
	strItemType = 'Light Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Light_Material_Name_All():
	strItemType = 'Light Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Light_Material_Name_Selected():
	strItemType = 'Light Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Light_Material_Name_UnSelected():
	strItemType = 'Light Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Light_Material_ID_All():
	strItemType = 'Light Material'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Light_Material_ID_Selected():
	strItemType = 'Light Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Light_Material_ID_UnSelected():
	strItemType = 'Light Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Light_Material_Add_New():
	strItemType = 'lightMaterial'
	lx.eval('shader.create {%s}' % strItemType)
def Linear_Falloff_Count_All():
	strItemType = 'Linear Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Linear_Falloff_Count_Selected():
	strItemType = 'Linear Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Linear_Falloff_Count_UnSelected():
	strItemType = 'Linear Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Linear_Falloff_Name_All():
	strItemType = 'Linear Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Linear_Falloff_Name_Selected():
	strItemType = 'Linear Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Linear_Falloff_Name_UnSelected():
	strItemType = 'Linear Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Linear_Falloff_ID_All():
	strItemType = 'Linear Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Linear_Falloff_ID_Selected():
	strItemType = 'Linear Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Linear_Falloff_ID_UnSelected():
	strItemType = 'Linear Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Linear_Falloff_Add_New():
	strItemType = 'falloff.linear'
	lx.eval('item.create {%s}' % strItemType)
def Linear_Force_Count_All():
	strItemType = 'Linear Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Linear_Force_Count_Selected():
	strItemType = 'Linear Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Linear_Force_Count_UnSelected():
	strItemType = 'Linear Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Linear_Force_Name_All():
	strItemType = 'Linear Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Linear_Force_Name_Selected():
	strItemType = 'Linear Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Linear_Force_Name_UnSelected():
	strItemType = 'Linear Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Linear_Force_ID_All():
	strItemType = 'Linear Force'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Linear_Force_ID_Selected():
	strItemType = 'Linear Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Linear_Force_ID_UnSelected():
	strItemType = 'Linear Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Linear_Force_Add_New():
	strItemType = 'force.linear'
	lx.eval('item.create {%s}' % strItemType)
def Locator_Count_All():
	strItemType = 'Locator'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Locator_Count_Selected():
	strItemType = 'Locator'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Locator_Count_UnSelected():
	strItemType = 'Locator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Locator_Name_All():
	strItemType = 'Locator'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Locator_Name_Selected():
	strItemType = 'Locator'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Locator_Name_UnSelected():
	strItemType = 'Locator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Locator_ID_All():
	strItemType = 'Locator'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Locator_ID_Selected():
	strItemType = 'Locator'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Locator_ID_UnSelected():
	strItemType = 'Locator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Locator_Add_New():
	strItemType = 'locator'
	lx.eval('item.create {%s}' % strItemType)
def Magnet_Effector_Count_All():
	strItemType = 'Magnet Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Magnet_Effector_Count_Selected():
	strItemType = 'Magnet Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Magnet_Effector_Count_UnSelected():
	strItemType = 'Magnet Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Magnet_Effector_Name_All():
	strItemType = 'Magnet Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Magnet_Effector_Name_Selected():
	strItemType = 'Magnet Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Magnet_Effector_Name_UnSelected():
	strItemType = 'Magnet Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Magnet_Effector_ID_All():
	strItemType = 'Magnet Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Magnet_Effector_ID_Selected():
	strItemType = 'Magnet Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Magnet_Effector_ID_UnSelected():
	strItemType = 'Magnet Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Magnet_Effector_Add_New():
	strItemType = 'deform.magnet'
	lx.eval('item.create {%s}' % strItemType)
def Material_Count_All():
	strItemType = 'Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Material_Count_Selected():
	strItemType = 'Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Material_Count_UnSelected():
	strItemType = 'Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Material_Name_All():
	strItemType = 'Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Material_Name_Selected():
	strItemType = 'Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Material_Name_UnSelected():
	strItemType = 'Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Material_ID_All():
	strItemType = 'Material'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Material_ID_Selected():
	strItemType = 'Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Material_ID_UnSelected():
	strItemType = 'Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Material_Add_New():
	strItemType = 'advancedMaterial'
	lx.eval('shader.create {%s}' % strItemType)
def Mesh_Count_All():
	strItemType = 'Mesh'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Mesh_Count_Selected():
	strItemType = 'Mesh'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Mesh_Count_UnSelected():
	strItemType = 'Mesh'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Mesh_Name_All():
	strItemType = 'Mesh'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Mesh_Name_Selected():
	strItemType = 'Mesh'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Mesh_Name_UnSelected():
	strItemType = 'Mesh'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Mesh_ID_All():
	strItemType = 'Mesh'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Mesh_ID_Selected():
	strItemType = 'Mesh'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Mesh_ID_UnSelected():
	strItemType = 'Mesh'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Mesh_Add_New():
	strItemType = 'mesh'
	lx.eval('item.create {%s}' % strItemType)
def Morph_Influence_Count_All():
	strItemType = 'Morph Influence'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Morph_Influence_Count_Selected():
	strItemType = 'Morph Influence'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Morph_Influence_Count_UnSelected():
	strItemType = 'Morph Influence'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Morph_Influence_Name_All():
	strItemType = 'Morph Influence'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Morph_Influence_Name_Selected():
	strItemType = 'Morph Influence'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Morph_Influence_Name_UnSelected():
	strItemType = 'Morph Influence'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Morph_Influence_ID_All():
	strItemType = 'Morph Influence'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Morph_Influence_ID_Selected():
	strItemType = 'Morph Influence'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Morph_Influence_ID_UnSelected():
	strItemType = 'Morph Influence'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Morph_Influence_Add_New():
	strItemType = 'morphDeform'
	lx.eval('item.create {%s}' % strItemType)
def Newton_Force_Count_All():
	strItemType = 'Newton Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Newton_Force_Count_Selected():
	strItemType = 'Newton Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Newton_Force_Count_UnSelected():
	strItemType = 'Newton Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Newton_Force_Name_All():
	strItemType = 'Newton Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Newton_Force_Name_Selected():
	strItemType = 'Newton Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Newton_Force_Name_UnSelected():
	strItemType = 'Newton Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Newton_Force_ID_All():
	strItemType = 'Newton Force'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Newton_Force_ID_Selected():
	strItemType = 'Newton Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Newton_Force_ID_UnSelected():
	strItemType = 'Newton Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Newton_Force_Add_New():
	strItemType = 'force.newton'
	lx.eval('item.create {%s}' % strItemType)
def Noise_Count_All():
	strItemType = 'Noise'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Noise_Count_Selected():
	strItemType = 'Noise'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Noise_Count_UnSelected():
	strItemType = 'Noise'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Noise_Name_All():
	strItemType = 'Noise'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Noise_Name_Selected():
	strItemType = 'Noise'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Noise_Name_UnSelected():
	strItemType = 'Noise'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Noise_ID_All():
	strItemType = 'Noise'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Noise_ID_Selected():
	strItemType = 'Noise'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Noise_ID_UnSelected():
	strItemType = 'Noise'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Noise_Add_New():
	strItemType = 'noise'
	lx.eval('shader.create {%s}' % strItemType)
def Occlusion_Count_All():
	strItemType = 'Occlusion'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Occlusion_Count_Selected():
	strItemType = 'Occlusion'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Occlusion_Count_UnSelected():
	strItemType = 'Occlusion'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Occlusion_Name_All():
	strItemType = 'Occlusion'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Occlusion_Name_Selected():
	strItemType = 'Occlusion'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Occlusion_Name_UnSelected():
	strItemType = 'Occlusion'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Occlusion_ID_All():
	strItemType = 'Occlusion'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Occlusion_ID_Selected():
	strItemType = 'Occlusion'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Occlusion_ID_UnSelected():
	strItemType = 'Occlusion'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Occlusion_Add_New():
	strItemType = 'occlusion'
	lx.eval('shader.create {%s}' % strItemType)
def Photometric_Light_Count_All():
	strItemType = 'Photometric Light'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Photometric_Light_Count_Selected():
	strItemType = 'Photometric Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Photometric_Light_Count_UnSelected():
	strItemType = 'Photometric Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Photometric_Light_Name_All():
	strItemType = 'Photometric Light'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Photometric_Light_Name_Selected():
	strItemType = 'Photometric Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Photometric_Light_Name_UnSelected():
	strItemType = 'Photometric Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Photometric_Light_ID_All():
	strItemType = 'Photometric Light'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Photometric_Light_ID_Selected():
	strItemType = 'Photometric Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Photometric_Light_ID_UnSelected():
	strItemType = 'Photometric Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Photometric_Light_Add_New():
	strItemType = 'photometryLight'
	lx.eval('item.create {%s}' % strItemType)
def Pin_Count_All():
	strItemType = 'Pin'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Pin_Count_Selected():
	strItemType = 'Pin'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Pin_Count_UnSelected():
	strItemType = 'Pin'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Pin_Name_All():
	strItemType = 'Pin'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Pin_Name_Selected():
	strItemType = 'Pin'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Pin_Name_UnSelected():
	strItemType = 'Pin'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Pin_ID_All():
	strItemType = 'Pin'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Pin_ID_Selected():
	strItemType = 'Pin'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Pin_ID_UnSelected():
	strItemType = 'Pin'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Pin_Add_New():
	strItemType = 'consPin'
	lx.eval('item.create {%s}' % strItemType)
def Point_Count_All():
	strItemType = 'Point'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Point_Count_Selected():
	strItemType = 'Point'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Point_Count_UnSelected():
	strItemType = 'Point'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Point_Name_All():
	strItemType = 'Point'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Point_Name_Selected():
	strItemType = 'Point'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Point_Name_UnSelected():
	strItemType = 'Point'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Point_ID_All():
	strItemType = 'Point'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Point_ID_Selected():
	strItemType = 'Point'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Point_ID_UnSelected():
	strItemType = 'Point'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Point_Add_New():
	strItemType = 'consPoint'
	lx.eval('item.create {%s}' % strItemType)
def Point_Light_Count_All():
	strItemType = 'Point Light'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Point_Light_Count_Selected():
	strItemType = 'Point Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Point_Light_Count_UnSelected():
	strItemType = 'Point Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Point_Light_Name_All():
	strItemType = 'Point Light'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Point_Light_Name_Selected():
	strItemType = 'Point Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Point_Light_Name_UnSelected():
	strItemType = 'Point Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Point_Light_ID_All():
	strItemType = 'Point Light'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Point_Light_ID_Selected():
	strItemType = 'Point Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Point_Light_ID_UnSelected():
	strItemType = 'Point Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Point_Light_Add_New():
	strItemType = 'pointLight'
	lx.eval('item.create {%s}' % strItemType)
def Poisson_Cells_Count_All():
	strItemType = 'Poisson Cells'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Poisson_Cells_Count_Selected():
	strItemType = 'Poisson Cells'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Poisson_Cells_Count_UnSelected():
	strItemType = 'Poisson Cells'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Poisson_Cells_Name_All():
	strItemType = 'Poisson Cells'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Poisson_Cells_Name_Selected():
	strItemType = 'Poisson Cells'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Poisson_Cells_Name_UnSelected():
	strItemType = 'Poisson Cells'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Poisson_Cells_ID_All():
	strItemType = 'Poisson Cells'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Poisson_Cells_ID_Selected():
	strItemType = 'Poisson Cells'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Poisson_Cells_ID_UnSelected():
	strItemType = 'Poisson Cells'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Poisson_Cells_Add_New():
	strItemType = 'val.noise.poisson'
	lx.eval('shader.create {%s}' % strItemType)
def Poly_Count_All(Requires_ItemID):
	strItemType = 'Poly'
	asVariant = 'all'
	return __fn_pyModo_Component_Count(Requires_ItemID,strItemType,asVariant)
def Poly_Count_Selected(Requires_ItemID):
	strItemType = 'Poly'
	asVariant = 'selected'
	return __fn_pyModo_Component_Count(Requires_ItemID,strItemType,asVariant)
def Poly_Count_UnSelected(Requires_ItemID):
	strItemType = 'Poly'
	asVariant = 'unselected'
	return __fn_pyModo_Component_Count(Requires_ItemID,strItemType,asVariant)
def Poly_Index_All(Requires_ItemID):
	strItemType = 'Poly'
	asVariant = 'all'
	return __fn_pyModo_Component_Index(Requires_ItemID,strItemType,asVariant)
def Poly_Index_Selected(Requires_ItemID):
	strItemType = 'Poly'
	asVariant = 'selected'
	return __fn_pyModo_Component_Index(Requires_ItemID,strItemType,asVariant)
def Poly_Index_UnSelected(Requires_ItemID):
	strItemType = 'Poly'
	asVariant = 'unselected'
	return __fn_pyModo_Component_Index(Requires_ItemID,strItemType,asVariant)
def Portal_Count_All():
	strItemType = 'Portal'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Portal_Count_Selected():
	strItemType = 'Portal'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Portal_Count_UnSelected():
	strItemType = 'Portal'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Portal_Name_All():
	strItemType = 'Portal'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Portal_Name_Selected():
	strItemType = 'Portal'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Portal_Name_UnSelected():
	strItemType = 'Portal'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Portal_ID_All():
	strItemType = 'Portal'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Portal_ID_Selected():
	strItemType = 'Portal'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Portal_ID_UnSelected():
	strItemType = 'Portal'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Portal_Add_New():
	strItemType = 'portal'
	lx.eval('item.create {%s}' % strItemType)
def Position_Count_All():
	strItemType = 'Position'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Position_Count_Selected():
	strItemType = 'Position'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Position_Count_UnSelected():
	strItemType = 'Position'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Position_Name_All():
	strItemType = 'Position'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Position_Name_Selected():
	strItemType = 'Position'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Position_Name_UnSelected():
	strItemType = 'Position'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Position_ID_All():
	strItemType = 'Position'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Position_ID_Selected():
	strItemType = 'Position'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Position_ID_UnSelected():
	strItemType = 'Position'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Radial_Falloff_Count_All():
	strItemType = 'Radial Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Radial_Falloff_Count_Selected():
	strItemType = 'Radial Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Radial_Falloff_Count_UnSelected():
	strItemType = 'Radial Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Radial_Falloff_Name_All():
	strItemType = 'Radial Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Radial_Falloff_Name_Selected():
	strItemType = 'Radial Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Radial_Falloff_Name_UnSelected():
	strItemType = 'Radial Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Radial_Falloff_ID_All():
	strItemType = 'Radial Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Radial_Falloff_ID_Selected():
	strItemType = 'Radial Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Radial_Falloff_ID_UnSelected():
	strItemType = 'Radial Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Radial_Falloff_Add_New():
	strItemType = 'falloff.radial'
	lx.eval('item.create {%s}' % strItemType)
def Radial_Force_Count_All():
	strItemType = 'Radial Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Radial_Force_Count_Selected():
	strItemType = 'Radial Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Radial_Force_Count_UnSelected():
	strItemType = 'Radial Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Radial_Force_Name_All():
	strItemType = 'Radial Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Radial_Force_Name_Selected():
	strItemType = 'Radial Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Radial_Force_Name_UnSelected():
	strItemType = 'Radial Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Radial_Force_ID_All():
	strItemType = 'Radial Force'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Radial_Force_ID_Selected():
	strItemType = 'Radial Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Radial_Force_ID_UnSelected():
	strItemType = 'Radial Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Radial_Force_Add_New():
	strItemType = 'force.radial'
	lx.eval('item.create {%s}' % strItemType)
def Render_Count_All():
	strItemType = 'Render'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Render_Count_Selected():
	strItemType = 'Render'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Render_Count_UnSelected():
	strItemType = 'Render'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Render_Name_All():
	strItemType = 'Render'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Render_Name_Selected():
	strItemType = 'Render'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Render_Name_UnSelected():
	strItemType = 'Render'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Render_ID_All():
	strItemType = 'Render'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Render_ID_Selected():
	strItemType = 'Render'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Render_ID_UnSelected():
	strItemType = 'Render'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Render_Output_Count_All():
	strItemType = 'Render Output'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Render_Output_Count_Selected():
	strItemType = 'Render Output'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Render_Output_Count_UnSelected():
	strItemType = 'Render Output'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Render_Output_Name_All():
	strItemType = 'Render Output'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Render_Output_Name_Selected():
	strItemType = 'Render Output'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Render_Output_Name_UnSelected():
	strItemType = 'Render Output'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Render_Output_ID_All():
	strItemType = 'Render Output'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Render_Output_ID_Selected():
	strItemType = 'Render Output'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Render_Output_ID_UnSelected():
	strItemType = 'Render Output'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Render_Output_Add_New():
	strItemType = 'renderOutput'
	lx.eval('item.create {%s}' % strItemType)
def Replicator_Count_All():
	strItemType = 'Replicator'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Replicator_Count_Selected():
	strItemType = 'Replicator'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Replicator_Count_UnSelected():
	strItemType = 'Replicator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Replicator_Name_All():
	strItemType = 'Replicator'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Replicator_Name_Selected():
	strItemType = 'Replicator'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Replicator_Name_UnSelected():
	strItemType = 'Replicator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Replicator_ID_All():
	strItemType = 'Replicator'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Replicator_ID_Selected():
	strItemType = 'Replicator'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Replicator_ID_UnSelected():
	strItemType = 'Replicator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Replicator_Add_New():
	strItemType = 'replicator'
	lx.eval('item.create {%s}' % strItemType)
def Ripples_Count_All():
	strItemType = 'Ripples'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Ripples_Count_Selected():
	strItemType = 'Ripples'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Ripples_Count_UnSelected():
	strItemType = 'Ripples'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Ripples_Name_All():
	strItemType = 'Ripples'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Ripples_Name_Selected():
	strItemType = 'Ripples'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Ripples_Name_UnSelected():
	strItemType = 'Ripples'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Ripples_ID_All():
	strItemType = 'Ripples'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Ripples_ID_Selected():
	strItemType = 'Ripples'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Ripples_ID_UnSelected():
	strItemType = 'Ripples'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Ripples_Add_New():
	strItemType = 'ripples'
	lx.eval('shader.create {%s}' % strItemType)
def Rotation_Count_All():
	strItemType = 'Rotation'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Rotation_Count_Selected():
	strItemType = 'Rotation'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Rotation_Count_UnSelected():
	strItemType = 'Rotation'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Rotation_Name_All():
	strItemType = 'Rotation'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Rotation_Name_Selected():
	strItemType = 'Rotation'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Rotation_Name_UnSelected():
	strItemType = 'Rotation'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Rotation_ID_All():
	strItemType = 'Rotation'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Rotation_ID_Selected():
	strItemType = 'Rotation'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Rotation_ID_UnSelected():
	strItemType = 'Rotation'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def RPC_Texture_Count_All():
	strItemType = 'RPC Texture'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def RPC_Texture_Count_Selected():
	strItemType = 'RPC Texture'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def RPC_Texture_Count_UnSelected():
	strItemType = 'RPC Texture'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def RPC_Texture_Name_All():
	strItemType = 'RPC Texture'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def RPC_Texture_Name_Selected():
	strItemType = 'RPC Texture'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def RPC_Texture_Name_UnSelected():
	strItemType = 'RPC Texture'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def RPC_Texture_ID_All():
	strItemType = 'RPC Texture'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def RPC_Texture_ID_Selected():
	strItemType = 'RPC Texture'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def RPC_Texture_ID_UnSelected():
	strItemType = 'RPC Texture'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def RPC_Texture_Add_New():
	strItemType = 'val.RpcTexture'
	lx.eval('shader.create {%s}' % strItemType)
def RT_Curvature_Count_All():
	strItemType = 'RT Curvature'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def RT_Curvature_Count_Selected():
	strItemType = 'RT Curvature'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def RT_Curvature_Count_UnSelected():
	strItemType = 'RT Curvature'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def RT_Curvature_Name_All():
	strItemType = 'RT Curvature'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def RT_Curvature_Name_Selected():
	strItemType = 'RT Curvature'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def RT_Curvature_Name_UnSelected():
	strItemType = 'RT Curvature'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def RT_Curvature_ID_All():
	strItemType = 'RT Curvature'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def RT_Curvature_ID_Selected():
	strItemType = 'RT Curvature'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def RT_Curvature_ID_UnSelected():
	strItemType = 'RT Curvature'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def RT_Curvature_Add_New():
	strItemType = 'val.RTCurvature'
	lx.eval('shader.create {%s}' % strItemType)
def Scale_Count_All():
	strItemType = 'Scale'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Scale_Count_Selected():
	strItemType = 'Scale'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Scale_Count_UnSelected():
	strItemType = 'Scale'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Scale_Name_All():
	strItemType = 'Scale'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Scale_Name_Selected():
	strItemType = 'Scale'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Scale_Name_UnSelected():
	strItemType = 'Scale'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Scale_ID_All():
	strItemType = 'Scale'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Scale_ID_Selected():
	strItemType = 'Scale'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Scale_ID_UnSelected():
	strItemType = 'Scale'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def BaseShader_Count_All():
	strItemType = 'Shader'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def BaseShader_Count_Selected():
	strItemType = 'Shader'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def BaseShader_Count_UnSelected():
	strItemType = 'Shader'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def BaseShader_Name_All():
	strItemType = 'Shader'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def BaseShader_Name_Selected():
	strItemType = 'Shader'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def BaseShader_Name_UnSelected():
	strItemType = 'Shader'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def BaseShader_ID_All():
	strItemType = 'Shader'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def BaseShader_ID_Selected():
	strItemType = 'Shader'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def BaseShader_ID_UnSelected():
	strItemType = 'Shader'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def BaseShader_Add_New():
	strItemType = 'defaultShader'
	lx.eval('shader.create {%s}' % strItemType)
def Skin_Material_Count_All():
	strItemType = 'Skin Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Skin_Material_Count_Selected():
	strItemType = 'Skin Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Skin_Material_Count_UnSelected():
	strItemType = 'Skin Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Skin_Material_Name_All():
	strItemType = 'Skin Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Skin_Material_Name_Selected():
	strItemType = 'Skin Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Skin_Material_Name_UnSelected():
	strItemType = 'Skin Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Skin_Material_ID_All():
	strItemType = 'Skin Material'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Skin_Material_ID_Selected():
	strItemType = 'Skin Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Skin_Material_ID_UnSelected():
	strItemType = 'Skin Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Skin_Material_Add_New():
	strItemType = 'material.skinMateria'
	lx.eval('shader.create {%s}' % strItemType)
def Slide_Hinge_Count_All():
	strItemType = 'Slide Hinge'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Slide_Hinge_Count_Selected():
	strItemType = 'Slide Hinge'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Slide_Hinge_Count_UnSelected():
	strItemType = 'Slide Hinge'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Slide_Hinge_Name_All():
	strItemType = 'Slide Hinge'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Slide_Hinge_Name_Selected():
	strItemType = 'Slide Hinge'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Slide_Hinge_Name_UnSelected():
	strItemType = 'Slide Hinge'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Slide_Hinge_ID_All():
	strItemType = 'Slide Hinge'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Slide_Hinge_ID_Selected():
	strItemType = 'Slide Hinge'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Slide_Hinge_ID_UnSelected():
	strItemType = 'Slide Hinge'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Slide_Hinge_Add_New():
	strItemType = 'consSlideHinge'
	lx.eval('item.create {%s}' % strItemType)
def Soft_Lag_Count_All():
	strItemType = 'Soft Lag'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Soft_Lag_Count_Selected():
	strItemType = 'Soft Lag'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Soft_Lag_Count_UnSelected():
	strItemType = 'Soft Lag'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Soft_Lag_Name_All():
	strItemType = 'Soft Lag'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Soft_Lag_Name_Selected():
	strItemType = 'Soft Lag'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Soft_Lag_Name_UnSelected():
	strItemType = 'Soft Lag'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Soft_Lag_ID_All():
	strItemType = 'Soft Lag'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Soft_Lag_ID_Selected():
	strItemType = 'Soft Lag'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Soft_Lag_ID_UnSelected():
	strItemType = 'Soft Lag'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Soft_Lag_Add_New():
	strItemType = 'softLag'
	lx.eval('item.create {%s}' % strItemType)
def Spline_Falloff_Count_All():
	strItemType = 'Spline Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Spline_Falloff_Count_Selected():
	strItemType = 'Spline Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Spline_Falloff_Count_UnSelected():
	strItemType = 'Spline Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Spline_Falloff_Name_All():
	strItemType = 'Spline Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Spline_Falloff_Name_Selected():
	strItemType = 'Spline Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Spline_Falloff_Name_UnSelected():
	strItemType = 'Spline Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Spline_Falloff_ID_All():
	strItemType = 'Spline Falloff'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Spline_Falloff_ID_Selected():
	strItemType = 'Spline Falloff'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Spline_Falloff_ID_UnSelected():
	strItemType = 'Spline Falloff'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Spline_Falloff_Add_New():
	strItemType = 'falloff.spline'
	lx.eval('item.create {%s}' % strItemType)
def Spot_Light_Count_All():
	strItemType = 'Spot Light'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Spot_Light_Count_Selected():
	strItemType = 'Spot Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Spot_Light_Count_UnSelected():
	strItemType = 'Spot Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Spot_Light_Name_All():
	strItemType = 'Spot Light'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Spot_Light_Name_Selected():
	strItemType = 'Spot Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Spot_Light_Name_UnSelected():
	strItemType = 'Spot Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Spot_Light_ID_All():
	strItemType = 'Spot Light'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Spot_Light_ID_Selected():
	strItemType = 'Spot Light'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Spot_Light_ID_UnSelected():
	strItemType = 'Spot Light'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Spot_Light_Add_New():
	strItemType = 'spotLight'
	lx.eval('item.create {%s}' % strItemType)
def Spring_Count_All():
	strItemType = 'Spring'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Spring_Count_Selected():
	strItemType = 'Spring'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Spring_Count_UnSelected():
	strItemType = 'Spring'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Spring_Name_All():
	strItemType = 'Spring'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Spring_Name_Selected():
	strItemType = 'Spring'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Spring_Name_UnSelected():
	strItemType = 'Spring'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Spring_ID_All():
	strItemType = 'Spring'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Spring_ID_Selected():
	strItemType = 'Spring'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Spring_ID_UnSelected():
	strItemType = 'Spring'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Spring_Add_New():
	strItemType = 'consSpring'
	lx.eval('item.create {%s}' % strItemType)
def Surface_Generator_Count_All():
	strItemType = 'Surface Generator'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Surface_Generator_Count_Selected():
	strItemType = 'Surface Generator'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Surface_Generator_Count_UnSelected():
	strItemType = 'Surface Generator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Surface_Generator_Name_All():
	strItemType = 'Surface Generator'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Surface_Generator_Name_Selected():
	strItemType = 'Surface Generator'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Surface_Generator_Name_UnSelected():
	strItemType = 'Surface Generator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Surface_Generator_ID_All():
	strItemType = 'Surface Generator'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Surface_Generator_ID_Selected():
	strItemType = 'Surface Generator'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Surface_Generator_ID_UnSelected():
	strItemType = 'Surface Generator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Surface_Generator_Add_New():
	strItemType = 'surfGen'
	lx.eval('shader.create {%s}' % strItemType)
def Texture_Locator_Count_All():
	strItemType = 'Texture Locator'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Texture_Locator_Count_Selected():
	strItemType = 'Texture Locator'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Texture_Locator_Count_UnSelected():
	strItemType = 'Texture Locator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Texture_Locator_Name_All():
	strItemType = 'Texture Locator'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Texture_Locator_Name_Selected():
	strItemType = 'Texture Locator'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Texture_Locator_Name_UnSelected():
	strItemType = 'Texture Locator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Texture_Locator_ID_All():
	strItemType = 'Texture Locator'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Texture_Locator_ID_Selected():
	strItemType = 'Texture Locator'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Texture_Locator_ID_UnSelected():
	strItemType = 'Texture Locator'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Texture_Locator_Add_New():
	strItemType = 'txtrLocator'
	lx.eval('item.create {%s}' % strItemType)
def ThinFilm_Material_Count_All():
	strItemType = 'ThinFilm Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def ThinFilm_Material_Count_Selected():
	strItemType = 'ThinFilm Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def ThinFilm_Material_Count_UnSelected():
	strItemType = 'ThinFilm Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def ThinFilm_Material_Name_All():
	strItemType = 'ThinFilm Material'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def ThinFilm_Material_Name_Selected():
	strItemType = 'ThinFilm Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def ThinFilm_Material_Name_UnSelected():
	strItemType = 'ThinFilm Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def ThinFilm_Material_ID_All():
	strItemType = 'ThinFilm Material'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def ThinFilm_Material_ID_Selected():
	strItemType = 'ThinFilm Material'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def ThinFilm_Material_ID_UnSelected():
	strItemType = 'ThinFilm Material'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def ThinFilm_Material_Add_New():
	strItemType = 'material.thinfilm'
	lx.eval('shader.create {%s}' % strItemType)
def Turbulence_Force_Count_All():
	strItemType = 'Turbulence Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Turbulence_Force_Count_Selected():
	strItemType = 'Turbulence Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Turbulence_Force_Count_UnSelected():
	strItemType = 'Turbulence Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Turbulence_Force_Name_All():
	strItemType = 'Turbulence Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Turbulence_Force_Name_Selected():
	strItemType = 'Turbulence Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Turbulence_Force_Name_UnSelected():
	strItemType = 'Turbulence Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Turbulence_Force_ID_All():
	strItemType = 'Turbulence Force'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Turbulence_Force_ID_Selected():
	strItemType = 'Turbulence Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Turbulence_Force_ID_UnSelected():
	strItemType = 'Turbulence Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Turbulence_Force_Add_New():
	strItemType = 'force.turbulence'
	lx.eval('item.create {%s}' % strItemType)
def Vert_Count_All(Requires_ItemID):
	strItemType = 'Vert'
	asVariant = 'all'
	return __fn_pyModo_Component_Count(Requires_ItemID,strItemType,asVariant)
def Vert_Count_Selected(Requires_ItemID):
	strItemType = 'Vert'
	asVariant = 'selected'
	return __fn_pyModo_Component_Count(Requires_ItemID,strItemType,asVariant)
def Vert_Count_UnSelected(Requires_ItemID):
	strItemType = 'Vert'
	asVariant = 'unselected'
	return __fn_pyModo_Component_Count(Requires_ItemID,strItemType,asVariant)
def Vert_Index_All(Requires_ItemID):
	strItemType = 'Vert'
	asVariant = 'all'
	return __fn_pyModo_Component_Index(Requires_ItemID,strItemType,asVariant)
def Vert_Index_Selected(Requires_ItemID):
	strItemType = 'Vert'
	asVariant = 'selected'
	return __fn_pyModo_Component_Index(Requires_ItemID,strItemType,asVariant)
def Vert_Index_UnSelected(Requires_ItemID):
	strItemType = 'Vert'
	asVariant = 'unselected'
	return __fn_pyModo_Component_Index(Requires_ItemID,strItemType,asVariant)
def Volume_Count_All():
	strItemType = 'Volume'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Volume_Count_Selected():
	strItemType = 'Volume'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Volume_Count_UnSelected():
	strItemType = 'Volume'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Volume_Name_All():
	strItemType = 'Volume'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Volume_Name_Selected():
	strItemType = 'Volume'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Volume_Name_UnSelected():
	strItemType = 'Volume'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Volume_ID_All():
	strItemType = 'Volume'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Volume_ID_Selected():
	strItemType = 'Volume'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Volume_ID_UnSelected():
	strItemType = 'Volume'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Volume_Add_New():
	strItemType = 'volume'
	lx.eval('item.create {%s}' % strItemType)
def Vortex_Effector_Count_All():
	strItemType = 'Vortex Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Vortex_Effector_Count_Selected():
	strItemType = 'Vortex Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Vortex_Effector_Count_UnSelected():
	strItemType = 'Vortex Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Vortex_Effector_Name_All():
	strItemType = 'Vortex Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Vortex_Effector_Name_Selected():
	strItemType = 'Vortex Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Vortex_Effector_Name_UnSelected():
	strItemType = 'Vortex Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Vortex_Effector_ID_All():
	strItemType = 'Vortex Effector'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Vortex_Effector_ID_Selected():
	strItemType = 'Vortex Effector'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Vortex_Effector_ID_UnSelected():
	strItemType = 'Vortex Effector'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Vortex_Effector_Add_New():
	strItemType = 'deform.vortex'
	lx.eval('item.create {%s}' % strItemType)
def Vortex_Force_Count_All():
	strItemType = 'Vortex Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Vortex_Force_Count_Selected():
	strItemType = 'Vortex Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Vortex_Force_Count_UnSelected():
	strItemType = 'Vortex Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Vortex_Force_Name_All():
	strItemType = 'Vortex Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Vortex_Force_Name_Selected():
	strItemType = 'Vortex Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Vortex_Force_Name_UnSelected():
	strItemType = 'Vortex Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Vortex_Force_ID_All():
	strItemType = 'Vortex Force'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Vortex_Force_ID_Selected():
	strItemType = 'Vortex Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Vortex_Force_ID_UnSelected():
	strItemType = 'Vortex Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Vortex_Force_Add_New():
	strItemType = 'force.vortex'
	lx.eval('item.create {%s}' % strItemType)
def Weave_Count_All():
	strItemType = 'Weave'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Weave_Count_Selected():
	strItemType = 'Weave'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Weave_Count_UnSelected():
	strItemType = 'Weave'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Weave_Name_All():
	strItemType = 'Weave'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Weave_Name_Selected():
	strItemType = 'Weave'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Weave_Name_UnSelected():
	strItemType = 'Weave'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Weave_ID_All():
	strItemType = 'Weave'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Weave_ID_Selected():
	strItemType = 'Weave'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Weave_ID_UnSelected():
	strItemType = 'Weave'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Weave_Add_New():
	strItemType = 'weave'
	lx.eval('shader.create {%s}' % strItemType)
def Weight_Container_Count_All():
	strItemType = 'Weight Container'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Weight_Container_Count_Selected():
	strItemType = 'Weight Container'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Weight_Container_Count_UnSelected():
	strItemType = 'Weight Container'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Weight_Container_Name_All():
	strItemType = 'Weight Container'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Weight_Container_Name_Selected():
	strItemType = 'Weight Container'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Weight_Container_Name_UnSelected():
	strItemType = 'Weight Container'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Weight_Container_ID_All():
	strItemType = 'Weight Container'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Weight_Container_ID_Selected():
	strItemType = 'Weight Container'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Weight_Container_ID_UnSelected():
	strItemType = 'Weight Container'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Weight_Container_Add_New():
	strItemType = 'weightContainer'
	lx.eval('item.create {%s}' % strItemType)
def Weight_Map_Texture_Count_All():
	strItemType = 'Weight Map Texture'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Weight_Map_Texture_Count_Selected():
	strItemType = 'Weight Map Texture'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Weight_Map_Texture_Count_UnSelected():
	strItemType = 'Weight Map Texture'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Weight_Map_Texture_Name_All():
	strItemType = 'Weight Map Texture'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Weight_Map_Texture_Name_Selected():
	strItemType = 'Weight Map Texture'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Weight_Map_Texture_Name_UnSelected():
	strItemType = 'Weight Map Texture'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Weight_Map_Texture_ID_All():
	strItemType = 'Weight Map Texture'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Weight_Map_Texture_ID_Selected():
	strItemType = 'Weight Map Texture'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Weight_Map_Texture_ID_UnSelected():
	strItemType = 'Weight Map Texture'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Weight_Map_Texture_Add_New():
	strItemType = 'vmapTexture'
	lx.eval('shader.create {%s}' % strItemType)
def Wind_Force_Count_All():
	strItemType = 'Wind Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Wind_Force_Count_Selected():
	strItemType = 'Wind Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Wind_Force_Count_UnSelected():
	strItemType = 'Wind Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Wind_Force_Name_All():
	strItemType = 'Wind Force'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Wind_Force_Name_Selected():
	strItemType = 'Wind Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Wind_Force_Name_UnSelected():
	strItemType = 'Wind Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Wind_Force_ID_All():
	strItemType = 'Wind Force'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Wind_Force_ID_Selected():
	strItemType = 'Wind Force'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Wind_Force_ID_UnSelected():
	strItemType = 'Wind Force'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Wind_Force_Add_New():
	strItemType = 'force.wind'
	lx.eval('item.create {%s}' % strItemType)
def Wood_Count_All():
	strItemType = 'Wood'
	asVariant = 'all'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Wood_Count_Selected():
	strItemType = 'Wood'
	asVariant = 'selected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Wood_Count_UnSelected():
	strItemType = 'Wood'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Count(strItemType,asVariant)
def Wood_Name_All():
	strItemType = 'Wood'
	asVariant = 'all'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Wood_Name_Selected():
	strItemType = 'Wood'
	asVariant = 'selected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Wood_Name_UnSelected():
	strItemType = 'Wood'
	asVariant = 'unselected'
	return __fn_pyModo_Item_Name(strItemType,asVariant)
def Wood_ID_All():
	strItemType = 'Wood'
	asVariant = 'all'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Wood_ID_Selected():
	strItemType = 'Wood'
	asVariant = 'selected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Wood_ID_UnSelected():
	strItemType = 'Wood'
	asVariant = 'unselected'
	return __fn_pyModo_Item_ID(strItemType,asVariant)
def Wood_Add_New():
	strItemType = 'wood'
	lx.eval('shader.create {%s}' % strItemType)
####################################################
####################################################

def Scene_SaveAs(Requires_FullPath):
	lx.eval('!scene.saveas {%s}' % (Requires_FullPath))

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
	return __fn_pyModo_Scene_Main('name',Requires_SceneIndex)

def Scene_Name_Get_All():
	return __fn_pyModo_Scene_Main('name')

def Scene_Index_Get_All():
	return __fn_pyModo_Scene_Main('index')

def Scene_FilePath(Requires_SceneIndex):
	return __fn_pyModo_Scene_Main('file',Requires_SceneIndex)

def Scene_FilePath_Get_All():
	return __fn_pyModo_Scene_Main('file')

def Scene_Format(Requires_SceneIndex):
	return __fn_pyModo_Scene_Main('format',Requires_SceneIndex)

def Scene_Format_Get_All():
	return __fn_pyModo_Scene_Main('format')

def __fn_pyModo_Scene_Main(varCheck, *args):
	Scene_Check_List = []

	TotalScenes = Scene_Count_All()

	if not args:
		for EachScene in range(0,TotalScenes):
			lx.eval('!scene.set {%s}' % EachScene)
			Scene_Check_List.append(lx.eval('query sceneservice scene.%s ? {%s}' % (varCheck,EachScene)))
	if args:
		EachScene = args
		lx.eval('!scene.set {%s}' % EachScene)
		Scene_Check_List.append(lx.eval('query sceneservice scene.%s ? {%s}' % (varCheck,EachScene)))

	return Scene_Check_List
####################################################
####################################################
#ITEM START


def Item_Get_Name(Requires_ItemID):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		return __fn_pyModo_Scene_ItemName(EachItem)

####################################################
####################################################

def Item_Get_ID(Requires_ItemName):
	if type(Requires_ItemName) is list: TheList = Requires_ItemName
	else:   TheList = str.split(Requires_ItemName,',')
	for EachItem in TheList:
		return __fn_pyModo_Scene_ItemID(EachItem)

####################################################
####################################################

def Item_Set_Name(Requires_ItemID,RequiresNameAsString):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		lx.eval('select.Item item:{%s} mode: set' % EachItem)
		lx.eval('!item.name {%s}' % RequiresNameAsString)
####################################################
####################################################

def Item_Delete(Requires_ItemID):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		lx.eval('select.Item item:{%s} mode: set' % EachItem)
		lx.eval('!item.delete')
####################################################
####################################################

def Item_Duplicate(Requires_ItemID):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		lx.eval('select.Item item:{%s} mode: set' % EachItem)
		lx.eval('!item.duplicate false locator false true')
####################################################
####################################################

def Item_Instance(Requires_ItemID):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		lx.eval('select.Item item:{%s} mode: set' % EachItem)
		lx.eval('!item.duplicate true locator false true')
####################################################
####################################################

def Item_Select(Requires_ItemID):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')

	intTotalMeshes = 0

	for EachItem in TheList:
		if intTotalMeshes == 0:
			lx.eval('select.Item item:{%s} mode: set' % EachItem)
		else: lx.eval('select.subItem item:{%s} mode: add' % EachItem)

		intTotalMeshes +=1
####################################################
####################################################

def Item_DeSelect(Requires_ItemID):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		lx.eval('select.Item item:{%s} mode: remove' % EachItem)
####################################################
####################################################

def Item_Channel_Get_Value(Requires_Channel_Name):
	return __fn_pyModo_Item_Channel_Main(Requires_Channel_Name)
####################################################
####################################################

def Item_Channel_Edit(Requires_ChannelName, Requires_ChannelValue):
	lx.eval('item.channel {%s} {%s}' % (Requires_ChannelName,Requires_ChannelValue))
####################################################
####################################################

def Item_Channel_Get_Names(Requires_ItemID):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	Item_Select (TheList)
	return __fn_pyModo_Item_Channel_Main('chan_name')
####################################################
####################################################

def Scene_Get_Item_Names_All():
	return __fn_pyModo_Scene_ItemList('name')

def Scene_Get_Item_IDs_All():
	return __fn_pyModo_Scene_ItemList('idD')

def Scene_Get_Item_Labels_All():
	return __fn_pyModo_Scene_ItemList('typeLabel')

def Scene_Get_Item_Types_All():
	return __fn_pyModo_Scene_ItemList('type')

def __fn_pyModo_Scene_ItemList(ItemCheck):

	SceneItems = lx.Eval('query sceneservice item.N ? ')

	ItemCheckList = []

	for EachItem in range(SceneItems):
		if ItemCheck == 'name':
			retVal = lx.eval('query sceneservice item.name ? {%s}' % EachItem)
		if ItemCheck == 'ID':
			retVal =  lx.eval('query sceneservice item.id ? {%s}'  % EachItem)
		if ItemCheck == 'typeLabel':
			retVal = lx.eval('query sceneservice item.typeLabel ? {%s}'  % EachItem)
		if ItemCheck == 'type':
			retVal = lx.eval('query sceneservice item.type ? {%s}'  % EachItem)

		ItemCheckList.Append (retVal)

	return ItemCheckList
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

####################################################
####################################################
#MODO START

def Modo_Log(RequiresVariableNameHere):
	lx.out (RequiresVariableNameHere)
####################################################
####################################################

def Modo_UserMessage_Info(strMsgTitle, strMsgToUser):
	return __fn_pyModo_MsgBox('info',strMsgTitle,strMsgToUser)
####################################################
####################################################

def Modo_UserMessage_OkCancel(strMsgTitle, strMsgToUser):
	return __fn_pyModo_MsgBox('OkCancel',strMsgTitle,strMsgToUser)
####################################################
####################################################

def Modo_UserMessage_YesNo(strMsgTitle, strMsgToUser):
	return __fn_pyModo_MsgBox('YesNo',strMsgTitle,strMsgToUser)
####################################################
####################################################

def Vert_Select(Requires_Vert_Index):
	Layer_Index = lx.eval('query layerservice layer.index ? current')
	lx.eval('select.type vertex')
	lx.eval('select.element layer:{%s} type:vertex mode:add index:{%s}' % (Layer_Index, Requires_Vert_Index))

def Vert_DeSelect(Requires_Vert_Index):
	Layer_Index = lx.eval('query layerservice layer.index ? current')
	lx.eval('select.type vertex')
	lx.eval('select.element layer:{%s} type:vertex mode:remove index:{%s}' % (Layer_Index, Requires_Vert_Index))

def Vert_Delete(): lx.eval('delete')

def Vert_Copy(): lx.eval('copy')

def Vert_Paste(): lx.eval('paste')

def Vert_Invert_Selection(): lx.eval('select.invert')

def Edge_Select(Requires_Edge_Index):
	Layer_Index = lx.eval('query layerservice layer.index ? current')
	lx.eval('select.type edge')
	EdgeIndex = Requires_Edge_Index[1:-1]
	EdgeIndex = EdgeIndex.split(',')
	FirstEdgeIndex = EdgeIndex[0]
	LastEdgeIndex = EdgeIndex[1]
	lx.eval('select.element layer:{%s} type:edge mode:add index:{%s} index2:{%s}' % (Layer_Index, FirstEdgeIndex, LastEdgeIndex))

def Edge_DeSelect(Requires_Edge_Index):
	Layer_Index = lx.eval('query layerservice layer.index ? current')
	lx.eval('select.type edge')
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

####################################################
####################################################

def Modo_Convert_To_Verts(): lx.eval('select.convert vertex')

def Modo_Convert_To_Edges(): lx.eval('select.convert edge')

def Modo_Convert_To_Polygons(): lx.eval('select.convert polygon')

def Vert_Mode_Set(): lx.eval('select.type vertex')

def Edge_Mode_Set(): lx.eval('select.type edge')

def Poly_Mode_Set(): lx.eval('select.type polygon')

def Vert_DeSelect_All(): lx.eval('select.drop vertex')

def Edge_DeSelect_All(): lx.eval('select.drop edge')

def Poly_DeSelect_All(): lx.eval('select.drop polygon')

def Center_DeSelect(): lx.eval('select.drop center')

def Pivot_DeSelect(): lx.eval('select.drop pivot')

def Item_DeSelect(): lx.eval('select.drop item')
####################################################
####################################################

def Vert_WorldPos_X_(Requires_ItemID):
	V_Wpos_X_List = []
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		V_Indx_List = Vert_Index_Selected(EachItem)
		if not V_Indx_List: V_Indx_List = Vert_Index_All(EachItem)

		for eachV_Indx in V_Indx_List:
			V_Wpos_X =  lx.eval('query layerservice vert.wpos ? {%s}' % eachV_Indx)[0]
			V_Wpos_X_List.append (V_Wpos_X)
	return V_Wpos_X_List

def Vert_WorldPos_Y_(Requires_ItemID):
	V_Wpos_Y_List = []
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		V_Indx_List = Vert_Index_Selected(EachItem)
		if not V_Indx_List: V_Indx_List = Vert_Index_All(EachItem)

		for eachV_Indx in V_Indx_List:
			V_Wpos_Y =  lx.eval('query layerservice vert.wpos ? {%s}' % eachV_Indx)[1]
			V_Wpos_Y_List.append (V_Wpos_Y)
	return V_Wpos_Y_List

def Vert_WorldPos_Z_(Requires_ItemID):
	V_Wpos_Z_List = []
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		V_Indx_List = Vert_Index_Selected(EachItem)
		if not V_Indx_List: V_Indx_List = Vert_Index_All(EachItem)

		for eachV_Indx in V_Indx_List:
			V_Wpos_Z =  lx.eval('query layerservice vert.wpos ? {%s}' % eachV_Indx)[2]
			V_Wpos_Z_List.append (V_Wpos_Z)
	return V_Wpos_Z_List
####################################################
####################################################

def Vert_Average_Position_X_Get(Requires_ItemID):
	return __fn_pyModo_Vert_Average_Position_Get(Requires_ItemID,'X')

def Vert_Average_Position_Y_Get(Requires_ItemID):
	return __fn_pyModo_Vert_Average_Position_Get(Requires_ItemID,'Y')

def Vert_Average_Position_Z_Get(Requires_ItemID):
	return __fn_pyModo_Vert_Average_Position_Get(Requires_ItemID,'Z')

def __fn_pyModo_Vert_Average_Position_Get(Requires_ItemID,Enter_X_Y_Z_or_ALL):
	if not __fn_pyModo_Check_if_String(Enter_X_Y_Z_or_ALL): Enter_X_Y_Z_or_ALL = str(Enter_X_Y_Z_or_ALL)
	AXIS_mod = Enter_X_Y_Z_or_ALL.upper()

	AveXVertPos = 0#
	AveYVertPos = 0#
	AveZVertPos = 0#

	xVerts = []
	yVerts = []
	zVerts = []
	AvgPos_XYZ = []

	#convert selection to verts
	strSelectionMode = Modo_Component_Mode_Get()
	Modo_Convert_To_Verts()
	Vert_Mode_Set()

	VertList = Vert_Index_Selected(Requires_ItemID)

	if not VertList: VertList = Vert_Index_All(Requires_ItemID)

	for EachVert in VertList:

		xVertPos =  lx.eval('query layerservice vert.wpos ? {%s}' % EachVert)[0]
		xVerts.Append (xVertPos)

		yVertPos =  lx.eval('query layerservice vert.wpos ? {%s}' % EachVert)[1]
		yVerts.Append (yVertPos)

		zVertPos =  lx.eval('query layerservice vert.wpos ? {%s}' % EachVert)[2]
		zVerts.Append (zVertPos)

	AveXVertPos = sum(xVerts) / len(xVerts)
	AveYVertPos = sum(yVerts) / len(yVerts)
	AveZVertPos = sum(zVerts) / len(zVerts)

	lx.eval('select.type {%s}' % strSelectionMode)

	if AXIS_mod == 'X': return AveXVertPos
	if AXIS_mod == 'Y': return AveYVertPos
	if AXIS_mod == 'Z': return AveZVertPos

	if AXIS_mod == 'ALL':
		AvgPos_XYZ.Append (AveXVertPos)
		AvgPos_XYZ.Append (AveYVertPos)
		AvgPos_XYZ.Append (AveZVertPos)
		return AvgPos_XYZ
####################################################
####################################################

def SelectionSet_AddTo(RequiresName):
	if not __fn_pyModo_Check_if_String(RequiresName): RequiresName = str(RequiresName)
	try: lx.eval('select.editSet {%s} add' % RequiresName )
	except: pass

def SelectionSet_RemoveFrom(RequiresName):
	if not __fn_pyModo_Check_if_String(RequiresName): RequiresName = str(RequiresName)
	try: lx.eval('select.editSet {%s} remove' % RequiresName )
	except: pass

def SelectionSet_Select(RequiresName):
	if not __fn_pyModo_Check_if_String(RequiresName): RequiresName = str(RequiresName)
	try: lx.eval('!select.useSet {%s} select' % RequiresName )
	except: pass

def SelectionSet_DeSelect(RequiresName):
	if not __fn_pyModo_Check_if_String(RequiresName): RequiresName = str(RequiresName)
	try: lx.eval('!select.useSet {%s} deselect' % RequiresName )
	except: pass

def SelectionSet_Delete(RequiresName):
	if not __fn_pyModo_Check_if_String(RequiresName): RequiresName = str(RequiresName)
	try: lx.eval('!select.deleteSet {%s}' % RequiresName )
	except: pass

def __fn_pyModo_Check_if_String(RequiresName):
	return isinstance(RequiresName, str)
####################################################
####################################################

def Item_Locking_Set_On(Requires_ItemID):
	__fn_pyModo_Item_Lock_State(Requires_ItemID,1)

def Item_Locking_Set_Off(Requires_ItemID):
	__fn_pyModo_Item_Lock_State(Requires_ItemID,0)

def __fn_pyModo_Item_Lock_State(Requires_ItemID,blnState):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		Item_Select (EachItem)
		lx.eval('item.channel lock {%s}' % blnState)

def Item_Visibility_Set_On(Requires_ItemID):
	__fn_pyModo_Item_Visibility_State(Requires_ItemID,1)

def Item_Visibility_Set_Off(Requires_ItemID):
	__fn_pyModo_Item_Visibility_State(Requires_ItemID,0)

def __fn_pyModo_Item_Visibility_State(Requires_ItemID,blnState):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		lx.eval('layer.setVisibility {%s} {%s}' % (EachItem,blnState))

def Vert_Locking_Set_On(Requires_ItemID):
	__fn_pyModo_Vert_Lock_State(Requires_ItemID,1)

def Vert_Locking_Set_Off(Requires_ItemID):
	__fn_pyModo_Vert_Lock_State(Requires_ItemID,0)

def __fn_pyModo_Vert_Lock_State(Requires_ItemID,blnState):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')

	if blnState == 1: SelSetName = 'pyModoSS_VertLocking_Add'
	if blnState == 0: SelSetName = 'pyModoSS_VertLocking_Remove'

	SelectionSet_AddTo (SelSetName)

	for EachItem in TheList:
		Item_Select (EachItem)
		Vert_Mode_Set()
		SelectionSet_Select (SelSetName)
		if blnState == 1: lx.eval('lock.sel')
		if blnState == 0: lx.eval('unlock')
		SelectionSet_Delete (SelSetName)
####################################################
####################################################

def Modo_Transform_Scale(Requires_ItemID, SclX, SclY, SclZ):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		Item_Select (EachItem)
		lx.eval('transform.channel scl.X {%s}' % SclX)
		lx.eval('transform.channel scl.Y {%s}' % SclY)
		lx.eval('transform.channel scl.Z {%s}' % SclZ)

def Modo_Transform_Rotate(Requires_ItemID, RotX, RotY, RotZ):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		Item_Select (EachItem)
		lx.eval('transform.channel rot.X {%s}' % RotX)
		lx.eval('transform.channel rot.Y {%s}' % RotY)
		lx.eval('transform.channel rot.Z {%s}' % RotZ)

def Modo_Transform_Move(Requires_ItemID, PosX, PosY, PosZ):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		Item_Select (EachItem)
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
	ItemScaleID = Item_Scale_Get_ID(Requires_From_ID)

	for eachScl_ID in ItemScaleID:
		Item_Select (eachScl_ID)
	SclX_Val = round(float(Item_Channel_Get_Value('scl.X')),12)
	SclY_Val = round(float(Item_Channel_Get_Value('scl.Y')),12)
	SclZ_Val = round(float(Item_Channel_Get_Value('scl.Z')),12)

	NewSize_X = SclX_Val * SizeX_ratio
	NewSize_Y = SclY_Val * SizeY_ratio
	NewSize_Z = SclZ_Val * SizeZ_ratio

	Item_Select(Requires_From_ID)

	if AXIS_mod == 'X': Modo_Transform_Channel_Edit(eachScl_ID,'scl.X',NewSize_X)
	if AXIS_mod == 'Y': Modo_Transform_Channel_Edit(eachScl_ID,'scl.Y',NewSize_Y)
	if AXIS_mod == 'Z': Modo_Transform_Channel_Edit(eachScl_ID,'scl.Z',NewSize_Z)

	if AXIS_mod == 'ALL':
		Modo_Transform_Channel_Edit(eachScl_ID,'scl.X',NewSize_X)
		Modo_Transform_Channel_Edit(eachScl_ID,'scl.Y',NewSize_Y)
		Modo_Transform_Channel_Edit(eachScl_ID,'scl.Z',NewSize_Z)

def Modo_Transform_Channel_Edit(Requires_Channel_ID, Requires_Channel_Name, Requires_NewValue):
	lx.eval('select.channel {%s:%s} set ' % (Requires_Channel_ID,Requires_Channel_Name))
	lx.eval('channel.value {%s} channel:{%s:%s}' % (Requires_NewValue,Requires_Channel_ID,Requires_Channel_Name))

def Item_Scale_Get_ID(Requires_ItemID):
	Scale_ID_List = []
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		SclID = lx.eval('query sceneservice item.xfrmScl ? {%s}' % EachItem)
		Scale_ID_List.append (SclID)
	return Scale_ID_List

def Item_Rotate_Get_ID(Requires_ItemID):
	Rotate_ID_List = []
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		RotID = lx.eval('query sceneservice item.xfrmRot ? {%s}' % EachItem)
		Rotate_ID_List.append (RotID)
	return Rotate_ID_List

def Item_Position_Get_ID(Requires_ItemID):
	Position_ID_List = []
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		PosID = lx.eval('query sceneservice item.xfrmPos ? {%s}' % EachItem)
		Position_ID_List.append (PosID)
	return Position_ID_List

def Item_Add_Scale_Channel(Requires_ItemID):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		lx.eval('transform.add scl {%s} adv:1' % EachItem)

def Item_Add_Rotate_Channel(Requires_ItemID):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		lx.eval('transform.add rot {%s} adv:1' % EachItem)

def Item_Add_Move_Channel(Requires_ItemID):
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		lx.eval('transform.add pos {%s} adv:1' % EachItem)
####################################################
####################################################

def Shader_Effect_Set(Requires_ItemID, Requires_EffectName):
	if not __fn_pyModo_Check_if_String(Requires_EffectName): Requires_EffectName = str(Requires_EffectName)
	EffectName = Requires_EffectName.lower()

	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:
		Item_Select (EachItem)
		lx.eval('shader.setEffect {%s}' % EffectName)
####################################################
####################################################

def Item_ReSizeX_MaintainAspect(Requires_ItemID, EnterNewSize):
	__fn_pyModo_Item_ReSize_Main(Requires_ItemID, EnterNewSize,'X',1)

def Item_ReSizeY_MaintainAspect(Requires_ItemID, EnterNewSize):
	__fn_pyModo_Item_ReSize_Main(Requires_ItemID, EnterNewSize,'Y',1)

def Item_ReSizeZ_MaintainAspect(Requires_ItemID, EnterNewSize):
	__fn_pyModo_Item_ReSize_Main(Requires_ItemID, EnterNewSize, 'Z',1)

def Item_ReSize(Requires_ItemID, EnterNewSize, Enter_X_Y_Z_or_ALL):
	__fn_pyModo_Item_ReSize_Main(Requires_ItemID, EnterNewSize, Enter_X_Y_Z_or_ALL,0)

def __fn_pyModo_Item_ReSize_Main(Requires_ItemID, EnterNewSize, Enter_X_Y_Z_or_ALL, blnAspectRatio):
	if not __fn_pyModo_Check_if_String(Enter_X_Y_Z_or_ALL): Enter_X_Y_Z_or_ALL = str(Enter_X_Y_Z_or_ALL)
	AXIS_mod = Enter_X_Y_Z_or_ALL.upper()

	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:

		Item_Select (EachItem)

		ItemDimX = Mesh_Dimension_X_(EachItem)
		ItemDimY = Mesh_Dimension_Y_(EachItem)
		ItemDimZ = Mesh_Dimension_Z_(EachItem)

		#check compare size difference

		SizeX_ratio = EnterNewSize / ItemDimX
		SizeY_ratio = EnterNewSize / ItemDimY
		SizeZ_ratio = EnterNewSize / ItemDimZ

		#Get the scale channel values
		ItemScaleID = Item_Scale_Get_ID(EachItem)

		for eachScl_ID in ItemScaleID:

			if eachScl_ID == None:
				Item_Add_Scale_Channel (EachItem)
				eachScl_ID = Item_Scale_Get_ID(EachItem)[0]

		Item_Select (eachScl_ID)

		SclX_Val = round(float(Item_Channel_Get_Value('scl.X')),12)
		SclY_Val = round(float(Item_Channel_Get_Value('scl.Y')),12)
		SclZ_Val = round(float(Item_Channel_Get_Value('scl.Z')),12)

		if blnAspectRatio == 0:
                
			NewSize_X = SclX_Val * SizeX_ratio
			NewSize_Y = SclY_Val * SizeY_ratio
			NewSize_Z = SclZ_Val * SizeZ_ratio

			if AXIS_mod == 'X': Modo_Transform_Channel_Edit(eachScl_ID,'scl.X',NewSize_X)
			if AXIS_mod == 'Y': Modo_Transform_Channel_Edit(eachScl_ID,'scl.Y',NewSize_Y)
			if AXIS_mod == 'Z': Modo_Transform_Channel_Edit(eachScl_ID,'scl.Z',NewSize_Z)

			if AXIS_mod == 'ALL':
				Modo_Transform_Channel_Edit(eachScl_ID,'scl.X',NewSize_X)
				Modo_Transform_Channel_Edit(eachScl_ID,'scl.Y',NewSize_Y)
				Modo_Transform_Channel_Edit(eachScl_ID,'scl.Z',NewSize_Z)

		if blnAspectRatio == 1:
               
			if AXIS_mod == 'X':
				NewSize_X = SclX_Val * SizeX_ratio
				NewSize_Y = SclY_Val * SizeX_ratio
				NewSize_Z = SclZ_Val * SizeX_ratio
				Modo_Transform_Channel_Edit(eachScl_ID,'scl.X',NewSize_X)
				Modo_Transform_Channel_Edit(eachScl_ID,'scl.Y',NewSize_Y)
				Modo_Transform_Channel_Edit(eachScl_ID,'scl.Z',NewSize_Z)
			if AXIS_mod == 'Y':
				NewSize_X = SclX_Val * SizeY_ratio
				NewSize_Y = SclY_Val * SizeY_ratio
				NewSize_Z = SclZ_Val * SizeY_ratio
				Modo_Transform_Channel_Edit(eachScl_ID,'scl.X',NewSize_X)
				Modo_Transform_Channel_Edit(eachScl_ID,'scl.Y',NewSize_Y)
				Modo_Transform_Channel_Edit(eachScl_ID,'scl.Z',NewSize_Z)
			if AXIS_mod == 'Z':
				NewSize_X = SclX_Val * SizeZ_ratio
				NewSize_Y = SclY_Val * SizeZ_ratio
				NewSize_Z = SclZ_Val * SizeZ_ratio
				Modo_Transform_Channel_Edit(eachScl_ID,'scl.X',NewSize_X)
				Modo_Transform_Channel_Edit(eachScl_ID,'scl.Y',NewSize_Y)
				Modo_Transform_Channel_Edit(eachScl_ID,'scl.Z',NewSize_Z)
####################################################
####################################################

def Modo_UserDataEntry_asFloat(UserInstructions_asString):
	return __fn_pyModo_UserDataEntry_Main(UserInstructions_asString,'float')

def Modo_UserDataEntry_asInteger(UserInstructions_asString):
	return __fn_pyModo_UserDataEntry_Main(UserInstructions_asString,'integer')

def Modo_UserDataEntry_asString(UserInstructions_asString):
	return __fn_pyModo_UserDataEntry_Main(UserInstructions_asString,'string')

def __fn_pyModo_UserDataEntry_Main(strUserInstructions,DataType):
	try:
		if not lx.eval('query scriptsysservice userValue.isDefined ? UserDataEntry'):
			lx.eval('!user.defNew UserDataEntry type:%s life:momentary' % DataType)
		lx.eval('!user.def UserDataEntry username {%s}' % strUserInstructions)
		lx.eval('?user.value UserDataEntry')

		UserVal = lx.eval('user.value UserDataEntry ?')

		return UserVal

	except:
		sys.exit()
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

def Mesh_Dimension_X_(Requires_ItemID): return  __fn_pyModo_Mesh_Dimension(Requires_ItemID,'X')

def Mesh_Dimension_Y_(Requires_ItemID): return  __fn_pyModo_Mesh_Dimension(Requires_ItemID,'Y')

def Mesh_Dimension_Z_(Requires_ItemID): return  __fn_pyModo_Mesh_Dimension(Requires_ItemID,'Z')

def __fn_pyModo_Mesh_Dimension(Requires_ItemID,strAxis):
	strSelectionMode = Modo_Component_Mode_Get()
	Modo_Convert_To_Verts()

	int_Rounder = 25
	#get the dimensions of the mesh
	dbl_X_hi = max(Vert_WorldPos_X_(Requires_ItemID))
	dbl_X_lo = min(Vert_WorldPos_X_(Requires_ItemID))
	dbl_Y_hi = max(Vert_WorldPos_Y_(Requires_ItemID))
	dbl_Y_lo = min(Vert_WorldPos_Y_(Requires_ItemID))
	dbl_Z_hi = max(Vert_WorldPos_Z_(Requires_ItemID))
	dbl_Z_lo = min(Vert_WorldPos_Z_(Requires_ItemID))

	dbl_X_Dimension = round(dbl_X_hi - dbl_X_lo, int_Rounder)
	dbl_Y_Dimension = round(dbl_Y_hi - dbl_Y_lo, int_Rounder)
	dbl_Z_Dimension = round(dbl_Z_hi - dbl_Z_lo, int_Rounder)

	lx.eval('select.type {%s}' % strSelectionMode)

	if strAxis == 'X': return dbl_X_Dimension
	if strAxis == 'Y': return dbl_Y_Dimension
	if strAxis == 'Z': return dbl_Z_Dimension


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
	file_FullPath = open(FullFilePath,'a')
	if type(Requires_DataList) is list: TheList = Requires_DataList
	else: TheList = str.split(Requires_DataList,',')
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
	Curve_Select (Requires_ItemID)
	Total_CurveCount = Poly_Count_Selected(Requires_ItemID)
	Curve_DeSelect (Requires_ItemID)
	return Total_CurveCount

def Curve_Select(Requires_ItemID):
	Item_Select (Requires_ItemID)
	lx.eval('select.polygon add type curve 3')

def Curve_DeSelect(Requires_ItemID):
	Item_Select (Requires_ItemID)
	lx.eval('select.polygon remove type curve 3')

def Curve_Get_Length(Requires_ItemID):
	CurveLengthList = []
	CurveLength = 0.0
	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')

	for EachItem in TheList:
		if Poly_Count_All(EachItem) > 0:
			Item_Select (EachItem)
			lx.eval('select.polygon add type curve 3')
			PolyCurves = Poly_Index_Selected(EachItem)
			for EachCurve in PolyCurves:
				Poly_DeSelect_All()
				Poly_Mode_Set()
				Poly_Select (EachCurve)
				Modo_Convert_To_Edges()
				CurveEdges = lx.evalN('query layerservice edges ? selected')
				CurveLength = 0.0
				for EachEdge in CurveEdges:
					EdgeIndex =  lx.eval('query layerservice edge.index ? {%s}' % EachEdge)
					CurveLength += lx.eval('query layerservice edge.length ? {%s}' % EdgeIndex)

				CurveLengthList.append (CurveLength)

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
	s.select('scene.index', 'current') #select current scene

	s.select('selection', 'all')
	selitems = s.queryN('selection')

	for item in selitems:
		s.select('item.id', item)
		item_channelN = s.query('channel.N')

		for channel in range(item_channelN):
			s.select('channel.index', str(channel))
			chan_name  = s.query('channel.name')

			if chan_name == Channel:
				chan_value = s.query('channel.value')

			#chan_type  = s.query('channel.type')

			chName_List.append (chan_name)
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

def __fn_pyModo_Component_Count(Requires_ItemID,strItemType,asVariant):

	V_TOT_ALL = 0
	V_TOT_SEL = 0
	V_TOT_UNS = 0
	E_TOT_ALL = 0
	E_TOT_SEL = 0
	E_TOT_UNS = 0
	P_TOT_ALL = 0
	P_TOT_SEL = 0
	P_TOT_UNS = 0

	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')
	for EachItem in TheList:

		lx.eval('select.Item item:{%s} mode: set' % EachItem)
		lx.eval('query layerservice layer.name ? current')

		if strItemType == 'Vert':
			lx.eval('select.type vertex')
			VertCount_All = lx.eval('query layerservice vert.N ? all')
			V_TOT_ALL += VertCount_All
			VertCount_Selected = lx.eval('query layerservice vert.N ? selected')
			V_TOT_SEL += VertCount_Selected
			VertCount_UnSelected = VertCount_All - VertCount_Selected
			V_TOT_UNS += VertCount_UnSelected

		if strItemType == 'Edge':
			lx.eval('select.type edge')
			EdgeCount_All = lx.eval('query layerservice edge.N ? all')
			E_TOT_ALL += EdgeCount_All
			EdgeCount_Selected = lx.eval('query layerservice edge.N ? selected')
			E_TOT_SEL += EdgeCount_Selected
			EdgeCount_UnSelected = EdgeCount_All - EdgeCount_Selected
			E_TOT_UNS += EdgeCount_UnSelected

		if strItemType == 'Poly':
			lx.eval('select.type polygon')
			PolyCount_All = lx.eval('query layerservice poly.N ? all')
			P_TOT_ALL += PolyCount_All
			PolyCount_Selected = lx.eval('query layerservice poly.N ? selected')
			P_TOT_SEL += PolyCount_Selected
			PolyCount_UnSelected = PolyCount_All - PolyCount_Selected
			P_TOT_UNS += PolyCount_UnSelected

	if strItemType == 'Vert':
		if asVariant =='all':
			return V_TOT_ALL
		elif asVariant =='selected':
			return V_TOT_SEL
		elif asVariant =='unselected':
			return V_TOT_UNS
	if strItemType == 'Edge':
		if asVariant =='all':
			return E_TOT_ALL
		elif asVariant =='selected':
			return E_TOT_SEL
		elif asVariant =='unselected':
			return E_TOT_UNS
	if strItemType == 'Poly':
		if asVariant =='all':
			return P_TOT_ALL
		elif asVariant =='selected':
			return P_TOT_SEL
		elif asVariant =='unselected':
			return P_TOT_UNS
####################################################
####################################################

def __fn_pyModo_Component_Index(Requires_ItemID,strItemType,asVariant):

	V_TOT_ALL_LIST = []
	V_TOT_SEL_LIST = []
	V_TOT_UNS_LIST = []
	E_TOT_ALL_LIST = []
	E_TOT_SEL_LIST = []
	E_TOT_UNS_LIST = []
	P_TOT_ALL_LIST = []
	P_TOT_SEL_LIST = []
	P_TOT_UNS_LIST = []

	if type(Requires_ItemID) is list: TheList = Requires_ItemID
	else:   TheList = str.split(Requires_ItemID,',')

	if asVariant =='unselected':
		lx.eval('select.invert')
               
	for EachItem in TheList:

		lx.eval('select.Item item:{%s} mode: set' % EachItem)
		lx.eval('query layerservice layer.name ? current')

		if strItemType == 'Vert':
			lx.eval('select.type vertex')
			if asVariant =='all':
				VertCount_All = lx.evalN('query layerservice verts ? all')
				for EachVert in VertCount_All:
					EachVertIndex =  lx.eval('query layerservice vert.index ? {%s}' % EachVert)
					V_TOT_ALL_LIST.append (EachVertIndex)

			elif asVariant =='selected':
				VertCount_Selected = lx.evalN('query layerservice verts ? selected')
				for EachVert in VertCount_Selected:
					EachVertIndex =  lx.eval('query layerservice vert.index ? {%s}' % EachVert)
					V_TOT_SEL_LIST.append (EachVertIndex)

			elif asVariant =='unselected':
				VertCount_UnSelected = lx.evalN('query layerservice verts ? selected')
				for EachVert in VertCount_UnSelected:
					EachVertIndex =  lx.eval('query layerservice vert.index ? {%s}' % EachVert)
					V_TOT_UNS_LIST.append (EachVertIndex)

		if strItemType == 'Edge':
			lx.eval('select.type edge')
			if asVariant =='all':
				EdgeCount_All = lx.evalN('query layerservice edges ? all')
				for EachEdge in EdgeCount_All:
					EachEdgeIndex =  lx.eval('query layerservice edge.index ? {%s}' % EachEdge)
					E_TOT_ALL_LIST.append (EachEdgeIndex)

			elif asVariant =='selected':
				EdgeCount_Selected = lx.evalN('query layerservice edges ? selected')
				for EachEdge in EdgeCount_Selected:
					EachEdgeIndex =  lx.eval('query layerservice edge.index ? {%s}' % EachEdge)
					E_TOT_SEL_LIST.append (EachEdgeIndex)

			elif asVariant =='unselected':
				EdgeCount_UnSelected = lx.evalN('query layerservice edges ? selected')
				for EachEdge in EdgeCount_UnSelected:
					EachEdgeIndex =  lx.eval('query layerservice edge.index ? {%s}' % EachEdge)
					E_TOT_UNS_LIST.append (EachEdgeIndex)

		if strItemType == 'Poly':
			lx.eval('select.type polygon')
			if asVariant =='all':
				PolyCount_All = lx.evalN('query layerservice polys ? all')
				for EachPoly in PolyCount_All:
					EachPolyIndex =  lx.eval('query layerservice poly.index ? {%s}' % EachPoly)
					P_TOT_ALL_LIST.append (EachPolyIndex)

			elif asVariant =='selected':
				PolyCount_Selected = lx.evalN('query layerservice polys ? selected')
				for EachPoly in PolyCount_Selected:
					EachPolyIndex =  lx.eval('query layerservice poly.index ? {%s}' % EachPoly)
					P_TOT_SEL_LIST.append (EachPolyIndex)

			elif asVariant =='unselected':
				PolyCount_UnSelected = lx.evalN('query layerservice polys ? selected')
				for EachPoly in PolyCount_UnSelected:
					EachPolyIndex =  lx.eval('query layerservice poly.index ? {%s}' % EachPoly)
					P_TOT_UNS_LIST.append (EachPolyIndex)


	if strItemType == 'Vert':
		if asVariant =='all':
			return V_TOT_ALL_LIST
		elif asVariant =='selected':
			return V_TOT_SEL_LIST
		elif asVariant =='unselected':
			return V_TOT_UNS_LIST
	if strItemType == 'Edge':
		if asVariant =='all':
			return E_TOT_ALL_LIST
		elif asVariant =='selected':
			return E_TOT_SEL_LIST
		elif asVariant =='unselected':
			return E_TOT_UNS_LIST
	if strItemType == 'Poly':
		if asVariant =='all':
			return P_TOT_ALL_LIST
		elif asVariant =='selected':
			return P_TOT_SEL_LIST
		elif asVariant =='unselected':
			return P_TOT_UNS_LIST
####################################################
####################################################

def __fn_pyModo_MsgBox(strMsgType,strMsgTitle,strMsgToUser):
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

def __fn_pyModo_Item_Count(strItemType,asVariant):

	intTotal = 0
	blnTrue = 1
	blnFalse = 0

	SceneItemCount = __fn_pyModo_Scene_Items()

	for EachItem in range(0,SceneItemCount):

		ItemType = __fn_pyModo_Scene_ItemType(EachItem)
		ItemID =  __fn_pyModo_Scene_ItemID(EachItem)

		if ItemType == strItemType:

			if asVariant == 'all':
				intTotal += 1

			if asVariant == 'selected':
				blnSelected  = __fn_pyModo_Scene_ItemsSelected(ItemID)
				if blnSelected == blnTrue:
					intTotal += 1

			if asVariant == 'unselected':
				blnUnSelected  = __fn_pyModo_Scene_ItemsSelected(ItemID)
				if blnUnSelected == blnFalse:
					intTotal += 1


	return intTotal
####################################################
####################################################

def __fn_pyModo_Item_Name(strItemType,asVariant):

	Name_List = []
	blnTrue = 1
	blnFalse = 0

	SceneItemCount = __fn_pyModo_Scene_Items()

	for EachItem in range(0,SceneItemCount):

		ItemType = __fn_pyModo_Scene_ItemType(EachItem)
		ItemID =  __fn_pyModo_Scene_ItemID(EachItem)
		ItemName = __fn_pyModo_Scene_ItemName(EachItem)

		if ItemType == strItemType:

			if asVariant == 'all':
				Name_List.append (ItemName)

			if asVariant == 'selected':
				blnSelected  = __fn_pyModo_Scene_ItemsSelected(ItemID)
				if blnSelected == blnTrue:
					Name_List.append (ItemName)

			if asVariant == 'unselected':
				blnUnSelected  = __fn_pyModo_Scene_ItemsSelected(ItemID)
				if blnUnSelected == blnFalse:
					Name_List.append (ItemName)

	return Name_List
####################################################
####################################################

def __fn_pyModo_Item_ID(strItemType,asVariant):

	ID_List = []
	blnTrue = 1
	blnFalse = 0

	SceneItemCount = __fn_pyModo_Scene_Items()

	for EachItem in range(0,SceneItemCount):

		ItemType = __fn_pyModo_Scene_ItemType(EachItem)
		ItemID =  __fn_pyModo_Scene_ItemID(EachItem)

		if ItemType == strItemType:

			if asVariant == 'all':
				ID_List.append (ItemID)

			if asVariant == 'selected':
				blnSelected  = __fn_pyModo_Scene_ItemsSelected(ItemID)
				if blnSelected == blnTrue:
					ID_List.append (ItemID)

			if asVariant == 'unselected':
				blnUnSelected  = __fn_pyModo_Scene_ItemsSelected(ItemID)
				if blnUnSelected == blnFalse:
					ID_List.append (ItemID)

	return ID_List

#above are the private parts.... :)
####################################################
####################################################
