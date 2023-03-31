from typing import List, Union, Collection, Mapping, Optional
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
        print(self.__name_of_instance)

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer = list()

        positives = list()
        negatives = list()
        num_zeroes = 0

        for num in nums:
            if num == 0:
                num_zeroes += 1
            elif num > 0:
                positives.append(num)
            else: 
                negatives.append(num)

        s_positives = set(positives)
        s_negatives = set(negatives)

        for i in range(len(positives)):
            for j in range(i+1,len(positives)):
                k = positives[i] + positives[j]
                if -k in s_negatives:
                    mi = min(positives[i],positives[j])
                    ma = max(positives[i],positives[j])
                    answer.append((-k,mi,ma))


        for i in range(len(negatives)):
            for j in range(i+1,len(negatives)):
                k = negatives[i] + negatives[j]
                if -k in s_positives:
                    mi = min(negatives[i],negatives[j])
                    ma = max(negatives[i],negatives[j])
                    answer.append((mi,ma,-k))

        if num_zeroes >= 1:
            for num in s_positives:
                if -num in s_negatives:
                    answer.append((-num,0,num))

        if num_zeroes >= 3:
            answer.append((0,0,0))

        return list(set(answer))
    
class SolutionTwo:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        nums = sorted(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            new_target = -nums[i]
            while j < k:
                summ = nums[j] + nums[k]
                if summ < new_target:
                    j += 1
                elif summ > new_target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j+1] == nums[j]:
                        j += 1
                    j += 1
                    while k > j and nums[k-1] == nums[k]:
                        k -= 1
                    k -= 1
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
