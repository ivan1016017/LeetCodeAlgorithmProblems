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

    def findWords(self, words: List[str]) -> List[str]:
        first_row: List[str] = ["q", "w", "e", "r", "t","y","u","i","o","p"]
        second_row: List[str] = ["a", "s", "d", "f", "g","h","j","k","l"]
        third_row: List[str] = ["z", "x", "c", "v", "b","n","m"]
        flag_first_row = False 
        flag_second_row = False 
        flag_third_row = False 
        to_lowercase_list  = list()
        answer = list()

        for i in range(len(words)):
            to_lowercase_list.append(words[i].lower())


        for i in range(len(words)):
            flag_first_row = False 
            flag_second_row = False 
            flag_third_row = False 

            for letter in to_lowercase_list[i]:

                if letter not in first_row:
                    flag_first_row = True
                    break 

            if flag_first_row == False:
                answer.append(words[i])
                continue

            for letter in to_lowercase_list[i]:

                if letter not in second_row:
                    flag_second_row = True
                    break 

            if flag_second_row == False:
                answer.append(words[i])
                continue


            for letter in to_lowercase_list[i]:

                if letter not in third_row:
                    flag_third_row = True
                    break 

            if flag_third_row == False:
                answer.append(words[i])
                continue
         
        return answer


class SolutionTwo:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = {"q":1,
                  "w":1,
                  "e":1,
                  "r":1,
                  "t":1,
                  "y":1,
                  "u":1,
                  "i":1,
                  "o":1,
                  "p":1,
                  "a":2,
                  "s":2,
                  "d":2,
                  "f":2,
                  "g":2,
                  "h":2,
                  "j":2,
                  "k":2,
                  "l":2,
                  "z":3,
                  "x":3,
                  "c":3,
                  "v":3,
                  "b":3,
                  "n":3,
                  "m":3,
        }                        
        final_list = []
        for list_words in words:
            current_word = []
            for list_letters_words in list_words:
                current_word.append(keyboard[list_letters_words.lower()])
            current_word = list(set(current_word))
            if len(current_word) == 1:
                final_list.append(list_words)
            
        return(final_list)


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

print(factory('sdfsd').findWords(words = ["Hello","Alaska","Dad","Peace"]))
# print(factory('sdfsd').findWords(words = ["Hello","Alaska","Dad","Peace"]))




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

