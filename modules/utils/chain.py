'''
chain.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.0
@date: 28/06/17
@status: WRK
'''
# import sys
# sys.path.append("..")
import pandas as pd
import json
import os.path

from modules.utils.pySqlite import pySqlite3
# import modules.utils.module_switcher as module_switcher

import modules.mail_module
import modules.time_module

# ====================== SYSTEM =======================

class System(object):
    """docstring for Mail."""

    def __init__(self, chain):
        self.flag = chain

    def user_input(self):
        return input('> ')

    def equals(self):
        print('=== EQUALS ===')
        module_chosen = choose_module('condition')
        print('=== EQUALS ARG1 ===')
        cond = choose_condition(module_chosen)
        arg1 = set_condition(module_chosen, cond)
        print('=== EQUALS ARG2 ===')
        cond = choose_condition(module_chosen)
        arg2 = set_condition(module_chosen, cond)
        return [arg1 == arg2, [module_chosen, cond, cond]]

    def grater(self):
        print('=== GRATER ===')
        module_chosen = choose_module('condition')
        print('=== GRATER ARG1 ===')
        cond = choose_condition(module_chosen)
        arg1 = set_condition(module_chosen, cond)
        print('=== GRATER ARG2 ===')
        cond = choose_condition(module_chosen)
        arg2 = set_condition(module_chosen, cond)
        return [arg1 > arg2, [module_chosen, cond, cond]]

    def lower(self):
        print('=== LOWER ===')
        module_chosen = choose_module('condition')
        print('=== LOWER ARG1 ===')
        cond = choose_condition(module_chosen)
        arg1 = set_condition(module_chosen, cond)
        print('=== LOWER ARG2 ===')
        cond = choose_condition(module_chosen)
        arg2 = set_condition(module_chosen, cond)
        return [arg1 < arg2, [module_chosen, cond, cond]]

    def puts(self):
        arg = input('> ')
        return arg

# modules
FLAG = True
MAIL = modules.mail_module.Mail(FLAG)
TIME = modules.time_module.Time(FLAG)
SYS = System(FLAG)

# utils
DB = pySqlite3()

def module_switcher(arg):
    switcher = {
        'MAIL': MAIL,
        'TIME': TIME,
        'SYSTEM': SYS
    }
    funAction = switcher[arg]
    return funAction


def validator( limit, input_text, range_err, value_err):
    flag = True

    while flag:
        try:
            chosen = int(input(input_text))

            if chosen not in limit:
                print(range_err)
            else:
                flag = False
                return chosen

        except ValueError as e:
            print(value_err)

def valid(query_result, key):
    # print('query',query_result)
    return list(map(lambda x: int(x[key]), query_result))


def show_modules( where):
    query = '''
        SELECT *
        FROM Module
        WHERE {}=1
    '''.format(where)
    result = DB.execute_check_fetch_dict(query)
    limit = valid(result, 'id_module')
    print(pd.DataFrame(result, columns=['id_module', 'module_name']))

    # returns the range of valid module's id
    return limit

def choose_module( where):
    limit = show_modules(where)
    input_text = 'Module id: '
    range_err = 'The module id must be in the list'
    value_err = 'The module number must be an integer'

    # returns the id of the module chosen by the user
    return validator(limit, input_text, range_err, value_err)

def show_conditions( id_module):
    id_module = (id_module,)
    query = '''
        SELECT *
        FROM condition
        WHERE id_module=?
    '''
    result = DB.execute_check_fetch_dict(query, id_module)
    print(pd.DataFrame(result, columns=[
          'id_condition', 'condition_name']))
    limit = valid(result, 'id_condition')

    # returns the range of valid condition's id
    return limit

def choose_condition( module_chosen):
    limit = show_conditions(module_chosen)
    input_text = 'Condition id: '
    range_err = 'The condition id must be in the list'
    value_err = 'The condition number must be an integer'

    return validator(limit, input_text, range_err, value_err)

def show_actions(id_module):
    id_module = (id_module,)
    query = '''
        SELECT *
        FROM action
        WHERE id_module=?
    '''
    result = DB.execute_check_fetch_dict(query, id_module)
    print(pd.DataFrame(result, columns=['id_action', 'action_name']))
    limit = valid(result, 'id_action')
    return limit

def choose_action(module_chosen):
    limit = show_actions(module_chosen)
    input_text = 'Action id: '
    range_err = 'The action id must be in the list'
    value_err = 'The action number must be an integer'

    # returns the id of the action chosen by the user
    return validator(limit, input_text, range_err, value_err)

def set_condition( id_module, id_condition):
    id_module = (id_module,)
    query = '''
        SELECT module_name
        FROM Module
        WHERE id_module=?
    '''

    result = DB.execute_check_fetch_dict(query, id_module)
    module = module_switcher(result[0]['module_name'].upper())

    id_condition = (id_condition,)

    query = '''
        SELECT condition_name
        FROM Condition
        WHERE id_condition=?
    '''

    condition = DB.execute_check_fetch_dict(query, id_condition)

    # method exec
    return getattr(module, condition[0]['condition_name'])()

def set_action(id_module, id_action):
    id_module = (id_module,)
    query = '''
        SELECT module_name
        FROM Module
        WHERE id_module=?
    '''

    result = DB.execute_check_fetch_dict(query, id_module)
    module = module_switcher(result[0]['module_name'].upper())

    id_action = (id_action,)

    query = '''
        SELECT action_name
        FROM Action
        WHERE id_action=?
    '''

    action = DB.execute_check_fetch_dict(query, id_action)

    # method exec
    return getattr(module, action[0]['action_name'])()

def check_condition( IF_dict): #TODO: DEV
    if_id_module = IF_dict['if_id_module']
    if_id_condition = IF_dict['if_id_condition']
    condition = IF_dict['condition']

# ====================== MAKE CHAIN =======================

def copy(path):
    with open('data/chains_data/base/chain.json', 'r') as f:
        json_data = json.load(f)

    if os.path.isfile(path):
        return False

    with open(path, 'w') as f:
        f.write(json.dumps(json_data))

    return True


def edit(path, if_keys, then_keys, args):
    with open(path, 'r') as f:
        json_data = json.load(f)
        i = 0
        for key in if_keys:
            json_data['IF'][key] = args[i]
            i += 1
        for key in then_keys:
            json_data['THEN'][key] = args[i]
            i += 1

    with open(path, 'w') as f:
        f.write(json.dumps(json_data))


def new_chain(path, args):
    if_keys = ('if_id_module', 'if_id_condition', 'condition')
    then_keys = ('then_id_module', 'then_id_condition', 'action')

    if copy(path):
        edit(path, if_keys, then_keys, args)
        return True
    else:
        return False
