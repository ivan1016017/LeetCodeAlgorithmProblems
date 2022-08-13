from typing import List 
from abc import ABC, abstractmethod

class Solution:

    __name_of_instance = 'Solution'

    def __init__(self) -> None: 
        if Solution.__name_of_instance != 'Solution':
            raise Exception('This is a singleton class.')
        else: 
            Solution.__name_of_instance = self 


    @staticmethod
    def get_instance() -> None: 
        print(Solution.__name_of_instance)

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        solution: int = 0

        seats.sort()
        students.sort()

        for i in range(len(seats)):
            solution += abs(seats[i] - students[i])

        return solution


class SolutionTwo:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats_cnt, students_cnt = [0] * (max(seats) + 1), [0] * (max(students) + 1)
        for seat in seats:
            seats_cnt[seat] += 1
        for student in students:
            students_cnt[student] += 1
        ans = 0
        i = j = 1
        while i < len(students_cnt):
            if students_cnt[i]:
                # find the next available seat
                while j < len(seats_cnt) and not seats_cnt[j]:
                    j += 1
                ans += abs(i - j)
                seats_cnt[j] -= 1
                students_cnt[i] -= 1
            else:
                i += 1
        return ans

def factory(name:str = 'SolutionOne'):
    
    localizers = {
        'SolutionOne': Solution,
        'SolutionTwo': SolutionTwo 
    }

    return localizers.get(name, Solution)() 

class WrittenText: 

    def __init__(self,text:str) -> None: 
        self._text = text 

    def render(self) -> str: 
        return self._text

class UnderlineWrapper(WrittenText): 

    def __init__(self, wrappedClass) -> None: 
        self._wrappedClass = wrappedClass

    def render(self) -> str: 
        return '<u>{}</u>'.format(self._wrappedClass.render())

class ItaliclineWrapper(WrittenText):
    
    def __init__(self, wrappedClass) -> None:
        self._wrappedClass = wrappedClass
        
    def render(self) -> str:
        return "<i>{}</i>".format(self._wrappedClass.render()) 

class LogisticRegression:
    
    def __init__(self) -> None: 
        self.name = 'regression'
        
    def model_type(self) -> str: 
        return "Regression Model"

class XGBoost:

    def __init__(self, max_depth: int = None) -> None:
        self.name = 'XGBoost'
        self.max_depth = max_depth 

    def ml_model_type(self) -> str:
        return 'Ensemble Technique'

    def __str__(self) -> str: 

        return f"This is an instance of the XGBoost class with max_depth {self.max_depth}"

class Adapter: 

    def __init__(self,obj,**adapter_methods) -> None: 
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
        
class Production:
    
    def __init__(self, model: MlModel):
        self.model = model 
        self.is_fitted = False 
        
    def predict(self):
        
        if self.is_fitted:
            self.model.predict()
            self.is_fitted = False 
        else: 
            self.model.is_fitted()
            self.is_fitted = True


print(factory('sdfsdf').minMovesToSeat(seats = [3,1,5], students = [2,7,4]))

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
ml_model.predict()
ml_model.predict()


