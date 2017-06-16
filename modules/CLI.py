'''
CLI.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.2
@date: 16/06/17
@status: DEV
'''
import pandas as pd
from utils.pySqlite3 import pySqlite3
from modules.mail_module import Mail
from modules.time_module import Time
from modules.system_module import System

# costants
MAIL = Mail()
TIME = Time()
SYS = System()
DB = pySqlite3()

def module_switcher(arg):
    switcher = {
        'MAIL': MAIL,
        'TIME': TIME,
        'SYSTEM': SYS
    }
    funAction = switcher[arg]
    return funAction

def validator(limit, input_text, range_err, value_err):
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

def test():
    if_condition = lambda x: x == x
    then_action = lambda x: print('siamo nel ' + str(x))

    CHAIN(if_condition(TIME.current_year()), then_action(TIME.current_year()), None)

def show_modules(where):
    query = '''
        SELECT *
        FROM Module
        WHERE {}=1
    '''.format(where)
    result = DB.execute_check_fetch_dict(query)
    limit = valid(result,'id_module')
    print(pd.DataFrame(result, columns=['id_module', 'module_name']))
    return limit


def choose_module(where):
    limit = show_modules(where)
    input_text = 'Module id: '
    range_err = 'The module id must be in the list'
    value_err = 'The module number must be an integer'

    return validator(limit, input_text, range_err, value_err)


def show_conditions(id_module):
    id_module = (id_module,)
    query = '''
        SELECT *
        FROM condition
        WHERE id_module=?
    '''
    result = DB.execute_check_fetch_dict(query, id_module)
    print(pd.DataFrame(result, columns=[
          'id_condition', 'condition_name']))
    limit = valid(result,'id_condition')
    return limit


def choose_condition(module_chosen):
    limit = show_conditions(module_chosen)
    input_text = 'Condition id: '
    range_err = 'The condition id must be in the list'
    value_err = 'The condition number must be an integer'

    return validator(limit, input_text, range_err, value_err)

def set_condition(id_module, id_condition):
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
    return getattr(module,condition[0]['condition_name'])()



def CLI():
    module_chosen = choose_module('condition')
    print('module_chosen:', module_chosen)
    condition_chosen = choose_condition(module_chosen)
    result = set_condition(module_chosen, condition_chosen)
    print('result',result)
    if result:
        module_chosen = choose_module('action')
    else:
        pass
