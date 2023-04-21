from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:

    __name_of_instance = 'SolutionOne'

    def __int__(self) -> None: 
        if Solution.__name_of_instance != 'SolutionOne':
            raise Exception('This is a singleton class')
        else: 
            Solution.__name_of_instance = self 

    @abstractmethod
    def get_instance() -> None: 
        print(Solution.__name_of_instance)

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtracking(i,j,word,board):
                    return True 
        return False 

    def backtracking(self,i,j,word,board):

        if len(word) == 0: 
            return True 
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False 
        
        if board[i][j] == word[0]:
            board[i][j] = '*'
            if self.backtracking(i-1,j,word[1:],board) or self.backtracking(i+1,j,word[1:],board) or self.backtracking(i,j-1,word[1:],board) or self.backtracking(i,j+1,word[1:],board):
                return True 
            board[i][j] = word[0]

        return False 

class SolutionTwo:
    def neighbors(self, board, r, c):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        nbs = []
        for d in directions:
            nr = r + d[0]
            nc = c + d[1]
            if (0 <= nr < len(board)) and (0 <= nc < len(board[nr])):
                nbs.append((nr, nc))
        return nbs
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        q = list()
				
        for r in range(len(board)): # find starting points
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    q.append((r, c))
                    
        for (r, c) in q:
            visited = set()
            stack = list()
            stack.append((r, c, 0, False)) # regular forward moving node
            while stack:
                cr, cc, i, backtrack = stack.pop()
                if backtrack:
                    visited.remove((cr, cc))
                    continue
                    
                visited.add((cr, cc))
                stack.append((cr, cc, i, True)) # add backtracking node
                if i == (len(word) - 1):
                    return True
            
                for nr, nc in self.neighbors(board, cr, cc):
                    if (nr, nc) in visited:
                        continue
                    if board[nr][nc] == word[i + 1]:
                        stack.append((nr, nc, i + 1, False)) # forward-moving node
            
        return False
    
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



    

