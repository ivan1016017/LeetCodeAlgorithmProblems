
class MyStack:

    def __init__(self):
        self.sample = list()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.sample.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.sample.pop()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.sample[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.sample
