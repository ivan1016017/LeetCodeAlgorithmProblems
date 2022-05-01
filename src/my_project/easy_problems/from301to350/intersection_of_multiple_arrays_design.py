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
    def get_instance()-> None:
        print(Solution.__name_of_instance)
        
        
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        
        dict_nums = defaultdict(int)
        for list_num in nums:
            set_num = set(list_num)
            for num in set_num:
                dict_nums[num] += 1 
                
        answer = list()
        
        for num in dict_nums:
            if dict_nums[num] >=len(nums):
                answer.append(num)
                
        answer.sort()
                
        return answer 
    
    
class SolutionTwo:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted(list(set.intersection(*map(set, nums))))
    
    
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
    
    def __init__(self,wrappedClass) -> None:
        self.wrappedClass = wrappedClass
        
    def render(self) -> str: 
        return "<u>{}</u>".format(self.wrappedClass.render())
    
    
class ItaliclineWrapper(WrittenText):
    
    def __init__(self, wrappedClass) -> None:
        self._wrappedClass = wrappedClass
        
    def render(self) -> str:
        return "<i>{}</i>".format(self._wrappedClass.render()) 
    
    
class LogisticRegression:
    
    def __init__(self) -> None:
        self.name = 'regression' 
        
    def model_type(self) -> str:
        return "Regression Model"
    
class XGBoost:
    
    def __init__(self) -> None:
        self.name = 'xgboost'
        
    def ml_model_type(self) -> str:
        return "Emsemble Technique"
    
class Adapter:
    
    def __init__(self,obj,**adapter_methods) -> None:
        self.obj = obj 
        self.__dict__.update(adapter_methods)
        
    def __getattr__(self,attr):
        return getattr(self.obj,attr)
    
    def original_dict(self):
        return self.obj.__obj__

    
print(factory("sjdfsdf").intersection(nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
# print(factory("sjdfsdf").intersection(nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
Solution.get_instance()

before = WrittenText("Eyes of the world.")

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
    
    
