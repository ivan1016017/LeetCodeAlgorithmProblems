from typing import List



class Solution:
    
    __name_of_instance = 'SolutionOne'
    
    def __init__(self):
        if Solution.__name_of_instance != 'SolutionOne':
            raise Exception('This is a singleton class')
        else:
            Solution.__name_of_instance = self
            
    @staticmethod
    def get_instance():
        print(Solution.__name_of_instance)
        
        
    def isPalindrome(self, x: int) -> bool:      
        x = str(x) 
        len_x = len(x)
        for i in range(len_x//2):
            if x[i] != x[len_x-1-i]:
                return False 
        return True
    
    
class SolutionTwo:
    
    def isPalindrome(self, x:int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        x = str(x)
        lmost = 0
        rmost = len(x)-1
        while lmost <= rmost:
            if x[lmost] != x[rmost]:
                return False
            else:
                lmost += 1
                rmost -= 1
        return True
    
    
    
def factorySolution(name = "Solution"):
    
    localizers = {
        'Solution': Solution,
        'SolutionTwo': SolutionTwo
    }
    
    return localizers[name]()


class WrittenText: 
    
    def __init__(self, text):
        self._text = text 
        
    def render(self):
        return self._text 
    
class UnderlineWrapper(WrittenText):
    
    def __init__(self,wrappedClass):
        self._wrappedClass = wrappedClass
        
    def render(self):
        return "<u>{}</u>".format(self._wrappedClass.render())
        
class ItalicWrapper(WrittenText):
    
    def __init__(self,wrappedClass):
        self._wrappedClass = wrappedClass
        
    def render(self):
        return "<i>{}</i>".format(self._wrappedClass.render()) 
    
    
    
class LogisticRegression:
    
    def __init__(self):
        self.name = 'knn' 
        
    def model_type(self):
        return 'Regression Model'

class XGBoost: 
    
    def __init__(self):
        self.name = 'xgboost'
        
    def ml_type(self):
        return 'Ensemble technique'
    
class Adapter: 
    
    def __init__(self,obj, **adapter_methods):
        self.obj = obj 
        self.__dict__.update(adapter_methods)
        
    def __getattr__(self,attr):
        return getattr(self.obj, attr)
    
    def original_dict(self):
        return self.obj.__dict__


print(factorySolution('Solution').isPalindrome(121))

before = WrittenText('word') 
after = ItalicWrapper(UnderlineWrapper(before))
print('before', before.render())
print('after', after.render())

logistic = LogisticRegression()
xgboost = XGBoost()
objects = list()

objects.append(Adapter(logistic, model_type = logistic.model_type()))
objects.append(Adapter(xgboost, model_type = xgboost.ml_type()))

for obj in objects: 
    print("A {0} model of type {1}".format(obj.name, obj.model_type))

