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
    print('=== Action List ===')
    print('0. New Chain\n1. FUBAR')
    limit = [0, 1]
    input_text = 'Action id: '
    range_err = 'The action id must be in the list'
    value_err = 'The action number must be an integer'

    # returns the id of the action chosen by the user
    val = validator(limit, input_text, range_err, value_err)

    os.system('clear')
    print('=-=-= New Chain =-=-=')
    if val == 0:
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
    else:
        print('FUBAR')
