'''
chain.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.1
@date: 30/06/17
@status: WRK
'''

# import sys
# sys.path.append("..")
import pandas as pd
import json
import os.path

from modules.utils.pySqlite import pySqlite3

import modules.mail_module
import modules.time_module

# ====================== SYSTEM =======================

class System(object):
    """docstring for Mail."""

    def __init__(self, chain):
        self.flag = chain

    def user_input(self):
        return input('> ')

    def equals(self, args=None):
        if args is None:
            print('=== EQUALS ===')
            module_chosen = choose_module('condition')
            print('=== EQUALS ARG1 ===')
            cond1 = choose_condition(module_chosen)
            arg1 = set_condition(module_chosen, cond1)
            print('=== EQUALS ARG2 ===')
            cond2 = choose_condition(module_chosen)
            arg2 = set_condition(module_chosen, cond2)
            if arg1[0] is True:
                return [arg1[1] == arg2, [module_chosen, cond1, cond2, True, arg1[1]]]
            elif arg2[0] is True:
                return [arg1 == arg2[1], [module_chosen, cond1, cond2, False, arg2[1]]]
            else:
                return [arg1 == arg2, [module_chosen, cond1, cond2, None]]
        else:
            if args[3] is True:
                arg1 = args[4]
                arg2 = set_condition(args[0], args[2])[1]
                return arg1 == arg2
            elif args[3] is False:
                arg1 = set_condition(args[0], args[1])[1]
                arg2 = args[4]
                return arg1 == arg2
            elif args[3] is None:
                arg1 = set_condition(args[0], args[1])[1]
                arg2 = set_condition(args[0], args[2])[1]
                return arg1 == arg2

    def grater(self, args=None):
        if args is None:
            print('=== GRATER ===')
            module_chosen = choose_module('condition')
            print('=== GRATER ARG1 ===')
            cond1 = choose_condition(module_chosen)
            arg1 = set_condition(module_chosen, cond1)
            print('=== GRATER ARG2 ===')
            cond2 = choose_condition(module_chosen)
            arg2 = set_condition(module_chosen, cond2)
            if arg1[0] is True:
                return [arg1[1] > arg2, [module_chosen, cond1, cond2, True, arg1[1]]]
            elif arg2[0] is True:
                return [arg1 > arg2[1], [module_chosen, cond1, cond2, False, arg2[1]]]
            else:
                return [arg1 > arg2, [module_chosen, cond1, cond2, None]]
        else:
            if args[3] is True:
                arg1 = args[4]
                arg2 = set_condition(args[0], args[2])[1]
                return arg1 > arg2
            elif args[3] is False:
                arg1 = set_condition(args[0], args[1])[1]
                arg2 = args[4]
                return arg1 > arg2
            elif args[3] is None:
                arg1 = set_condition(args[0], args[1])[1]
                arg2 = set_condition(args[0], args[2])[1]
                return arg1 > arg2

    def lower(self):
        if args is None:
            print('=== LOWER ===')
            module_chosen = choose_module('condition')
            print('=== LOWER ARG1 ===')
            cond1 = choose_condition(module_chosen)
            arg1 = set_condition(module_chosen, cond1)
            print('=== LOWER ARG2 ===')
            cond2 = choose_condition(module_chosen)
            arg2 = set_condition(module_chosen, cond2)
            if arg1[0] is True:
                return [arg1[1] < arg2, [module_chosen, cond1, cond2, True, arg1[1]]]
            elif arg2[0] is True:
                return [arg1 < arg2[1], [module_chosen, cond1, cond2, False, arg2[1]]]
            else:
                return [arg1 < arg2, [module_chosen, cond1, cond2, None]]
        else:
            if args[3] is True:
                arg1 = args[4]
                arg2 = set_condition(args[0], args[2])[1]
                return arg1 < arg2
            elif args[3] is False:
                arg1 = set_condition(args[0], args[1])[1]
                arg2 = args[4]
                return arg1 < arg2
            elif args[3] is None:
                arg1 = set_condition(args[0], args[1])[1]
                arg2 = set_condition(args[0], args[2])[1]
                return arg1 < arg2

    def puts(self, args=None):
        if args is None:
            arg = input('> ')
            return arg
        else:
            print(args)

    def putz(self): # TODO: print a function result
        input_text = '0 custom\n1 from module\n> '
        range_err = 'please, choose 0 or 1'
        value_err = 'you must choose 0 or 1'
        tmp = validator(limit, input_text, range_err, value_err)
        if tmp == 0:
            arg = input('> ')
            return arg
        else:
            pass

# ====================== CHAIN =======================

# modules
FLAG = False
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

def set_condition(id_module, id_condition, args=None):
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

    if args is None:
        # method exec
        return getattr(module, condition[0]['condition_name'])()
    else:
        # method exec with parameters
        return getattr(module, condition[0]['condition_name'])(args)

def set_action(id_module, id_action, args=None):
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

    if args is None:
        # method exec
        return getattr(module, action[0]['action_name'])()
    else:
        # method exec with parameters
        return getattr(module, action[0]['action_name'])(args)

# ====================== MAKE CHAIN =======================

def copy(path):
    with open('data/chains_data/base/chains_template.json', 'r') as f:
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
    then_keys = ('then_id_module', 'then_id_action', 'action')

    if copy(path):
        edit(path, if_keys, then_keys, args)
        return True
    else:
        return False
