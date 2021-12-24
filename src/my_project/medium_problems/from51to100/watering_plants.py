from typing import List 

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        return_count: int  = 0
        temp_capacity: int  = capacity 
        
        len_plants: int = len(plants)
        
        for i in range(len_plants):
            if temp_capacity < plants[i]:
                return_count += i*2
                temp_capacity = capacity - plants[i]
            else: 
                temp_capacity -= plants[i]
                
        
        return len_plants + return_count