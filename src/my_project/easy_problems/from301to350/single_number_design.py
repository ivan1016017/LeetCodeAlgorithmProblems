from typing import List 
from collections import defaultdict

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
        
        
    def singleNumber(self, nums: List[int]) -> int:
        
        temp_dict = defaultdict(int)
        
        for num in nums: 
            temp_dict[num] +=1
            
        for num in temp_dict:
            if temp_dict[num] == 1:
                return num
        
        return -1
    
class SolutionTwo:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        r=nums[0]
        for i in range(1,n):
            r = r ^ nums[i] 

        return r
    
def factory(name = 'SolutionOne'):
    
    localizers = {
        'SolutionOne': Solution, 
        'SolutionTwo': SolutionTwo
    }
    
    return localizers.get(name, Solution)()


class WrittenText: 
    
    def __init__(self,text) -> None:
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
        return getattr(self.obj,attr)
    
    def original_dict(self):
        return self.obj.__dict__


print(factory('sdfsdf').singleNumber([1,2,1,2,7]))




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

