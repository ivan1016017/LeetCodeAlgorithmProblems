from typing import List, Union 
from abc import ABC, abstractmethod
import collections



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

    '''
    Sort all time points and label the start and end points. Move a vertical line from left to right.
    When it meets a start point, curr_rooms += 1. When it meets an end point, curr_rooms -= 1.
    (if there is a tie: put end point before start point). Update the maximal occupied rooms during the move.
    
    '''

    def minMeetingRooms(self, intervals):
        lst = []
        for start, end in intervals:
            lst.append((start, 1))
            lst.append((end, -1))
        lst.sort()

        print(lst)
        res, curr_rooms = 0, 0
        for t, n in lst:
            curr_rooms += n
            res = max(res, curr_rooms)
        return res


class SolutionTwo:

    '''
    It is easy to observe that the minimum number of conference rooms needed is 
    equal to the size of the maximum set of pairwise overlapping intervals. 
    This can be calculated as follows: We first sort the intervals in ascending 
    start time to obtain intervals_sorted. Then we iterate over intervals_sorted, 
    and for each intervals_sorted[i], we calculate the number of intervals intervals_
    sorted[j] (j < i) that has nontrivial overlap with intervals_sorted[i]. Denote the 
    number by N_i. The minimum number of conference rooms needed is then given 
    by the maximum of (N_i+1) over i.

    To calculate N_i for each i, we first initialize a queue end_points of end time 
    of each interval sorted in ascending order. We also use a counter pop_count to 
    record the number of elements that has been dequeued from end_points. Then for 
    each intervals_sorted[i], we dequeue from end_points, and update pop_count, until 
    end_points[0] > intervals_sorted[i].start. It is easy to see that pop_count is 
    precisely the number of intervals intervals_sorted[j] that has 
    intervals_sorted[j].end <= intervals_sorted[i].start, which is the number of 
    intervals intervals_sorted[j] (j < i) that has trivial overlap with intervals_sorted[i]. 
    Therefore, the number N_i is given by i-pop_count.
    '''
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x: x[0])
        end_points = collections.deque(sorted([interval[1] for interval in intervals]))
        print(intervals)
        print(end_points)
        res = 1
        pop_count = 0
        for i in range(1, len(intervals)):
            while end_points and end_points[0] <= intervals[i][0]:
                print('inside')
                end_points.popleft()
                pop_count += 1
            print('pop_count ----> ',pop_count)
            res = max(res, i-pop_count+1)
            print(res)
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

# print(factory('sdfds').minMeetingRooms(intervals = [[0,30],[5,10],[15,20]]))
# print(factory('sdfds').minMeetingRooms(intervals = [[0,30],[5,10],[15,20]]))


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

solution = Solution()

print(solution.minMeetingRooms([[2,11],[6,16],[11,16]]))
