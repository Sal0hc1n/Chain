'''
Module.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.2
@date: 13/06/17
@status: WRK
'''


class Module(object):
    """docstring for Module."""

    def __init__(self):
        self.path = ''
        self.jsn = pyJson(self.path)
        self.jsn.set({'module_name': 'module'})
        self.cond = False  # False: the module doesn't have conditions
        self.act = False  # False: the module doesn't have actions
        self.COND = []
        self.ACT = []

    def get_path(self):
        return self.path

    def get_conditions(self):
        if cond:
            return COND

    def get_actions(self, arg):
        if act:
            return COND

    def condition(self, arg):  # select the condition that has to be executed
        switcher = {
            'example': example
        }
        funAction = switcher[arg]
        funAction()

    def action(self, arg):  # select the action that has to be executed
        switcher = {
            'example': example
        }
        funAction = switcher[arg]
        funAction()
