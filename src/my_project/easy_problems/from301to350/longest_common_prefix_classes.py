from typing import List, Optional


class Solution:
    
    __name_of_instance = "Solution"
    
    def __init__(self) -> None:
        if Solution.__name_of_instance != "Solution":
            raise Exception("This is a singleton class")
        else: Solution.__name_of_instance = self 
        
    @staticmethod
    def get_instance(self) -> None:
        print(Solution.__name_of_instance)
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        answer: str = ""
        j: int = 0
        
        min_word: str = min(strs, key=len)
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
        
        result = ""
        i = 0
        len_s = len(strs)
        
        if len_s == 0:
            return result 
        
        first_word = strs[0]
        bench_mark = len(min(strs))
        
        while i < bench_mark:
            for word in strs:

                if first_word[i] != word[i]:
                    return result 
            result += first_word[i]
            i+=1
                
        return result
    
def factory(name = "Solution"):
    
    localizers = {
        "SolutionOne": Solution,
        "SolutionTwo": SolutionTwo
    }
    
    return localizers.get(name, Solution)()

class WrittenText: 
    
    def __init__(self,text:str) -> None:
        self._text = text 
        
    def render(self) -> str:
        return self._text
    
class UnderlineWrapper(WrittenText):
    
    def __init__(self,wrappedClass) -> None:
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
    
    def __init__(self, max_depth: int = None) -> None:
        self.name = "xgboost" 
        self.max_depth = max_depth
        
    def ml_model_type(self) -> str: 
        return "Ensemble Technique"
    
    def __str__(self) -> str:
        
        return f"This is an instance of the XGBoost class with max_depth {self.max_depth}"
    
class Adapter:
    
    def __init__(self,obj,**adapter_methods) -> None:
        self.obj = obj 
        self.__dict__.update(adapter_methods)
        
    def __getattr__(self,attr):
        return getattr(self.obj, attr)
    
    def original_dict(self):
        return self.obj.__dict__
    
before = WrittenText("Eyes of the world.")

after = UnderlineWrapper(ItaliclineWrapper(before))

print(before.render())
print(after.render())


print(factory("sdfsd").longestCommonPrefix(strs = ["flower","flow","flight"]))
# print(factory("sdfsd").longestCommonPrefix(strs = ["flower","flow","flight"]))


logistic = LogisticRegression()
xgboost = XGBoost()
objects = list()

objects.append(Adapter(logistic, model_type = logistic.model_type()))
objects.append(Adapter(xgboost, model_type = xgboost.ml_model_type()))

for obj in objects: 
    print("A {0} model of type {1}".format(obj.name, obj.model_type))


second_xgboost = XGBoost(7)
print(second_xgboost)
