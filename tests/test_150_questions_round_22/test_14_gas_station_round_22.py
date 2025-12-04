import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_14_gas_station import Solution

class GasStationTestCase(unittest.TestCase):

    def test_gas_station_first_case(self):
        solution = Solution()
        output = solution.canCompleteCircuit(gas = [1,2,3,4,5], 
                                             cost = [3,4,5,1,2])
        target = 3 
        self.assertEqual(output, target)

    def test_gas_station_second_case(self):
        solution = Solution()
        output = solution.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3])
        target = -1 
        self.assertEqual(output, target)        