'''
Time_module.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 0.2
@date: 13/06/17
@status: TBT
'''

import time

from modules.base.module import Module
from utils.pyJson import pyJson


class Time(Module):
    """docstring for Time."""

    def __init__(self):
        self.path = 'data/modules_data/time.json'
        self.jsn = pyJson(self.path)
        self.jsn.set({'module_name': 'Time_module'})
        self.cond = True
        self.act = True
        self.COND = ['current_time', 'current_year', 'current_month', 'current_month_day',
                     'current_hour', 'current_min', 'current_sec', 'current_week_day', 'current_year_day']
        self.ACT = ['current_time', 'current_time_formatted', 'delay']

    def condition(self, arg):
        switcher = {
            self.COND[0]: current_time,
            self.COND[1]: current_year,
            self.COND[2]: current_month,
            self.COND[3]: current_month_day,
            self.COND[4]: current_hour,
            self.COND[5]: current_min,
            self.COND[6]: current_sec,
            self.COND[7]: current_week_day,
            self.COND[8]: current_year_day
        }
        funAction = switcher[arg]
        funAction()

    def action(self, arg):
        switcher = {
            self.ACT[0]: current_time,
            self.ACT[1]: current_time_formatted,
            self.ACT[2]: delay
        }
        funAction = switcher[arg]
        funAction()

    def current_time(self):
        '''time.struct_time(tm_year=2017, tm_mon=6, tm_mday=11, tm_hour=17, tm_min=55, tm_sec=51, tm_wday=6, tm_yday=162, tm_isdst=1)'''
        return time.localtime(time.time())

    def current_year(self):
        return self.current_time[0]

    def current_month(self):
        return self.current_time[1]

    def current_month_day(self):
        return self.current_time[2]

    def current_hour(self):
        return self.current_time[3]

    def current_min(self):
        return self.current_time[4]

    def current_sec(self):
        return self.current_time[5]

    def current_week_day(self):
        return self.current_time[6]

    def current_year_day(self):
        return self.current_time[7]

    def current_time_formatted(self):
        '''Sun Jun 11 17:58:32 2017'''
        return time.asctime(time.localtime(time.time()))

    def delay(self):
        seconds = self.jsn.get('seconds')
        time.delay(seconds)
