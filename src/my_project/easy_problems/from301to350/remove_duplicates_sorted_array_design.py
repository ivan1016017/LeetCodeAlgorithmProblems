from typing import List 

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
    
    def removeDuplicates(self, nums: List[int]) -> int:
        
        len_nums = len(nums)
        
        if len_nums == 0 or len_nums ==1: 
            return len_nums 
        
        j = 0 
        
        for i in range(len_nums-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j+=1
                
        nums[j] = nums[len_nums-1]
        
        return j+1
    
    
class SolutionTwo:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = 1
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
                length += 1
        return length
    
def factory(name ='SoluitionOne'):
    
    localizers = {
        'SolutionOne':Solution,
        'SolutionTwo':SolutionTwo
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
    
    
    def __init__(self, obj, **adapter_methods) -> None:
        self.obj = obj 
        self.__dict__.update(adapter_methods)
        
    def __getattr__(self,attr):
        return getattr(self.obj,attr)
    
    def original_dict(self):
        return self.obj.__dict__
    


print(factory('sdfds').removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# print(factory('sdfds').removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


before = WrittenText('Eyes of the world')

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