from typing import List, Union 
from abc import ABC, abstractmethod


class Solution:

    __name_of_instance = 'SolutionOne'

    def __init__(self) -> None: 
        if Solution.__name_of_instance != 'SolutionOne':
            raise Exception('This is a singleton class')
        else: 
            Solution.__name_of_instance = self 

    @abstractmethod
    def get_instance() -> None: 
        print(Solution.__name_of_instance)

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        bound_down = list()
        bound_up = list()
        if not nums:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower)+'->'+str(upper)]

        answer = list()


        if nums[0] - lower >= 1:
            if nums[0] - lower == 1: 
                bound_down.append("{}".format(lower))
            else:
                bound_down.append("{}->{}".format(lower,nums[0]-1))

        
        if upper - nums[-1] >= 1:
            if upper - nums[-1] == 1: 
                bound_up.append("{}".format(upper))
            else:
                bound_up.append("{}->{}".format(nums[-1]+1,upper))

        for i in range(len(nums)-1):
            
            if nums[i+1] - nums[i] == 2: 
                answer.append("{}".format(nums[i]+1))
            elif nums[i+1] - nums[i] > 2:
                answer.append("{}->{}".format(nums[i]+1,nums[i+1]-1))

        return bound_down + answer + bound_up

    
class SolutionTwo:
    def findMissingRanges(self, nums, lower, upper):
        res = []
        nums = [lower-1] + nums + [upper+1]
        left_p = 0
        right_p = 1
        while right_p < len(nums):
            left = nums[left_p]
            right = nums[right_p]
            if left+1 == right-1:
                res.append(str(left+1))
            elif (right-1) - (left+1) > 0:
                res.append(str(left+1) + "->" + str(right-1))
            left_p += 1
            right_p += 1
        return res

class WrittenText: 

    def __init__(self,text:str) -> None: 
        self._text = text 

    def render(self) -> str: 
        return self._text 

class UnderlineWrapper(WrittenText):

    def __init__(self,wrappedClass:WrittenText):
        self._wrappedClass = wrappedClass

    def render(self) -> str: 
        return '<u>{}</u>'.format(self._wrappedClass.render())

class ItaliclineWrapper(WrittenText):
    
    def __init__(self, wrappedClass:WrittenText) -> None:
        self._wrappedClass = wrappedClass
        
    def render(self) -> str:
        return "<i>{}</i>".format(self._wrappedClass.render()) 

class LogisticRegression:

    def __init__(self) -> None: 
        self.name = 'Logistic'

    def model_type(self) -> str: 
        return 'Regression Model'

class XGBoost: 

    def __init__(self,max_depth:int=None) -> None: 
        self.name = 'XGBoost'
        self.max_depth = max_depth 

    def ml_model_type(self) -> str: 
        return 'Ensemblem Technique'

    def __str__(self):
        return f"This is an instance of the class XGBoost with max_depth {self.max_depth}"

class Adapter: 

    def __init__(self,obj,**adapter_methods):
        self.obj = obj 
        self.__dict__.update(adapter_methods)

    def __getattr__(self,attr):
        return getattr(self.obj,attr)

    def original_dict(self):
        return self.obj.__dict__ 

class MlModel:
    @abstractmethod
    def predict(self):
        pass 

class RandomForest(MlModel):

    def predict(self):
        print("Random forest predicted value")

    def is_fitted(self):
        print("Random forest model fits the data")

class LightGBM(MlModel):
    def predict(self):
        print("LightGBM predicted value")
        
    def is_fitted(self):
        print("LightGBM model fits the data")

class Production(MlModel):

    def __init__(self,model:MlModel):
        self.model = model 
        self.is_fitted = False 

    def predict(self):
        
        if self.is_fitted:
            self.model.predict()
            self.is_fitted = False 
        else: 
            self.model.is_fitted()
            self.is_fitted = True 

def factory(name:str = 'SolutionOne') -> Union[Solution,SolutionTwo]:

    localizers = {
        'SolutionOne': Solution,
        'SolutionTwo': SolutionTwo
    }

    return localizers.get(name,Solution)()


print(factory('sdfsd').findMissingRanges(nums = [0,1,3,50,75], lower = 0, upper = 99))
# print(factory('sdfsd').findMissingRanges(nums = [0,1,3,50,75], lower = 0, upper = 99))




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

second_xgboost = XGBoost(7)
print(second_xgboost)

random_forest = RandomForest()

ml_model = Production(random_forest)
# this is a new comment
ml_model.predict()
ml_model.predict()  
