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

    def numberToWords(self, num):

        dic1 = {9:"Nine", 8:"Eight", 7:"Seven", 6:"Six", 
                5:"Five", 4:"Four", 3:"Three", 2:"Two", 1:"One"}
        dic2 = {90:"Ninety", 80:"Eighty", 70:"Seventy", 60:"Sixty", 
                50:"Fifty", 40:"Forty", 30:"Thirty", 20:"Twenty"} 
        dic3 = {19:"Nineteen", 18:"Eighteen", 17:"Seventeen", 
                16:"Sixteen", 15:"Fifteen", 14:"Fourteen", 13:"Thirteen", 
                12:"Twelve", 11:"Eleven", 10:"Ten"}
        
        def helper(num):
            if num < 10: 
                return dic1[num]
            elif  10 <= num <20: 
                return dic3[num]
            elif num < 100:
                res = []
                q, num = divmod(num,10)
                res.append(dic2[q*10])
                if num > 0:
                    res.append(' '+dic1[num])
                return ''.join(res)
            elif num < 1000:
                q, num = divmod(num,100)
                if num == 0:
                    return dic1[q]+ ' ' + 'Hundred'
                else: 
                    return dic1[q] + ' ' + 'Hundred' + ' ' + helper(num)
            elif num < 1000000:
                q, num = divmod(num,1000)
                if num == 0:
                    return helper(q) + ' ' + 'Thousand'
                else: 
                    return helper(q) + ' ' + 'Thousand' + ' ' + helper(num)
            elif num < 1000000000:
                q, num = divmod(num, 1000000)
                if num == 0:
                    return helper(q)+" "+"Million"
                else:
                    return helper(q)+" "+"Million"+" "+helper(num)
            else:
                q, num = divmod(num, 1000000000)
                if num == 0:
                    return helper(q)+" "+"Billion"
                else:
                    return helper(q)+" "+"Billion"+" "+helper(num)  
        
        if num == 0:
            return 'Zero'
        
        return helper(num)
    
class SolutionTwo:
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
            'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n/10-2]] + words(n%10)
            if n < 1000:
                return [to19[n/100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(p+1):
                    return words(n/1000**p) + [w] + words(n%1000**p)
        return ' '.join(words(num)) or 'Zero'
    
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


            
