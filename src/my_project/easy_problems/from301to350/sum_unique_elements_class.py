from typing import List, Union
from abc import ABC, abstractmethod
from collections import defaultdict

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

    def sumOfUnique(self, nums: List[int]) -> int:

        solution = 0
        solution_dict = defaultdict(int)

        for num in nums:
            solution_dict[num] += 1 

        for key, value in solution_dict.items():
            
            if value == 1:
                solution += key 
        
        return solution 


class SolutionTwo:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if i in hashmap.keys():
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        sum = 0
        for k, v in hashmap.items():
            if v == 1: sum += k
        return sum

class WrittenText:

    def __init__(self,text:str) -> None:
        self._text = text 

    def render(self) -> str: 
        return self._text 

class UnderlineWrapper(WrittenText): 

    def __init__(self,wrappedClass:WrittenText) -> None:
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
        return 'Ensemble Technique'

    def __str__(self) -> str: 
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
    
    def __init__(self, model: MlModel):
        self.model = model 
        self.is_fitted = False 
        
    def predict(self):
        
        if self.is_fitted:
            self.model.predict()
            self.is_fitted = False 
        else: 
            self.model.is_fitted()
            self.is_fitted = True 

def factory(name: str = 'SolutionOne') -> Union[Solution,SolutionTwo]:

    localizers = {
        'SolutionOne': Solution,
        'SolutionTwo': SolutionTwo 
    }

    return localizers.get(name,Solution)()

print(factory('sfsd').sumOfUnique(nums = [1,2,3,2]))
# print(factory('sfsd').sumOfUnique(nums = [1,2,3,2]))

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




