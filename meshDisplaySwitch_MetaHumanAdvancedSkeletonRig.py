import maya.cmds as cmds

main_ctrl = 'Main'  # Your actual main control
attr_name = 'meshDisplay'

# Map of your LOD mesh groups
group_sets = {
    'head': ['head_lod0_grp', 'head_lod1_grp', 'head_lod2_grp', 'head_lod3_grp'],
    'body': ['body_lod0_grp', 'body_lod1_grp', 'body_lod2_grp', 'body_lod3_grp']
}

for part, lod_groups in group_sets.items():
    for index, group in enumerate(lod_groups):
        if not cmds.objExists(group):
            print(f"Warning: {group} does not exist. Skipping.")
            continue

        cond_node = f"{group}_vis_cond"
        if not cmds.objExists(cond_node):
            cond_node = cmds.createNode('condition', name=cond_node)

        cmds.setAttr(f"{cond_node}.operation", 0)  # Equal
        cmds.setAttr(f"{cond_node}.firstTerm", index)
        cmds.setAttr(f"{cond_node}.colorIfTrueR", 1)
        cmds.setAttr(f"{cond_node}.colorIfFalseR", 0)

        if not cmds.isConnected(f"{main_ctrl}.{attr_name}", f"{cond_node}.secondTerm"):
            cmds.connectAttr(f"{main_ctrl}.{attr_name}", f"{cond_node}.secondTerm", force=True)

        if not cmds.isConnected(f"{cond_node}.outColorR", f"{group}.visibility"):
            cmds.connectAttr(f"{cond_node}.outColorR", f"{group}.visibility", force=True)