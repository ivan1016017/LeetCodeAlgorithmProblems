from typing import List 

class Solution:
    
    __name_of_instance = "SolutionOne"
    
    def __init__(self) -> None:
        if Solution.__name_of_instance != "SolutionOne":
            raise Exception("This is a singleton class.")
        else: 
            Solution.__name_of_instance = self 
            
    @staticmethod
    def get_instance(self) -> None:
        print(Solution.__name_of_instance)
    
    def longestCommonPrefix(self, strs: List[str]) -> str:

        answer = ""
        j = 0
        
        min_word = min(strs, key=len)
        benchmark = len(min_word)
        
        while j < benchmark:
            for word in strs:
                if word[j] != min_word[j]:
                    return answer 
            answer = answer + min_word[j]
            j+=1     
        
        return answer 
   
    
class SolutionTwo:
    
     def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
    
def factory(name = "SolutionOne"):
    
    localizers = {
        "SolutionOne": Solution,
        "SolutionTwo": SolutionTwo
    }
    
    return localizers.get(name, Solution)()


class WrittenText:
    
    def __init__(self, text) -> None:
        self._text = text 
        
    def render(self) -> str:
        return self._text
    
class UnderlineWrapper(WrittenText):
    
    def __init__(self, wrappedClass) -> None:
        self.wrappedClass = wrappedClass
        
    def render(self) -> str:
        return "<u>{}</u>".format(self.wrappedClass.render())
    
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
    
    def __init__(self) -> None:
        self.name = 'xgboost'
        
    def ml_model_type(self) -> str:
        return "Emsemble Technique"
    
class Adapter: 
    
    def __init__(self, obj, **adapter_methods) -> None:
        self.obj = obj 
        self.__dict__.update(adapter_methods)
        
    def __getattr__(self, attr):
        return getattr(self.obj, attr)
    
    def original_dict(self):
        return self.obj.__dict__
        

print(factory("sdfsdf").longestCommonPrefix(["flower","flow","flight"]))
# print(factory("sdfsdf").longestCommonPrefix(["flower","flow","flight"]))

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



