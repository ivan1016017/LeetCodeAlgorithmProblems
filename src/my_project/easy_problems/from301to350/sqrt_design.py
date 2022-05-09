from typing import List 

class Solution:
    
    __name_of_instance = "SolutionOne"
    
    def __init__(self) -> None:
        if Solution.__name_of_instance != "SolutionOne":
            raise Exception("This is a singleton class.")
        else:
            Solution.__name_of_instance = self
        
    @staticmethod
    def get_instance(self) -> None:
        print(Solution.__name_of_instance)
    
    def mySqrt(self, x: int) -> int:
        
        left, right = 0, x 
        
        while left <= right:
            
            mid = (left + right)//2 
            if mid**2 > x: 
                right = mid - 1 
            elif mid**2 < x:
                left = mid + 1  
            else:
                return mid 
            
        return right
    
    
class SolutionTwo:
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1
                
def factory(name = "SolutionOne"):
    
    localizers = {
        "SolutionOne": Solution,
        "SolutionTwo": SolutionTwo
    }
    
    return localizers.get(name, Solution)()

class WrittenText: 
    
    def __init__(self, text) -> None:
        self._text = text 
        
    def render(self) -> str:
        return self._text
    
class UnderlineWrapper(WrittenText):
    
    def __init__(self, wrapperClass) -> None:
        self.wrapperClass = wrapperClass
        
    def render(self) -> str:
        return "<u>{}</u>".format(self.wrapperClass.render())
    
    
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
        return getattr(self.obj,attr)
    
    def original_dict(self):
        return self.obj.__dict__

print(factory('sdfsdf').mySqrt(9))
# print(factory('sdfsdf').mySqrt(9))

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

                