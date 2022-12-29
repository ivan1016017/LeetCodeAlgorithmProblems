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

    def largestVariance(self, s: str) -> int:
        res = 0
        chars = list(set(s))
		
		# Loop through each pari of (c1, c2)
        for i in range(len(chars)):
            for j in range(i+1, len(chars)):
                c1, c2 = chars[i], chars[j]
				
				# keep track of count(c1) - count(c2) 
                diff = 0 
				
				# max and min of diff
				# result should be maximum of (diff - min_diff, max_diff - diff)
				# e.g. "baabaa", at index = 0, min_diff = -1. when index = 5, diff = 4 - 2 = 2, result = diff - min_diff = 2 - (-1) = 3
                max_diff = min_diff = 0
				
				# diff at the previous occurance of c1/c2
                last_c1_diff = last_c2_diff = 0 
				
				# check wether we have met c1/c2 during the loop
                meet_c1 = meet_c2 = False
				
                for c in s:
                    if c == c1:
                        meet_c1 = True
                        diff += 1
						
						#  use last_c1_diff instead of diff because we have to make sure that c1 is in the rest part of the substring. 
						# e.g. [c1, c1, c2, c2, c2]
						# At index = 1, if we use diff = 2 -> max_diff = 2
						# At index = 4, diff = 2 - 3 = -1, result = max_diff - diff = 3. 
						# Though we have [c2, c2, c2] as a substring, c1 is not in this string and the result is invalid
                        max_diff = max(last_c1_diff, max_diff)
						
                        last_c1_diff = diff
                    elif c == c2:
                        meet_c2 = True
                        diff -= 1
                        min_diff = min(last_c2_diff, min_diff)
                        last_c2_diff = diff
                    else:
                        continue
					
					# update the result only when we have met both c1 and c2 
                    if meet_c1 and meet_c2:
                        res = max(diff - min_diff, max_diff - diff, res)
        return res


class SolutionTwo:
    def largestVariance(self, s: str) -> int:
        res = 0
        chars = list(set(s))
		
        for i in range(len(chars)):
            for j in range(i+1, len(chars)):
                c1, c2 = chars[i], chars[j]
				
                diff = 0 			
                max_diff = min_diff = 0			
                last_c1_diff = last_c2_diff = 0 			
                meet_c1 = meet_c2 = False
				
                for c in s:
                    if c == c1:
                        meet_c1 = True
                        diff += 1
                        max_diff = max(last_c1_diff, max_diff)					
                        last_c1_diff = diff
                    elif c == c2:
                        meet_c2 = True
                        diff -= 1
                        min_diff = min(last_c2_diff, min_diff)
                        last_c2_diff = diff
                    else:
                        continue			
                    if meet_c1 and meet_c2:
                        res = max(diff - min_diff, max_diff - diff, res)
        return res

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

print(factory('sdfsd').largestVariance(s = "aababbb"))
# print(factory('sdfsd').largestVariance(s = "aababbb"))


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