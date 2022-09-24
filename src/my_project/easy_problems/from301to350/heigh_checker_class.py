from abc import abstractmethod
from sqlite3 import adapt
from typing import List, Union 

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

    def heightChecker(self, heights: List[int]) -> int:
        
        original = heights.copy() 
        heights.sort()
        len_heights = len(heights)
        solution = 0

        for i in range(len_heights):
            if (original[i] != heights[i]):
                solution += 1 

        return solution      

class SolutionTwo:
    def heightChecker(self, heights: List[int]) -> int:
        sort_heights = sorted(heights)
        return sum([0 if heights[i] == sort_heights[i] else 1 for i in range(len(heights))])   

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
        return f"This is an instance fo the class XGBoost with max_depth {self.max_depth}"

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

def factory(name: str = 'SolutionOne') -> Union[Solution,SolutionTwo]:

    localizers = {
        'SolutionOne': Solution,
        'SolutionTwo': SolutionTwo 
    }

    return localizers.get(name, Solution)()

print(factory('sdfasd').heightChecker(heights = [1,1,4,2,1,3]))
# print(factory('sdfasd').heightChecker(heights = [1,1,4,2,1,3]))

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