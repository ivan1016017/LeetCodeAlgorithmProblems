from typing import List, Union, Optional
from abc import ABC, abstractmethod

# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    __name_of_instance = 'SolutionOne'

    def __init__(self):

        if Solution.__name_of_instance != 'SolutionOne':
            raise Exception('This is a singleton class')
        else: 
            Solution.__name_of_instance = self 

        # define the variable that will take the results across different methods
        self.head = None 

    @abstractmethod
    def get_instance(self) -> None: 
        print(Solution.__name_of_instance)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        prev = None 
        temp_carry = 0
        temp = None 


        # define while statemente to iterate the sum process

        while (l1 is not None or l2 is not None):


        # take the values from the node lists and turn them zero if they are None

            f_value = 0 if l1 is None else l1.val
            s_value = 0 if l2 is None else l2.val

        # take the sum of the values

            sum = temp_carry + f_value + s_value 

        # define the reminder of the sum

            temp_carry = 1 if sum >= 10 else 0

        # take the sum that is going to be places in the linked list

            sum = sum if sum < 10 else sum % 10

        # define the temp nodelist that is going to be inserted in the nested linked list
            temp = ListNode(sum)
            if self.head is None: 
                self.head = temp 
            else: 
                prev.next = temp 


        #pass to the next linked list and iterate the process
            prev = temp 

        # pass to the next values if the nex value in the linked list is not empty

            if l1 is not None: 
                l1 = l1.next 
            if l2 is not None: 
                l2 = l2.next 

        if temp_carry > 0:
            temp.next = ListNode(temp_carry)

        return self.head

class SolutionTwo:
    def addTwoNumbers(self, l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        n = toint(l1) + toint(l2)
        first = last = ListNode(n % 10)
        while n > 9:
            n /= 10
            last.next = last = ListNode(n % 10)
        return first

class WrittenText:

    def __init__(self,text:str=None) -> None: 
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
        return f'This is an instance of the XGBoost with max_depth {self.max_depth}'

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

print(factory('sdfd').addTwoNumbers(ListNode(2,ListNode(4,ListNode(3))), ListNode(5,ListNode(6,ListNode(4)))))

# print(factory('sdfd').addTwoNumbers(ListNode(2,ListNode(4,ListNode(3))), ListNode(5,ListNode(6,ListNode(4)))))


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