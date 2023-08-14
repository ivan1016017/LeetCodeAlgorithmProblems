from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    
	def isSubsequence(self, s: str, t: str) -> bool:
		for i in range (0, len(s)):    
			try:
				index = t.index(s[i])
			except ValueError: 
				return False

			t = t[index+1:]

		return True


class SolutionTwo:
    
    def isSubsequence(self, s: str, t: str) -> bool:
        ## RC ##
        ## APPROACH : 2 POINTERS ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##

        p1 = p2 = 0
        while p1 < len(s) and p2 < len(t):
            # move both pointers or just the right pointer
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        return p1 == len(s)
		
