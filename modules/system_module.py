'''
system_module.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 0.1
@date: 15/06/17
@status: DEV
'''

import modules.CLI
from modules.base.module import Module

class System(Module):
    """docstring for Mail."""

    def __init__(self):
        self.cond = True
        self.act = True

    def user_input(self):
        return input('> ')

    def equals(self):
        print('===EQUALS===')
        module_chosen = modules.CLI.choose_module('condition')
        print('===EQUALS ARG1===')
        cond = modules.CLI.choose_condition(module_chosen)
        arg1 = modules.CLI.set_condition(module_chosen,cond)
        print('===EQUALS ARG2===')
        cond = modules.CLI.choose_condition(module_chosen)
        arg2 = modules.CLI.set_condition(module_chosen,cond)
        return arg1 == arg2

    def puts(self):
        arg = input('> ')
        print(arg)
