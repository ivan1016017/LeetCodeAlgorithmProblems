from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod


class Solution:

    __name_of_instance = 'SolutionOne'

    def __init__(self) -> None:
        if Solution.__name_of_instance != 'SolutionOne':
            raise Exception('This is a singleton class')
        else: 
            Solution.__name_of_instance = self 

    @staticmethod
    def get_instance() -> None: 
        print(Solution.__name_of_instance)


    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ## RC ##
        ## APPRAOCH : IN-PLACE MANIPULATION ##
        #  when the value needs to be updated, we donot just change  0 to 1 / 1 to 0 but we do in increments and decrements of 2. (table explains)        
        ##   previous value state change  current state   current value
        ##   0              no change     dead            0
        ##   1              no change     live            1
        ##   0              changed (+2)  live            2
        ##   1              changed (-2)  dead            -1
        
		## TIME COMPLEXITY : O(MxN) ##
		## SPACE COMPLEXITY : O(1) ##

        directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0                # live neighbors count
                for x, y in directions: # check and count neighbors in all directions
                    if ( i + x < len(board) and i + x >= 0 ) and ( j + y < len(board[0]) and j + y >=0 ) and abs(board[i + x][j + y]) == 1:
                        live += 1
                if board[i][j] == 1 and (live < 2 or live > 3):     # Rule 1 or Rule 3
                    board[i][j] = -1
                if board[i][j] == 0 and live == 3:                  # Rule 4
                    board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if(board[i][j] > 0) else 0
        return board
    


class SolutionTwo:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        def getNeighbourLivesCount(x, y):
            count = (
                (board[x-1][y] if x>0 else 0) +
                (board[x-1][y-1] if x>0 and y>0 else 0) +
                (board[x-1][y+1] if x>0 and y<n-1 else 0) +
                (board[x+1][y] if x<m-1 else 0) +
                (board[x+1][y-1] if x<m-1 and y>0 else 0) +
                (board[x+1][y+1] if x<m-1 and y<n-1 else 0) +
                (board[x][y-1] if y>0 else 0) +
                (board[x][y+1] if y<n-1 else 0)
            )
            return count

        points = []
        for i in range(m):
            for j in range(n):
                count = getNeighbourLivesCount(i, j)
                if count<2 or count>3:
                    if board[i][j] != 0:
                        points.append((i,j,0))
                elif count==3:
                    if board[i][j] != 1:
                        points.append((i,j,1))
        
        for (i,j,val) in points:
            board[i][j] = val

class WrittenText:

    def __init__(self, text:str) -> None: 
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

    def __init__(self,max_depth:int=None):
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

def factory(name:str='SolutionOne') -> Solution:

    localizers = {
        'SolutionOne':Solution,
    }

    return localizers.get(name,Solution)()

# a = ListNode(1,ListNode(2))
# b = ListNode(3,ListNode(4))

# solution = Solution()
# print(solution.addTwoNumbers(a,b).val)


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


# solution = Solution()

# print(solution.calculate(s = "(100+(4+5+2)-3)+(6+8)")) 
# print('*******************')
# print(solution.calculate(s = " 2-1 + 2 "))

# a = 2
# b = 3
# sign = 1 
# result = a*sign*b 
# print(result)
# sign=-1
# print(result)


            




