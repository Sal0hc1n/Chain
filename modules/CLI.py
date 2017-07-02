'''
CLI.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.4
@date: 28/06/17
@status: WRK
'''

import os

from modules.utils.chain import choose_module, choose_condition, set_condition, choose_action, set_action, validator, new_chain

def CLI():

    os.system('clear')
    print('=-=-= New Chain =-=-=')
    par = []
    name = input('chain name: ')
    path = 'data/chains_data/'+name+'.json'

    os.system('clear')
    print('=+=+= IF =+=+=')
    module_chosen = choose_module('condition')
    par.append(module_chosen)

    os.system('clear')
    print('=*=*= Condition =*=*=')
    condition_chosen = choose_condition(module_chosen)
    par.append(condition_chosen)
    result_condition = set_condition(module_chosen, condition_chosen) # exec later
    par.append(result_condition)

    os.system('clear')
    print('=+=+= THEN =+=+=')
    module_chosen = choose_module('action')
    par.append(module_chosen)

    os.system('clear')
    print('=*=*= Action =*=*=')
    action_chosen = choose_action(module_chosen)
    par.append(action_chosen)
    result_action = set_action(module_chosen, action_chosen)
    par.append(result_action)

    print(par)
    new_chain(path, par)
