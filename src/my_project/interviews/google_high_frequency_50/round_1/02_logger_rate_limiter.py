from typing import List 
from collections import defaultdict


class Logger:

    def __init__(self):
        self.logger_dict = defaultdict(int)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message not in self.logger_dict:
            self.logger_dict[message] = timestamp
            return True 
        else: 
            if timestamp - self.logger_dict[message] >= 10:
                self.logger_dict[message] = timestamp
                return True 
            else: 
                return False 


