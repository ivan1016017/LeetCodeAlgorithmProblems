from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import Counter, defaultdict

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

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        seen = Counter(nums[:k]) #from collections import Counter (elements and their respective count are stored as a dictionary)
        summ = sum(nums[:k])
        
        
        res = 0
        if len(seen) == k:
            res = summ
            
            
        for i in range(k, len(nums)):
            summ += nums[i] - nums[i-k]
            seen[nums[i]] += 1
            seen[nums[i-k]] -= 1
            
            if seen[nums[i-k]] == 0:
                del seen[nums[i-k]]
                
            if len(seen) == k:
                res = max(res, summ) 
                
        return res
    
class SolutionTwo:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int) #to store the elements of the sliding window.
        
        total = 0
        res = 0 
        for i in range(k):
            hm[nums[i]] += 1
            total += nums[i]
        
        # if all keys of the hashmap(elements of window) are distinct, then store their sum in res.
        if len(hm) == k:
            res = total
            
        for i in range(k, len(nums)):
            add = nums[i] #element to add in the window.
            remo = nums[i - k] #element to remove from window.
            
            hm[add] += 1
            hm[remo] -= 1
            if hm[remo] == 0:
                hm.pop(remo)
                
            total += add
            total -= remo
            
            # if all keys of the hashmap(elements of window) are distinct,
            # then take max of res and total(sum of current window)
            if len(hm) == k:
                res = max(res, total)
        
        return res
    
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


            


