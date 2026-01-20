from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution: 

    def calculate(self, s: str) -> int:
        """
        Evaluate a basic calculator expression with +, -, and parentheses.
        Uses a stack to handle nested parentheses.
        
        Time: O(n), Space: O(n)
        """
        stack = []
        result = 0
        current_num = 0
        sign = 1  # 1 for positive, -1 for negative
        
        for char in s:
            if char.isdigit():
                # Build multi-digit number
                current_num = current_num * 10 + int(char)
            elif char == '+':
                # Add previous number with its sign
                result += sign * current_num
                current_num = 0
                sign = 1
            elif char == '-':
                # Add previous number with its sign
                result += sign * current_num
                current_num = 0
                sign = -1
            elif char == '(':
                # Save current result and sign to stack
                stack.append(result)
                stack.append(sign)
                # Reset for new sub-expression
                result = 0
                sign = 1
            elif char == ')':
                # Complete current number
                result += sign * current_num
                current_num = 0
                # Pop sign and previous result from stack
                result *= stack.pop()  # Apply sign before parenthesis
                result += stack.pop()  # Add previous result
        
        # Add the last number
        result += sign * current_num
        
        return result