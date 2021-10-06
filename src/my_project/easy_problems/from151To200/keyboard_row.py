from typing import List 

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row: List[str] = ["q", "w", "e", "r", "t","y","u","i","o","p"]
        second_row: List[str] = ["a", "s", "d", "f", "g","h","j","k","l"]
        third_row: List[str] = ["z", "x", "c", "v", "b","n","m"]
        flag_first_row = False 
        flag_second_row = False 
        flag_third_row = False 
        to_lowercase_list  = list()
        answer = list()

        for i in range(len(words)):
            to_lowercase_list.append(words[i].lower())


        for i in range(len(words)):
            flag_first_row = False 
            flag_second_row = False 
            flag_third_row = False 

            for letter in to_lowercase_list[i]:

                if letter not in first_row:
                    flag_first_row = True
                    break 

            if flag_first_row == False:
                answer.append(words[i])
                continue

            for letter in to_lowercase_list[i]:

                if letter not in second_row:
                    flag_second_row = True
                    break 

            if flag_second_row == False:
                answer.append(words[i])
                continue


            for letter in to_lowercase_list[i]:

                if letter not in third_row:
                    flag_third_row = True
                    break 

            if flag_third_row == False:
                answer.append(words[i])
                continue
         
        return answer


        


solution = Solution()

print(solution.findWords(words = ["Hello","Alaska","Dad","Peace"]))

print(solution.findWords(words = ["omk"]))

print(solution.findWords(words = ["adsdf","sfd"]))


