from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        
        for token in tokens:
            if token in operators:
                # Pop two operands (note: order matters for - and /)
                b = stack.pop()
                a = stack.pop()
                
                # Apply operation
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                else:  # token == '/'
                    # Truncate toward zero
                    result = int(a / b)
                
                stack.append(result)
            else:
                # It's a number, push to stack
                stack.append(int(token))
        
        # Final result is the only element left in stack
        return stack[0]