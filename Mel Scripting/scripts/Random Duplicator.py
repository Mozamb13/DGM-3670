import maya.cmds as cmds
import random

def RandPlac (dup, xMin, yMin, zMin, xMax, yMax, zMax):
    
    sel = cmds.ls(selection=True)
    
    randDup = dup
    
    xMinRand= xMin
    xMaxRand= xMax
    yMinRand= yMin
    yMaxRand= yMax
    zMinRand= zMin
    zMaxRand= zMax
    
    i=0
    while i < randDup:
        
        sel.append(cmds.duplicate(sel[0], rr=True))
        
        yMove = random.randrange(yMinRand, yMaxRand)
        xMove = random.randrange(xMinRand, xMaxRand)
        zMove = random.randrange(zMinRand, zMaxRand)
        
        
        cmds.move (xMove, yMove, zMove, sel[i], r=True, ws=True)
        
        i+=1
        
RandPlac(5,3,3,3,8,8,8)        