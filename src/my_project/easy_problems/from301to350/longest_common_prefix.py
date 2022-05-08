from typing import List



class Solution:
    
    __name_of_instance = "SolutionOne"
    
    def __init__(self) -> None: 
        if Solution.__name_of_instance != "SolutionOne":
            raise Exception("This is a singleton class.")
        else: 
            Solution.__name_of_instance = self 
            
    @staticmethod
    def get_instance() -> None:
        print(Solution.__name_of_instance)
        
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        answer: str = ""
        j: int = 0
        
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
        # set flag boolean, and temp_index values
        flag = False
        temp_index = 0
        temp_str = ""

        # check empty list
        if len(strs) == 0 or "" in strs:
            return temp_str
        else:
            # while (flag)
            while (not flag):
                # loop through the list of lists
                if len(strs) == 1:
                    return temp_str + strs[0]
                for i in range(len(strs) - 1):
                    # check if pairs of list have the same entries in the same index
                    try:
                        strs[i][temp_index]
                        strs[i + 1][temp_index]
                        
                    except:
                        return temp_str
                    else: 
                        if strs[i][temp_index] != strs[i + 1][temp_index]:
                            print("Hi")
                            flag = True
                            break

                        
                if not flag:
                    temp_str += strs[0][temp_index]
                    temp_index += 1
                else:
                    break
            return temp_str
        
        
def factory(name = "SolutionOne"):
    
    localizers = {
        "SolutionOne": Solution,
        "SolutionTwo": SolutionTwo
    }
    
    return localizers.get(name, Solution)()

class WrittenText: 
    
    def __init__(self, text:str) -> None:
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
    
    def __init__(self,obj,**adapter_methods) -> None:
        self.obj = obj 
        self.__dict__.update(adapter_methods)
        
    def __getattr__(self,attr):
        return getattr(self.obj,attr)
    
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
    
    