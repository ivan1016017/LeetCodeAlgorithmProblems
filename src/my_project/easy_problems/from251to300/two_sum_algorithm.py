from typing import List 


class Solution:
    
    __name_of_instance = 'SolutionOne'
    
    @staticmethod
    def get_instance():
        print(Solution.__name_of_instance)
        
    def __init__(self):
        if Solution.__name_of_instance != 'SolutionOne':
            raise Exception('This is a singleton class')
        else:
            Solution.__name_of_instance = self
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = dict()
        
        for i in range(len(nums)):
            if target - nums[i] in temp:
                return [temp[target-nums[i]],i]
            temp[nums[i]] = i
            
class SolutionTwo: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [hash_table[nums[i]], i]
            else:
                hash_table[target - nums[i]] = i
                         
                
def factory(solution = "Solution"):
    
    localizers = {
        "Solution": Solution,
        "SolutionTwo": SolutionTwo
    }
    
    return localizers[solution]()

class WrittenText: 
    
    def __init__(self, text):
        self._text = text 
        
    def render(self):
        return self._text 
    
class UnderlineWrapper(WrittenText):
    
    def __init__(self, wrappedClass):
        self._wrappedClass = wrappedClass
        
        
    def render(self):
        return "<u>{}</u>".format(self._wrappedClass.render())
                
                
class ItalicWrapper(WrittenText):
    
    def __init__(self, wrappedClass):
        self._wrappedClass = wrappedClass
        
        
    def render(self):
        return "<i>{}</i>".format(self._wrappedClass.render())


print(factory('Solution').twoSum(nums = [2,7,11,15], target = 9))
# print(factory('Solution').twoSum(nums = [2,7,11,15], target = 9))


before_decorator = WrittenText('LeetCode')
after_decorator = ItalicWrapper(UnderlineWrapper(before_decorator))

print("before", before_decorator.render())
print("after", after_decorator.render())


# solution = Solution()
