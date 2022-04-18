from typing import List


class Solution:
    
    __name_of_instance = 'SolutionOne'
    
    def __init__(self) -> None:
        if Solution.__name_of_instance != 'SolutionOne':
            raise Exception('This is a singleton class')
        else:
            Solution.__name_of_instance = self 
            
    @staticmethod
    def get_instance() -> None:
        print(Solution.__name_of_instance)
            
    def romanToInt(self, s: str) -> int:
        
        answer = 0
        len_s = len(s)
        
        roman_dict = {"I":1, "V":5, "X":10, "L":50,"C":100,"D":500,"M":1000}
        
        answer += roman_dict[s[len_s-1]]
        
        for i in range(len_s-1):
            if roman_dict[s[len_s-2-i]] < roman_dict[s[len_s-1-i]]:
                answer -= roman_dict[s[len_s-2-i]]
            elif roman_dict[s[len_s-2-i]] >= roman_dict[s[len_s-1-i]]:
                answer += roman_dict[s[len_s-2-i]]
                
        return answer 
    
class SolutionTwo:
    
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
    
    
def factory(name = 'Solution'):
    
    localizers = {
        'Solution': Solution,
        'SolutionTwo': SolutionTwo
    }
    
    return localizers.get(name, Solution)()

class WritttenText:
    
    def __init__(self,text) -> None:
        self._text = text 
        
    def render(self):
        return self._text
    
class UnderlineWrapper(WritttenText):
    
    def __init__(self, wrappedClass) -> None:
        self._wrappedClass = wrappedClass
        
    def render(self) -> str:
        return "<u>{}</u>".format(self._wrappedClass.render())
    
class ItalicWrapper(WritttenText):
    
    def __init__(self, wrappedClass) -> None:
        self._wrappedClass = wrappedClass
        
    def render(self) -> str:
        return "<i>{}</i>".format(self._wrappedClass.render())
    

class LogisticRegression:
    
    def __init__(self) -> None:
        self.name = 'regression'
        
    def model_type(self) -> str:
        return 'Regression Model'
    
class XGBoost:
    
    def __init__(self) -> None:
        self.name = 'xgboost'
        
    def ml_model_type(self) -> str:
        return 'Ensemble Technique'
    
class Adapter: 
    
    def __init__(self, obj, **adapter_methods) -> None:
        self.obj = obj
        self.__dict__.update(adapter_methods)
    
    def __getattr__(self,attr):
        return getattr(self.obj, attr)
    
    
print(factory('Solutiosdfsdfn').romanToInt('III'))

before = WritttenText('word')
after = UnderlineWrapper(ItalicWrapper(before))

print(before.render())
print(after.render())

logistic = LogisticRegression()
xgboost = XGBoost()
objects = list()

objects.append(Adapter(logistic, model_type = logistic.model_type()))
objects.append(Adapter(xgboost, model_type = xgboost.ml_model_type()))

for obj in objects: 
    print("A {0} model of type {1}".format(obj.name, obj.model_type))
        

    
    
