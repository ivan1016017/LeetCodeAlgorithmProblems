from typing import List, Union
from abc import ABC, abstractmethod
from collections import defaultdict


class ParkingSystem:

    __name_of_instance = 'SolutionOne'

    def __init__(self, big: int, medium: int, small: int):
        if ParkingSystem.__name_of_instance != 'SolutionOne':
            raise Exception('This is a singleton class')
        else: 
            ParkingSystem.__name_of_instance = self

        self.parking_space=[big,medium,small]

    @abstractmethod
    def get_instance(self) -> None: 
        print(ParkingSystem.__name_of_instance)

    def addCar(self, carType: int) -> bool:
        if(self.parking_space[carType-1]!=0):
            self.parking_space[carType-1]-=1
            return True
        return False

class ParkingSystemTwo:

    def __init__(self, big: int, medium: int, small: int):
        self.dict_parking = defaultdict(int)
        self.big = big 
        self.medium = medium 
        self.small = small 
                

    def addCar(self, carType: int) -> bool:

        if carType == 1:
            if self.dict_parking[1] + 1 <= self.big:
                self.dict_parking[1] += 1
                return True
            else: 
                return False 
        elif carType == 2:
            if self.dict_parking[2] + 1 <= self.medium:
                self.dict_parking[2] += 1
                return True 
            else: 
                return False 
        else:
            if self.dict_parking[3] + 1 <= self.small:
                self.dict_parking[3] += 1
                return True
            else:
                return False 

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

def factory(name:str='SolutionOne') -> Union[ParkingSystem,ParkingSystemTwo]:

    localizers = {
        'SolutionOne':ParkingSystem,
        'SolutionTwo':ParkingSystemTwo
    }

    return localizers.get(name,ParkingSystem)()

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








