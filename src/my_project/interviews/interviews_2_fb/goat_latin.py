from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        vowels = ['a','e','i','o','u', 'A','E','I','O','U']
        list_vowels = sentence.split(' ')


        for i in range(len(list_vowels)):
            if list_vowels[i][0] in vowels:
                list_vowels[i] += 'ma' + (i+1)*'a'
            else: 
                list_vowels[i] = list_vowels[i][1:] + list_vowels[i][0] + 'ma' + (i+1)*'a'


        return ' '.join(list_vowels)
