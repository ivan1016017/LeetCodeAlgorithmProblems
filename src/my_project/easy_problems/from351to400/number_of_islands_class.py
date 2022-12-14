from typing import List, Union
from abc import ABC, abstractmethod
from collections import deque

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


    def numIslands(self, grid: List[List[str]]) -> int:

        m: int = len(grid)
        n: int = len(grid[0])
        num_islands: int = 0

        def bfs(i,j):
            queue = deque()
            queue.append([i,j])

            while queue: 

                for _ in range(len(queue)):
                    i,j = queue.popleft()

                    for x, y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                        # exploring the whole land
                        if x>=0 and x<m and y>=0 and y<n and grid[x][y]=='1':
                            queue.append([x,y])
                            grid[x][y]='in land'

        for i in range(m):
            for j in range(n):
                #visiting new islands
                if grid[i][j]!='in land' and grid[i][j]=='1':
                    grid[i][j]='in land'
                    bfs(i,j)
                    num_islands+=1

        return num_islands

class SolutionTwo():
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # idea is to make connected components count 1 only by making them 0 once visited
        self.sum = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.sum += self.find_islands(grid, row, col)
        return self.sum
        
    def find_islands(self, grid,i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
            grid[i][j] = "0"
            # go top left right bottom 
            # make all 1's 0 till all connected becomes zero
            # then return 1 as all connected componets forms one island
            # done
            self.find_islands(grid, i + 1, j)
            self.find_islands(grid, i, j-1)
            self.find_islands(grid, i-1, j)
            self.find_islands(grid, i, j + 1)
            return 1
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
        return f'This is an instance of the class XGBoost with max_depth {self.max_depth}'

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
        print('Random fores predicted value')

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

print(factory('sdfsd').numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

# print(factory('sdfsd').numIslands(grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]))



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
