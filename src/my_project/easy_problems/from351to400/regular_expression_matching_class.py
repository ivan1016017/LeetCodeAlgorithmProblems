from typing import List, Union
from abc import ABC, abstractmethod

class Solution:

    __name_of_instnace = 'SolutionOne'

    def __init__(self) -> None: 
        if Solution.__name_of_instnace != 'SolutionOne':
            raise Exception('This is a singleton class')
        else: 
            Solution.__name_of_instnace = self 

    @abstractmethod
    def get_instance(self) -> None: 
        print(Solution.__name_of_instnace)

    def isMatch(self, s, p):
        if not p: return not s
        if not s: return len(p) > 1 and p[1] == '*' and self.isMatch(s, p[2:])
        Matched = (p[0] == '.' or p[0] == s[0])
        if len(p) > 1 and p[1] == '*':
            return (Matched and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        return Matched and self.isMatch(s[1:], p[1:])

class SolutionTwo:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1) for i in range(len(s)+1)]
		# Update the corner case of matching two empty strings. egg s='a' p='a', so s[0] = p[0]  ==> dp[1][1] == dp[0][0], we can see dp[0][0] need to set True
        dp[0][0] = True
		# Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the dp table is vertically updated by the one before previous
        for j in range(2,len(p)+1):
            if p[j-1] == '*':  
                dp[0][j] = dp[0][j-2]
        
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                dp[i][j] = (p[j-1] in [s[i-1],'.']  and dp[i-1][j-1]) or (p[j-1] == '*' and ((p[j-2] in [s[i-1],'.'] and dp[i-1][j] ) or (dp[i][j-2]))) 
        return dp[len(s)][len(p)]

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
        

print(factory('sdfsd').isMatch(s = "aa", p = "a"))
# print(factory('sdfsd').isMatch(s = "aa", p = "a"))



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

