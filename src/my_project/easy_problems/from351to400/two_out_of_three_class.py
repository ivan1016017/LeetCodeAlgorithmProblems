from typing import List, Union 
from abc import ABC, abstractmethod
from collections import defaultdict

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

    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        unique_nums1 = list()
        unique_nums2 = list()
        unique_nums3 = list()

        count_dict = defaultdict(int)

        for num in nums1:
            if num not in unique_nums1:
                unique_nums1.append(num) 

        for num in nums2:
            if num not in unique_nums2:
                unique_nums2.append(num)

        for num in nums3:
            if num not in unique_nums3:
                unique_nums3.append(num)

        for num in unique_nums1 + unique_nums2 + unique_nums3:
            count_dict[num] += 1

        solution = list()

        for key, value in count_dict.items():

            if value >=2:
                solution.append(key)

        return solution 


class SolutionTwo:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        temp = list()
        for num in nums1:
            if num not in temp:
                temp.append(num)
        nums1 = temp

        temp = []
        for num in nums2:
            if num not in temp:
                temp.append(num)
        nums2 = temp

        temp = []
        for num in nums3:
            if num not in temp:
                temp.append(num)
        nums3 = temp

        temp_dict = {}

        for num in nums1 + nums2 + nums3:
            temp_dict[num] = 0
        
        for num in nums1 + nums2 + nums3:
            temp_dict[num] += 1

        answer = list()

        for num in temp_dict.keys():
            if temp_dict[num] >= 2:
                answer.append(num)

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

def factory(name:str='SolutionOne') -> Union[Solution,SolutionTwo]:

    localizers = {
        'SolutionOne': Solution,
        'SolutionTwo': SolutionTwo 
    }

    return localizers.get(name,Solution)()

print(factory('asdfsd').twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]))

# print(factory('asdfsd').twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]))

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