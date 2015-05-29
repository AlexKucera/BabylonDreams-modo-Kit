#!/usr/bin/python


# pyModoT (Tools)
#Author Keith Sheppard
#3/31/2015 8:26:58 PM


import lx


def Mirror_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set *.mirror ?')
    else:
        lx.eval('tool.set *.mirror {%s}' % args)


def RadialSweep_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Radial Sweep" ?')
    else:
        lx.eval('tool.set "Radial Sweep" {%s}' % args)


def Mirror_Instance_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Instance Mirror" ?')
    else:
        lx.eval('tool.set "Instance Mirror" {%s}' % args)


def Mirror_Replicate_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Replica Mirror" ?')
    else:
        lx.eval('tool.set "Replica Mirror" {%s}' % args)


def Patch_Curves_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set patch.draw ?')
    else:
        lx.eval('tool.set patch.draw {%s}' % args)


def Curve_Extrude_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Curve Extrude" ?')
    else:
        lx.eval('tool.set "Curve Extrude" {%s}' % args)


def Bezier_Extrude_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Bezier Extrude" ?')
    else:
        lx.eval('tool.set "Bezier Extrude" {%s}' % args)


def Pen_Extrude_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Pen Extrude" ?')
    else:
        lx.eval('tool.set "Pen Extrude" {%s}' % args)


def Curve_Clone_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "*.Curve Clone" ?')
    else:
        lx.eval('tool.set "*.Curve Clone" {%s}' % args)


def Curve_Instance_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Curve Instance" ?')
    else:
        lx.eval('tool.set "Curve Instance" {%s}' % args)


def Curve_Replicate_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Curve Replicate" ?')
    else:
        lx.eval('tool.set "Curve Replicate" {%s}' % args)


def Curve_Clone_xForm_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "xform.Curve Clone" ?')
    else:
        lx.eval('tool.set "xform.Curve Clone" {%s}' % args)


def Bezier_Clone_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "*.Bezier Clone" ?')
    else:
        lx.eval('tool.set "*.Bezier Clone" {%s}' % args)


def Bezier_Instance_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Bezier Instance" ?')
    else:
        lx.eval('tool.set "Bezier Instance" {%s}' % args)


def Bezier_Replicate_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Bezier Replicate" ?')
    else:
        lx.eval('tool.set "Bezier Replicate" {%s}' % args)


def Bezier_Clone_xForm_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "xform.Bezier Clone" ?')
    else:
        lx.eval('tool.set "xform.Bezier Clone" {%s}' % args)


def Pen_Clone_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "*.Pen Clone" ?')
    else:
        lx.eval('tool.set "*.Pen Clone" {%s}' % args)


def Pen_Instance_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Pen Instance" ?')
    else:
        lx.eval('tool.set "Pen Instance" {%s}' % args)


def Pen_Replicate_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Pen Replicate" ?')
    else:
        lx.eval('tool.set "Pen Replicate" {%s}' % args)


def Pen_Clone_xForm_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "xform.Pen Clone" ?')
    else:
        lx.eval('tool.set "xform.Pen Clone" {%s}' % args)


def Scatter_Clone_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "*.Scatter Clone" ?')
    else:
        lx.eval('tool.set "*.Scatter Clone" {%s}' % args)


def Scatter_Instance_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Instance Scatter" ?')
    else:
        lx.eval('tool.set "Instance Scatter" {%s}' % args)


def Scatter_Replicate_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Replica Scatter" ?')
    else:
        lx.eval('tool.set "Replica Scatter" {%s}' % args)


def Scatter_Clone_xForm_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "xform.Scatter Clone" ?')
    else:
        lx.eval('tool.set "xform.Scatter Clone" {%s}' % args)


def Clone_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set *.clone ?')
    else:
        lx.eval('tool.set *.clone {%s}' % args)


def Clone_Instance_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Instance Clone" ?')
    else:
        lx.eval('tool.set "Instance Clone" {%s}' % args)


def Clone_Replicate_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Replica Clone" ?')
    else:
        lx.eval('tool.set "Replica Clone" {%s}' % args)


def Array_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set *.array ?')
    else:
        lx.eval('tool.set *.array {%s}' % args)


def Array_Instance_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Instance Array" ?')
    else:
        lx.eval('tool.set "Instance Array" {%s}' % args)


def Array_Replicate_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Replica Array" ?')
    else:
        lx.eval('tool.set "Replica Array" {%s}' % args)


def Array_xForm_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set xform.array ?')
    else:
        lx.eval('tool.set xform.array {%s}' % args)


def Radial_Array_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "*.Radial Array" ?')
    else:
        lx.eval('tool.set "*.Radial Array" {%s}' % args)


def Radial_Instance_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Instance Radial Array" ?')
    else:
        lx.eval('tool.set "Instance Radial Array" {%s}' % args)


def Radial_Replicate_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Replica Radial Array" ?')
    else:
        lx.eval('tool.set "Replica Radial Array" {%s}' % args)


def Radial_Array_xForm_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "xform.Radial Array" ?')
    else:
        lx.eval('tool.set "xform.Radial Array" {%s}' % args)


def Mesh_Paint_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "*.Mesh Paint Smooth" ?')
    else:
        lx.eval('tool.set "*.Mesh Paint Smooth" {%s}' % args)


def Mesh_Paint_Instance_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "*.Mesh Paint Instance" ?')
    else:
        lx.eval('tool.set "*.Mesh Paint Instance" {%s}' % args)


def Mesh_Paint_Replicate_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "*.Mesh Paint Replica" ?')
    else:
        lx.eval('tool.set "*.Mesh Paint Replica" {%s}' % args)


def Paste_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set paste.tool ?')
    else:
        lx.eval('tool.set paste.tool {%s}' % args)


def Mirror_Axis_X_Set():
    lx.eval('tool.setAttr gen.mirror axis 0')


def Mirror_Axis_Y_Set():
    lx.eval('tool.setAttr gen.mirror axis 1')


def Mirror_Axis_Z_Set():
    lx.eval('tool.setAttr gen.mirror axis 2')


def Mirror_Angle_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.mirror angle ?')
    else:
        lx.eval('tool.setAttr gen.mirror angle {%s}' % args)


def Mirror_Center_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.mirror cenX ?')
    else:
        lx.eval('tool.setAttr gen.mirror cenX {%s}' % args)


def Mirror_Center_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.mirror cenY ?')
    else:
        lx.eval('tool.setAttr gen.mirror cenY {%s}' % args)


def Mirror_Center_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.mirror cenZ ?')
    else:
        lx.eval('tool.setAttr gen.mirror cenZ {%s}' % args)


def Mirror_Left_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.mirror leftX ?')
    else:
        lx.eval('tool.setAttr gen.mirror leftX {%s}' % args)


def Mirror_Left_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.mirror leftY ?')
    else:
        lx.eval('tool.setAttr gen.mirror leftY {%s}' % args)


def Mirror_Left_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.mirror leftZ ?')
    else:
        lx.eval('tool.setAttr gen.mirror leftZ {%s}' % args)


def Mirror_Up_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.mirror upX ?')
    else:
        lx.eval('tool.setAttr gen.mirror upX {%s}' % args)


def Mirror_Up_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.mirror upY ?')
    else:
        lx.eval('tool.setAttr gen.mirror upY {%s}' % args)


def Mirror_Up_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.mirror upZ ?')
    else:
        lx.eval('tool.setAttr gen.mirror upZ {%s}' % args)


def Helix_Generator_Count_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.helix sides ?')
    else:
        lx.eval('tool.setAttr gen.helix sides {%s}' % args)


def Helix_Axis_X_Set():
    lx.eval('tool.setAttr gen.helix axis 0')


def Helix_Axis_Y_Set():
    lx.eval('tool.setAttr gen.helix axis 1')


def Helix_Axis_Z_Set():
    lx.eval('tool.setAttr gen.helix axis 2')


def Helix_Generator_Axis_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.helix vecX ?')
    else:
        lx.eval('tool.setAttr gen.helix vecX {%s}' % args)


def Helix_Generator_Axis_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.helix vecY ?')
    else:
        lx.eval('tool.setAttr gen.helix vecY {%s}' % args)


def Helix_Generator_Axis_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.helix vecZ ?')
    else:
        lx.eval('tool.setAttr gen.helix vecZ {%s}' % args)


def Helix_Generator_Center_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.helix cenX ?')
    else:
        lx.eval('tool.setAttr gen.helix cenX {%s}' % args)


def Helix_Generator_Center_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.helix cenY ?')
    else:
        lx.eval('tool.setAttr gen.helix cenY {%s}' % args)


def Helix_Generator_Center_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.helix cenZ ?')
    else:
        lx.eval('tool.setAttr gen.helix cenZ {%s}' % args)


def Helix_Generator_Start_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.helix start ?')
    else:
        lx.eval('tool.setAttr gen.helix start {%s}' % args)


def Helix_Generator_End_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.helix end ?')
    else:
        lx.eval('tool.setAttr gen.helix end {%s}' % args)


def Helix_Generator_Offset_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.helix offset ?')
    else:
        lx.eval('tool.setAttr gen.helix offset {%s}' % args)


def Bridge_Remove_Poly_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge remove ?')
    else:
        lx.eval('tool.setAttr edge.bridge remove {%s}' % args)


def Bridge_Flip_Poly_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge flip ?')
    else:
        lx.eval('tool.setAttr edge.bridge flip {%s}' % args)


def Bridge_ReverseDirection_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge orient ?')
    else:
        lx.eval('tool.setAttr edge.bridge orient {%s}' % args)


def Bridge_AutoConnection_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge connect ?')
    else:
        lx.eval('tool.setAttr edge.bridge connect {%s}' % args)


def Bridge_MakeUV_Connected_Set():
    lx.eval('tool.setAttr edge.bridge uvs none')


def Bridge_Curve_Automatic_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge autoStep ?')
    else:
        lx.eval('tool.setAttr edge.bridge autoStep {%s}' % args)


def Bridge_Curve_AutomaticSteps_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge steps ?')
    else:
        lx.eval('tool.setAttr edge.bridge steps {%s}' % args)


def Patch_Curves_Mode_DefinePatch_Set():
    lx.eval('tool.setAttr patch.draw mode definePatch')


def Patch_Curves_Mode_Extend_Set():
    lx.eval('tool.setAttr patch.draw mode extend')


def Patch_Curves_Mode_MoveKnot_Set():
    lx.eval('tool.setAttr patch.draw mode moveKnot')


def Patch_Curves_Mode_MoveEdge_Set():
    lx.eval('tool.setAttr patch.draw mode moveEdge')


def Patch_Curves_Mode_EditEdge_Set():
    lx.eval('tool.setAttr patch.draw mode editEdge')


def Patch_Curves_Index_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr patch.draw index ?')
    else:
        lx.eval('tool.setAttr patch.draw index {%s}' % args)


def Patch_Curves_Position_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr patch.draw posX ?')
    else:
        lx.eval('tool.setAttr patch.draw posX {%s}' % args)


def Patch_Curves_Position_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr patch.draw posY ?')
    else:
        lx.eval('tool.setAttr patch.draw posY {%s}' % args)


def Patch_Curves_Position_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr patch.draw posZ ?')
    else:
        lx.eval('tool.setAttr patch.draw posZ {%s}' % args)


def Patch_Curves_Knot_Select_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr patch.draw knot ?')
    else:
        lx.eval('tool.setAttr patch.draw knot {%s}' % args)


def Patch_Curves_StartControl_Vert_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr patch.draw scon ?')
    else:
        lx.eval('tool.setAttr patch.draw scon {%s}' % args)


def Patch_Curves_EndControl_Vert_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr patch.draw econ ?')
    else:
        lx.eval('tool.setAttr patch.draw econ {%s}' % args)


def Patch_Curves_PerPendicular_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr patch.draw seg1 ?')
    else:
        lx.eval('tool.setAttr patch.draw seg1 {%s}' % args)


def Patch_Curves_Parallel_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr patch.draw seg2 ?')
    else:
        lx.eval('tool.setAttr patch.draw seg2 {%s}' % args)


def Patch_Curves_Type1_Knot_Set():
    lx.eval('tool.setAttr patch.draw type 1 knot')


def Patch_Curves_Type1_Length_Set():
    lx.eval('tool.setAttr patch.draw type 1 length')


def Patch_Curves_Type2_Knot_Set():
    lx.eval('tool.setAttr patch.draw type 2 knot')


def Patch_Curves_Type2_Length_Set():
    lx.eval('tool.setAttr patch.draw type 2 length')


def Patch_Curves_Save_Boundaries_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr patch.draw bound ?')
    else:
        lx.eval('tool.setAttr patch.draw bound {%s}' % args)


def Patch_Curves_Freeze_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr patch.draw freeze ?')
    else:
        lx.eval('tool.setAttr patch.draw freeze {%s}' % args)


def Patch_Curves_Flip_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr patch.draw flip ?')
    else:
        lx.eval('tool.setAttr patch.draw flip {%s}' % args)


def Patch_Curves_MakeUV_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr patch.draw uvs ?')
    else:
        lx.eval('tool.setAttr patch.draw uvs {%s}' % args)


def Pen_Generator_Type_Closed_Set():
    lx.eval('tool.setAttr gen.pen type polygon')


def Pen_Generator_Type_Open_Set():
    lx.eval('tool.setAttr gen.pen type lines')


def Pen_Generator_AlignToPath_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.pen align ?')
    else:
        lx.eval('tool.setAttr gen.pen align {%s}' % args)


def Pen_Generator_AlignToNormal_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.pen orient ?')
    else:
        lx.eval('tool.setAttr gen.pen orient {%s}' % args)


def Pen_Generator_StartAtSource_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.pen local ?')
    else:
        lx.eval('tool.setAttr gen.pen local {%s}' % args)


def Pen_Generator_CornerScale_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.pen corner ?')
    else:
        lx.eval('tool.setAttr gen.pen corner {%s}' % args)


def Pen_Generator_Current_Point_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.pen current ?')
    else:
        lx.eval('tool.setAttr gen.pen current {%s}' % args)


def Pen_Generator_Position_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.pen posX ?')
    else:
        lx.eval('tool.setAttr gen.pen posX {%s}' % args)


def Pen_Generator_Position_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.pen posY ?')
    else:
        lx.eval('tool.setAttr gen.pen posY {%s}' % args)


def Pen_Generator_Position_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.pen posZ ?')
    else:
        lx.eval('tool.setAttr gen.pen posZ {%s}' % args)


def Eff_SweepUV_None_Set():
    lx.eval('tool.setAttr effector.sweep uvs none')


def Eff_SweepUV_U_Set():
    lx.eval('tool.setAttr effector.sweep uvs u')


def Eff_SweepUV_V_Set():
    lx.eval('tool.setAttr effector.sweep uvs v')


def Eff_Sweep_Invert_Poly_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr effector.sweep flip ?')
    else:
        lx.eval('tool.setAttr effector.sweep flip {%s}' % args)


def Eff_Sweep_CapStart_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr effector.sweep cap0 ?')
    else:
        lx.eval('tool.setAttr effector.sweep cap0 {%s}' % args)


def Eff_Sweep_CapEnd_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr effector.sweep cap1 ?')
    else:
        lx.eval('tool.setAttr effector.sweep cap1 {%s}' % args)


def Eff_Clone_Replace_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr effector.clone replace ?')
    else:
        lx.eval('tool.setAttr effector.clone replace {%s}' % args)


def Eff_Clone_Flip_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr effector.clone flip ?')
    else:
        lx.eval('tool.setAttr effector.clone flip {%s}' % args)


def Eff_Clone_Merge_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr effector.clone merge ?')
    else:
        lx.eval('tool.setAttr effector.clone merge {%s}' % args)


def Eff_Clone_Distance__Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr effector.clone dist ?')
    else:
        lx.eval('tool.setAttr effector.clone dist {%s}' % args)


def Eff_Clone_Source_Active_Set():
    lx.eval('tool.setAttr effector.clove source active')


def Eff_Clone_Source_Specific_Set():
    lx.eval('tool.setAttr effector.clove source specific')


def Eff_Clone_Source_AllBackGrnd_Set():
    lx.eval('tool.setAttr effector.clove source inactive')


def Eff_Clone_Source_Random_Set():
    lx.eval('tool.setAttr effector.clove source random')


def Eff_Clone_Source_Preset_Set():
    lx.eval('tool.setAttr effector.clove source preset')


def Eff_Clone_Mesh_Item_Index_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr effector.clone item ?')
    else:
        lx.eval('tool.setAttr effector.clone item {%s}' % args)


def Eff_Item_Parent_Off_Set():
    lx.eval('tool.setAttr effector.item parent off')


def Eff_Item_Parent_Hierarchy_Set():
    lx.eval('tool.setAttr effector.item parent hierarchy')


def Eff_Item_Parent_Root_Set():
    lx.eval('tool.setAttr effector.item parent root')


def Eff_Item_Parent_Primary_Set():
    lx.eval('tool.setAttr effector.item parent primary')


def Eff_Item_Parent_Instance_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr effector.item instance ?')
    else:
        lx.eval('tool.setAttr effector.item instance {%s}' % args)


def Eff_Item_Parent_BoundBox_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr effector.item bbox ?')
    else:
        lx.eval('tool.setAttr effector.item bbox {%s}' % args)


def Eff_Item_Hierarchy_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr effector.item hierarchy ?')
    else:
        lx.eval('tool.setAttr effector.item hierarchy {%s}' % args)


def Eff_Item_Source_Active_Set():
    lx.eval('tool.setAttr effector.item source active')


def Eff_Item_Source_Specific_Set():
    lx.eval('tool.setAttr effector.item source specific')


def Eff_Item_Source_AllBackGrnd_Set():
    lx.eval('tool.setAttr effector.item source inactive')


def Eff_Item_Source_Random_Set():
    lx.eval('tool.setAttr effector.item source random')


def Eff_Item_Source_Preset_Set():
    lx.eval('tool.setAttr effector.item source preset')


def Eff_Item_Index_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr effector.item item ?')
    else:
        lx.eval('tool.setAttr effector.item item {%s}' % args)


def Eff_Replica_Source_Active_Set():
    lx.eval('tool.setAttr effector.replica source active')


def Eff_Replica_Source_Specific_Set():
    lx.eval('tool.setAttr effector.replica source pick')


def Eff_Replica_Source_AllBackGrndMesh_Set():
    lx.eval('tool.setAttr effector.replica source background')


def Eff_Replica_Source_MeshPreset_Set():
    lx.eval('tool.setAttr effector.replica source preset')


def Effectors_Replica_Item_Index_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr effector.replica item ?')
    else:
        lx.eval('tool.setAttr effector.replica item {%s}' % args)


def PathSteps_Automatic_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.pathsteps auto ?')
    else:
        lx.eval('tool.setAttr gen.pathsteps auto {%s}' % args)


def PathSteps_Steps_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.pathsteps number ?')
    else:
        lx.eval('tool.setAttr gen.pathsteps number {%s}' % args)


def PathSteps_SmoothAngle_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.pathsteps smooth ?')
    else:
        lx.eval('tool.setAttr gen.pathsteps smooth {%s}' % args)


def PathSteps_AlignToPath_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.pathsteps align ?')
    else:
        lx.eval('tool.setAttr gen.pathsteps align {%s}' % args)


def PathSteps_AlignToNormal_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.pathsteps orient ?')
    else:
        lx.eval('tool.setAttr gen.pathsteps orient {%s}' % args)


def PathSteps_StartAtSource_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.pathsteps local ?')
    else:
        lx.eval('tool.setAttr gen.pathsteps local {%s}' % args)


def Curve_Path_Mode_Add_Set():
    lx.eval('tool.setAttr gen.curve mode add')


def Curve_Path_Mode_Edit_Set():
    lx.eval('tool.setAttr gen.curve mode edit')


def Curve_Path_Mode_Delete_Set():
    lx.eval('tool.setAttr gen.curve mode delete')


def Curve_Path_PathPoint_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.curve ptX ?')
    else:
        lx.eval('tool.setAttr gen.curve ptX {%s}' % args)


def Curve_Path_PathPoint_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.curve ptY ?')
    else:
        lx.eval('tool.setAttr gen.curve ptY {%s}' % args)


def Curve_Path_PathPoint_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.curve ptZ ?')
    else:
        lx.eval('tool.setAttr gen.curve ptZ {%s}' % args)


def Curve_Path_BankAngle_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.curve bank ?')
    else:
        lx.eval('tool.setAttr gen.curve bank {%s}' % args)


def Curve_Path_Closed_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.curve closed ?')
    else:
        lx.eval('tool.setAttr gen.curve closed {%s}' % args)


def Curve_Path_StartControl_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.curve start ?')
    else:
        lx.eval('tool.setAttr gen.curve start {%s}' % args)


def Curve_Path_EndControl_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.curve end ?')
    else:
        lx.eval('tool.setAttr gen.curve end {%s}' % args)


def Curve_Path_ByLength_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.curve length ?')
    else:
        lx.eval('tool.setAttr gen.curve length {%s}' % args)


def Curve_Path_CreatePoly_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.curve poly ?')
    else:
        lx.eval('tool.setAttr gen.curve poly {%s}' % args)


def Curve_Path_FlipPoly_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.curve flip ?')
    else:
        lx.eval('tool.setAttr gen.curve flip {%s}' % args)


def Curve_Path_MakeUV_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.curve uvs ?')
    else:
        lx.eval('tool.setAttr gen.curve uvs {%s}' % args)


def Bezier_Path_Mode_Add_Set():
    lx.eval('tool.setAttr gen.bezier mode add')


def Bezier_Path_Mode_Edit_Set():
    lx.eval('tool.setAttr gen.bezier mode edit')


def Bezier_Path_Mode_Delete_Set():
    lx.eval('tool.setAttr gen.bezier mode delete')


def Bezier_Path_PathPoint_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.bezier ptX ?')
    else:
        lx.eval('tool.setAttr gen.bezier ptX {%s}' % args)


def Bezier_Path_PathPoint_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.bezier ptY ?')
    else:
        lx.eval('tool.setAttr gen.bezier ptY {%s}' % args)


def Bezier_Path_PathPoint_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.bezier ptZ ?')
    else:
        lx.eval('tool.setAttr gen.bezier ptZ {%s}' % args)


def Bezier_Path_Path_In_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.bezier inX ?')
    else:
        lx.eval('tool.setAttr gen.bezier inX {%s}' % args)


def Bezier_Path_Path_In_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.bezier inY ?')
    else:
        lx.eval('tool.setAttr gen.bezier inY {%s}' % args)


def Bezier_Path_Path_In_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.bezier inZ ?')
    else:
        lx.eval('tool.setAttr gen.bezier inZ {%s}' % args)


def Bezier_Path_Path_Out_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.bezier outX ?')
    else:
        lx.eval('tool.setAttr gen.bezier outX {%s}' % args)


def Bezier_Path_Path_Out_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.bezier outY ?')
    else:
        lx.eval('tool.setAttr gen.bezier outY {%s}' % args)


def Bezier_Path_Path_Out_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.bezier outZ ?')
    else:
        lx.eval('tool.setAttr gen.bezier outZ {%s}' % args)


def Bezier_Path_BankAngle_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.bezier bank ?')
    else:
        lx.eval('tool.setAttr gen.bezier bank {%s}' % args)


def Bezier_Path_Closed_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.bezier closed ?')
    else:
        lx.eval('tool.setAttr gen.bezier closed {%s}' % args)


def Bezier_Path_Length_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.bezier length ?')
    else:
        lx.eval('tool.setAttr gen.bezier length {%s}' % args)


def Bezier_Path_CreatePoly_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.bezier poly ?')
    else:
        lx.eval('tool.setAttr gen.bezier poly {%s}' % args)


def Bezier_Path_MakeUV_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.bezier uvs ?')
    else:
        lx.eval('tool.setAttr gen.bezier uvs {%s}' % args)


def Scatter_Clone_Count_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.scatter num ?')
    else:
        lx.eval('tool.setAttr gen.scatter num {%s}' % args)


def Scatter_Generator_Seed_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.scatter seed ?')
    else:
        lx.eval('tool.setAttr gen.scatter seed {%s}' % args)


def Scatter_Generator_Center_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.scatter cenX ?')
    else:
        lx.eval('tool.setAttr gen.scatter cenX {%s}' % args)


def Scatter_Generator_Center_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.scatter cenY ?')
    else:
        lx.eval('tool.setAttr gen.scatter cenY {%s}' % args)


def Scatter_Generator_Center_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.scatter cenZ ?')
    else:
        lx.eval('tool.setAttr gen.scatter cenZ {%s}' % args)


def Scatter_Generator_Range_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.scatter rangeX ?')
    else:
        lx.eval('tool.setAttr gen.scatter rangeX {%s}' % args)


def Scatter_Generator_Range_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.scatter rangeY ?')
    else:
        lx.eval('tool.setAttr gen.scatter rangeY {%s}' % args)


def Scatter_Generator_Range_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.scatter rangeZ ?')
    else:
        lx.eval('tool.setAttr gen.scatter rangeZ {%s}' % args)


def Scatter_Generator_Scale_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.scatter sclX  ?')
    else:
        lx.eval('tool.setAttr gen.scatter sclX  {%s}' % args)


def Scatter_Generator_Scale_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.scatter sclX  ?')
    else:
        lx.eval('tool.setAttr gen.scatter sclX  {%s}' % args)


def Scatter_Generator_Scale_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.scatter sclX  ?')
    else:
        lx.eval('tool.setAttr gen.scatter sclX  {%s}' % args)


def Scatter_Generator_Rotate_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.scatter angP ?')
    else:
        lx.eval('tool.setAttr gen.scatter angP {%s}' % args)


def Scatter_Generator_Rotate_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.scatter angH ?')
    else:
        lx.eval('tool.setAttr gen.scatter angH {%s}' % args)


def Scatter_Generator_Rotate_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.scatter angB ?')
    else:
        lx.eval('tool.setAttr gen.scatter angB {%s}' % args)


def Linear_Generator_Count_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.linear num ?')
    else:
        lx.eval('tool.setAttr gen.linear num {%s}' % args)


def Linear_Generator_Offset_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.linear offX ?')
    else:
        lx.eval('tool.setAttr gen.linear offX {%s}' % args)


def Linear_Generator_Offset_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.linear offY ?')
    else:
        lx.eval('tool.setAttr gen.linear offY {%s}' % args)


def Linear_Generator_Offset_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.linear offZ ?')
    else:
        lx.eval('tool.setAttr gen.linear offZ {%s}' % args)


def Linear_Generator_Scale_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.linear sclX ?')
    else:
        lx.eval('tool.setAttr gen.linear sclX {%s}' % args)


def Linear_Generator_Scale_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.linear sclY ?')
    else:
        lx.eval('tool.setAttr gen.linear sclY {%s}' % args)


def Linear_Generator_Scale_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.linear sclZ ?')
    else:
        lx.eval('tool.setAttr gen.linear sclZ {%s}' % args)


def Linear_Generator_Rotate_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.linear angP ?')
    else:
        lx.eval('tool.setAttr gen.linear angP {%s}' % args)


def Linear_Generator_Rotate_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.linear angH ?')
    else:
        lx.eval('tool.setAttr gen.linear angH {%s}' % args)


def Linear_Generator_Rotate_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.linear angB ?')
    else:
        lx.eval('tool.setAttr gen.linear angB {%s}' % args)


def Clone_Between_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.linear between ?')
    else:
        lx.eval('tool.setAttr gen.linear between {%s}' % args)


def Clone_AngleSnap_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.linear snap ?')
    else:
        lx.eval('tool.setAttr gen.linear snap {%s}' % args)


def Linear_Generator_Angle_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.linear snapAngle ?')
    else:
        lx.eval('tool.setAttr gen.linear snapAngle {%s}' % args)


def Array_Generator_Count_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array numX ?')
    else:
        lx.eval('tool.setAttr gen.array numX {%s}' % args)


def Array_Generator_Count_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array numY ?')
    else:
        lx.eval('tool.setAttr gen.array numY {%s}' % args)


def Array_Generator_Count_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array numZ ?')
    else:
        lx.eval('tool.setAttr gen.array numZ {%s}' % args)


def Array_Generator_Offset_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array offX ?')
    else:
        lx.eval('tool.setAttr gen.array offX {%s}' % args)


def Array_Generator_Offset_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array offY ?')
    else:
        lx.eval('tool.setAttr gen.array offY {%s}' % args)


def Array_Generator_Offset_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array offZ ?')
    else:
        lx.eval('tool.setAttr gen.array offZ {%s}' % args)


def Array_Generator_Jitter_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array jitX ?')
    else:
        lx.eval('tool.setAttr gen.array jitX {%s}' % args)


def Array_Generator_Jitter_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array jitY ?')
    else:
        lx.eval('tool.setAttr gen.array jitY {%s}' % args)


def Array_Generator_Jitter_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array jitZ ?')
    else:
        lx.eval('tool.setAttr gen.array jitZ {%s}' % args)


def Array_Generator_Scale_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array sclX ?')
    else:
        lx.eval('tool.setAttr gen.array sclX {%s}' % args)


def Array_Generator_Scale_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array sclY ?')
    else:
        lx.eval('tool.setAttr gen.array sclY {%s}' % args)


def Array_Generator_Scale_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array sclZ ?')
    else:
        lx.eval('tool.setAttr gen.array sclZ {%s}' % args)


def Array_Generator_Rotate_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array angP ?')
    else:
        lx.eval('tool.setAttr gen.array angP {%s}' % args)


def Array_Generator_Rotate_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array angH ?')
    else:
        lx.eval('tool.setAttr gen.array angH {%s}' % args)


def Array_Generator_Rotate_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array angB ?')
    else:
        lx.eval('tool.setAttr gen.array angB {%s}' % args)


def Array_Between_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr gen.array between ?')
    else:
        lx.eval('tool.setAttr gen.array between {%s}' % args)


def Paste_Center_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paste.tool cenX ?')
    else:
        lx.eval('tool.setAttr paste.tool cenX {%s}' % args)


def Paste_Center_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paste.tool cenY ?')
    else:
        lx.eval('tool.setAttr paste.tool cenY {%s}' % args)


def Paste_Center_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paste.tool cenZ ?')
    else:
        lx.eval('tool.setAttr paste.tool cenZ {%s}' % args)


def Paste_Size_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paste.tool sizeX ?')
    else:
        lx.eval('tool.setAttr paste.tool sizeX {%s}' % args)


def Paste_Size_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paste.tool sizeY ?')
    else:
        lx.eval('tool.setAttr paste.tool sizeY {%s}' % args)


def Paste_Size_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paste.tool sizeZ ?')
    else:
        lx.eval('tool.setAttr paste.tool sizeZ {%s}' % args)


def Paste_Bias_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paste.tool biasX ?')
    else:
        lx.eval('tool.setAttr paste.tool biasX {%s}' % args)


def Paste_Bias_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paste.tool biasY ?')
    else:
        lx.eval('tool.setAttr paste.tool biasY {%s}' % args)


def Paste_Bias_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paste.tool biasZ ?')
    else:
        lx.eval('tool.setAttr paste.tool biasZ {%s}' % args)


def Mesh_Paint_Mode_Slide_Set():
    lx.eval('tool.setAttr paint.mesh pmod slide')


def Mesh_Paint_Mode_Stroke_Set():
    lx.eval('tool.setAttr paint.mesh pmod stroke')


def Mesh_Paint_Mode_scaleRot_Set():
    lx.eval('tool.setAttr paint.mesh pmod scaleRot')


def Mesh_Paint_BrushDensity_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paint.mesh dens ?')
    else:
        lx.eval('tool.setAttr paint.mesh dens {%s}' % args)


def Mesh_Paint_SizeMode_Uniform_Set():
    lx.eval('tool.setAttr paint.mesh smod uniform')


def Mesh_Paint_SizeMode_Adaptive_Set():
    lx.eval('tool.setAttr paint.mesh smod adaptive')


def Mesh_Paint_SizeMode_Random_Set():
    lx.eval('tool.setAttr paint.mesh smod random')


def Mesh_Paint_SizeMode_AdaptiveRandom_Set():
    lx.eval('tool.setAttr paint.mesh smod adaptRandom')


def Mesh_Paint_Size_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paint.mesh sizX ?')
    else:
        lx.eval('tool.setAttr paint.mesh sizX {%s}' % args)


def Mesh_Paint_Size_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paint.mesh sizY ?')
    else:
        lx.eval('tool.setAttr paint.mesh sizY {%s}' % args)


def Mesh_Paint_Size_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paint.mesh sizZ ?')
    else:
        lx.eval('tool.setAttr paint.mesh sizZ {%s}' % args)


def Mesh_Paint_RotateMode_Uniform_Set():
    lx.eval('tool.setAttr tool.setAttr paint.mesh rmod uniform')


def Mesh_Paint_RotateMode_SurfaceAlign_Set():
    lx.eval('tool.setAttr paint.mesh rmod alignToPolygon')


def Mesh_Paint_RotateMode_Random_Set():
    lx.eval('tool.setAttr tool.setAttr paint.mesh rmod random')


def Mesh_Paint_RotateMode_AlignRandom_Set():
    lx.eval('tool.setAttr tool.setAttr paint.mesh rmod alignRandom')


def Mesh_Paint_RotateMode_TabletAlign_Set():
    lx.eval('tool.setAttr tool.setAttr paint.mesh rmod alignTablet')


def Mesh_Paint_RotateMode_TabletAlign_NoPitch_Set():
    lx.eval('tool.setAttr tool.setAttr paint.mesh rmod headingTablet')


def Mesh_Paint_RotateMode_ScreenAlign_Set():
    lx.eval('tool.setAttr tool.setAttr paint.mesh rmod alignScreenTablet')


def Mesh_Paint_RotateMode_ScreenAlign_NoPitch_Set():
    lx.eval('tool.setAttr paint.mesh rmod headingScreenTablet')


def Mesh_Paint_Rotate_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paint.mesh rotX ?')
    else:
        lx.eval('tool.setAttr paint.mesh rotX {%s}' % args)


def Mesh_Paint_Rotate_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paint.mesh rotY ?')
    else:
        lx.eval('tool.setAttr paint.mesh rotY {%s}' % args)


def Mesh_Paint_Rotate_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr paint.mesh rotZ ?')
    else:
        lx.eval('tool.setAttr paint.mesh rotZ {%s}' % args)


def Mesh_Paint_ParamOne_Falloff_Set():
    lx.eval('tool.setAttr paint.mesh param1 falloff')


def Mesh_Paint_ParamOne_Pressure_Set():
    lx.eval('tool.setAttr paint.mesh param1 pressure')


def Mesh_Paint_ParamOne_Slope_Set():
    lx.eval('tool.setAttr paint.mesh param1 slope')


def Mesh_Paint_ParamOne_Altitude_Set():
    lx.eval('tool.setAttr paint.mesh param1 altitude')


def Mesh_Paint_ParamOne_OneLessSlope_Set():
    lx.eval('tool.setAttr paint.mesh param1 slope1')


def Mesh_Paint_ParamOne_OneLessAlt_Set():
    lx.eval('tool.setAttr paint.mesh param1 altitude1')


def Mesh_Paint_EffectOne_None_Set():
    lx.eval('tool.setAttr paint.mesh pfx1 none')


def Mesh_Paint_EffectOne_Density_Set():
    lx.eval('tool.setAttr paint.mesh pfx1 density')


def Mesh_Paint_EffectOne_Size_Set():
    lx.eval('tool.setAttr paint.mesh pfx1 size')


def Mesh_Paint_EffectOne_Rotate_Set():
    lx.eval('tool.setAttr paint.mesh pfx1 rotation')


def Mesh_Paint_EffectOne_SizeDensity_Set():
    lx.eval('tool.setAttr paint.mesh pfx1 sizeDensity')


def Mesh_Paint_ParamTwo_Falloff_Set():
    lx.eval('tool.setAttr paint.mesh param2 falloff')


def Mesh_Paint_ParamTwo_Pressure_Set():
    lx.eval('tool.setAttr paint.mesh param2 pressure')


def Mesh_Paint_ParamTwo_Slope_Set():
    lx.eval('tool.setAttr paint.mesh param2 slope')


def Mesh_Paint_ParamTwo_Altitude_Set():
    lx.eval('tool.setAttr paint.mesh param2 altitude')


def Mesh_Paint_ParamTwo_OneLessSlope_Set():
    lx.eval('tool.setAttr paint.mesh param2 slope1')


def Mesh_Paint_ParamTwo_OneLessAlt_Set():
    lx.eval('tool.setAttr paint.mesh param2 altitude1')


def Mesh_Paint_EffectTwo_None_Set():
    lx.eval('tool.setAttr paint.mesh pfx2 none')


def Mesh_Paint_EffectTwo_Density_Set():
    lx.eval('tool.setAttr paint.mesh pfx2 density')


def Mesh_Paint_EffectTwo_Size_Set():
    lx.eval('tool.setAttr paint.mesh pfx2 size')


def Mesh_Paint_EffectTwo_Rotate_Set():
    lx.eval('tool.setAttr paint.mesh pfx2 rotation')


def Mesh_Paint_EffectTwo_SizeDensity_Set():
    lx.eval('tool.setAttr paint.mesh pfx2 sizeDensity')


def Smooth_Brush_Size_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr brush.smooth size ?')
    else:
        lx.eval('tool.setAttr brush.smooth size {%s}' % args)


def Smooth_Brush_AutoScale_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr brush.smooth autoScale ?')
    else:
        lx.eval('tool.setAttr brush.smooth autoScale {%s}' % args)


def Smooth_Brush_Bias_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr brush.smooth bias ?')
    else:
        lx.eval('tool.setAttr brush.smooth bias {%s}' % args)


def Smooth_Brush_Shape_Linear_Set():
    lx.eval('tool.setAttr brush.smooth shape linear')


def Smooth_Brush_Shape_Smooth_Set():
    lx.eval('tool.setAttr brush.smooth shape smooth')


def Smooth_Brush_Shape_Bulge_Set():
    lx.eval('tool.setAttr brush.smooth shape bulge')


def Smooth_Brush_Shape_Fat_Set():
    lx.eval('tool.setAttr brush.smooth shape fat')


def Smooth_Brush_Shape_Sharp_Set():
    lx.eval('tool.setAttr brush.smooth shape sharp')


def Smooth_Brush_Shape_VerySharp_Set():
    lx.eval('tool.setAttr brush.smooth shape sharp2')


def Smooth_Brush_In_Weight_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr brush.smooth p0 ?')
    else:
        lx.eval('tool.setAttr brush.smooth p0 {%s}' % args)


def Smooth_Brush_Out_Weight_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr brush.smooth p1 ?')
    else:
        lx.eval('tool.setAttr brush.smooth p1 {%s}' % args)


def Smooth_Brush_In_Slope_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr brush.smooth s0 ?')
    else:
        lx.eval('tool.setAttr brush.smooth s0 {%s}' % args)


def Smooth_Brush_Out_Slope_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr brush.smooth s1 ?')
    else:
        lx.eval('tool.setAttr brush.smooth s1 {%s}' % args)


def Falloff_Linear_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.linear ?')
    else:
        lx.eval('tool.set falloff.linear {%s}' % args)


def Falloff_Linear_Start_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.linear startX ?')
    else:
        lx.eval('tool.setAttr falloff.linear startX {%s}' % args)


def Falloff_Linear_Start_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.linear startY ?')
    else:
        lx.eval('tool.setAttr falloff.linear startY {%s}' % args)


def Falloff_Linear_Start_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.linear startZ ?')
    else:
        lx.eval('tool.setAttr falloff.linear startZ {%s}' % args)


def Falloff_Linear_End_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.linear endX ?')
    else:
        lx.eval('tool.setAttr falloff.linear endX {%s}' % args)


def Falloff_Linear_End_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.linear endY ?')
    else:
        lx.eval('tool.setAttr falloff.linear endY {%s}' % args)


def Falloff_Linear_End_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.linear endZ ?')
    else:
        lx.eval('tool.setAttr falloff.linear endZ {%s}' % args)


def Falloff_Linear_Symmetry_None_Set():
    lx.eval('tool.setAttr falloff.linear symmetric none')


def Falloff_Linear_Symmetry_Start_Set():
    lx.eval('tool.setAttr falloff.linear symmetric start')


def Falloff_Linear_Symmetry_End_Set():
    lx.eval('tool.setAttr falloff.linear symmetric end')


def Falloff_Linear_Shape_Linear_Set():
    lx.eval('tool.setAttr falloff.linear shape linear')


def Falloff_Linear_Shape_EaseIn_Set():
    lx.eval('tool.setAttr falloff.linear shape easeIn')


def Falloff_Linear_Shape_EaseOut_Set():
    lx.eval('tool.setAttr falloff.linear shape easeOut')


def Falloff_Linear_Shape_Smooth_Set():
    lx.eval('tool.setAttr falloff.linear shape smooth')


def Falloff_Linear_Shape_Custom_Set():
    lx.eval('tool.setAttr falloff.linear shape custom')


def Falloff_Linear_Shape_In_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.linear p0 ?')
    else:
        lx.eval('tool.setAttr falloff.linear p0 {%s}' % args)


def Falloff_Linear_Shape_Out_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.linear p1 ?')
    else:
        lx.eval('tool.setAttr falloff.linear p1 {%s}' % args)


def Falloff_Linear_MixMode_Multiply_Set():
    lx.eval('tool.setAttr falloff.linear mix multiply')


def Falloff_Linear_MixMode_Add_Set():
    lx.eval('tool.setAttr falloff.linear mix add')


def Falloff_Linear_MixMode_Subtract_Set():
    lx.eval('tool.setAttr falloff.linear mix subtract')


def Falloff_Linear_MixMode_Max_Set():
    lx.eval('tool.setAttr falloff.linear mix max')


def Falloff_Linear_MixMode_Min_Set():
    lx.eval('tool.setAttr falloff.linear mix min')


def Falloff_Linear_AutoSize_X_Set():
    lx.eval('falloff.axisAutoSize axis:0')


def Falloff_Linear_AutoSize_Y_Set():
    lx.eval('falloff.axisAutoSize axis:1')


def Falloff_Linear_AutoSize_Z_Set():
    lx.eval('falloff.axisAutoSize axis:2')


def Falloff_AutoSize_Set():
    lx.eval('falloff.autoSize')


def Falloff_Linear_Reverse_Set():
    lx.eval('falloff.reverse')


def Falloff_Cylinder_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.cylinder ?')
    else:
        lx.eval('tool.set falloff.cylinder {%s}' % args)


def Falloff_Cylinder_Center_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.cylinder cenX ?')
    else:
        lx.eval('tool.setAttr falloff.cylinder cenX {%s}' % args)


def Falloff_Cylinder_Center_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.cylinder cenY ?')
    else:
        lx.eval('tool.setAttr falloff.cylinder cenY {%s}' % args)


def Falloff_Cylinder_Center_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.cylinder cenZ ?')
    else:
        lx.eval('tool.setAttr falloff.cylinder cenZ {%s}' % args)


def Falloff_Cylinder_Size_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.cylinder sizX ?')
    else:
        lx.eval('tool.setAttr falloff.cylinder sizX {%s}' % args)


def Falloff_Cylinder_Size_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.cylinder sizY ?')
    else:
        lx.eval('tool.setAttr falloff.cylinder sizY {%s}' % args)


def Falloff_Cylinder_Size_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.cylinder sizZ ?')
    else:
        lx.eval('tool.setAttr falloff.cylinder sizZ {%s}' % args)


def Falloff_Cylinder_Axis_X_Set():
    lx.eval('tool.setAttr falloff.cylinder axis 0')


def Falloff_Cylinder_Axis_Y_Set():
    lx.eval('tool.setAttr falloff.cylinder axis 1')


def Falloff_Cylinder_Axis_Z_Set():
    lx.eval('tool.setAttr falloff.cylinder axis 2')


def Falloff_Cylinder_Shape_Linear_Set():
    lx.eval('tool.setAttr falloff.cylinder shape linear')


def Falloff_Cylinder_Shape_EaseIn_Set():
    lx.eval('tool.setAttr falloff.cylinder shape easeIn')


def Falloff_Cylinder_Shape_EaseOut_Set():
    lx.eval('tool.setAttr falloff.cylinder shape easeOut')


def Falloff_Cylinder_Shape_Smooth_Set():
    lx.eval('tool.setAttr falloff.cylinder shape smooth')


def Falloff_Cylinder_Shape_Custom_Set():
    lx.eval('tool.setAttr falloff.cylinder shape custom')


def Falloff_Cylinder_Shape_In_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.cylinder p0 ?')
    else:
        lx.eval('tool.setAttr falloff.cylinder p0 {%s}' % args)


def Falloff_Cylinder_Shape_Out_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.cylinder p1 ?')
    else:
        lx.eval('tool.setAttr falloff.cylinder p1 {%s}' % args)


def Falloff_Cylinder_MixMode_Multiply_Set():
    lx.eval('tool.setAttr falloff.cylinder mix multiply')


def Falloff_Cylinder_MixMode_Add_Set():
    lx.eval('tool.setAttr falloff.cylinder mix add')


def Falloff_Cylinder_MixMode_Subtract_Set():
    lx.eval('tool.setAttr falloff.cylinder mix subtract')


def Falloff_Cylinder_MixMode_Max_Set():
    lx.eval('tool.setAttr falloff.cylinder mix max')


def Falloff_Cylinder_MixMode_Min_Set():
    lx.eval('tool.setAttr falloff.cylinder mix min')


def Falloff_Radial_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.radial ?')
    else:
        lx.eval('tool.set falloff.radial {%s}' % args)


def Falloff_Radial_Center_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.radial cenX ?')
    else:
        lx.eval('tool.setAttr falloff.radial cenX {%s}' % args)


def Falloff_Radial_Center_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.radial cenY ?')
    else:
        lx.eval('tool.setAttr falloff.radial cenY {%s}' % args)


def Falloff_Radial_Center_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.radial cenZ ?')
    else:
        lx.eval('tool.setAttr falloff.radial cenZ {%s}' % args)


def Falloff_Radial_Size_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.radial sizX ?')
    else:
        lx.eval('tool.setAttr falloff.radial sizX {%s}' % args)


def Falloff_Radial_Size_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.radial sizY ?')
    else:
        lx.eval('tool.setAttr falloff.radial sizY {%s}' % args)


def Falloff_Radial_Size_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.radial sizZ ?')
    else:
        lx.eval('tool.setAttr falloff.radial sizZ {%s}' % args)


def Falloff_Radial_Axis_X_Set():
    lx.eval('tool.setAttr falloff.radial axis 0')


def Falloff_Radial_Axis_Y_Set():
    lx.eval('tool.setAttr falloff.radial axis 1')


def Falloff_Radial_Axis_Z_Set():
    lx.eval('tool.setAttr falloff.radial axis 2')


def Falloff_Radial_Shape_Linear_Set():
    lx.eval('tool.setAttr falloff.radial shape linear')


def Falloff_Radial_Shape_EaseIn_Set():
    lx.eval('tool.setAttr falloff.radial shape easeIn')


def Falloff_Radial_Shape_EaseOut_Set():
    lx.eval('tool.setAttr falloff.radial shape easeOut')


def Falloff_Radial_Shape_Smooth_Set():
    lx.eval('tool.setAttr falloff.radial shape smooth')


def Falloff_Radial_Shape_Custom_Set():
    lx.eval('tool.setAttr falloff.radial shape custom')


def Falloff_Radial_Shape_In_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.radial p0 ?')
    else:
        lx.eval('tool.setAttr falloff.radial p0 {%s}' % args)


def Falloff_Radial_Shape_Out_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.radial p1 ?')
    else:
        lx.eval('tool.setAttr falloff.radial p1 {%s}' % args)


def Falloff_Radial_MixMode_Multiply_Set():
    lx.eval('tool.setAttr falloff.radial mix multiply')


def Falloff_Radial_MixMode_Add_Set():
    lx.eval('tool.setAttr falloff.radial mix add')


def Falloff_Radial_MixMode_Subtract_Set():
    lx.eval('tool.setAttr falloff.radial mix subtract')


def Falloff_Radial_MixMode_Max_Set():
    lx.eval('tool.setAttr falloff.radial mix max')


def Falloff_Radial_MixMode_Min_Set():
    lx.eval('tool.setAttr falloff.radial mix min')


def Falloff_AirBrush_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.airbrush ?')
    else:
        lx.eval('tool.set falloff.airbrush {%s}' % args)


def Falloff_AirBrush_Center_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr tool.setAttr falloff.airbrush cenX ?')
    else:
        lx.eval('tool.setAttr tool.setAttr falloff.airbrush cenX {%s}' % args)


def Falloff_AirBrush_Center_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr tool.setAttr falloff.airbrush cenY ?')
    else:
        lx.eval('tool.setAttr tool.setAttr falloff.airbrush cenY {%s}' % args)


def Falloff_AirBrush_Size_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.airbrush size ?')
    else:
        lx.eval('tool.setAttr falloff.airbrush size {%s}' % args)


def Falloff_AirBrush_Strength_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.airbrush strength ?')
    else:
        lx.eval('tool.setAttr falloff.airbrush strength {%s}' % args)


def Falloff_AirBrush_Transparent_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.airbrush trans ?')
    else:
        lx.eval('tool.setAttr falloff.airbrush trans {%s}' % args)


def Falloff_AirBrush_MixMode_Multiply_Set():
    lx.eval('tool.setAttr falloff.airbrush mix multiply')


def Falloff_AirBrush_MixMode_Add_Set():
    lx.eval('tool.setAttr falloff.airbrush mix add')


def Falloff_AirBrush_MixMode_Subtract_Set():
    lx.eval('tool.setAttr falloff.airbrush mix subtract')


def Falloff_AirBrush_MixMode_Max_Set():
    lx.eval('tool.setAttr falloff.airbrush mix max')


def Falloff_AirBrush_MixMode_Min_Set():
    lx.eval('tool.setAttr falloff.airbrush mix min')


def Falloff_Screen_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.screen ?')
    else:
        lx.eval('tool.set falloff.screen {%s}' % args)


def Falloff_Screen_Center_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr tool.setAttr falloff.screen cenX ?')
    else:
        lx.eval('tool.setAttr tool.setAttr falloff.screen cenX {%s}' % args)


def Falloff_Screen_Center_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr tool.setAttr falloff.screen cenY ?')
    else:
        lx.eval('tool.setAttr tool.setAttr falloff.screen cenY {%s}' % args)


def Falloff_Screen_Size_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.screen size ?')
    else:
        lx.eval('tool.setAttr falloff.screen size {%s}' % args)


def Falloff_Screen_Strength_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.screen strength ?')
    else:
        lx.eval('tool.setAttr falloff.screen strength {%s}' % args)


def Falloff_Screen_Transparent_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.screen trans ?')
    else:
        lx.eval('tool.setAttr falloff.screen trans {%s}' % args)


def Falloff_Screen_MixMode_Multiply_Set():
    lx.eval('tool.setAttr falloff.screen mix multiply')


def Falloff_Screen_MixMode_Add_Set():
    lx.eval('tool.setAttr falloff.screen mix add')


def Falloff_Screen_MixMode_Subtract_Set():
    lx.eval('tool.setAttr falloff.screen mix subtract')


def Falloff_Screen_MixMode_Max_Set():
    lx.eval('tool.setAttr falloff.screen mix max')


def Falloff_Screen_MixMode_Min_Set():
    lx.eval('tool.setAttr falloff.screen mix min')


def Falloff_Element_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.element ?')
    else:
        lx.eval('tool.set falloff.element {%s}' % args)


def Falloff_Element_Mode_Auto_Set():
    lx.eval('tool.elementMode auto')


def Falloff_Element_Mode_AutoCenter_Set():
    lx.eval('tool.elementMode autoCent')


def Falloff_Element_Mode_Vertex_Set():
    lx.eval('tool.elementMode vertex')


def Falloff_Element_Mode_Edge_Set():
    lx.eval('tool.elementMode edge')


def Falloff_Element_Mode_EdgeCenter_Set():
    lx.eval('tool.elementMode edgeCent')


def Falloff_Element_Mode_Poly_Set():
    lx.eval('tool.elementMode polygon')


def Falloff_Element_Mode_PolyCenter_Set():
    lx.eval('tool.elementMode polyCent')


def Falloff_Element_Range_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.element dist ?')
    else:
        lx.eval('tool.setAttr falloff.element dist {%s}' % args)


def Falloff_Element_ConEle_Element_Set():
    lx.eval('tool.setAttr falloff.element connect element')


def Falloff_Element_ConEle_UseConnect_Set():
    lx.eval('tool.setAttr falloff.element connect connect')


def Falloff_Element_ConEle_Rigid_Set():
    lx.eval('tool.setAttr falloff.element connect rigid')


def Falloff_Element_ConEle_EdgeLoop_Set():
    lx.eval('tool.setAttr falloff.element connect loop')


def Falloff_Element_MixMode_Multiply_Set():
    lx.eval('tool.setAttr falloff.element mix multiply')


def Falloff_Element_MixMode_Add_Set():
    lx.eval('tool.setAttr falloff.element mix add')


def Falloff_Element_MixMode_Subtract_Set():
    lx.eval('tool.setAttr falloff.element mix subtract')


def Falloff_Element_MixMode_Max_Set():
    lx.eval('tool.setAttr falloff.element mix max')


def Falloff_Element_MixMode_Min_Set():
    lx.eval('tool.setAttr falloff.element mix min')


def Falloff_Noise_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.noise ?')
    else:
        lx.eval('tool.set falloff.noise {%s}' % args)


def Falloff_Noise_Scale_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.noise scale ?')
    else:
        lx.eval('tool.setAttr falloff.noise scale {%s}' % args)


def Falloff_Noise_MixMode_Multiply_Set():
    lx.eval('tool.setAttr falloff.noise mix multiply')


def Falloff_Noise_MixMode_Add_Set():
    lx.eval('tool.setAttr falloff.noise mix add')


def Falloff_Noise_MixMode_Subtract_Set():
    lx.eval('tool.setAttr falloff.noise mix subtract')


def Falloff_Noise_MixMode_Max_Set():
    lx.eval('tool.setAttr falloff.noise mix max')


def Falloff_Noise_MixMode_Min_Set():
    lx.eval('tool.setAttr falloff.noise mix min')


def Falloff_Curvature_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.curvature ?')
    else:
        lx.eval('tool.set falloff.curvature {%s}' % args)


def Falloff_Curvature_Scale_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.curvature scale ?')
    else:
        lx.eval('tool.setAttr falloff.curvature scale {%s}' % args)


def Falloff_Curvature_MixMode_Multiply_Set():
    lx.eval('tool.setAttr falloff.curvature mix multiply')


def Falloff_Curvature_MixMode_Add_Set():
    lx.eval('tool.setAttr falloff.curvature mix add')


def Falloff_Curvature_MixMode_Subtract_Set():
    lx.eval('tool.setAttr falloff.curvature mix subtract')


def Falloff_Curvature_MixMode_Max_Set():
    lx.eval('tool.setAttr falloff.curvature mix max')


def Falloff_Curvature_MixMode_Min_Set():
    lx.eval('tool.setAttr falloff.curvature mix min')


def Falloff_VertexMap_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.vertexMap ?')
    else:
        lx.eval('tool.set falloff.vertexMap {%s}' % args)


def Falloff_VertexMap_Mode_Magnitude_Set():
    lx.eval('tool.setAttr falloff.vertexMap mode magnitude')


def Falloff_VertexMap_Mode_Component_Set():
    lx.eval('tool.setAttr falloff.vertexMap mode component')


def Falloff_VertexMap_Index_U_Set():
    lx.eval('tool.setAttr falloff.vertexMap index 0')


def Falloff_VertexMap_Index_V_Set():
    lx.eval('tool.setAttr falloff.vertexMap index 1')


def Falloff_VertexMap_MixMode_Multiply_Set():
    lx.eval('tool.setAttr falloff.vertexMap mix multiply')


def Falloff_VertexMap_MixMode_Add_Set():
    lx.eval('tool.setAttr falloff.vertexMap mix add')


def Falloff_VertexMap_MixMode_Subtract_Set():
    lx.eval('tool.setAttr falloff.vertexMap mix subtract')


def Falloff_VertexMap_MixMode_Max_Set():
    lx.eval('tool.setAttr falloff.vertexMap mix max')


def Falloff_VertexMap_MixMode_Min_Set():
    lx.eval('tool.setAttr falloff.vertexMap mix min')


def Falloff_Path_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set PathFalloff ?')
    else:
        lx.eval('tool.set PathFalloff {%s}' % args)


def Falloff_Path_Size_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.path size ?')
    else:
        lx.eval('tool.setAttr falloff.path size {%s}' % args)


def Falloff_Path_MixMode_Multiply_Set():
    lx.eval('tool.setAttr falloff.path mix multiply')


def Falloff_Path_MixMode_Add_Set():
    lx.eval('tool.setAttr falloff.path mix add')


def Falloff_Path_MixMode_Subtract_Set():
    lx.eval('tool.setAttr falloff.path mix subtract')


def Falloff_Path_MixMode_Max_Set():
    lx.eval('tool.setAttr falloff.path mix max')


def Falloff_Path_MixMode_Min_Set():
    lx.eval('tool.setAttr falloff.path mix min')


def Falloff_Lasso_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.lasso ?')
    else:
        lx.eval('tool.set falloff.lasso {%s}' % args)


def Falloff_Lasso_Style_Lasso_Set():
    lx.eval('tool.setAttr falloff.lasso style lasso')


def Falloff_Lasso_Style_Rectangle_Set():
    lx.eval('tool.setAttr falloff.lasso style rectangle')


def Falloff_Lasso_Style_Circle_Set():
    lx.eval('tool.setAttr falloff.lasso style circle')


def Falloff_Lasso_Style_Ellipse_Set():
    lx.eval('tool.setAttr falloff.lasso style ellipse')


def Falloff_Lasso_Soft_Border_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.lasso soft ?')
    else:
        lx.eval('tool.setAttr falloff.lasso soft {%s}' % args)


def Falloff_Lasso_MixMode_Multiply_Set():
    lx.eval('tool.setAttr falloff.lasso mix multiply')


def Falloff_Lasso_MixMode_Add_Set():
    lx.eval('tool.setAttr falloff.lasso mix add')


def Falloff_Lasso_MixMode_Subtract_Set():
    lx.eval('tool.setAttr falloff.lasso mix subtract')


def Falloff_Lasso_MixMode_Max_Set():
    lx.eval('tool.setAttr falloff.lasso mix max')


def Falloff_Lasso_MixMode_Min_Set():
    lx.eval('tool.setAttr falloff.lasso mix min')


def Falloff_Image_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.image ?')
    else:
        lx.eval('tool.set falloff.image {%s}' % args)


def Falloff_Image_Repeat_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.image repeat ?')
    else:
        lx.eval('tool.setAttr falloff.image repeat {%s}' % args)


def Falloff_Image_SoftBorder_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.image soft ?')
    else:
        lx.eval('tool.setAttr falloff.image soft {%s}' % args)


def Falloff_Image_UseUV_Maps_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.image vmap ?')
    else:
        lx.eval('tool.setAttr falloff.image vmap {%s}' % args)


def Falloff_Image_Scale_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.image scale ?')
    else:
        lx.eval('tool.setAttr falloff.image scale {%s}' % args)


def Falloff_Image_Pos_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.image posx ?')
    else:
        lx.eval('tool.setAttr falloff.image posx {%s}' % args)


def Falloff_Image_Pos_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.image posy ?')
    else:
        lx.eval('tool.setAttr falloff.image posy {%s}' % args)


def Falloff_Image_Rotation_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr  falloff.image rot ?')
    else:
        lx.eval('tool.setAttr  falloff.image rot {%s}' % args)


def Falloff_Selection_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.selection ?')
    else:
        lx.eval('tool.set falloff.selection {%s}' % args)


def Falloff_Selection_Shape_Linear_Set():
    lx.eval('tool.setAttr falloff.selection shape linear')


def Falloff_Selection_Shape_EaseIn_Set():
    lx.eval('tool.setAttr falloff.selection shape easeIn')


def Falloff_Selection_Shape_EaseOut_Set():
    lx.eval('tool.setAttr falloff.selection shape easeOut')


def Falloff_Selection_Shape_Smooth_Set():
    lx.eval('tool.setAttr falloff.selection shape smooth')


def Falloff_Selection_Shape_Custom_Set():
    lx.eval('tool.setAttr falloff.selection shape custom')


def Falloff_Selection_Shape_In_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.selection p0 ?')
    else:
        lx.eval('tool.setAttr falloff.selection p0 {%s}' % args)


def Falloff_Selection_Shape_Out_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.selection p1 ?')
    else:
        lx.eval('tool.setAttr falloff.selection p1 {%s}' % args)


def Falloff_Selection_MixMode_Multiply_Set():
    lx.eval('tool.setAttr falloff.selection mix multiply')


def Falloff_Selection_MixMode_Add_Set():
    lx.eval('tool.setAttr falloff.selection mix add')


def Falloff_Selection_MixMode_Subtract_Set():
    lx.eval('tool.setAttr falloff.selection mix subtract')


def Falloff_Selection_MixMode_Max_Set():
    lx.eval('tool.setAttr falloff.selection mix max')


def Falloff_Selection_MixMode_Min_Set():
    lx.eval('tool.setAttr falloff.selection mix min')


def Falloff_SoftSelection_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.softSelection ?')
    else:
        lx.eval('tool.set falloff.softSelection {%s}' % args)


def Falloff_SoftSelection_Radius_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.softSelection radius ?')
    else:
        lx.eval('tool.setAttr falloff.softSelection radius {%s}' % args)


def Falloff_SoftSelection_UseConnect_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.softSelection connect ?')
    else:
        lx.eval('tool.setAttr falloff.softSelection connect {%s}' % args)


def Falloff_SoftSelection_Shape_Linear_Set():
    lx.eval('tool.setAttr falloff.softSelection shape linear')


def Falloff_SoftSelection_Shape_EaseIn_Set():
    lx.eval('tool.setAttr falloff.softSelection shape easeIn')


def Falloff_SoftSelection_Shape_EaseOut_Set():
    lx.eval('tool.setAttr falloff.softSelection shape easeOut')


def Falloff_SoftSelection_Shape_Smooth_Set():
    lx.eval('tool.setAttr falloff.softSelection shape smooth')


def Falloff_SoftSelection_Shape_Custom_Set():
    lx.eval('tool.setAttr falloff.softSelection shape custom')


def Falloff_SoftSelection_Shape_In_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.softSelection p0 ?')
    else:
        lx.eval('tool.setAttr falloff.softSelection p0 {%s}' % args)


def Falloff_SoftSelection_Shape_Out_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.softSelection p1 ?')
    else:
        lx.eval('tool.setAttr falloff.softSelection p1 {%s}' % args)


def Falloff_SoftSelection_MixMode_Multiply_Set():
    lx.eval('tool.setAttr falloff.softSelection mix multiply')


def Falloff_SoftSelection_MixMode_Add_Set():
    lx.eval('tool.setAttr falloff.softSelection mix add')


def Falloff_SoftSelection_MixMode_Subtract_Set():
    lx.eval('tool.setAttr falloff.softSelection mix subtract')


def Falloff_SoftSelection_MixMode_Max_Set():
    lx.eval('tool.setAttr falloff.softSelection mix max')


def Falloff_SoftSelection_MixMode_Min_Set():
    lx.eval('tool.setAttr falloff.softSelection mix min')


def Falloff_SoftSelection_ShowVertex_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.softSelection showVertex ?')
    else:
        lx.eval('tool.setAttr falloff.softSelection showVertex {%s}' % args)


def Falloff_SoftSelection_ShowEdge_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr falloff.softSelection showEdge ?')
    else:
        lx.eval('tool.setAttr falloff.softSelection showEdge {%s}' % args)


def Falloff_Invert_Set():
    lx.eval('tool.set falloff.invert on falloff')


def Falloff_Add_Linear_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.linear on falloff ?')
    else:
        lx.eval('tool.set falloff.linear on falloff {%s}' % args)


def Falloff_Add_Cylinder_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.cylinder on falloff ?')
    else:
        lx.eval('tool.set falloff.cylinder on falloff {%s}' % args)


def Falloff_Add_Radial_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.radial on falloff ?')
    else:
        lx.eval('tool.set falloff.radial on falloff {%s}' % args)


def Falloff_Add_AirBrush_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.airbrush on falloff ?')
    else:
        lx.eval('tool.set falloff.airbrush on falloff {%s}' % args)


def Falloff_Add_Screen_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.screen on falloff ?')
    else:
        lx.eval('tool.set falloff.screen on falloff {%s}' % args)


def Falloff_Add_Elemenet_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.element on falloff ?')
    else:
        lx.eval('tool.set falloff.element on falloff {%s}' % args)


def Falloff_Add_Noise_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.noise on falloff ?')
    else:
        lx.eval('tool.set falloff.noise on falloff {%s}' % args)


def Falloff_Add_Curvature_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.curvature on falloff ?')
    else:
        lx.eval('tool.set falloff.curvature on falloff {%s}' % args)


def Falloff_Add_VertexMap_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.vertexMap on falloff ?')
    else:
        lx.eval('tool.set falloff.vertexMap on falloff {%s}' % args)


def Falloff_Add_Path_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.path on falloff ?')
    else:
        lx.eval('tool.set falloff.path on falloff {%s}' % args)


def Falloff_Add_Lasso_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.lasso on falloff ?')
    else:
        lx.eval('tool.set falloff.lasso on falloff {%s}' % args)


def Falloff_Add_Image_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.image on falloff ?')
    else:
        lx.eval('tool.set falloff.image on falloff {%s}' % args)


def Falloff_Add_Selection_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set falloff.selection on falloff ?')
    else:
        lx.eval('tool.set falloff.selection on falloff {%s}' % args)


def Quantize_Step_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.quantize X ?')
    else:
        lx.eval('tool.setAttr xfrm.quantize X {%s}' % args)


def Quantize_Step_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.quantize Y ?')
    else:
        lx.eval('tool.setAttr xfrm.quantize Y {%s}' % args)


def Quantize_Step_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.quantize Z ?')
    else:
        lx.eval('tool.setAttr xfrm.quantize Z {%s}' % args)


def Quantize_SlipUV_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.quantize lockUV ?')
    else:
        lx.eval('tool.setAttr xfrm.quantize lockUV {%s}' % args)


def Quantize_Morph_None_Set():
    lx.eval('tool.setAttr xfrm.quantize morph none')


def Quantize_Morph_Transform_Set():
    lx.eval('tool.setAttr xfrm.quantize morph xfrm')


def Quantize_Morph_KeepPositions_Set():
    lx.eval('tool.setAttr xfrm.quantize morph keep')


def Bend_Angle_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.bend angle ?')
    else:
        lx.eval('tool.setAttr xfrm.bend angle {%s}' % args)


def Bend_Spine_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.bend spineX ?')
    else:
        lx.eval('tool.setAttr xfrm.bend spineX {%s}' % args)


def Bend_Spine_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.bend spineY ?')
    else:
        lx.eval('tool.setAttr xfrm.bend spineY {%s}' % args)


def Bend_Spine_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.bend spineZ ?')
    else:
        lx.eval('tool.setAttr xfrm.bend spineZ {%s}' % args)


def Bend_SlipUV_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.bend lockUV ?')
    else:
        lx.eval('tool.setAttr xfrm.bend lockUV {%s}' % args)


def Bend_Morph_None_Set():
    lx.eval('tool.setAttr xfrm.bend morph none')


def Bend_Morph_Transform_Set():
    lx.eval('tool.setAttr xfrm.bend morph xfrm')


def Bend_Morph_Keep_Set():
    lx.eval('tool.setAttr xfrm.bend morph keep')


def Push_Distance_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.push dist ?')
    else:
        lx.eval('tool.setAttr xfrm.push dist {%s}' % args)


def Push_Selection_Normals_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.push select ?')
    else:
        lx.eval('tool.setAttr xfrm.push select {%s}' % args)


def Element_Move_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set ElementMove ?')
    else:
        lx.eval('tool.set ElementMove {%s}' % args)


def Flex_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set Flex ?')
    else:
        lx.eval('tool.set Flex {%s}' % args)


def Soft_Move_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set xfrm.magnet ?')
    else:
        lx.eval('tool.set xfrm.magnet {%s}' % args)


def Soft_Drag_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set xfrm.softDrag ?')
    else:
        lx.eval('tool.set xfrm.softDrag {%s}' % args)


def Shear_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set xfrm.shear ?')
    else:
        lx.eval('tool.set xfrm.shear {%s}' % args)


def Smooth_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set xfrm.smooth ?')
    else:
        lx.eval('tool.set xfrm.smooth {%s}' % args)


def Jitter_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set xfrm.jitter ?')
    else:
        lx.eval('tool.set xfrm.jitter {%s}' % args)


def Quantize_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set xfrm.quantize ?')
    else:
        lx.eval('tool.set xfrm.quantize {%s}' % args)


def SoftSelection_Move_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set SoftSelectionMove ?')
    else:
        lx.eval('tool.set SoftSelectionMove {%s}' % args)


def SoftSelection_Rotate_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set SoftSelectionRotate ?')
    else:
        lx.eval('tool.set SoftSelectionRotate {%s}' % args)


def SoftSelection_Scale_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set SoftSelectionScale ?')
    else:
        lx.eval('tool.set SoftSelectionScale {%s}' % args)


def SoftSelection_Transform_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set SoftSelectionTransform ?')
    else:
        lx.eval('tool.set SoftSelectionTransform {%s}' % args)


def Twist_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set xfrm.twist ?')
    else:
        lx.eval('tool.set xfrm.twist {%s}' % args)


def Bend_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set Bend ?')
    else:
        lx.eval('tool.set Bend {%s}' % args)


def Vortex_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set xfrm.vortex ?')
    else:
        lx.eval('tool.set xfrm.vortex {%s}' % args)


def Swirl_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set Swirl ?')
    else:
        lx.eval('tool.set Swirl {%s}' % args)


def Push_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set xfrm.push ?')
    else:
        lx.eval('tool.set xfrm.push {%s}' % args)


def Taper_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set xfrm.taper ?')
    else:
        lx.eval('tool.set xfrm.taper {%s}' % args)


def Bulge_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set xfrm.pole ?')
    else:
        lx.eval('tool.set xfrm.pole {%s}' % args)


def Flare_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set Flare ?')
    else:
        lx.eval('tool.set Flare {%s}' % args)


def Slice_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set poly.knife ?')
    else:
        lx.eval('tool.set poly.knife {%s}' % args)


def Curve_Slice_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set "Curve Slice" ?')
    else:
        lx.eval('tool.set "Curve Slice" {%s}' % args)


def Edge_Slice_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set edge.knife ?')
    else:
        lx.eval('tool.set edge.knife {%s}' % args)


def Pen_Slice_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set PenKnife ?')
    else:
        lx.eval('tool.set PenKnife {%s}' % args)


def Loop_Slice_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set poly.loopSlice ?')
    else:
        lx.eval('tool.set poly.loopSlice {%s}' % args)


def Axis_Slice_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set poly.julienne ?')
    else:
        lx.eval('tool.set poly.julienne {%s}' % args)


def Julienne_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set Julienne ?')
    else:
        lx.eval('tool.set Julienne {%s}' % args)


def Dicer_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set Dicer ?')
    else:
        lx.eval('tool.set Dicer {%s}' % args)


def Tack_Tool_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set prop.tool ?')
    else:
        lx.eval('tool.set prop.tool {%s}' % args)


def Vertex_Tool_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set prim.makeVertex ?')
    else:
        lx.eval('tool.set prim.makeVertex {%s}' % args)


def Bevel_Vert_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set vert.bevel ?')
    else:
        lx.eval('tool.set vert.bevel {%s}' % args)


def Extrude_Vertex_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set vert.extrude ?')
    else:
        lx.eval('tool.set vert.extrude {%s}' % args)


def Merge_Tool_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set vert.merge ?')
    else:
        lx.eval('tool.set vert.merge {%s}' % args)


def Extrude_Edge_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set edge.extrude ?')
    else:
        lx.eval('tool.set edge.extrude {%s}' % args)


def Extend_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set edge.extend ?')
    else:
        lx.eval('tool.set edge.extend {%s}' % args)


def Bevel_Edge_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set edge.bevel ?')
    else:
        lx.eval('tool.set edge.bevel {%s}' % args)


def Bridge_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set edge.bridge ?')
    else:
        lx.eval('tool.set edge.bridge {%s}' % args)


def Slide_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set EdgeSlide ?')
    else:
        lx.eval('tool.set EdgeSlide {%s}' % args)


def Add_Loop_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set edge.addLoop ?')
    else:
        lx.eval('tool.set edge.addLoop {%s}' % args)


def Add_Point_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set edge.addPoint ?')
    else:
        lx.eval('tool.set edge.addPoint {%s}' % args)


def Pen_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set prim.pen ?')
    else:
        lx.eval('tool.set prim.pen {%s}' % args)


def Bevel_Poly_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set poly.bevel ?')
    else:
        lx.eval('tool.set poly.bevel {%s}' % args)


def Smooth_Shift_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set poly.smshift ?')
    else:
        lx.eval('tool.set poly.smshift {%s}' % args)


def Thicken_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set Thicken ?')
    else:
        lx.eval('tool.set Thicken {%s}' % args)


def Sketch_Extrude_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set poly.sweep ?')
    else:
        lx.eval('tool.set poly.sweep {%s}' % args)


def Spikey_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set poly.spikey ?')
    else:
        lx.eval('tool.set poly.spikey {%s}' % args)


def Shift_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set poly.shift ?')
    else:
        lx.eval('tool.set poly.shift {%s}' % args)


def Inset_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set poly.inset ?')
    else:
        lx.eval('tool.set poly.inset {%s}' % args)


def Reduction_Tool_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set poly.reduct ?')
    else:
        lx.eval('tool.set poly.reduct {%s}' % args)


def Topology_Pen_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set mesh.topology ?')
    else:
        lx.eval('tool.set mesh.topology {%s}' % args)


def Jitter_Enable_X_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.jitter enableX ?')
    else:
        lx.eval('tool.setAttr xfrm.jitter enableX {%s}' % args)


def Jitter_Enable_Y_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.jitter enableY ?')
    else:
        lx.eval('tool.setAttr xfrm.jitter enableY {%s}' % args)


def Jitter_Enable_Z_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.jitter enableZ ?')
    else:
        lx.eval('tool.setAttr xfrm.jitter enableZ {%s}' % args)


def Jitter_Range_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.jitter rangeX ?')
    else:
        lx.eval('tool.setAttr xfrm.jitter rangeX {%s}' % args)


def Jitter_Range_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.jitter rangeY ?')
    else:
        lx.eval('tool.setAttr xfrm.jitter rangeY {%s}' % args)


def Jitter_Range_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.jitter rangeZ ?')
    else:
        lx.eval('tool.setAttr xfrm.jitter rangeZ {%s}' % args)


def Jitter_Seed_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.jitter seed  ?')
    else:
        lx.eval('tool.setAttr xfrm.jitter seed  {%s}' % args)


def Jitter_SlipUV_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.jitter lockUV ?')
    else:
        lx.eval('tool.setAttr xfrm.jitter lockUV {%s}' % args)


def Jitter_Morph_None_Set():
    lx.eval('tool.setAttr xfrm.jitter morph none')


def Jitter_Morph_Transform_Set():
    lx.eval('tool.setAttr xfrm.jitter morph xfrm')


def Jitter_Morph_Keep_Set():
    lx.eval('tool.setAttr xfrm.jitter morph keep')


def Smooth_Strength_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.smooth strn ?')
    else:
        lx.eval('tool.setAttr xfrm.smooth strn {%s}' % args)


def Smooth_Iterations_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.smooth iter ?')
    else:
        lx.eval('tool.setAttr xfrm.smooth iter {%s}' % args)


def Smooth_Thread_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.smooth thread ?')
    else:
        lx.eval('tool.setAttr xfrm.smooth thread {%s}' % args)


def Smooth_SlipUV_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.smooth lockUV ?')
    else:
        lx.eval('tool.setAttr xfrm.smooth lockUV {%s}' % args)


def Slice_Start_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.knife startX ?')
    else:
        lx.eval('tool.setAttr poly.knife startX {%s}' % args)


def Slice_Start_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.knife startY ?')
    else:
        lx.eval('tool.setAttr poly.knife startY {%s}' % args)


def Slice_Start_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.knife startZ ?')
    else:
        lx.eval('tool.setAttr poly.knife startZ {%s}' % args)


def Slice_End_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.knife endX ?')
    else:
        lx.eval('tool.setAttr poly.knife endX {%s}' % args)


def Slice_End_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.knife endY ?')
    else:
        lx.eval('tool.setAttr poly.knife endY {%s}' % args)


def Slice_End_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.knife endZ ?')
    else:
        lx.eval('tool.setAttr poly.knife endZ {%s}' % args)


def Slice_Fast_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.knife fast ?')
    else:
        lx.eval('tool.setAttr poly.knife fast {%s}' % args)


def Slice_Angle_Snap_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.knife snap ?')
    else:
        lx.eval('tool.setAttr poly.knife snap {%s}' % args)


def Slice_Angle_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.knife snapAngle ?')
    else:
        lx.eval('tool.setAttr poly.knife snapAngle {%s}' % args)


def Edge_Slice_Split_Middle_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.knife middle  ?')
    else:
        lx.eval('tool.setAttr edge.knife middle  {%s}' % args)


def Edge_Slice_SplitPoly_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.knife split ?')
    else:
        lx.eval('tool.setAttr edge.knife split {%s}' % args)


def Edge_Slice_Show_None_Set():
    lx.eval('tool.setAttr edge.knife show none')


def Edge_Slice_Show_Position_Set():
    lx.eval('tool.setAttr edge.knife show position')


def Edge_Slice_Show_Distance_Set():
    lx.eval('tool.setAttr edge.knife show distances')


def Edge_Slice_Position_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.knife pos ?')
    else:
        lx.eval('tool.setAttr edge.knife pos {%s}' % args)


def Edge_Slice_Offset_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.knife offset ?')
    else:
        lx.eval('tool.setAttr edge.knife offset {%s}' % args)


def Edge_Slice_SnapValue_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.knife snap ?')
    else:
        lx.eval('tool.setAttr edge.knife snap {%s}' % args)


def Edge_Slice_InsidePolygons_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.knife inside ?')
    else:
        lx.eval('tool.setAttr edge.knife inside {%s}' % args)


def Edge_Slice_AlwaysRaycast_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.knife raycast ?')
    else:
        lx.eval('tool.setAttr edge.knife raycast {%s}' % args)


def Loop_Slice_Edit_Move_Set():
    lx.eval('tool.setAttr poly.loopSlice edit move')


def Loop_Slice_Edit_Add_Set():
    lx.eval('tool.setAttr poly.loopSlice edit add')


def Loop_Slice_Edit_Remove_Set():
    lx.eval('tool.setAttr tool.setAttr poly.loopSlice edit remove')


def Loop_Slice_Mode_Free_Set():
    lx.eval('tool.setAttr tool.setAttr poly.loopSlice mode free')


def Loop_Slice_Mode_Uniform_Set():
    lx.eval('tool.setAttr poly.loopSlice mode uniform')


def Loop_Slice_Mode_Symmetry_Set():
    lx.eval('tool.setAttr poly.loopSlice mode symmetry')


def Loop_Slice_Current_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.loopSlice curr ?')
    else:
        lx.eval('tool.setAttr poly.loopSlice curr {%s}' % args)


def Loop_Slice_Count_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.loopSlice count ?')
    else:
        lx.eval('tool.setAttr poly.loopSlice count {%s}' % args)


def Loop_Slice_Uniform_Set():
    lx.eval('poly.uniformLoopSlice')


def Loop_Slice_Slice_Selected_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.loopSlice select  ?')
    else:
        lx.eval('tool.setAttr poly.loopSlice select  {%s}' % args)


def Loop_Slice_Keep_Quads_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.loopSlice quad  ?')
    else:
        lx.eval('tool.setAttr poly.loopSlice quad  {%s}' % args)


def Loop_Slice_Slice_Ngons_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.loopSlice ngon  ?')
    else:
        lx.eval('tool.setAttr poly.loopSlice ngon  {%s}' % args)


def Loop_Slice_Preserve_Curvature_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.loopSlice curvature ?')
    else:
        lx.eval('tool.setAttr poly.loopSlice curvature {%s}' % args)


def Loop_Slice_Tension_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.loopSlice tension ?')
    else:
        lx.eval('tool.setAttr poly.loopSlice tension {%s}' % args)


def Loop_Slice_Inset_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.loopSlice depth ?')
    else:
        lx.eval('tool.setAttr poly.loopSlice depth {%s}' % args)


def Loop_Slice_Position_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.loopSlice pos ?')
    else:
        lx.eval('tool.setAttr poly.loopSlice pos {%s}' % args)


def Loop_Slice_Length_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.loopSlice sw ?')
    else:
        lx.eval('tool.setAttr poly.loopSlice sw {%s}' % args)


def Loop_Slice_Slider_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.loopSlice sx ?')
    else:
        lx.eval('tool.setAttr poly.loopSlice sx {%s}' % args)


def Loop_Slice_Slider_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.loopSlice sy ?')
    else:
        lx.eval('tool.setAttr poly.loopSlice sy {%s}' % args)


def Axis_Slice_Mode_Number_Set():
    lx.eval('tool.setAttr poly.julienne mode number')


def Axis_Slice_Mode_Size_Set():
    lx.eval('tool.setAttr poly.julienne mode size')


def Axis_Slice_Number_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.julienne numX ?')
    else:
        lx.eval('tool.setAttr poly.julienne numX {%s}' % args)


def Axis_Slice_Number_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.julienne numY ?')
    else:
        lx.eval('tool.setAttr poly.julienne numY {%s}' % args)


def Axis_Slice_Number_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.julienne numZ ?')
    else:
        lx.eval('tool.setAttr poly.julienne numZ {%s}' % args)


def Axis_Slice_Size_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.julienne sizX ?')
    else:
        lx.eval('tool.setAttr poly.julienne sizX {%s}' % args)


def Axis_Slice_Size_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.julienne sizY ?')
    else:
        lx.eval('tool.setAttr poly.julienne sizY {%s}' % args)


def Axis_Slice_Size_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.julienne sizZ ?')
    else:
        lx.eval('tool.setAttr poly.julienne sizZ {%s}' % args)


def Axis_Slice_Offset_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.julienne offX ?')
    else:
        lx.eval('tool.setAttr poly.julienne offX {%s}' % args)


def Axis_Slice_Offset_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.julienne offX ?')
    else:
        lx.eval('tool.setAttr poly.julienne offX {%s}' % args)


def Axis_Slice_Offset_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.julienne offX ?')
    else:
        lx.eval('tool.setAttr poly.julienne offX {%s}' % args)


def Axis_Slice_Hold_Slice_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.julienne hold ?')
    else:
        lx.eval('tool.setAttr poly.julienne hold {%s}' % args)


def Eff_Cleaver_Preview_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr effector.cleaver preview ?')
    else:
        lx.eval('tool.setAttr effector.cleaver preview {%s}' % args)


def Eff_Cleaver_Random_Seed_Set():
    lx.eval('tool.setAttr effector.cleaver seed')


def Eff_Cleaver_Randomness_Set():
    lx.eval('tool.setAttr effector.cleaver disorder')


def Eff_Cleaver_Gap_Set():
    lx.eval('tool.setAttr effector.cleaver gap')


def Eff_Cleaver_Inner_Material_Set():
    lx.eval('tool.setAttr effector.cleaver surface')


def Eff_Cleaver_MaxCuts_Set():
    lx.eval('tool.setAttr effector.cleaver maxCuts')


def Eff_Cleaver_Frag_Scale_X_Set():
    lx.eval('tool.setAttr effector.cleaver planeBiasX')


def Eff_Cleaver_Frag_Scale_Y_Set():
    lx.eval('tool.setAttr effector.cleaver planeBiasX')


def Eff_Cleaver_Frag_Scale_Z_Set():
    lx.eval('tool.setAttr effector.cleaver planeBiasX')


def Tack_Tool_Center_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prop.tool cenX ?')
    else:
        lx.eval('tool.setAttr prop.tool cenX {%s}' % args)


def Tack_Tool_Center_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prop.tool cenY ?')
    else:
        lx.eval('tool.setAttr prop.tool cenY {%s}' % args)


def Tack_Tool_Center_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prop.tool cenZ ?')
    else:
        lx.eval('tool.setAttr prop.tool cenZ {%s}' % args)


def Tack_Tool_Align_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prop.tool align ?')
    else:
        lx.eval('tool.setAttr prop.tool align {%s}' % args)


def Tack_Tool_Rotate_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prop.tool rotX ?')
    else:
        lx.eval('tool.setAttr prop.tool rotX {%s}' % args)


def Tack_Tool_Rotate_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prop.tool rotY ?')
    else:
        lx.eval('tool.setAttr prop.tool rotY {%s}' % args)


def Tack_Tool_Rotate_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prop.tool rotZ ?')
    else:
        lx.eval('tool.setAttr prop.tool rotZ {%s}' % args)


def Tack_Tool_Offset_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prop.tool offset ?')
    else:
        lx.eval('tool.setAttr prop.tool offset {%s}' % args)


def Tack_Tool_Size_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prop.tool size ?')
    else:
        lx.eval('tool.setAttr prop.tool size {%s}' % args)


def Tack_Tool_Move_ConVert_Set():
    lx.eval('tool.setAttr prop.tool connect')


def Tack_Tool_Move_Closes_Element_Set():
    lx.eval('tool.setAttr prop.tool mode')


def Tack_Tool_Copy_Geometry_Set():
    lx.eval('tool.setAttr prop.tool copy')


def Tack_Tool_Make_Bridge_Set():
    lx.eval('tool.setAttr prop.tool bridge')


def Vertex_Tool_Position_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.makeVertex cenX ?')
    else:
        lx.eval('tool.setAttr prim.makeVertex cenX {%s}' % args)


def Vertex_Tool_Position_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.makeVertex cenY ?')
    else:
        lx.eval('tool.setAttr prim.makeVertex cenY {%s}' % args)


def Vertex_Tool_Position_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.makeVertex cenZ ?')
    else:
        lx.eval('tool.setAttr prim.makeVertex cenZ {%s}' % args)


def Vertex_Tool_Point_Poly_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.makeVertex polygon ?')
    else:
        lx.eval('tool.setAttr prim.makeVertex polygon {%s}' % args)


def Bevel_Vert_Inset_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr vert.bevel inset ?')
    else:
        lx.eval('tool.setAttr vert.bevel inset {%s}' % args)


def Bevel_Vert_Use_Material_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr vert.bevel useMat ?')
    else:
        lx.eval('tool.setAttr vert.bevel useMat {%s}' % args)


def Bevel_Vert_MaterialName_Index_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr vert.bevel matName ?')
    else:
        lx.eval('tool.setAttr vert.bevel matName {%s}' % args)


def Bevel_Vert_Round_Level_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr vert.bevel level ?')
    else:
        lx.eval('tool.setAttr vert.bevel level {%s}' % args)


def Extrude_Vert_Extrude_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr vert.extrude shift ?')
    else:
        lx.eval('tool.setAttr vert.extrude shift {%s}' % args)


def Extrude_Vert_Width_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr vert.extrude inset ?')
    else:
        lx.eval('tool.setAttr vert.extrude inset {%s}' % args)


def Extrude_Vert_Use_Material_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr vert.extrude useMat ?')
    else:
        lx.eval('tool.setAttr vert.extrude useMat {%s}' % args)


def Extrude_Vert_MaterialName_Index_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr vert.extrude matName ?')
    else:
        lx.eval('tool.setAttr vert.extrude matName {%s}' % args)


def Merge_Vert_Distance_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr vert.merge dist ?')
    else:
        lx.eval('tool.setAttr vert.merge dist {%s}' % args)


def Merge_Vert_Keep_OneVertPoly_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr vert.merge keep ?')
    else:
        lx.eval('tool.setAttr vert.merge keep {%s}' % args)


def Merge_Vert_Test_Morph_Positions_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr vert.merge morph ?')
    else:
        lx.eval('tool.setAttr vert.merge morph {%s}' % args)


def Topology_Pen_Offset_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr mesh.topology offsetX ?')
    else:
        lx.eval('tool.setAttr mesh.topology offsetX {%s}' % args)


def Topology_Pen_Offset_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr mesh.topology offsetY ?')
    else:
        lx.eval('tool.setAttr mesh.topology offsetY {%s}' % args)


def Topology_Pen_Offset_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr mesh.topology offsetZ ?')
    else:
        lx.eval('tool.setAttr mesh.topology offsetZ {%s}' % args)


def Topology_Pen_Mode_Move_Set():
    lx.eval('tool.setAttr mesh.topology mode move')


def Topology_Pen_Mode_Duplicate_Set():
    lx.eval('tool.setAttr mesh.topology mode duplicate')


def Topology_Pen_Mode_Remove_Set():
    lx.eval('tool.setAttr mesh.topology mode remove')


def Topology_Pen_Mode_Split_Set():
    lx.eval('tool.setAttr mesh.topology mode split')


def Topology_Pen_Mode_AddLoop_Set():
    lx.eval('tool.setAttr mesh.topology mode addLoop')


def Topology_Pen_Mode_Point_Set():
    lx.eval('tool.setAttr mesh.topology mode point')


def Topology_Pen_Mode_Fill_Set():
    lx.eval('tool.setAttr mesh.topology mode fill')


def Topology_Pen_EdgeLoop_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr mesh.topology loop ?')
    else:
        lx.eval('tool.setAttr mesh.topology loop {%s}' % args)


def Topology_Pen_EdgeSlide_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr mesh.topology slide ?')
    else:
        lx.eval('tool.setAttr mesh.topology slide {%s}' % args)


def Topology_Pen_BackFace_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr mesh.topology backFace ?')
    else:
        lx.eval('tool.setAttr mesh.topology backFace {%s}' % args)


def Topology_Pen_InnerSnap_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr mesh.topology innerSnap ?')
    else:
        lx.eval('tool.setAttr mesh.topology innerSnap {%s}' % args)


def Topology_Pen_SlipUV_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr mesh.topology lockUV ?')
    else:
        lx.eval('tool.setAttr mesh.topology lockUV {%s}' % args)


def Topology_Pen_Ray_InActive_Surf_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr mesh.topology raycast ?')
    else:
        lx.eval('tool.setAttr mesh.topology raycast {%s}' % args)


def Topology_Pen_AddLoop_Pos_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr mesh.topology position ?')
    else:
        lx.eval('tool.setAttr mesh.topology position {%s}' % args)


def Topology_Pen_Split_Middle_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr mesh.topology middle ?')
    else:
        lx.eval('tool.setAttr mesh.topology middle {%s}' % args)


def Topology_Pen_Fill_Quad_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr mesh.topology quadOnly ?')
    else:
        lx.eval('tool.setAttr mesh.topology quadOnly {%s}' % args)


def Topology_Pen_Fill_Range_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr  mesh.topology range ?')
    else:
        lx.eval('tool.setAttr  mesh.topology range {%s}' % args)


def Extrude_Edge_Extrude_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extrude shift ?')
    else:
        lx.eval('tool.setAttr edge.extrude shift {%s}' % args)


def Extrude_Edge_Width_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extrude inset ?')
    else:
        lx.eval('tool.setAttr edge.extrude inset {%s}' % args)


def Extrude_Edge_Use_Material_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extrude useMat ?')
    else:
        lx.eval('tool.setAttr edge.extrude useMat {%s}' % args)


def Extrude_Edge_MaterialName_Index_Set():
    lx.eval('tool.setAttr edge.extrude matName')


def Extend_Edge_Offset_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend offX ?')
    else:
        lx.eval('tool.setAttr edge.extend offX {%s}' % args)


def Extend_Edge_Offset_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend offY ?')
    else:
        lx.eval('tool.setAttr edge.extend offY {%s}' % args)


def Extend_Edge_Offset_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend offZ ?')
    else:
        lx.eval('tool.setAttr edge.extend offZ {%s}' % args)


def Extend_Edge_Rotate_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend rotX ?')
    else:
        lx.eval('tool.setAttr edge.extend rotX {%s}' % args)


def Extend_Edge_Rotate_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend rotY ?')
    else:
        lx.eval('tool.setAttr edge.extend rotY {%s}' % args)


def Extend_Edge_Rotate_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend rotZ ?')
    else:
        lx.eval('tool.setAttr edge.extend rotZ {%s}' % args)


def Extend_Edge_Scale_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend sclX ?')
    else:
        lx.eval('tool.setAttr edge.extend sclX {%s}' % args)


def Extend_Edge_Scale_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend sclY ?')
    else:
        lx.eval('tool.setAttr edge.extend sclY {%s}' % args)


def Extend_Edge_Scale_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend sclZ ?')
    else:
        lx.eval('tool.setAttr edge.extend sclZ {%s}' % args)


def Extend_Edge_Segments_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend segs ?')
    else:
        lx.eval('tool.setAttr edge.extend segs {%s}' % args)


def Extend_Edge_Inset_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend inset ?')
    else:
        lx.eval('tool.setAttr edge.extend inset {%s}' % args)


def Extend_Edge_Shift_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend shift ?')
    else:
        lx.eval('tool.setAttr edge.extend shift {%s}' % args)


def Extend_Edge_Handle_Move_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend moveHandle ?')
    else:
        lx.eval('tool.setAttr edge.extend moveHandle {%s}' % args)


def Extend_Edge_Handle_Rotate_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend rotateHandle ?')
    else:
        lx.eval('tool.setAttr edge.extend rotateHandle {%s}' % args)


def Extend_Edge_Handle_Scale_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend scaleHandle ?')
    else:
        lx.eval('tool.setAttr edge.extend scaleHandle {%s}' % args)


def Extend_Edge_Handle_Local_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.extend localHandle ?')
    else:
        lx.eval('tool.setAttr edge.extend localHandle {%s}' % args)


def Extend_Edge_Plane_None_Set():
    lx.eval('tool.setAttr edge.extend planeHandle none')


def Extend_Edge_Plane_Move_Set():
    lx.eval('tool.setAttr edge.extend planeHandle move')


def Extend_Edge_Plane_Scale_Set():
    lx.eval('tool.setAttr edge.extend planeHandle scale')


def Extend_Edge_Haul_Global_Set():
    lx.eval('tool.setAttr edge.extend hauling global')


def Extend_Edge_Haul_Local_Set():
    lx.eval('tool.setAttr edge.extend hauling local')


def Extend_Edge_MakeUV_None_Set():
    lx.eval('tool.setAttr edge.extend uvs none')


def Extend_Edge_MakeUV_U_Set():
    lx.eval('tool.setAttr edge.extend uvs u')


def Extend_Edge_MakeUV_V_Set():
    lx.eval('tool.setAttr edge.extend uvs v')


def Bevel_Edge_Mode_Inset_Set():
    lx.eval('tool.setAttr edge.bevel mode inset')


def Bevel_Edge_Mode_Width_Set():
    lx.eval('tool.setAttr edge.bevel mode width')


def Bevel_Edge_Value_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bevel inset ?')
    else:
        lx.eval('tool.setAttr edge.bevel inset {%s}' % args)


def Bevel_Edge_Use_Material_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bevel useMat ?')
    else:
        lx.eval('tool.setAttr edge.bevel useMat {%s}' % args)


def Bevel_Edge_MaterialName_Index_Set():
    lx.eval('tool.setAttr edge.bevel matName')


def Bevel_Edge_Round_Level_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bevel level ?')
    else:
        lx.eval('tool.setAttr edge.bevel level {%s}' % args)


def Bevel_Edge_Sharp_Corner_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bevel sharp ?')
    else:
        lx.eval('tool.setAttr edge.bevel sharp {%s}' % args)


def Bevel_Edge_Shape_Round_Set():
    lx.eval('tool.setAttr edge.bevel shape round')


def Bevel_Edge_Shape_Square_Set():
    lx.eval('tool.setAttr edge.bevel shape square')


def Bevel_Edge_Shape_Sharp_Set():
    lx.eval('tool.setAttr edge.bevel shape sharp')


def Bridge_Segments_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge segments ?')
    else:
        lx.eval('tool.setAttr edge.bridge segments {%s}' % args)


def Bridge_Twist_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge twist ?')
    else:
        lx.eval('tool.setAttr edge.bridge twist {%s}' % args)


def Bridge_Mode_Linear_Set():
    lx.eval('tool.setAttr edge.bridge mode linear')


def Bridge_Mode_Curve_Set():
    lx.eval('tool.setAttr edge.bridge mode curve')


def Bridge_Mode_Smooth_Set():
    lx.eval('tool.setAttr edge.bridge mode smooth')


def Bridge_RemovePoly_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge remove ?')
    else:
        lx.eval('tool.setAttr edge.bridge remove {%s}' % args)


def Bridge_FlipPoly_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge flip ?')
    else:
        lx.eval('tool.setAttr edge.bridge flip {%s}' % args)


def Bridge_Reverse_Direction_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge orient ?')
    else:
        lx.eval('tool.setAttr edge.bridge orient {%s}' % args)


def Bridge_AutoConnect_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge connect ?')
    else:
        lx.eval('tool.setAttr edge.bridge connect {%s}' % args)


def Bridge_Continuous_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge continuous ?')
    else:
        lx.eval('tool.setAttr edge.bridge continuous {%s}' % args)


def Bridge_UseGuideCurve_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge guideCurve ?')
    else:
        lx.eval('tool.setAttr edge.bridge guideCurve {%s}' % args)


def Bridge_Tension_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge tension ?')
    else:
        lx.eval('tool.setAttr edge.bridge tension {%s}' % args)


def Bridge_MakeUV_None_Set():
    lx.eval('tool.setAttr edge.bridge uvs none')


def Bridge_MakeUV_U_Set():
    lx.eval('tool.setAttr edge.bridge uvs u')


def Bridge_MakeUV_V_Set():
    lx.eval('tool.setAttr edge.bridge uvs v')


def Bridge_Curve_Auto_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge autoStep ?')
    else:
        lx.eval('tool.setAttr edge.bridge autoStep {%s}' % args)


def Bridge_Curve_Steps_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.bridge steps ?')
    else:
        lx.eval('tool.setAttr edge.bridge steps {%s}' % args)


def Slide_Edge_Mode_Radial_Set():
    lx.eval('tool.setAttr edge.slide mode radial')


def Slide_Edge_Mode_Linear_Set():
    lx.eval('tool.setAttr edge.slide mode linear')


def Slide_Edge_Direction_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.slide dirX ?')
    else:
        lx.eval('tool.setAttr edge.slide dirX {%s}' % args)


def Slide_Edge_Direction_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.slide dirY ?')
    else:
        lx.eval('tool.setAttr edge.slide dirY {%s}' % args)


def Slide_Edge_Direction_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.slide dirZ ?')
    else:
        lx.eval('tool.setAttr edge.slide dirZ {%s}' % args)


def Slide_Edge_InterPolate_Dist_Set():
    lx.eval('tool.setAttr edge.slide interpolation distance')


def Slide_Edge_InterPolate_Perc_Set():
    lx.eval('tool.setAttr edge.slide interpolation percent')


def Slide_Edge_Distance_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.slide dist ?')
    else:
        lx.eval('tool.setAttr edge.slide dist {%s}' % args)


def Slide_Edge_Percent_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.slide percent ?')
    else:
        lx.eval('tool.setAttr edge.slide percent {%s}' % args)


def Slide_Edge_Merge_Verts_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.slide merge  ?')
    else:
        lx.eval('tool.setAttr edge.slide merge  {%s}' % args)


def Slide_Edge_StopAtEdges_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.slide stop ?')
    else:
        lx.eval('tool.setAttr edge.slide stop {%s}' % args)


def Slide_Edge_Duplicate_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.slide duplicate ?')
    else:
        lx.eval('tool.setAttr edge.slide duplicate {%s}' % args)


def Slide_Edge_Loop_Slide_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.slide loop ?')
    else:
        lx.eval('tool.setAttr edge.slide loop {%s}' % args)


def Slide_Edge_Segments_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.slide segs ?')
    else:
        lx.eval('tool.setAttr edge.slide segs {%s}' % args)


def Slide_Edge_Preserve_Curvature_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.slide curvature ?')
    else:
        lx.eval('tool.setAttr edge.slide curvature {%s}' % args)


def Slide_Edge_Tension_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.slide tension ?')
    else:
        lx.eval('tool.setAttr edge.slide tension {%s}' % args)


def Slide_Edge_SlipUV_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.slide lockUV ?')
    else:
        lx.eval('tool.setAttr edge.slide lockUV {%s}' % args)


def Add_Loop_Edge_Position_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addLoop position ?')
    else:
        lx.eval('tool.setAttr edge.addLoop position {%s}' % args)


def Add_Loop_Edge_Spllit_Middle_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addLoop middle ?')
    else:
        lx.eval('tool.setAttr edge.addLoop middle {%s}' % args)


def Add_Loop_Edge_Keep_Quads_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addLoop quad ?')
    else:
        lx.eval('tool.setAttr edge.addLoop quad {%s}' % args)


def Add_Loop_Edge_Show_Position_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addLoop showPosition ?')
    else:
        lx.eval('tool.setAttr edge.addLoop showPosition {%s}' % args)


def Add_Loop_Edge_Show_Distance_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addLoop showDistance ?')
    else:
        lx.eval('tool.setAttr edge.addLoop showDistance {%s}' % args)


def Add_Loop_Edge_Abs_Distance_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addLoop absDistance ?')
    else:
        lx.eval('tool.setAttr edge.addLoop absDistance {%s}' % args)


def Add_Loop_Edge_Offset_End_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addLoop absFromEnd ?')
    else:
        lx.eval('tool.setAttr edge.addLoop absFromEnd {%s}' % args)


def Add_Loop_Edge_Both_Sides_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addLoop bothSides ?')
    else:
        lx.eval('tool.setAttr edge.addLoop bothSides {%s}' % args)


def Add_Loop_Edge_Preserve_Curvature_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addLoop curvature ?')
    else:
        lx.eval('tool.setAttr edge.addLoop curvature {%s}' % args)


def Add_Loop_Edge_Tension_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addLoop tension  ?')
    else:
        lx.eval('tool.setAttr edge.addLoop tension  {%s}' % args)


def Add_Loop_Edge_DistanceOne_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addLoop distance ?')
    else:
        lx.eval('tool.setAttr edge.addLoop distance {%s}' % args)


def Add_Loop_Edge_DistanceTwo_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addLoop altDistance ?')
    else:
        lx.eval('tool.setAttr edge.addLoop altDistance {%s}' % args)


def Add_Point_Edge_Position_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addPoint position ?')
    else:
        lx.eval('tool.setAttr edge.addPoint position {%s}' % args)


def Add_Point_Edge_DistanceOne_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addPoint distance ?')
    else:
        lx.eval('tool.setAttr edge.addPoint distance {%s}' % args)


def Add_Point_Edge_DistanceTwo_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addPoint altDistance ?')
    else:
        lx.eval('tool.setAttr edge.addPoint altDistance {%s}' % args)


def Add_Point_Edge_Split_Middle_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addPoint middle ?')
    else:
        lx.eval('tool.setAttr edge.addPoint middle {%s}' % args)


def Add_Point_Edge_Show_Position_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addPoint showPosition ?')
    else:
        lx.eval('tool.setAttr edge.addPoint showPosition {%s}' % args)


def Add_Point_Edge_Show_Distance_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addPoint showDistance ?')
    else:
        lx.eval('tool.setAttr edge.addPoint showDistance {%s}' % args)


def Add_Point_Edge_Preserve_Curvature_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addPoint curvature ?')
    else:
        lx.eval('tool.setAttr edge.addPoint curvature {%s}' % args)


def Add_Point_Edge_Tension_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr edge.addPoint tension ?')
    else:
        lx.eval('tool.setAttr edge.addPoint tension {%s}' % args)


def Pen_Poly_Type_Polygon_Set():
    lx.eval('tool.setAttr prim.pen type polygon')


def Pen_Poly_Type_Lines_Set():
    lx.eval('tool.setAttr prim.pen type lines')


def Pen_Poly_Type_Vertices_Set():
    lx.eval('tool.setAttr prim.pen type vertices')


def Pen_Poly_Type_SplinePatch_Set():
    lx.eval('tool.setAttr prim.pen type spatch')


def Pen_Poly_Type_Subdivs_Set():
    lx.eval('tool.setAttr prim.pen type subdiv')


def Pen_Poly_Type_Polylines_Set():
    lx.eval('tool.setAttr prim.pen type polyline')


def Pen_Poly_Current_Point_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen current ?')
    else:
        lx.eval('tool.setAttr prim.pen current {%s}' % args)


def Pen_Poly_Position_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen posX ?')
    else:
        lx.eval('tool.setAttr prim.pen posX {%s}' % args)


def Pen_Poly_Position_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen posY ?')
    else:
        lx.eval('tool.setAttr prim.pen posY {%s}' % args)


def Pen_Poly_Position_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen posZ ?')
    else:
        lx.eval('tool.setAttr prim.pen posZ {%s}' % args)


def Pen_Poly_Flip_Polygon_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen flip ?')
    else:
        lx.eval('tool.setAttr prim.pen flip {%s}' % args)


def Pen_Poly_Close_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen close ?')
    else:
        lx.eval('tool.setAttr prim.pen close {%s}' % args)


def Pen_Poly_Merge_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen merge ?')
    else:
        lx.eval('tool.setAttr prim.pen merge {%s}' % args)


def Pen_Poly_Make_Quads_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen quad ?')
    else:
        lx.eval('tool.setAttr prim.pen quad {%s}' % args)


def Pen_Poly_WallMode_Off_Set():
    lx.eval('tool.setAttr prim.pen wall off')


def Pen_Poly_WallMode_Inner_Set():
    lx.eval('tool.setAttr prim.pen wall inner')


def Pen_Poly_WallMode_Outer_Set():
    lx.eval('tool.setAttr prim.pen wall outer')


def Pen_Poly_WallMode_BothSides_Set():
    lx.eval('tool.setAttr prim.pen wall both')


def Pen_Poly_WallMode_Offset_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen offset ?')
    else:
        lx.eval('tool.setAttr prim.pen offset {%s}' % args)


def Pen_Poly_Inset_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen inset ?')
    else:
        lx.eval('tool.setAttr prim.pen inset {%s}' % args)


def Pen_Poly_Segments_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen segs ?')
    else:
        lx.eval('tool.setAttr prim.pen segs {%s}' % args)


def Pen_Poly_Show_Angle_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen showAngle ?')
    else:
        lx.eval('tool.setAttr prim.pen showAngle {%s}' % args)


def Pen_Poly_Show_Handles_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen showHandle ?')
    else:
        lx.eval('tool.setAttr prim.pen showHandle {%s}' % args)


def Pen_Poly_Show_Numbers_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen showNumber ?')
    else:
        lx.eval('tool.setAttr prim.pen showNumber {%s}' % args)


def Pen_Poly_Select_New_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen selectNew ?')
    else:
        lx.eval('tool.setAttr prim.pen selectNew {%s}' % args)


def Pen_Poly_MakeUV_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr prim.pen uvs ?')
    else:
        lx.eval('tool.setAttr prim.pen uvs {%s}' % args)


def Pen_Poly_Project_Axis_Set():
    lx.eval('tool.setAttr prim.pen proj axis')


def Pen_Poly_Project_BackDrop_Set():
    lx.eval('tool.setAttr prim.pen proj back')


def Pen_Poly_U_Direction_Set():
    lx.eval('tool.setAttr prim.pen proj u')


def Pen_Poly_V_Direction_Set():
    lx.eval('tool.setAttr prim.pen proj v')


def Bevel_Poly_Shift_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.bevel shift ?')
    else:
        lx.eval('tool.setAttr poly.bevel shift {%s}' % args)


def Bevel_Poly_Shift_PlusMinus_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.bevel srand ?')
    else:
        lx.eval('tool.setAttr poly.bevel srand {%s}' % args)


def Bevel_Poly_Inset_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.bevel inset ?')
    else:
        lx.eval('tool.setAttr poly.bevel inset {%s}' % args)


def Bevel_Poly_Inset_PlusMinus_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.bevel irand ?')
    else:
        lx.eval('tool.setAttr poly.bevel irand {%s}' % args)


def Bevel_Poly_Edges_Inner_Set():
    lx.eval('tool.setAttr poly.bevel edges inner')


def Bevel_Poly_Edges_Outer_Set():
    lx.eval('tool.setAttr poly.bevel edges outer')


def Bevel_Poly_Use_Material_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.bevel useMat ?')
    else:
        lx.eval('tool.setAttr poly.bevel useMat {%s}' % args)


def Bevel_Poly_MaterialName_Index_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.bevel matName ?')
    else:
        lx.eval('tool.setAttr poly.bevel matName {%s}' % args)


def Bevel_Poly_GroupPoly_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.bevel group ?')
    else:
        lx.eval('tool.setAttr poly.bevel group {%s}' % args)


def Bevel_Poly_Segments_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.bevel segs ?')
    else:
        lx.eval('tool.setAttr poly.bevel segs {%s}' % args)


def Bevel_Poly_MakeUV_Connected_Set():
    lx.eval('tool.setAttr poly.bevel uvs none')


def Bevel_Poly_MakeUV_U_Set():
    lx.eval('tool.setAttr poly.bevel uvs u')


def Bevel_Poly_MakeUV_V_Set():
    lx.eval('tool.setAttr poly.bevel uvs v')


def Smooth_Shift_Poly_Offset_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.smshift shift ?')
    else:
        lx.eval('tool.setAttr poly.smshift shift {%s}' % args)


def Smooth_Shift_Poly_Scale_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.smshift scale ?')
    else:
        lx.eval('tool.setAttr poly.smshift scale {%s}' % args)


def Smooth_Shift_Poly_SmoothAngle_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.smshift maxAngle ?')
    else:
        lx.eval('tool.setAttr poly.smshift maxAngle {%s}' % args)


def Smooth_Shift_Poly_Thicken_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.smshift thicken ?')
    else:
        lx.eval('tool.setAttr poly.smshift thicken {%s}' % args)


def Smooth_Shift_Poly_Sharp_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.smshift sharp ?')
    else:
        lx.eval('tool.setAttr poly.smshift sharp {%s}' % args)


def Sketch_Extrude_Mode_Sweep_Set():
    lx.eval('tool.setAttr poly.sweep mode sweep')


def Sketch_Extrude_Mode_EditPath_Set():
    lx.eval('tool.setAttr poly.sweep mode editPath')


def Sketch_Extrude_Mode_DelKnot_Set():
    lx.eval('tool.setAttr poly.sweep mode deleteKnot')


def Sketch_Extrude_Mode_DelPath_Set():
    lx.eval('tool.setAttr poly.sweep mode deletePath')


def Sketch_Extrude_Mode_UniSpans_Set():
    lx.eval('tool.setAttr poly.sweep mode uniformSpan')


def Sketch_Extrude_Mode_Straight_Set():
    lx.eval('tool.setAttr poly.sweep mode straight')


def Sketch_Extrude_MoveByPath_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.sweep path ?')
    else:
        lx.eval('tool.setAttr poly.sweep path {%s}' % args)


def Sketch_Extrude_Uniform_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.sweep uniform ?')
    else:
        lx.eval('tool.setAttr poly.sweep uniform {%s}' % args)


def Sketch_Extrude_AlignToPath_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.sweep align ?')
    else:
        lx.eval('tool.setAttr poly.sweep align {%s}' % args)


def Sketch_Extrude_Precision_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.sweep prec ?')
    else:
        lx.eval('tool.setAttr poly.sweep prec {%s}' % args)


def Sketch_Extrude_Scale_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.sweep scale ?')
    else:
        lx.eval('tool.setAttr poly.sweep scale {%s}' % args)


def Sketch_Extrude_Spin_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.sweep spin ?')
    else:
        lx.eval('tool.setAttr poly.sweep spin {%s}' % args)


def Sketch_Extrude_MakeUV_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.sweep uv ?')
    else:
        lx.eval('tool.setAttr poly.sweep uv {%s}' % args)


def Sketch_Extrude_U_Repeat_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.sweep urep ?')
    else:
        lx.eval('tool.setAttr poly.sweep urep {%s}' % args)


def Sketch_Extrude_V_Repeat_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.sweep vrep ?')
    else:
        lx.eval('tool.setAttr poly.sweep vrep {%s}' % args)


def Sketch_Extrude_U_Rotate_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.sweep urot ?')
    else:
        lx.eval('tool.setAttr poly.sweep urot {%s}' % args)


def Spikey_Factor_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.spikey factor ?')
    else:
        lx.eval('tool.setAttr poly.spikey factor {%s}' % args)


def Shift_Poly_Shift_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.shift shift ?')
    else:
        lx.eval('tool.setAttr poly.shift shift {%s}' % args)


def Inset_Poly_Inset_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.inset inset ?')
    else:
        lx.eval('tool.setAttr poly.inset inset {%s}' % args)


def Reduction_Tool_Number_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.reduct number ?')
    else:
        lx.eval('tool.setAttr poly.reduct number {%s}' % args)


def Reduction_Tool_BoundaryWeight_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.reduct boundaryWeight ?')
    else:
        lx.eval('tool.setAttr poly.reduct boundaryWeight {%s}' % args)


def Reduction_Tool_MatBorderWeight_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.reduct materialWeight ?')
    else:
        lx.eval('tool.setAttr poly.reduct materialWeight {%s}' % args)


def Reduction_Tool_LegacyMode_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.reduct method ?')
    else:
        lx.eval('tool.setAttr poly.reduct method {%s}' % args)


def Transform_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set Transform ?')
    else:
        lx.eval('tool.set Transform {%s}' % args)


def Move_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set TransformMove ?')
    else:
        lx.eval('tool.set TransformMove {%s}' % args)


def Rotate_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set TransformRotate ?')
    else:
        lx.eval('tool.set TransformRotate {%s}' % args)


def Scale_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set TransformScale ?')
    else:
        lx.eval('tool.set TransformScale {%s}' % args)


def Scale_Scale_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.transform SX ?')
    else:
        lx.eval('tool.setAttr xfrm.transform SX {%s}' % args)


def Scale_Scale_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.transform SY ?')
    else:
        lx.eval('tool.setAttr xfrm.transform SY {%s}' % args)


def Scale_Scale_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.transform SZ ?')
    else:
        lx.eval('tool.setAttr xfrm.transform SZ {%s}' % args)


def Scale_Absolute_Handle_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.transform absHandle  ?')
    else:
        lx.eval('tool.setAttr xfrm.transform absHandle  {%s}' % args)


def Scale_Negative_Scale_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.transform negScale ?')
    else:
        lx.eval('tool.setAttr xfrm.transform negScale {%s}' % args)


def Scale_SlipUV_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.transform lockUV ?')
    else:
        lx.eval('tool.setAttr xfrm.transform lockUV {%s}' % args)


def Tool_Apply_Set():
    lx.eval('tool.doApply')


def Morph_None_Set():
    lx.eval('tool.setAttr xfrm.transform morph none')


def Morph_Transform_Set():
    lx.eval('tool.setAttr xfrm.transform morph xfrm')


def Morph_Keep_Positions_Set():
    lx.eval('tool.setAttr xfrm.transform morph keep')


def Normal_None_Set():
    lx.eval('tool.setAttr xfrm.transform normal none')


def Normal_Edit_Set():
    lx.eval('tool.setAttr xfrm.transform normal edit')


def Normal_Update_Set():
    lx.eval('tool.setAttr xfrm.transform normal update')


def Rotate_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.transform RX ?')
    else:
        lx.eval('tool.setAttr xfrm.transform RX {%s}' % args)


def Rotate_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.transform RY ?')
    else:
        lx.eval('tool.setAttr xfrm.transform RY {%s}' % args)


def Rotate_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.transform RZ ?')
    else:
        lx.eval('tool.setAttr xfrm.transform RZ {%s}' % args)


def Move_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.transform TX ?')
    else:
        lx.eval('tool.setAttr xfrm.transform TX {%s}' % args)


def Move_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.transform TY ?')
    else:
        lx.eval('tool.setAttr xfrm.transform TY {%s}' % args)


def Move_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.transform TZ ?')
    else:
        lx.eval('tool.setAttr xfrm.transform TZ {%s}' % args)


def Transform_Haul_Translate_Set():
    lx.eval('tool.setAttr xfrm.transform H translate')


def Transform_Haul_Rotate_Set():
    lx.eval('tool.setAttr xfrm.transform H rotate')


def Transform_Haul_Scale_Set():
    lx.eval('tool.setAttr xfrm.transform H scale')


def Action_Center_Automatic_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set actr.auto on ?')
    else:
        lx.eval('tool.set actr.auto on {%s}' % args)


def Action_Center_Selection_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set actr.select ?')
    else:
        lx.eval('tool.set actr.select {%s}' % args)


def Action_Center_Selection_Border_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set actr.border ?')
    else:
        lx.eval('tool.set actr.border {%s}' % args)


def Action_Center_SelCenter_AutoAxis_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set actr.selectauto ?')
    else:
        lx.eval('tool.set actr.selectauto {%s}' % args)


def Action_Center_Element_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set actr.element ?')
    else:
        lx.eval('tool.set actr.element {%s}' % args)


def Action_Center_Screen_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set actr.screen ?')
    else:
        lx.eval('tool.set actr.screen {%s}' % args)


def Action_Center_Origin_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set actr.origin ?')
    else:
        lx.eval('tool.set actr.origin {%s}' % args)


def Action_Center_Parent_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set actr.parent ?')
    else:
        lx.eval('tool.set actr.parent {%s}' % args)


def Action_Center_Local_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set actr.local ?')
    else:
        lx.eval('tool.set actr.local {%s}' % args)


def Action_Center_Pivot_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set actr.pivot ?')
    else:
        lx.eval('tool.set actr.pivot {%s}' % args)


def Action_Center_PivotParent_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set actr.pivotparent ?')
    else:
        lx.eval('tool.set actr.pivotparent {%s}' % args)


def Action_Center_Center_Auto_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set center.auto ?')
    else:
        lx.eval('tool.set center.auto {%s}' % args)


def Action_Center_Center_Select_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set center.select ?')
    else:
        lx.eval('tool.set center.select {%s}' % args)


def Action_Center_Center_Border_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set center.border ?')
    else:
        lx.eval('tool.set center.border {%s}' % args)


def Action_Center_Center_Element_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set center.element ?')
    else:
        lx.eval('tool.set center.element {%s}' % args)


def Action_Center_Center_Screen_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set center.view ?')
    else:
        lx.eval('tool.set center.view {%s}' % args)


def Action_Center_Center_Origin_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set center.origin ?')
    else:
        lx.eval('tool.set center.origin {%s}' % args)


def Action_Center_Center_Parent_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set center.parent ?')
    else:
        lx.eval('tool.set center.parent {%s}' % args)


def Action_Center_Center_Local_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set center.local ?')
    else:
        lx.eval('tool.set center.local {%s}' % args)


def Action_Center_Center_Pivot_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set center.pivot ?')
    else:
        lx.eval('tool.set center.pivot {%s}' % args)


def Action_Center_Axis_Auto_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set axis.auto ?')
    else:
        lx.eval('tool.set axis.auto {%s}' % args)


def Action_Center_Axis_Select_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set center.select ?')
    else:
        lx.eval('tool.set center.select {%s}' % args)


def Action_Center_Axis_Element_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set axis.element ?')
    else:
        lx.eval('tool.set axis.element {%s}' % args)


def Action_Center_Axis_Screen_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set axis.view ?')
    else:
        lx.eval('tool.set axis.view {%s}' % args)


def Action_Center_Axis_Origin_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set axis.origin ?')
    else:
        lx.eval('tool.set axis.origin {%s}' % args)


def Action_Center_Axis_Parent_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set axis.parent ?')
    else:
        lx.eval('tool.set axis.parent {%s}' % args)


def Action_Center_Axis_Local_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set axis.local ?')
    else:
        lx.eval('tool.set axis.local {%s}' % args)


def Action_Center_Axis_Pivot_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set axis.pivot ?')
    else:
        lx.eval('tool.set axis.pivot {%s}' % args)


def Action_Center_Item_World_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set actr.worldAxis ?')
    else:
        lx.eval('tool.set actr.worldAxis {%s}' % args)


def Action_Center_Item_Local_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set actr.worldAxis ?')
    else:
        lx.eval('tool.set actr.worldAxis {%s}' % args)


def Action_Center_Item_Parent_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set actr.parentAxis ?')
    else:
        lx.eval('tool.set actr.parentAxis {%s}' % args)


def Element_Mode_Auto_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.elementMode auto ?')
    else:
        lx.eval('tool.elementMode auto {%s}' % args)


def Element_Mode_Auto_Center_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.elementMode autoCent ?')
    else:
        lx.eval('tool.elementMode autoCent {%s}' % args)


def Element_Mode_Vertex_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.elementMode vertex ?')
    else:
        lx.eval('tool.elementMode vertex {%s}' % args)


def Element_Mode_Edge_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.elementMode edge ?')
    else:
        lx.eval('tool.elementMode edge {%s}' % args)


def Element_Mode_Edge_Center_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.elementMode edgeCent ?')
    else:
        lx.eval('tool.elementMode edgeCent {%s}' % args)


def Element_Mode_Polygon_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.elementMode polygon ?')
    else:
        lx.eval('tool.elementMode polygon {%s}' % args)


def Element_Mode_Polygon_Center_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.elementMode polyCent ?')
    else:
        lx.eval('tool.elementMode polyCent {%s}' % args)


def Action_Center_Center_Auto_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr center.auto cenX ?')
    else:
        lx.eval('tool.setAttr center.auto cenX {%s}' % args)


def Action_Center_Center_Auto_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr center.auto cenY ?')
    else:
        lx.eval('tool.setAttr center.auto cenY {%s}' % args)


def Action_Center_Center_Auto_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr center.auto cenZ ?')
    else:
        lx.eval('tool.setAttr center.auto cenZ {%s}' % args)


def Action_Center_Action_Axis_X_Set():
    lx.eval('tool.setAttr axis.auto axis 0')


def Action_Center_Action_Axis_Y_Set():
    lx.eval('tool.setAttr axis.auto axis 1')


def Action_Center_Action_Axis_Z_Set():
    lx.eval('tool.setAttr axis.auto axis 2')


def Action_Center_Handle_None_Set():
    lx.eval('tool.setAttr axis.auto mode 0')


def Action_Center_Handle_Single_Set():
    lx.eval('tool.setAttr axis.auto mode 1')


def Action_Center_Handle_Double_Set():
    lx.eval('tool.setAttr axis.auto mode 2')


def Action_Center_Select_Mode_Center_Set():
    lx.eval('tool.setAttr center.select mode center')


def Action_Center_Select_Mode_Top_Set():
    lx.eval('tool.setAttr center.select mode top')


def Action_Center_Select_Mode_Bottom_Set():
    lx.eval('tool.setAttr center.select mode bottom')


def Action_Center_Select_Mode_Back_Set():
    lx.eval('tool.setAttr center.select mode back')


def Action_Center_Select_Mode_Front_Set():
    lx.eval('tool.setAttr center.select mode front')


def Action_Center_Select_Mode_Right_Set():
    lx.eval('tool.setAttr center.select mode right')


def Action_Center_Select_Mode_Left_Set():
    lx.eval('tool.setAttr center.select mode left')


def Action_Center_Axis_Origin_X_Set():
    lx.eval('tool.setAttr axis.origin axis 0')


def Action_Center_Axis_Origin_Y_Set():
    lx.eval('tool.setAttr axis.origin axis 1')


def Action_Center_Axis_Origin_Z_Set():
    lx.eval('tool.setAttr axis.origin axis 2')


def Action_Center_Axis_Pivot_X_Set():
    lx.eval('tool.setAttr axis.pivot axis 0')


def Action_Center_Axis_Pivot_Y_Set():
    lx.eval('tool.setAttr axis.pivot axis 1')


def Action_Center_Axis_Pivot_Z_Set():
    lx.eval('tool.setAttr axis.pivot axis 2')


def Axis_Rotate_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set xfrm.rotate ?')
    else:
        lx.eval('tool.set xfrm.rotate {%s}' % args)


def Axis_Angle_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.rotate angle ?')
    else:
        lx.eval('tool.setAttr xfrm.rotate angle {%s}' % args)


def Axis_Advanced_Handles_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.rotate mode ?')
    else:
        lx.eval('tool.setAttr xfrm.rotate mode {%s}' % args)


def Axis_SlipUV_OnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr xfrm.rotate lockUV ?')
    else:
        lx.eval('tool.setAttr xfrm.rotate lockUV {%s}' % args)


def Axis_Morph_None_Set():
    lx.eval('tool.setAttr xfrm.rotate morph none')


def Axis_Morph_Transform_Set():
    lx.eval('tool.setAttr xfrm.rotate morph xfrm')


def Axis_Morph_Keep_Positions_Set():
    lx.eval('tool.setAttr xfrm.rotate morph keep')


def Axis_Snap_Angle_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.snapAngle ?')
    else:
        lx.eval('tool.snapAngle {%s}' % args)


def Tool_Reset_Set():
    lx.eval('tool.reset')


def Extrude_Poly_pOnOff(*args):
    if len(args) < 1:
        return lx.eval('tool.set poly.extrude ?')
    else:
        lx.eval('tool.set poly.extrude {%s}' % args)


def Extrude_Poly_X_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.extrude shiftX ?')
    else:
        lx.eval('tool.setAttr poly.extrude shiftX {%s}' % args)


def Extrude_Poly_Y_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.extrude shiftY ?')
    else:
        lx.eval('tool.setAttr poly.extrude shiftY {%s}' % args)


def Extrude_Poly_Z_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.extrude shiftZ ?')
    else:
        lx.eval('tool.setAttr poly.extrude shiftZ {%s}' % args)


def Extrude_Poly_Segments_Value(*args):
    if len(args) < 1:
        return lx.eval('tool.setAttr poly.extrude segs ?')
    else:
        lx.eval('tool.setAttr poly.extrude segs {%s}' % args)


def Extrude_Poly_MakeUV_None_Set():
    lx.eval('tool.setAttr poly.extrude uvs none')


def Extrude_Poly_MakeUV_U_Set():
    lx.eval('tool.setAttr poly.extrude uvs u')


def Extrude_Poly_MakeUV_V_Set():
    lx.eval('tool.setAttr poly.extrude uvs v')


def Extrude_Poly_Mode_Auto_Set():
    lx.eval('tool.setAttr poly.extrude mode auto')


def Extrude_Poly_Mode_Thick_Set():
    lx.eval('tool.setAttr poly.extrude mode thick')


def Extrude_Poly_Mode_Shift_Set():
    lx.eval('tool.setAttr poly.extrude mode shift')


def pyModoTools_Help():
    lx.out('******************HELP FOR PYMODOT(TOOLS)****************************')
    lx.out('********************HAPPY SCRIPTING**********************************')
    lx.out('*********************************************************************')
    lx.out('method with extension _pOnOff : Can be queried or set')
    lx.out('method with extension _pOnOff : blank = GET')
    lx.out('method with extension _pOnOff : 1(one)is ON or 0(zero) is OFF = SET')
    lx.out('method with extension _pOnOff : exampleGET:  yourvariable = functionname(no value here) ')
    lx.out('method with extension _pOnOff : exampleSET:  functionname(1) ')
    lx.out('*********************************************************************')
    lx.out('*********************************************************************')
    lx.out('method with extension _OnOff : Can be queried or set')
    lx.out('method with extension _OnOff : blank = GET')
    lx.out('method with extension _OnOff : 1(one)is ON or 0(zero) is OFF = SET')
    lx.out('method with extension _OnOff : exampleGET:  yourvariable = functionname(no value here) ')
    lx.out('method with extension _OnOff : exampleSET:  functionname(1) ')
    lx.out('*********************************************************************')
    lx.out('*********************************************************************')
    lx.out('method with extension _Value : Can be queried or set')
    lx.out('method with extension _Value : blank = GET')
    lx.out('method with extension _Value : (value) = SET')
    lx.out('method with extension _Value : exampleGET:  yourvariable = functionname(no value here) ')
    lx.out('method with extension _Value : exampleSET:  functionname(9.876)')
    lx.out('*********************************************************************')
    lx.out('*********************************************************************')
    lx.out('method with extension _Set : Can be set only')
    lx.out('method with extension _Set : () = SET')
    lx.out('method with extension _Set : exampleSET:  functionname(no value here) - leave it blank! ')
    lx.out('*********************************************************************')
    lx.out('*********************************************************************')


####################################################
####################################################

def Pipeline_Action_Axis_Auto_Select():
    lx.eval('select.tool axis.auto')


def Pipeline_Action_Axis_Element_Select():
    lx.eval('select.tool axis.element')


def Pipeline_Action_Axis_Local_Select():
    lx.eval('select.tool axis.local')


def Pipeline_Action_Axis_Origin_Select():
    lx.eval('select.tool axis.origin')


def Pipeline_Action_Axis_Parent_Select():
    lx.eval('select.tool axis.parent')


def Pipeline_Action_Axis_Pivot_Select():
    lx.eval('select.tool axis.pivot')


def Pipeline_Action_Axis_Select_Select():
    lx.eval('select.tool axis.select')


def Pipeline_Action_Axis_View_Select():
    lx.eval('select.tool axis.view')


def Pipeline_Action_Center_Auto_Select():
    lx.eval('select.tool center.auto')


def Pipeline_Action_Center_Border_Select():
    lx.eval('select.tool center.border')


def Pipeline_Action_Center_Element_Select():
    lx.eval('select.tool center.element')


def Pipeline_Action_Center_Origin_Select():
    lx.eval('select.tool center.origin')


def Pipeline_Action_Center_Pivot_Select():
    lx.eval('select.tool center.pivot')


def Pipeline_Action_Center_Screen_Select():
    lx.eval('select.tool center.view')


def Pipeline_Action_Center_Select_Select():
    lx.eval('select.tool center.select')


def Pipeline_BackGround_Constraint_Select():
    lx.eval('select.tool const.bg')


def Pipeline_Bend_Select():
    lx.eval('select.tool xfrm.bend')


def Pipeline_Brush_Preset_Select():
    lx.eval('select.tool brush.preset')


def Pipeline_Brush_Preset_Select():
    lx.eval('select.tool brush.smooth')


def Pipeline_Content_Preset_Select():
    lx.eval('select.tool content.preset')


def Pipeline_Drag_Select():
    lx.eval('select.tool xfrm.drag')


def Pipeline_Edge_Add_Loop_Select():
    lx.eval('select.tool edge.addLoop')


def Pipeline_Edge_Bridge_Select():
    lx.eval('select.tool edge.bridge')


def Pipeline_Edge_Knife_Select():
    lx.eval('select.tool edge.knife')


def Pipeline_Edge_Slide_Select():
    lx.eval('select.tool edge.slide')


def Pipeline_Effector_Cleaver_Select():
    lx.eval('select.tool effector.cleaver')


def Pipeline_Effector_Clone_Select():
    lx.eval('select.tool effector.clone')


def Pipeline_Effector_Cutter_Select():
    lx.eval('select.tool effector.cutter')


def Pipeline_Effector_Item_Select():
    lx.eval('select.tool effector.item')


def Pipeline_Effector_Replica_Select():
    lx.eval('select.tool effector.replica')


def Pipeline_Effector_Sweep_Select():
    lx.eval('select.tool effector.sweep')


def Pipeline_Effector_Xform_Select():
    lx.eval('select.tool effector.xform')


def Pipeline_FallOff_AirBrush_Select():
    lx.eval('select.tool falloff.airbrush')


def Pipeline_FallOff_Element_Select():
    lx.eval('select.tool falloff.element')


def Pipeline_FallOff_Image_Select():
    lx.eval('select.tool falloff.image')


def Pipeline_FallOff_Linear_Select():
    lx.eval('select.tool falloff.linear')


def Pipeline_FallOff_Path_Select():
    lx.eval('select.tool falloff.path')


def Pipeline_FallOff_Radial_Select():
    lx.eval('select.tool falloff.radial')


def Pipeline_FallOff_Screen_Select():
    lx.eval('select.tool falloff.screen')


def Pipeline_FallOff_SoftSelection_Select():
    lx.eval('select.tool falloff.softSelection')


def Pipeline_Generator_Array_Select():
    lx.eval('select.tool gen.array')


def Pipeline_Generator_Bezier_Select():
    lx.eval('select.tool gen.bezier')


def Pipeline_Generator_Curve_Select():
    lx.eval('select.tool gen.curve')


def Pipeline_Generator_Helix_Select():
    lx.eval('select.tool gen.helix')


def Pipeline_Generator_Linear_Select():
    lx.eval('select.tool gen.linear')


def Pipeline_Generator_Mirror_Select():
    lx.eval('select.tool gen.mirror')


def Pipeline_Generator_PathSteps_Select():
    lx.eval('select.tool gen.pathseteps')


def Pipeline_Generator_Pen_Select():
    lx.eval('select.tool gen.pen')


def Pipeline_Generator_Scatter_Select():
    lx.eval('select.tool gen.scatter')


def Pipeline_Iamge_Ink_Select():
    lx.eval('select.tool ink.image')


def Pipeline_Jitter_Select():
    lx.eval('select.tool xfrm.jitter')


def Pipeline_Mesh_Topology_Select():
    lx.eval('select.tool mesh.topology')


def Pipeline_Paint_AirBrush_Select():
    lx.eval('select.tool paint.airbrush')


def Pipeline_Paint_Blur_Select():
    lx.eval('select.tool paint.blur')


def Pipeline_Paint_Clone_Select():
    lx.eval('select.tool paint.clone')


def Pipeline_Paint_Eraser_Select():
    lx.eval('select.tool paint.eraser')


def Pipeline_Paint_Fill_Select():
    lx.eval('select.tool paint.fill')


def Pipeline_Paint_Line_Select():
    lx.eval('select.tool paint.line')


def Pipeline_Paint_LinearGradient_Select():
    lx.eval('select.tool paint.linearGradient')


def Pipeline_Paint_Mesh_Select():
    lx.eval('select.tool paint.mesh')


def Pipeline_Paint_PaintBrush_Select():
    lx.eval('select.tool paint.paintbrush')


def Pipeline_Paint_Particle_Select():
    lx.eval('select.tool paint.particle')


def Pipeline_Paint_RadialGradient_Select():
    lx.eval('select.tool paint.radialGradient')


def Pipeline_Paint_Sharp_Select():
    lx.eval('select.tool paint.sharp')


def Pipeline_Paint_Smudge_Select():
    lx.eval('select.tool paint.smudge')


def Pipeline_Poly_Bevel_Select():
    lx.eval('select.tool poly.bevel')


def Pipeline_Poly_Extrude_Select():
    lx.eval('select.tool poly.extrude')


def Pipeline_Poly_LoopSlice_Select():
    lx.eval('select.tool poly.loopSlice')


def Pipeline_Poly_Slice_Select():
    lx.eval('select.tool poly.julienne')


def Pipeline_Poly_SmoothShift_Select():
    lx.eval('select.tool poly.smshift')


def Pipeline_Poly_Sweep_Select():
    lx.eval('select.tool poly.sweep')


def Pipeline_Primitive_Pen_Select():
    lx.eval('select.tool prim.pen')


def Pipeline_Primitive_Sketch_Select():
    lx.eval('select.tool prim.sketch')


def Pipeline_Primitive_Tube_Select():
    lx.eval('select.tool prim.tube')


def Pipeline_Push_Select():
    lx.eval('select.tool xfrm.push')


def Pipeline_Rotate_Select():
    lx.eval('select.tool xfrm.rotate')


def Pipeline_Smooth_Select():
    lx.eval('select.tool xfrm.smooth')


def Pipeline_Snap_Element_Select():
    lx.eval('select.tool snap.element')


def Pipeline_Snap_Pivot_Select():
    lx.eval('select.tool snap.pivot')


def Pipeline_SolidSketch_Select():
    lx.eval('select.tool solid.sketch')


def Pipeline_Transform_Select():
    lx.eval('select.tool xfrm.transform')

