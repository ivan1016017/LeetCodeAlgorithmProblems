from typing import List
from unicodedata import digit 

class Solution:
    
    __name_of_instance = "SolutionOne"
    
    def __init__(self) -> None:
        if Solution.__name_of_instance != "SolutionOne":
            raise Exception("This is a singleton class.")
        else: 
            Solution.__name_of_instance = self 
            
            
            
    def isHappy(self, n: int) -> bool:
        
        def get_next(n:int) -> int:
            total_sum = 0
            while n > 0:
                digit = n % 10
                n = n // 10
                total_sum += digit**2
            return total_sum
        
        seen = list()
        
        while n != 1 and n not in seen:
            seen.append(n)
            n = get_next(n)
            
        return n == 1
    
    
class SolutionTwo: 
    def isHappy(self, n: int) -> bool:  
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1
    
def factory(name = "SolutionOne"):
    
    localizers = {
        "SolutionOne": Solution,
        "SolutionTwo": SolutionTwo
    }
    
    return localizers.get(name, Solution)()


print(factory("sdfsdf").isHappy(n = 19))
# print(factory("sdfsdf").isHappy(n = 19))

class WrittenText: 
    
    def __init__(self,text:str) -> None:
        self._text = text 
        
    def render(self) -> str: 
        return self._text

class UnderlineWrapper(WrittenText):
    
    def __init__(self, wrappedClass) -> None:
        self._wrappedClass = wrappedClass
        
    def render(self) -> str:
        return "<u>{}</u>".format(self._wrappedClass.render())
    
class ItaliclineWrapper(WrittenText):
    
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

before = WrittenText('Eyes of the world.')

after = UnderlineWrapper(ItaliclineWrapper(before))

print(before.render())
print(after.render())

logistic = LogisticRegression()
xgboost = XGBoost()
objects = list()

objects.append(Adapter(logistic, model_type = logistic.model_type()))
objects.append(Adapter(xgboost, model_type = xgboost.ml_model_type()))

for obj in objects: 
    print("A {0} model of type {1}".format(obj.name, obj.model_type))

    
                
        