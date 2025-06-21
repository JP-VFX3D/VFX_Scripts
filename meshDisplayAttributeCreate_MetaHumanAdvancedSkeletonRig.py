import maya.cmds as cmds

ctrl = 'Main'

# If attribute doesn't exist, add it
if not cmds.attributeQuery('meshDisplay', node=ctrl, exists=True):
    cmds.addAttr(ctrl, longName='meshDisplay', attributeType='enum', enumName='Ultra:High:Medium:Low')
    
# Now make it non-keyable but visible in Channel Box
cmds.setAttr(f"{ctrl}.meshDisplay", edit=True, keyable=False, channelBox=True)
