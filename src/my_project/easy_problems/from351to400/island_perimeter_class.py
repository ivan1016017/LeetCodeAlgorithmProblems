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
    def get_instance(self) -> None: 
        print(Solution.__name_of_instance)

    def islandPerimeter(self, grid: List[List[int]]) -> int:

        solution = 0
        x = len(grid)
        y = len(grid[0])

        function_x_one = lambda i,j: 1 if i >= x-1 or grid[i+1][j] == 0 else 0
        function_x_two = lambda i,j: 1 if i-1 < 0 or grid[i-1][j] == 0 else 0 
        function_y_one = lambda i,j: 1 if j >= y-1 or grid[i][j+1] == 0 else 0 
        function_y_two = lambda i,j: 1 if j-1 < 0 or grid[i][j-1] == 0 else 0 
        for i in range(x):
            for j in range(y):

                if grid[i][j] == 1:

                    solution += function_x_one(i,j)
                    solution += function_x_two(i,j)
                    solution += function_y_one(i,j)
                    solution += function_y_two(i,j)

        return solution


class SolutionTwo:
	def islandPerimeter(self, grid: List[List[int]]) -> int:
		row = len(grid)
		col = len(grid[0])
		seen = set()

		def dfs(i,j):
			# if this square has already been visited, return 0 and do the next recursion 
			if (i, j) in seen: return 0
			# if out of bound, should always has 1 unit as a part of perimeter
			if i >= row or j >= col or i < 0 or j < 0: return 1
			# if it is an island, and not been visited, marked it as seen and keep doing recursion 
			if grid[i][j] == 1:
				seen.add((i,j))
				return dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
			# if it is a water square and never been visited, should has 1 unit as a part of perimeter  
			return 1

		for i in range(row):
			for j in range(col):
				if grid[i][j] == 1:
					return dfs(i,j)

		return 0

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

print(factory('sdfsd').islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
# print(factory('sdfsd').islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))




#adding new line
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


