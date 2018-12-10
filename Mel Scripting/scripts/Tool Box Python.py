import maya.cmds as cmds

class Toolbox():
    def __init__(self):
        self.mWin = 'Toolbox'

    def create(self):
        self.delete()

        self.mWin = cmds.window(self.mWin, title='My Toolbox')
        self.mCol = cmds.columnLayout(parent=self.mWin, adjustableColumn=True)
        cmds.button(parent=self.mCol, label='Renamer', command=lambda x: self.renameWin())
        cmds.button(parent=self.mCol, label='Locator', command=lambda x: self.locatorWin())
        cmds.button(parent=self.mCol, label='Random Placement Generator', command=lambda x: self.renameWin())
        cmds.button(parent=self.mCol, label='Control Creator', command=lambda x: self.locatorWin())
        cmds.button(parent=self.mCol, label='FK Joint Hierarchy Builder', command=lambda x: self.locatorWin())
        
        cmds.showWindow(self.mWin)

    def delete(self):
        if cmds.window(self.mWin, q=True, exists=True):
            cmds.deleteUI(self.mWin)

    def renameWin(self):
        import renamer
        renameTool = renamer.RenamerUI()
        renameTool.create()

    def locatorWin(self):
        import locatorTool
        locatorToolUI = locatorTool.LocatorTool()
        locatorToolUI.create()
        
    def renameWin(self):
        import renamer
        renameTool = renamer.RenamerUI()
        renameTool.create()

    def locatorWin(self):
        import locatorTool
        locatorToolUI = locatorTool.LocatorTool()
        locatorToolUI.create()
        
    def locatorWin(self):
        import locatorTool
        locatorToolUI = locatorTool.LocatorTool()
        locatorToolUI.create()
        
myVar =Toolbox()
myVar.create()         