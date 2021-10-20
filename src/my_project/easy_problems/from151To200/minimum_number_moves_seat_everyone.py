from typing import List 

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        answer: int = 0
        seats.sort()
        students.sort()
        len_seats: int = len(seats)

        for i in range(len_seats):
            answer += abs(seats[i] - students[i])

        return answer 


solution = Solution()

print(solution.minMovesToSeat(seats = [3,1,5], students = [2,7,4]))

print(solution.minMovesToSeat(seats = [4,1,5,9], students = [1,3,2,6]))

print(solution.minMovesToSeat(seats = [2,2,6,6], students = [1,3,2,6]))
