from typing import List, Union
import heapq
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

    def mergeKLists(self, lists):
        '''
        lists: List[ListNode]
        '''

        heap = [(lists[i],i) for i in range(len(lists)) if lists[i]]
        heapq.heapify(heap)
        head = None
        
        while heap: 
            nex = heapq.heappop(heap)
            node = ListNode(nex[0])
            index = nex[1]
            if not head:
                head = node
                trav = head 
            else: 
                trav.next = node 
                trav = trav.next 
            if lists[index].next:
                lists[index] = lists[index].next
                heapq.heappush(head,(lists[index].val,index))

        return head


class SolutionTwo:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        list_node_to_list = self.ListNodeToList(lists)
        sorted_list = self.merge_sort(list_node_to_list,0, len(list_node_to_list)-1)
        list_to_listNode = self.from_list_listNode(sorted_list)
        if list_to_listNode == []:
            list_to_listNode = ListNode("")
        return list_to_listNode

    def merge(self, A, p, q, r):
        # r,p and q are the indexes in the array

        # assign the values to temp arrays
        l_array = list();
        r_array = list()

        # l_array includes the q index
        for i in range(p, q + 1):
            l_array.append(A[i])
        # r_array does not include q index
        for j in range(q + 1, (r + 1)):
            r_array.append(A[j])

        # merge  the lowest items first
        i = 0;
        j = 0
        for k in range(p, r + 1):
            # add the remaining r_array to A
            if i > q - p:
                for l in range(k, r + 1):
                    A[l] = r_array[j]
                    j += 1
                break
            # add the remaining l_array to A
            if j > r - q - 1:
                for l in range(k, r + 1):
                    A[l] = l_array[i]
                    i += 1
                break
            if l_array[i] <= r_array[j]:
                A[k] = l_array[i]
                i += 1
                continue

            if l_array[i] > r_array[j]:
                A[k] = r_array[j]
                j += 1
                continue

        return A

    def merge_sort(self, A, p, r):
        # define the conditions for recursion
        if p < r:
            # define how to split the file
            q = (p + r) // 2
            self.merge_sort(A, p, q)
            self.merge_sort(A, q + 1, r)
            self.merge(A, p, q, r)
        return A

    def ListNodeToList(self, list_nodes: List[ListNode]) -> List:

        # define the list
        temp_list = list()
        # loop through the list of ListNodes
        for i in range(len(list_nodes)):
            # insert the first element of ListNode into list
            try:
                temp_list.append(list_nodes[i].val)
            except:
                continue
            # check if the next element of ListNode is available
            if list_nodes[i].next:
                # save the next element into temp_current
                temp_current = list_nodes[i].next
                # while loop
                while (temp_current):
                    # insert temp_current into temp_list
                    try:
                        temp_list.append(temp_current.val)
                    except:
                        temp_list.append(temp_current)
                    # assign nexc list_nodes[i] value to temp_current
                    try: temp_current = temp_current.next
                    except:
                        break
        return temp_list



    def from_list_listNode(self, list_numbers: List[int]) -> List[ListNode]:
        # define the scenario where the list is None
        # define the scenario where the list is empty
        if list_numbers is None or list_numbers == []:
            return []
        # the list is not empty
        # loop through the list
        temp = ListNode(list_numbers[0])
        current = temp
        for i in range(len(list_numbers)-1):
            # insert list_numbers entry to the ListNode.val
            current.next = ListNode(list_numbers[i+1])
            # set the next
            current = current.next
        return temp
        

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
        return f'This is an instance of the class XGBost with max_depth {self.max_depth}'

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
        