from typing import List

class Solution:

    def algo_1(self, input_file):

        
        with open(input_file, 'r') as infile, \
             open('odd_numbers.txt', 'w') as odd_nums, \
             open('even_numbers.txt', 'w') as even_nums:

            for line in infile:
                if not line:
                    continue
                try:
                    num = int(line)
                    if num % 2 == 0:
                        even_nums.write(f'{num}\n')
                    else:
                        odd_nums.write(f'{num}\n')
                except ValueError:
                    continue
    


solution = Solution()

solution.algo_1(input_file='numbers.txt')