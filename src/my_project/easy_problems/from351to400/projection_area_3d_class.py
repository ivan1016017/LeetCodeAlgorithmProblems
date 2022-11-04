from typing import List, Union 
from abc import ABC, abstractmethod


class Solution:

    __name_of_instance = 'SolutionOne'

    def __init__(self) -> None: 
        if Solution.__name_of_instance != 'SolutionOne':
            raise Exception('This is a singleton class')
        else: 
            Solution.__name_of_instance

    @abstractmethod
    def get_instance(self) -> None: 
        print(Solution.__name_of_instance)

    def projectionArea(self, grid: List[List[int]]) -> int:

        projection_xy = 0
        projection_xz = 0
        projection_yz = 0

        for row in grid:
            projection_xy += sum([1 for x in row if x != 0])
            projection_xz += max(row)

        def max_column(grid, j):
            temp = list()
            for i in range(len(grid)):
                temp.append(grid[i][j])
            return max(temp)

        for j in range(len(grid[0])):
            projection_yz += max_column(grid, j)

        return projection_xy + projection_xz + projection_yz


class SolutionTwo:
    def projectionArea(self, grid: List[List[int]]) -> int:

        res = 0
        c = 0
        len_grid = len(grid)

        for i in range(len_grid):
            res_1 = -1
            res_2 = -1

            for j in range(len_grid):

                if grid[i][j] == 0:
                    c += 1

                res_1 = max(res_1,grid[i][j])
                res_2 = max(res_2,grid[j][i])

            res += res_1 + res_2

        return res + len_grid**2 - c 

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

def factory(name:str='SolutionOne') -> Union[Solution,SolutionTwo]:

    localizers = {
        'SolutionOne':Solution,
        'SolutionTwo':SolutionTwo 
    }

    return localizers.get(name,Solution)()

print(factory('sdfsd').projectionArea(grid = [[1,2],[3,4]]))
# print(factory('sdfsd').projectionArea(grid = [[1,2],[3,4]]))



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