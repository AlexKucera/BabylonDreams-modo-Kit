#!/usr/bin/python


# pyModoS (Schematics)
#Author Keith Sheppard
#2/23/2015 6:24:08 PM


#importing pyModo for schematic operations
import pyModo as so
import lx


def ChanMod_Channel_Noise_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmNoise} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Channel_Oscillator_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmOscillator} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Channel_Relation_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmChannelRelation} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Channel_Sound_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmSound} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Channel_WaveForm_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmWaveform} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Color_Blend_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmColorBlend} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Color_Correct_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmColorCorrect} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Color_Gamma_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmColorGamma} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Color_HSV_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmColorHSV} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Color_Invert_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmColorInvert} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Color_Kelvin_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmColorKelvin} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Condition_A_Equals_B_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmLogic:equal} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Condition_A_GreaterThan_B_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmLogic:greaterThan} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Condition_A_GreaterThanOrEquals_B_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmLogic:greaterThanOrEqual} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Condition_A_LessThan_B_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmLogic:lessThan} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Condition_A_LessThanOrEquals_B_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmLogic:lessThanOrEqual} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Condition_A_NotEqualTo_B_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmLogic:notEqual} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Condition_AND_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmLogic:and} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Condition_OR_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmLogic:or} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Constraint_Direction_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmDirectionConstraint} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Constraint_Distance_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmDistanceConstraint } insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Constraint_Geometry_Normal_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmGeometryConstraint:normal} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Constraint_Geometry_Position_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmGeometryConstraint:position} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Constraint_Path_Normal_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmPathConstraint:curveNormal} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Constraint_Path_Path_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmPathConstraint:curvePath} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Constraint_Path_Position_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmPathConstraint:curvePosition} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Constraint_Transform_Position_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmTransformConstraint:pos} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Constraint_Transform_Rotation_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmTransformConstraint:rot} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Constraint_Transform_Scale_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmTransformConstraint:scl} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Basic_Addition_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathBasic:add} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Basic_Average_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathBasic:avg} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Basic_Divide_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathBasic:div} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Basic_Max_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathBasic:max} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Basic_Min_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathBasic:min} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Basic_Modulo_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathBasic:mod} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Basic_Multiply_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathBasic:mul} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Basic_Substract_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathBasic:sub} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Multiple_Addition_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathMulti:add} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Multiple_Average_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathMulti:avg} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Multiple_Divide_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathMulti:div} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Multiple_Max_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathMulti:max} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Multiple_Min_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathMulti:min} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Multiple_Multiply_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathMulti:mul} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Multiple_Substract_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathMulti:sub} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Absolute_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMath:abs} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Ceiling_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMath:ceil} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Constant_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmConstant} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Exp_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMath:exp} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Floor_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMath:floor} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Log_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMath:log} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Log10_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMath:log10} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Power_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMath:pow} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_SqareRoot_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMath:sqrt} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Trig_Cos_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathTrig:cos} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Trig_Sin_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathTrig:sin} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Math_Trig_Tan_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathTrig:tan} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Matrix_Blend_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMatrixBlend} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Matrix_Compose_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMatrixCompose} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Matrix_Construct_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMatrixConstruct} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Matrix_From_Euler_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMatrixFromEuler} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Matrix_To_Euler_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMatrixToEuler} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Matrix_Transpose_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMatrixTranspose} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Matrix_Vector_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMatrixVector} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Measure_Angle_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMeasureAngle} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Measure_Distance_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMeasureDistance} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Measure_Speed_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmSpeed} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Measure_Velocity_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmVelocity} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Probe_Curve_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmCurveProbe} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Probe_Falloff_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {probeFalloff} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Time_Time_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmTime} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Time_Cycler_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmCycler} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Time_Offset_Float_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmFloatOffset} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Time_Offset_Matrix_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMatrixOffset} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Time_Warp_Float_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmFloatWarp} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Time_Warp_Matrix_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMatrixWarp} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Vector_Math_Addition_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathVector:add} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Vector_Math_CrossProduct_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathVector:cross} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Vector_Math_DotProduct_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathVector:dot} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Vector_Math_Subtract_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmMathVector:sub} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Vector_Magnitude_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmVectorMagnitude} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Vector_None_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmVector:none} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Vector_Normalize_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmVector:norm} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Vector_Set_Length_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmVector:setLen} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Other_Clamp_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create { cmClamp} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Other_Dual_Joint_Planar_IK_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmIKDual2D} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Other_Dynamic_Parent_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmDynamicParent} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Other_Expression_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {Expression} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Other_Intersect_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmIntersect} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Other_Linear_Blend_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmLinearBlend} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Other_Random_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmRandom} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Other_Randomize_ID_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmPID} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Other_Revolve_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmRevolve} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Other_Simple_Kinematics_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmSimpleKinematics} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Other_Smooth_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmSmooth} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def ChanMod_Other_Switch_ToNode():
    __Init_WorkSpace()
    lx.eval('channelModifier.create {cmSwitch} insert:true')
    Node_Add_ItemToSchematic_ifSelected()


def Matrix_Channel_Effect_ToNode():
    __Init_WorkSpace()
    lx.eval('schematic.createItem ceMatrix')
    Node_Add_ItemToSchematic_ifSelected()


def Shader_Input_Shader_Input_ToNode():
    __Init_WorkSpace()
    lx.eval('shaderInput.create cmShaderEffects')
    Node_Add_ItemToSchematic_ifSelected()


def Shader_Input_Illuminate_ToNode():
    __Init_WorkSpace()
    lx.eval('shaderInput.create cmShaderLighting')
    Node_Add_ItemToSchematic_ifSelected()


def Shader_Input_RayType_ToNode():
    __Init_WorkSpace()
    lx.eval('shaderInput.create cmShaderRayType')
    Node_Add_ItemToSchematic_ifSelected()


def Shader_Input_RayCast_ToNode():
    __Init_WorkSpace()
    lx.eval('shaderInput.create cmShaderRaycast')
    Node_Add_ItemToSchematic_ifSelected()


def Shader_Input_Particle_Sample_ToNode():
    __Init_WorkSpace()
    lx.eval('cmShader.addInput {particleSample} true')
    Node_Add_ItemToSchematic_ifSelected()


def Shader_Input_Sample_Position_ToNode():
    __Init_WorkSpace()
    lx.eval('cmShader.addInput {sample.position} true')
    Node_Add_ItemToSchematic_ifSelected()


def Shader_Input_Sample_Ray_ToNode():
    __Init_WorkSpace()
    lx.eval('cmShader.addInput {sample.ray} true')
    Node_Add_ItemToSchematic_ifSelected()


def Shader_Input_Surface_Normal_ToNode():
    __Init_WorkSpace()
    lx.eval('cmShader.addInput { surface.normal} true')
    Node_Add_ItemToSchematic_ifSelected()


def Node_Delete_All_Channels(Requires_ItemID):
    __pyModo_Node_Del_Channels(Requires_ItemID, 'Del_ALLChannels')


def Node_Delete_Single_Channel(Requires_ItemID, ChannelName):
    __pyModo_Node_Del_Channels(Requires_ItemID, ChannelName)


def __pyModo_Node_Del_Channels(Requires_ItemID, strWhatToDelete):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:

        if strWhatToDelete != 'Del_ALLChannels':
            strWhatToDelete = strWhatToDelete.lower()
            Node_Select_Channel(EachItem, strWhatToDelete)
            lx.eval('schematic.remChannel')

        if strWhatToDelete == 'Del_ALLChannels':
            ChList = so.Item_Channel_Get_Names(EachItem)
            for eachCh in ChList:
                Node_Select_Channel(EachItem, eachCh)
                lx.eval('schematic.remChannel')


def Node_Add_All_Channels(Requires_ItemID):
    __pyModo_Node_Add_Channels(Requires_ItemID, 'Add_ALLChannels')


def Node_Add_Single_Channel(Requires_ItemID, ChannelName):
    __pyModo_Node_Add_Channels(Requires_ItemID, ChannelName)


def __pyModo_Node_Add_Channels(Requires_ItemID, strWhatToAdd):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:

        if strWhatToAdd != 'Add_ALLChannels':
            strWhatToAdd = strWhatToAdd.lower()
            Node_Select_Node(EachItem)
            lx.eval('schematic.addChannel chanIdx:%s' % strWhatToAdd)

        if strWhatToAdd == 'Add_ALLChannels':
            ChList = so.Item_Channel_Get_Names(EachItem)
            Node_Select_Node(EachItem)
            for eachCh in ChList:
                lx.eval('schematic.addChannel chanIdx:%s' % eachCh)


def Node_Select_Channel(Requires_OneItemID, ChannelName):
    if type(Requires_OneItemID) is list:
        TheList = Requires_OneItemID
    else:
        TheList = str.split(Requires_OneItemID, ',')

    for EachItem in TheList:
        lx.eval('select.channel {%s:%s} set' % (EachItem, ChannelName))


def Node_Select_Node(Requires_OneItemID):
    if type(Requires_OneItemID) is list:
        TheList = Requires_OneItemID
    else:
        TheList = str.split(Requires_OneItemID, ',')

    for EachItem in TheList:

        SchemeID = Node_Schematic_ID_Get(EachItem)

        for eachID in SchemeID:
            lx.eval('select.node %s set %s' % (eachID, eachID))


def Node_DeSelect_All():
    lx.eval('select.drop schmNode')


def Node_Add_ItemToSchematic_ifSelected():
    lx.eval('schematic.addItem')


def Node_Add_ItemToSchematic(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        lx.eval('schematic.addItem %s' % EachItem)


def Node_Connect_Channels(FromID, FromChannel, ToID, ToChannel):
    linkCh_Add = 'channel.link add ' + '{' + FromID + ':' + FromChannel + '} ' + '{' + ToID + ':' + ToChannel + '}'
    lx.eval(linkCh_Add)


def Node_DisConnect_Channels(FromID, FromChannel, ToID, ToChannel):
    linkCh_Rem = 'channel.link rem ' + '{' + FromID + ':' + FromChannel + '} ' + '{' + ToID + ':' + ToChannel + '}'
    lx.eval(linkCh_Rem)


def Node_Replace_Channel_Link(FromID, FromChannel, ToID, ToChannel):
    linkCh_Rep = 'channel.link replace ' + '{' + FromID + ':' + FromChannel + '} ' + '{' + ToID + ':' + ToChannel + '}'
    lx.eval(linkCh_Rep)


def Node_Remove_Node(Requires_ItemID):
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:
        Node_Select_Node(EachItem)
        lx.eval('schematic.remNode')


def Node_Connection_Test_ViewLog(FromID, FromChannel, ToID):
    __Node_Connection_Test(FromID, FromChannel, ToID, 'ViewLog')


def Node_Connection_Test_GetData(FromID, FromChannel, ToID):
    __Node_Connection_Test(FromID, FromChannel, ToID, 'GetData')


def __Node_Connection_Test(FromID, FromChannel, ToID, OutPut):
    ConTest = []
    FromName = so.Item_Name_Get(FromID)
    ToName = so.Item_Name_Get(ToID)
    Node_Add_ItemToSchematic(FromID)
    Node_Add_Single_Channel(FromID, FromChannel)
    Node_Add_ItemToSchematic(ToID)
    Node_Delete_All_Channels(ToID)

    Channel_List = so.Item_Channel_Get_Names(ToID)

    for eachCh in Channel_List:
        Node_Add_Single_Channel(ToID, eachCh)
        Node_Select_Channel(FromID, FromChannel)
        lx.eval('select.channel {%s:%s} add' % (ToID[0], eachCh))

        try:
            lx.eval('!channel.link toggle')
            ConTest.append(FromName + ' Channel: ' + FromChannel + ' To:' + ToName + ' Channel: ' + eachCh + '=' + 'Passed Connection Test')
            lx.eval('!channel.link toggle')

        except:
            ConTest.append(FromName + ' Channel: ' + FromChannel + ' To:' + ToName + ' Channel: ' + eachCh + '=' + 'Failed Connection Test')

    Node_Delete_All_Channels(FromID)
    Node_Delete_All_Channels(ToID)
    Node_Remove_Node(FromID)
    Node_Remove_Node(ToID)

    if OutPut == 'ViewLog':
        lx.eval('log.masterClear')
        for results in ConTest:
            so.Modo_Log(results)

    if OutPut == 'GetData':
        return ConTest


def Node_ParentTo_NodesFolder(Requires_ShaderTreeItemID):
    if type(Requires_ShaderTreeItemID) is list:
        TheList = Requires_ShaderTreeItemID
    else:
        TheList = str.split(Requires_ShaderTreeItemID, ',')

    for EachItem in TheList:
        lx.eval('texture.parent shaderFolder009 -1')


def Node_Schematic_Name_Get(Requires_ItemID):
    return __pyModo_Node_Schematic(Requires_ItemID, 'name')


def Node_Schematic_ID_Get(Requires_ItemID):
    return __pyModo_Node_Schematic(Requires_ItemID, 'id')


def __pyModo_Node_Schematic(Requires_ItemID, OutPut):
    Node_List = []
    if type(Requires_ItemID) is list:
        TheList = Requires_ItemID
    else:
        TheList = str.split(Requires_ItemID, ',')

    for EachItem in TheList:

        ItemName = so.Item_Name_Get(EachItem)

        SceneIDs = so.Scene_Get_Item_IDs_All()

        for eachID in SceneIDs:
            if eachID[:8] == 'schmNode':
                lx.eval('select.node %s set %s' % (eachID, eachID))
                NodeName = so.AfterItem_Create_or_Select_getItemName()
                #match item and schematic node ID
                if NodeName == ItemName:
                    if OutPut == 'name':
                        Node_List.append(NodeName)
                    if OutPut == 'id':
                        Node_List.append(eachID)

    return Node_List


def __Init_WorkSpace():
    Group_List = []

    SceneTags = so.Scene_Get_Item_Tags_All()

    for Tags in SceneTags:
        if Tags != None:
            for eachTag in Tags:
                if eachTag == 'workspace':
                    Group_List.append(eachTag)

    if not Group_List:
        WorkSpace_Create_CanSetName()
        __Init_WorkSpace()

    if Group_List:
        so.Item_Select(Group_List[0])
        WorkSpace_Select(Group_List[0])


def WorkSpace_Create_CanSetName(DefaultName='WorkSpace'):
    lx.eval('schematic.createWorkspace {%s} true' % DefaultName)


def WorkSpace_Select(Requires_ItemID):
    lx.eval('schematic.viewAssembly {%s} mode:workspace' % Requires_ItemID)


def Assembly_Create_fromSelectedItems(Requires_Name):
    lx.eval('group.create {%s} asm selItems ' % Requires_Name)


def Schematic_SetView_WorkSpace(RequiresItemID):
    lx.eval('schematic.setView workspace {%s}' % RequiresItemID)


def Schematic_SetView_Assembly(RequiresItemID):
    lx.eval('schematic.setView assembly {%s}' % RequiresItemID)


def Schematic_OverView_Layout_All():
    lx.eval('schematic.setView overview')


def Schematic_OverView_Layout_Item(RequiresItemID):
    lx.eval('schematic.setView overview {%s}' % RequiresItemID)


def Node_Delete_Channel_ifSelected():
    lx.eval('channel.delete')


###########################################################################
###########################################################################
###########################################################################
