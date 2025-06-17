from typing import List 

class Solution:

    def solution_1(self, names: List[str]):

        dic_answer = dict()

        for n in names: 

            if n not in dic_answer:
                dic_answer[n] = 1
            else: 
                dic_answer[n] += 1

        names.sort(key=lambda x: dic_answer[x], reverse=True)

        return names[0], dic_answer[names[0]]
    
    def solution_2(self, names: List[str]):

        names.sort(key=lambda x: len(x), reverse=True)    

        return len(names[0]), names[0]
    
    def solution_3(self, nums: List[str]):

        return len([n for n in nums if n % 7 == 0])    
    
    def solution_4(self, input_file):

        with open(input_file, 'r') as infile, \
             open('odd_numbers.txt', 'w') as odd_numbers, \
             open('even_numbers.txt', 'w') as even_numbers:
            
            for line in infile:
                if not line: 
                    continue
                try: 
                    num = int(line)
                    if num % 2 == 0:
                        even_numbers.write(f'{num}\n')
                    else:
                        odd_numbers.write(f'{num}\n')
                except ValueError:
                    continue
    

solution = Solution()

print(solution.solution_1(names=['mariana','luis','mariana']))

print(solution.solution_2(names=['mariana','luis','leonardo']))

print(solution.solution_3(nums=[7,14,5,6,9]))

solution.solution_4(input_file='numbers.txt')

