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

    def racecar(self, target: int) -> int:

        q = deque()
        q.append((0, 1, 0))
        while q:
            pos, speed, n = q.popleft()
            if pos == target:
                return n
            q.append((pos+speed, speed*2, n+1))
            if speed > 0:
                if pos + speed > target:
                    q.append((pos, -1, n+1))
            else:
                if pos + speed < target:
                    q.append((pos, 1, n + 1))

class SolutionTwo:
    def racecar(self, target: int) -> int:
        """
        AAARA
        pos 0 -> 1 -> 3 -> 7 -> 7 -> 6
        speed 1 -> 2 -> 4 -> 8 -> -1 -> -2
        
        intuition: get shortest sequence of instructions
            -> BFS # (pos, speed, steps)
        """
        queue = deque([(0, 1, 0)])
        while queue:
            for _ in range(len(queue)):
                prev_pos, prev_speed, prev_steps = queue.popleft()

                if prev_pos == target:
                    return prev_steps

                # case 1 -> A
                queue.append((prev_pos + prev_speed, prev_speed * 2, prev_steps + 1))

                # case 2 -> R (TLE)
                # queue.append((prev_pos, -1 if prev_speed >= 0 else 1, prev_steps + 1))

                # enhancement can be made here
                # there are two reasons when we want to reverse the car, having `R`
                # case 2.1 -> R
                #   if the car passed the target and its speed is still positive
                if prev_pos + prev_speed > target and prev_speed > 0:
                    queue.append((prev_pos, -1, prev_steps + 1))

                # case 2.1 -> R
                #   if the car has not reached the target and its speed is yet negative
                if prev_pos + prev_speed < target and prev_speed < 0:
                    queue.append((prev_pos, 1, prev_steps + 1))

        return -1


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

print(factory('sdfsdf').racecar(3))
# print(factory('sdfsdf').racecar(3))






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

