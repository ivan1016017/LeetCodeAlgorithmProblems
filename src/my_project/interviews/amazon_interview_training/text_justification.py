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

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
            
        result, current_list, num_of_letters = [],[], 0
        # result -> stores final result output
        # current_list -> stores list of words which are traversed but not yet added to result
        # num_of_letters -> stores number of chars corresponding to words in current_list
        
        for word in words:
            
            # total no. of chars in current_list + total no. of chars in current word
            # + total no. of words ~= min. number of spaces between words
            if num_of_letters + len(word) + len(current_list) > maxWidth:
                # size will be used for module "magic" for round robin
                # we use max. 1 because atleast one word would be there and to avoid modulo by 0
                size = max(1, len(current_list)-1)
                
                for i in range(maxWidth-num_of_letters):
                    # add space to each word in round robin fashion
                    index = i%size
                    current_list[index] += ' ' 
                
                # add current line of words to the output
                result.append("".join(current_list))
                current_list, num_of_letters = [], 0
            
            # add current word to the list and add length to char count
            current_list.append(word)
            num_of_letters += len(word)
        
        # form last line by join with space and left justify to maxWidth using ljust (python method)
        # that means pad additional spaces to the right to make string length equal to maxWidth
        result.append(" ".join(current_list).ljust(maxWidth))
        
        return result
    

class SolutionTwo:
	# Why slots: https://docs.python.org/3/reference/datamodel.html#slots
    # TLDR: 1. faster attribute access. 2. space savings in memory.
    # For letcode problems this can save ~ 0.1MB of memory <insert is something meme>
    __slots__ = ()
	
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
	    # Init return array in which, we'll store justified lines
        lines = []
		# current line width
        width = 0
		# current line words
        line = []
        
        for word in words:
			# Gather as many words that will fit under maxWidth restrictions.
			# Line length is a sum of:
			# 1) Current word length
			# 2) Sum of words already in the current line
			# 3) Number of spaces (each word needs to be separated by at least one space)
            if (len(word) + width + len(line)) <= maxWidth:
                width += len(word)
                line.append(word)
                continue
            
			# If the current line only contains one word, fill the remaining string with spaces.
            if len(line) == 1:
				# Use the format function to fill the remaining string with spaces easily and readable.
				# For letcode police, yes you could do something like:
				#     line = " ".join(line)
				#     line += " " * (maxWidth - len(line))
				#     lines.append(line)
				# to be more "raw", but I see no point in that.
                lines.append(
                    "{0: <{width}}".format( " ".join(line), width=maxWidth)
                )
            else:
			    # Else calculate how many common spaces and extra spaces are there for the current line.
				# Example:
                #  line = ['a', 'computer.', 'Art', 'is']
				# width left in line equals to: maxWidth - width: 20 - 15 = 5
				# len(line) - 1 because to the last word, we aren't adding any spaces
				# Now divmod will give us how many spaces are for all words and how many extra to distribute.
				# divmod(5, 3) = 1, 2
				# This means there should be one common space for each word, and for the first two, add one extra space.
                space, extra = divmod(
                    maxWidth - width,
                    len(line) - 1
                )
                
                i = 0
				# Distribute extra spaces first
				# There cannot be a case where extra spaces count is greater or equal to number words in the current line.
                while extra > 0:
                    line[i] += " "
                    extra -= 1
                    i += 1
                
				# Join line array into a string by common spaces, and append to justified lines.
                lines.append(
                    (" " * space).join(line)
                )
            
			# Create new line array with the current word in iteration, and reset current line width as well.
            line = [word]
            width = len(word)
        
		# Last but not least format last line to be left-justified with no extra space inserted between words.
		# No matter the input, there always be the last line at the end of for loop, which makes things even easier considering the requirement.
        lines.append(
            "{0: <{width}}".format(" ".join(line), width=maxWidth)
        )
        
        return lines
    
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


            


