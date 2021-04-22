
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sample = list()


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        return self.sample.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        x = self.sample[0]
        self.sample = self.sample[1:]
        return x


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.sample[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.sample