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

    def coinChange(self, coins: List[int], amount: int) -> int:

        '''
        Classic case of dynamic programing and counter example of greedy.
        dp[i] records the minimal coins needed to make up amount i. And it's one more 
        coin than the minimum of dp[i-j] for j in coins.
        All value in dp array are initialized as None. If all possibile dp[i-j] are None, 
        amount i is not reachable by any combination of coins as we leave it as None as well. 
        And I set a None value as -1 since we are required to return -1 if i is not able to be made up of.
        '''

        dp = [0] * (amount + 1)
        for i in range(1, amount+1):
            dp[i] = min((dp[i-j] for j in coins if i>=j and dp[i-j] >= 0), default=-2) + 1

        print(dp)
        return dp[amount]


class SolutionTwo:
    def coinChange(self, coins, amount):
        MAX = float('inf')
        if amount == 0:
            return 0
        dic = {}
        for c in coins:
            dic[c] = 1
        for v in range(1,amount+1):
            for s in coins:
                diff = v - s
                if v - s in dic:
                    if v not in dic:
                        dic[v] = dic[v-s] +1
                    else:
                        dic[v] = min(dic[v],dic[v-s]+1)
        if amount not in dic:
            return -1
        else:
            return dic[amount]

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

print(factory('sdfsd').coinChange(coins = [1,2,5], amount = 11))
# print(factory('sdfsd').coinChange(coins = [1,2,5], amount = 11))

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


