'''
Time_module.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.0
@date: 11/06/17
@status: TBT
'''

import time

from module import Module


class Time(Module):
    """docstring for Time."""

    def __init__(self, args):
        self.cond = True
        self.act = True

    def condition(self, arg):
        switcher = {
            'current_time': current_time
        }
        funAction = switcher[arg]
        funAction()

    def action(self, arg):
        switcher = {
            'current_time': current_time,
            'current_time_formatted': current_time_formatted
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
