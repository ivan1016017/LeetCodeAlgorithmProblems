from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        listnode_to_list = self.ListNodeToLIst(head)
        temp_list =list()
        for i in range(len(listnode_to_list)):
            if i != (len(listnode_to_list) - n):
                temp_list.append(listnode_to_list[i])
        return self.ListToListNode(temp_list)
    
    def ListNodeToLIst(self, head: ListNode) -> List:
        temp_list = list()
        temp_listNode = None
        try:
            head.val
        except:
            return []
        # add first element to list
        temp_list.append(head.val)

        # fill the list
        while head.next:
            temp_listNode = head.next
            head = temp_listNode

            if head:
                try:
                    head.val
                except:
                    temp_list.append(head)
                    break
                temp_list.append(head.val)
            else:
                break
        return temp_list
    
    def ListToListNode(self, list_numbers: List) -> ListNode:
        # initialize listNode
        result = ListNode(0)

        if list_numbers == []:
            return None
        # loop through the list
        result.val = list_numbers[0]
        temp = result
        for i in range(1,len(list_numbers)):
            temp.next = ListNode(list_numbers[i])
            temp = temp.next
        return result
    
class SolutionTwo:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        # advance fast to nth position
        for i in range(n):
            fast = fast.next
            
        if not fast:
            return head.next
        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
        # delete the node
        slow.next = slow.next.next
        return head
    
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
        return 'Ensemble Tecnique'

    def __str__(self) -> str: 
        return f"This is an instance of the class XGBoost with max_depth {self.max_depth}"

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





#adding new line
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

        

