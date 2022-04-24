from typing import List 
import math


class Solution:
    
    __name_of_instance = 'SolutionOne'
    
    def __init__(self) -> None:
        if Solution.__name_of_instance != 'SolutionOne':
            raise Exception('This is a singleton class.')
        else:
            Solution.__name_of_instance = self 
            
    @staticmethod
    def get_instance(self) -> None:
        print(Solution.__name_of_instance)
    
    
    def climbStairs(self, n: int) -> int:

        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a
    
class SolutionTwo:
    def climbStairs(self, n: int) -> int:
        j= 0
        temp = n
        count = 0
        for i in range(n):
            temp -= 2
            if temp < 0:
                break
            else:
                j += 1
                count += math.comb((n- (j*2) + j), j)
        return count +1
    
    
def factory(name = 'SolutionOne'):
    
    localizers = {
        'SolutionOne': Solution,
        'SolutionTwo': SolutionTwo
    }
    
    return localizers.get(name, Solution)()


class WrittenText:
    
    def __init__(self, text: str) -> None:
        self._text = text 
        
    def render(self) -> str:
        return self._text 
    
class UnderlineWrapper(WrittenText):
    
    def __init__(self, wrappedClass) -> None:
        self._wrappedClass = wrappedClass
        
    def render(self) -> str:
        return "<u>{}</u>".format(self._wrappedClass.render())
    
class ItalicWrapper(WrittenText):
    
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
    
    def __init__(self,obj,**adapter_methods) -> None:
        self.obj = obj
        self.__dict__.update(adapter_methods)
        
    def __getattr__(self,attr):
        return getattr(self.obj, attr)
    
    def original_dict(self):
        return self.obj.__dict__
    
    
    
print(factory('sdfshdf').climbStairs(2)) 

before = WrittenText('Eyes of the world.')  

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




