from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Find the starting gas station to complete the circuit.
        
        Key insights:
        1. If total gas < total cost, impossible to complete circuit
        2. If we can't reach station j from station i, then we can't reach j 
           from any station between i and j (they all have negative tank balance)
        3. If a solution exists, it's guaranteed to be unique
        
        Strategy: Greedy one-pass
        - Track total gas surplus/deficit
        - Track current tank from potential starting point
        - If tank goes negative, reset start to next station
        
        Time: O(n), Space: O(1)
        """
        
        n = len(gas)
        total_gas = 0      # Total gas surplus/deficit for entire circuit
        current_tank = 0   # Current gas in tank from start_station
        start_station = 0  # Potential starting station
        
        for i in range(n):
            # Calculate net gas at this station (gain - cost to next)
            net_gas = gas[i] - cost[i]
            
            # Add to both total and current tank
            total_gas += net_gas
            current_tank += net_gas
            
            # If current tank is negative, we can't reach next station from start_station
            # All stations from start_station to i are invalid starting points
            # Try starting from the next station (i + 1)
            if current_tank < 0:
                start_station = i + 1  # Reset starting point
                current_tank = 0        # Reset tank
        
        # If total gas is negative, impossible to complete circuit
        # Otherwise, start_station is the answer
        return start_station if total_gas >= 0 else -1