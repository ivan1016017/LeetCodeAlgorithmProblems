from typing import List, Union 
from abc import ABC, abstractmethod
import itertools

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

    # calculate the sum of presums for certain strength at index i
    # we will use it in calculating the sum of all subarrays containing particular element
    # we stuff it with an extra value at the end to accomodate the lookups at -1 for left 
    # boundary which includes the beginning of the array
    def get_presums(self, strength):
        n  = len(strength)
        res = [0] * (n + 2)
        cur_sum = 0
        
        for i in range(n):
            cur_sum += strength[i]
            res[i+1] = (res[i] + cur_sum)
                    
        return res
            
    def totalStrength(self, strength: List[int]) -> int:
        if not strength:
            return 0
        
        n = len(strength)
        res = 0
        stack = []
        
        pre_sums = self.get_presums(strength)
        print(pre_sums)
                
        # use monotonic stack to find the min for a certain range of subarrays
        # and add an extra element at the end of the iterable to make sure we'll pop all elements
        # from the stack
        for i, num in enumerate(itertools.chain(strength, [-float('inf')])):
            print(i,num,stack)
            while stack and num < strength[stack[-1]]:
                cur_min_idx = stack.pop()
                left  = stack[-1] if stack else -1
                
                # the TOTAL of all subarrays containing our minimum strength found above
                cur_sub_sum = (cur_min_idx - left) * (pre_sums[i] - pre_sums[cur_min_idx]) - (i - cur_min_idx ) * (pre_sums[cur_min_idx] - pre_sums[left])
                res +=  cur_sub_sum * strength[cur_min_idx]
                        
            stack.append(i)
                
        # i didn't use modular arithmetic along the way and only indicated its use here
        # cause in python int numbers don't have the limitation they may have in other languages
        return res % (10**9 + 7)

class SolutionTwo:
    def totalStrength(self, strength: List[int]) -> int:
        KMAX = 10 ** 9 + 7
        res, N = 0, len(strength)
        presum, total, tt, pl2r = [], 0, 0, []
        for i, v in enumerate(strength):
            total += v
            presum.append(total)
            tt += total
            pl2r.append(tt)
        
        pr2l, total, tt = [], 0, 0
        for i in range(N - 1, -1, -1):
            total += strength[i]
            tt += total
            pr2l.append(tt)
        pr2l.reverse()
            
        def complexsum(l, m, r):
			# use triangle to find the subarray sum between l and r (inclusive).
            res = (m - l + 1) * (r - m + 1) * strength[m]
            res += (m - l + 1) * ((total - presum[m]) * (r - m) - (pr2l[m + 2] if m < N - 2 else 0) + (pr2l[r+2] if r < N - 2 else 0))
            res += (r - m + 1) * ((presum[m-1] if m > 0 else 0) * (m - l) - (pl2r[m-2] if m > 1 else 0) + (pl2r[l-2] if l > 1 else 0))
            return res % KMAX
    
		# this is the same as in 907.
        stk = []
        for i in range(N):
            while stk and strength[stk[-1]] > strength[i]:
                idx = stk.pop()
                res += strength[idx] * complexsum((stk[-1] + 1) if stk else 0, idx, i - 1)
                res %= KMAX
            stk.append(i)
        while stk:
            idx = stk.pop()
            res += strength[idx] * complexsum((stk[-1] + 1) if stk else 0, idx, N - 1)
            res %= KMAX
        return res

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

print(factory('sdf').totalStrength([4,6,5]))
# print(factory('sdf').totalStrength([4,6,5]))


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

