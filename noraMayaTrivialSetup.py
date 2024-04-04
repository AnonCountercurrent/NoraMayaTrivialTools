from importlib import reload
import maya.cmds as cmds
import noraTrivialMain
reload(noraTrivialMain)


class NoraTrivialTools:
    def __init__(self):
        self.win_name = 'noraTrivialWin'
        if cmds.menuItem(self.win_name, ex=True):
            cmds.deleteUI(self.win_name)

    def load_window(self):
        if cmds.window(self.win_name, ex=True):
            cmds.deleteUI(self.win_name)
        win = noraTrivialMain.NoraTrivialMain()
        win.show()

