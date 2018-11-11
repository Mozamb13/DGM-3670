import maya.cmds as cmds

def CreateJoint():
    sels = cmds.ls(selection=True)
    cmds.select(cl = True)

    for sel in sels:
        cmds.matchTransform(cmds.joint(), sel)

CreateJoint()