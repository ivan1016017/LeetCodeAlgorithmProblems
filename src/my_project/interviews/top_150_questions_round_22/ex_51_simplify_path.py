from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Simplifies a Unix-style absolute path to its canonical form.
        
        Args:
            path: An absolute path string starting with '/'
            
        Returns:
            The simplified canonical path
        """
        # Stack to keep track of valid directory names
        stack = []
        
        # Split the path by '/' and process each component
        components = path.split('/')
        
        for component in components:
            # Skip empty strings (from consecutive slashes) and current directory markers
            if component == '' or component == '.':
                continue
            # Parent directory - pop from stack if possible
            elif component == '..':
                if stack:
                    stack.pop()
            # Valid directory or file name
            else:
                stack.append(component)
        
        # Build the canonical path
        # Start with '/' and join all directories with '/'
        return '/' + '/'.join(stack)