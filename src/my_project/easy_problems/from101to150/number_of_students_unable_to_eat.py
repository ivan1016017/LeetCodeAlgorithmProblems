from typing import List 

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        temp_first_item: int = None
        while sandwiches[0] in students:

            if students[0] == sandwiches[0]:
                students.remove(students[0])
                sandwiches.remove(sandwiches[0])
                if students == sandwiches:
                    return 0
            else: 
                temp_first_item = students[0]
                students = students[1:] + [temp_first_item]
                


        return len(students)

solution = Solution()

print(solution.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))


