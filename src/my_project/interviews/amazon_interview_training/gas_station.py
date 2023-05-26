from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod


'''
The total amount of gas in the circle must be >= the total cost. Intuitively I think this is fair. If my trip requires 
100 gallons of gas, but the total gas available across every gas station I encounter in this trip is only 90, how can I 
expect to complete my trip? I would need at least 100 gallons.
The question states that there is only one unique solution. I had difficulty proving to myself the solution is optimal 
because I kept considering situations where there's multiple solutions. For ex: gas = [10, 10, 10, 10], cost = [1,1,1,1]. 
In this example you could start at any gas station, but this input would never occur simply because the probem said so.
We greedily pick our start index. What this means is that as long as our current total gas is > 0, we might as well keep going. 
Personally I think picturing this in real life helps. If I have some gas right now, but then go through a few gas stations 
where the cost at each station is greater than the gas gained at that station, I still wouldn't change my start index because 
wherever I started at still contributed to where I am now. If I didn't start where I started, I'd have even less gas than I did now. 
Another way of thinking about it is like this. Assuming I start at station i (by default this means gas[i] must be >= cost[i]), 
there are 2 cases:
Case 1: The next station has positive gain (gas[i+1] > cost[i+1]). Then why would I change my start index? By combining these 2 stations, 
I have even more gas.
Case 2: The next station has negative/no gain (gas[i+1] <= cost[i+1]). Well, I'd still choose to start at i, because as long as 
my total gas is > 0, I'll be making a positive contribution to future stations.
'''
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

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost): return -1

        cur = 0
        res = 0

        for i in range(len(gas)):

            cur += gas[i]
            if cur < cost[i]:
                cur = 0
                res = i+1
            else:
                cur -= cost[i]

        return res
    

class SolutionTwo:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        base = 0 
        i = 0
        while( i < len(gas)):
            tank += gas[i] - cost[i]
            if( tank < 0 ):
                tank = 0 
                base = i+1;
            i+=1
        
        i = 0
        while( i < base ):
            tank += gas[i] - cost[i]
            if( tank < 0 ): return -1
            i+=1

        return base; 

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