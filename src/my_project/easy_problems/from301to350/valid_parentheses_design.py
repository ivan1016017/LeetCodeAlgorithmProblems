from typing import List, Optional 

class Solution:
    
    __name_of_instance = 'SolutionOne'
    
    def __init__(self) -> None:
        if Solution.__name_of_instance != 'SolutionOne':
            raise Exception('This is a singleton class.')
        else:
            Solution.__name_of_instance = self 
    
    @staticmethod
    def get_instance(self):
        print(Solution.__name_of_instance)
    
    def isValid(self, s: str) -> bool:
        
        temp = list()        
        list_parentheses = ["(","[","{"]
        
        for p in s:
            if p in list_parentheses:
                temp.append(p)
            else:
                if not temp:
                    return False
                other_half = temp.pop()
                
                if p == ")":
                    if other_half != "(":
                        return False 
                elif p == "]":
                    if other_half != "[":
                        return False 
                elif p == "}":
                    if other_half != "{":
                        return False 
                else: 
                    return False
                
        if temp:
            return False

        
        return True
    
    
class SolutionTwo:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''
    
    
def factory_solutions(name = 'SolutionOne'):
    
    localizers = {
        'SolutionOne': Solution,
        'SolutionTwo': SolutionTwo
    }
    
    
    return localizers.get(name, Solution)()


class WrittenText: 
    
    def __init__(self,text) -> None:
        self._text = text 
        
    def render(self) -> str:
        return self._text
    
    
class UnderlineWrapper(WrittenText):
    
    def __init__(self, wrappedClass) -> None:
        self._wrappedClass = wrappedClass
        
    def render(self) -> str:
        return "<u>{}</u>".format(self._wrappedClass.render())   
  
    
class ItaliclineWrapper(WrittenText):
    
    def __init__(self, wrappedClass) -> None:
        self._wrappedClass = wrappedClass
        
    def render(self) -> str:
        return "<i>{}</i>".format(self._wrappedClass.render())  
        
class LogisticRegression:
    
    def __init__(self) -> None:
        self.name = 'regression'
        
    def model_type(self) -> str:
        return 'Regression Model'
    
class XGBoost:
    
    def __init__(self) -> None:
        self.name = 'xgboost'
        
    def ml_model_type(self) -> str:
        return 'Ensemble Technique'
    
    
class Adapter:
    
    def __init__(self,obj,**adapter_methods) -> None:
        self.obj = obj
        self.__dict__.update(adapter_methods)
        
    def __getattr__(self,attr):
        return getattr(self.obj, attr)
    
    def original_dict(self):
        return self.obj.__dict__
        


print(factory_solutions('SolutionOnesdfsdf').isValid('()'))

before = WrittenText('Eyes of the world')

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
    