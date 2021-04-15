import re

file_name = 'valid_phone_numbers.txt'

class Solution():

    def validPhoneNumbers(self, entry_str: str) -> str:
        sample = entry_str
        pattern = re.compile(r'[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9] |'
                             r'[(][0-9][0-9][0-9][)] [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')
        matches = pattern.finditer(sample)
        temp = ""
        for item in matches:
            temp += item.group(0) + " "
        return temp

