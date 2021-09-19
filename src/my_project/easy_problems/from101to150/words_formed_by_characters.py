from typing import List 
from collections import defaultdict
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        flag: bool = False
        list_solutions_strings = list()
        dict_word = None 
        dict_chars = None 
        
        def from_string_to_dict(word:str) -> dict():            
            temp_dict = defaultdict(int)
            for letter in word:
                temp_dict[letter] += 1
            return temp_dict

        for word in words:
            flag = False
            dict_word = from_string_to_dict(word)
            dict_chars = from_string_to_dict(chars)
            
            for letter in word:

                if letter not in chars:
                    flag = True 
                    break 
                if letter in chars:
                    if dict_word[letter] > dict_chars[letter]:
                        flag = True
                        break 


            if flag == False:
                list_solutions_strings.append(word)


        return sum([len(word) for word in list_solutions_strings])

solution = Solution()

print(solution.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))

print(solution.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))
