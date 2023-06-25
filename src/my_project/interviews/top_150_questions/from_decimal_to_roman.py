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

    def intToRoman(self, num: int) -> str:
        # define the dictionary of the roman numbers
        roman_dict = { 1: "I", 4:"IV", 5:"V", 9:"IX", 10:"X",
                      40:"XL", 50:"L", 90:"XC", 100:"C",
                      400:"CD", 500:"D", 900:"CM", 1000:"M"}
        roman_to_arab_list = [1,4,5,9,10,40,50,90,100,400,500,900,1000,4000]

        flag = False
        temp = ''

        while not flag: 
            for i in range(13):
                if num >= roman_to_arab_list[i] and num < roman_to_arab_list[i+1]:
                    temp += roman_dict[roman_to_arab_list[i]]
                    num -= roman_to_arab_list[i]

            if num == 0:
                flag = True 

        return temp
    
class SolutionTwo:
    def intToRoman(self, num: int) -> str:
        # Creating Dictionary for Lookup
        num_map = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
        
        # Result Variable
        r = ''
        
        
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If n in list then add the roman value to result variable
            while n <= num:
                r += num_map[n]
                num-=n
        return r
    
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


            
        
 

