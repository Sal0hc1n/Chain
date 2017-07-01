'''
chain_daemon.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.0
@date: 28/06/17
@status: WRK
'''

import datetime
import sys
from os import walk
from time import sleep

from modules.utils.pyJson import pyJson
from modules.utils.chain import set_condition, set_action

# constants
FLAG = True

# utils
PJ = pyJson('data/chains_data')

def loop(sec=1):
    # print(datetime.datetime.now().strftime('%M:%S'))
    print(str(datetime.datetime.now())[:-7])
    i = 0
    conditions = fetch()
    while i < 5: # five second loop
        chain_name = check_condition(conditions)
        if chain_name is not None:
            execute_action(chain_name)
            print('LOG - ',chain_name,'has been Executed')
        sleep(sec)
        i += 1
    loop()

def fetch():
    conditions = []
    onlyfiles = []
    for (dirpath, dirnames, filenames) in walk(PJ.path):
        onlyfiles.extend(filenames)
        break

    for f in onlyfiles:
        conditions.append( [f, PJ.get(f, 'IF') ] )

    return conditions

def check_condition(conditions):
    for condition in conditions:
        # gather informations
        chain_name = condition[0]
        id_module = condition[1]['if_id_module']
        id_condition = condition[1]['if_id_condition']
        cond = condition[1]['condition']

        # check condition
        result = set_condition(id_module, id_condition, cond[1])

        if result is True:
            return chain_name

    return None

def execute_action(chain_name):
    # gather informations
    actions = PJ.get(chain_name, 'THEN')
    id_module = actions['then_id_module']
    id_action = actions['then_id_action']
    action = actions['action']

    # execute action
    set_action(id_module, id_action, action)

if __name__ == '__main__':
    # execute_action(check_condition(fetch()))
    loop()
