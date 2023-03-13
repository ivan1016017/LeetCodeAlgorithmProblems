from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        '''
        1971/01/01: Friday
        '''
        week = {0:'Friday', 1:'Saturday', 2:'Sunday', 3:'Monday', 4:'Tuesday', 5:'Wednesday', 6:'Thursday'}
        mon = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30}
        
        leap_num = 1 + (year-1-1972)//4 if year > 1971 else 0
		#calculate number of leap year from 1971 to (year-1) (both inclusive)
        year_total = (year-1971)*365 + leap_num
        month_total = sum([mon[i] for i in mon if i < month])
		#calculate number of days in the given year from January to (month-1) (both inclusive)
     
        if (year%4 == 0 and year%100 or year%400 == 0) and month > 2:
            res = year_total + month_total + day + 1
        else:
            res = year_total + month_total + day

        return week[(res-1)%7]