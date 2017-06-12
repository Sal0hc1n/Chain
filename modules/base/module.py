'''
Module.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.1
@date: 11/06/17
@status: WRK
'''


class Module(object):
    """docstring for Module."""

    def __init__(self, args):
        self.cond = False  # False: the module doesn't have conditions
        self.act = False  # False: the module doesn't have actions

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
