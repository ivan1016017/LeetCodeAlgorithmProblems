from typing import List 

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        s1 = s1.split(' ')
        s2 = s2.split(' ')
        dictionary_one = dict()
        dictionary_two = dict() 

        for word in s1: 
            dictionary_one[word] = 0

        for word in s2: 
            dictionary_two[word] = 0

        for word in s1: 
            dictionary_one[word] += 1
        for word in s2: 
            dictionary_two[word] += 1
        solution_list = list()

        first_list = list()
        second_list = list()

        for word in s1:
            if word not in s2 and dictionary_one[word] == 1:
                first_list.append(word)

        for word in s2:
            if word not in s1 and word not in first_list and dictionary_two[word] ==1:
                second_list.append(word)

        for word in first_list + second_list:
            solution_list.append(word)

        return solution_list


solution = Solution()

print(solution.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))

print(solution.uncommonFromSentences(s1 = "apple apple", s2 = "banana"))
