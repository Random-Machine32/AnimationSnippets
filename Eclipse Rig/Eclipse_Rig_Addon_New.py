import bpy

bpy.types.Object.selector = bpy.props.EnumProperty(
    items = [
        ('first', 'Bone Property', 'shows the properties of the bone selected'),
        ('second', 'Anti-lag', 'shows the anti-lag options')
    ]
)

bpy.types.Object.CompactMode = bpy.props.BoolProperty(name="Compact Mode")


class EclipseRigPanel(bpy.types.Panel):
    bl_label = "Eclipse Rig"
    bl_idname = "OBJECT_PT_EDGING_RIG"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Eclipse Rig"
    
    @classmethod
    def poll(self, context):
        
        obj = context.active_object
        
        if bpy.context.mode == "POSE" and bpy.context.active_object.get("rig_id") == "Eclipse_Rig":
            return True
        else:
            return False
        
        
    def draw(self, context):
        layout = self.layout
        col = layout.column()

        pose_bones = context.active_object.pose.bones
        selected_bones = [bone.name for bone in context.selected_pose_bones]
        selected_bones += [context.active_pose_bone.name]
        obj = context.object
        
        
        def is_selected(names):
                if obj['open'] == True:
                    return True
                if not obj['open']:
                    for name in names:
                        if name in selected_bones:
                            return True
                    return False
        def is_open(prop, num):
            num1 = int(num)
            if obj[prop] == num1:
                return True
            return False
            
        layout = self.layout    
        box = layout.box
        if obj.CompactMode == True:
            col.column()
        scene = context.scene
        mainB = col.box()
        if obj.CompactMode == True:
            mainB = mainB.column()
        mainB.label(text="Eclipse Rig Addon", icon="ARMATURE_DATA")
        mainB.prop(obj, "CompactMode", toggle = True)
        general_prop = obj.pose.bones["General Properties"]
        larm_prop = obj.pose.bones["ArmProp.L"]
        rarm_prop = obj.pose.bones["ArmProp.R"]
        lleg_prop = obj.pose.bones["LegProp.L"]
        rleg_prop = obj.pose.bones["LegProp.R"]
        face_prop = obj.pose.bones["Face Prop"]
        lfinger_prop = obj.pose.bones["FingerProp.L"]
        rfinger_prop = obj.pose.bones["FingerProp.R"]
        
        
        obn = bpy.context.active_object.name
        bon = bpy.context.active_bone
        
        selection = obj.selector
        if bon.name == "General Properties" or bon.name== "ArmProp.L" or bon.name== "ArmProp.R" or bon.name == "LegProp.L" or bon.name == "LegProp.R" or bon.name == "Face Prop" or bon.name == "FingerProp.L" or bon.name == "FingerProp.R":
            row = mainB.row()
            row.prop(obj, "selector", expand = True)
            if selection == "first":
                
                if bon.name == "General Properties":
                    settings = layout.box()
                    if obj.CompactMode == True:
                        settings = settings.column()
                    settings.label(text="General Settings", icon = "FILE_SCRIPT")
                    head_settings = settings.box()
                    head_settings.label(text="Head Settings", icon = "MONKEY")
                    if obj.CompactMode == True:
                        head_settings = head_settings.column()
                    head_settings.prop(general_prop, '["Global Head Rotation"]', toggle = True)
                    head_settings.prop(general_prop, '["Free Squash and Stretch"]', toggle = True)
                    head_settings.prop(general_prop, '["Squash and Stretch Shape"]', slider = True)
                    body_settings = settings.box()
                    body_settings.label(text="Torso Settings", icon = "MOD_CLOTH")
                    if obj.CompactMode == True:
                        body_settings = body_settings.column()
                    body_settings.prop(general_prop, '["Torso Tweaks"]', toggle = True)
                    row = body_settings.row()
                    row.prop(general_prop, '["Torso Type"]', slider = True)
                    row.prop(general_prop, '["Torso Shape"]', slider = True)
                    body_settings.prop(general_prop, '["Female"]', slider = True)
                    body_settings.prop(general_prop, '["Breathe"]', slider = True)
                    body_settings.prop(general_prop, '["Preset Bones"]', toggle = True)
                
                elif bon.name == "ArmProp.L":
                    settings = layout.box()
                    if obj.CompactMode == True:
                        settings = settings.column()
                    settings.label(text="Arm Settings", icon = "MOD_SKIN")
                    arm_settings = settings.box()
                    if obj.CompactMode == True:
                        arm_settings = arm_settings.column()
                    arm_settings.label(text="Kinematics", icon = "CON_KINEMATIC")
                    arm_settings.prop(larm_prop, '["IK"]', toggle = True)
                    row = arm_settings.row()
                    row.prop(larm_prop, '["IK World"]', toggle = True)
                    row.prop(larm_prop, '["Wrist Lock"]', toggle = True)
                    arm_settings.prop(larm_prop, '["Stretch Shape"]', slider = True)
                    arm_settings = settings.box()
                    if obj.CompactMode == True:
                        arm_settings = arm_settings.column()
                    arm_settings.label(text="Visibility", icon = "HIDE_OFF")
                    arm_settings.prop(larm_prop, '["Tweak"]', toggle = True)
                    arm_settings.prop(larm_prop, '["Twist"]', toggle = True)
                    
                elif bon.name == "ArmProp.R":
                    settings = layout.box()
                    settings.label(text="Arm Settings", icon = "MOD_SKIN")
                    arm_settings = settings.box()
                    if obj.CompactMode == True:
                        arm_settings = arm_settings.column()
                    arm_settings.label(text="Kinematics", icon = "CON_KINEMATIC")
                    arm_settings.prop(rarm_prop, '["IK"]', toggle = True)
                    row = arm_settings.row()
                    row.prop(rarm_prop, '["IK World"]', toggle = True)
                    row.prop(rarm_prop, '["Wrist Lock"]', toggle = True)
                    arm_settings.prop(rarm_prop, '["Stretch Shape"]', slider = True)
                    arm_settings = settings.box()
                    if obj.CompactMode == True:
                        arm_settings = arm_settings.column()
                    arm_settings.label(text="Visibility", icon = "HIDE_OFF")
                    arm_settings.prop(rarm_prop, '["Tweak"]', toggle = True)
                    arm_settings.prop(rarm_prop, '["Twist"]', toggle = True)
                
                elif bon.name == "LegProp.L":
                    settings = layout.box()
                    settings.label(text="Leg Settings",  icon = "POSE_HLT")
                    leg_settings = settings.box()
                    if obj.CompactMode == True:
                        leg_settings = leg_settings.column()
                    leg_settings.label(text="Visibility", icon = "HIDE_OFF")
                    leg_settings.prop(lleg_prop, '["Tweak"]', toggle = True)
                    leg_settings.prop(lleg_prop, '["Twist"]', toggle = True)
                    
                elif bon.name == "LegProp.R":
                    settings = layout.box()
                    settings.label(text="Leg Settings",  icon = "POSE_HLT")
                    leg_settings = settings.box()
                    if obj.CompactMode == True:
                        leg_settings = leg_settings.column()
                    leg_settings.label(text="Visibility", icon = "HIDE_OFF")
                    leg_settings.prop(rleg_prop, '["Tweak"]', toggle = True)
                    leg_settings.prop(rleg_prop, '["Twist"]', toggle = True)
                
                elif bon.name == "Face Prop":
                    settings = layout.box()
                    settings.label(text="Face Settings", icon = "MONKEY")
                    if obj.CompactMode == True:
                        settings = settings.column()
                    eye_settings = settings.box()
                    if obj.CompactMode == True:
                        eye_settings = eye_settings.column()
                    eye_settings.label(text="Eye Settings", icon = "HIDE_OFF")
                    eye_settings.prop(face_prop, '["Eyelashes"]', toggle = True)
                    eye_settings.prop(face_prop, '["Eye Tracker"]', toggle = True)
                    row = eye_settings.row()
                    row.prop(face_prop, '["Eyebrow Follow Eyelid"]', slider = True)
                    row.prop(face_prop, '["Eyebrow Follows"]', slider = True)
                    eye_settings.prop(face_prop, '["Eyelid follow"]', slider = True)
                    eye_settings.prop(face_prop, '["Squishy Blink"]', toggle = True)
                    mouth_settings = settings.box()
                    if obj.CompactMode == True:
                        mouth_settings = mouth_settings.column()
                    mouth_settings.label(text="Mouth Settings", icon = "MATSPHERE")
                    if obj.CompactMode == True:
                        mouth_settings.column()
                    mouth_settings.prop(face_prop, '["Mouth Thickness"]', slider = True)
                    mouth_settings.prop(face_prop, '["Pog Face"]', toggle = True)
                    
                elif bon.name == "FingerProp.L":
                    settings = layout.box()
                    if obj.CompactMode == True:
                        settings = settings.column()
                    settings.label(text="Finger Settings", icon = "VIEW_PAN")
                    settings = settings.row()
                    settings.prop(lfinger_prop, '["Fingers"]', toggle = True)
                    settings.prop(lfinger_prop, '["Fingers+"]', toggle = True)
                    
                elif bon.name == "FingerProp.R":
                    settings = layout.box()
                    if obj.CompactMode == True:
                        settings = settings.column()
                    settings.label(text="Finger Settings", icon = "VIEW_PAN")
                    settings = settings.row()
                    settings.prop(rfinger_prop, '["Fingers"]', toggle = True)
                    settings.prop(rfinger_prop, '["Fingers+"]', toggle = True)
                    
                
            elif selection == "second":
                settings = layout.box()
                if obj.CompactMode == True:
                    settings = settings.column()
                settings.label(text="Anti-lag settings", icon = "ERROR")
                settings.prop(general_prop, '["Anti-Lag Model"]', toggle = True)
                settings.prop(general_prop, '["Bevel Viewport"]', toggle = True)
                sub_settings = settings.box()
                if obj.CompactMode == True:
                    sub_settings = sub_settings.column()
                sub_settings.label(text="Subdivision Settings", icon = "MOD_SUBSURF")
                sub_settings.prop(general_prop, '["Viewport"]', slider = True)
                sub_settings.prop(general_prop, '["Render"]', slider = True)
                
                
        else:
            settings = layout.box()
            if obj.CompactMode == True:
                settings = settings.column()
            settings.label(text="Anti-lag settings", icon = "ERROR")
            settings.prop(general_prop, '["Anti-Lag Model"]', toggle = True)
            settings.prop(general_prop, '["Bevel Viewport"]', toggle = True)
            sub_settings = settings.box()
            if obj.CompactMode == True:
                sub_settings = sub_settings.column()
            sub_settings.label(text="Subdivision Settings", icon = "MOD_SUBSURF")
            sub_settings.prop(general_prop, '["Viewport"]', slider = True)
            sub_settings.prop(general_prop, '["Render"]', slider = True)
            

def register():
    bpy.utils.register_class(EclipseRigPanel)

def unregister():
    bpy.utils.unregister_class(EclipseRigPanel)
    
if __name__ == "__main__":
    register()