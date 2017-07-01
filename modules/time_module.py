'''
Time_module.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.1
@date: 01/07/17
@status: WRK
'''

import datetime
import os

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

class Time(object):
    """docstring for Time."""

    def __init__(self, chain):
        self.flag = chain

    def now(self):
        return [False, str(datetime.datetime.now())[:-7]]

    def today(self):
        return [False, str(datetime.date.today())]

    def hour(Self):
        return [False, str(datetime.datetime.now())[11:-10]]

    def custom_hour(self):
        print('=== CUSTOM HOUR ===')
        limit = range(24)
        input_text = 'Hour: '
        range_err = 'please, choose a number betweem 0 or 24'
        value_err = 'you must choose a number'
        hour = validator(limit, input_text, range_err, value_err)

        limit = range(60)
        input_text = 'Minutes: '
        range_err = 'please, choose a number betweem 0 or 59'
        value_err = 'you must choose a number'
        minutes = validator(limit, input_text, range_err, value_err)

        return [True, str(datetime.datetime(2016, 12, 15, hour, minutes, 00))][11:]

    def custom_datetime(self):
        print('=== CUSTOM DATETIME ===')
        # tmp = int(input('0 date\n1 datetime\n> '))
        limit = [0,1]
        input_text = '0 date\n1 datetime\n> '
        range_err = 'please, choose 0 or 1'
        value_err = 'you must choose 0 or 1'
        tmp = validator(limit, input_text, range_err, value_err)
        year = int(input('Year: '))
        month = int(input('Month: '))
        day = int(input('Day: '))
        if tmp == 1:
            hour = int(input('Hour: '))
            minutes = int(input('Minutes: '))
            seconds = int(input('Seconds: '))
        else:
            hour = 00
            minutes = 00
            seconds = 00

        return [True, str(datetime.datetime(year, month, day, hour, minutes, seconds))]

    def get_weekday(self):
        print('=== GET WEEKDAY ===')
        input_text = '0 today\n1 custom\n> '
        range_err = 'please, choose 0 or 1'
        value_err = 'you must choose 0 or 1'
        tmp = validator(limit, input_text, range_err, value_err)
        # tmp = int(input('0 today\n1 custom\n> '))
        if tmp == 0:
            print('=== GET WEEKDAY - TODAY ===')
            return [True, datetime.datetime.today().weekday()] # XXX
        else:
            print('=== GET WEEKDAY - CUSTOM ===')
            custom = self.custom_datetime()
            return [True, custom.weekday()] # XXX


    def delay(self, seconds):
        time.sleep(seconds)
        return True
