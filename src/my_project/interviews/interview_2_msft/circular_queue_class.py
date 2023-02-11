from typing import List, Union 
from abc import ABC, abstractmethod

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [-1]*k
        self.size = k
        self.num = 0
        self.head = 0
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.num < self.size:
            self.queue[(self.head+self.num) % self.size] = value
            self.num += 1
            return True
        else:
            return False
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.num == 0:
            return False
        else:
            self.queue[self.head] = -1
            self.head = (self.head+1) % self.size
            self.num -= 1
            return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.num == 0:
            return -1
        else:
            return self.queue[self.head]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.num == 0:
            return -1
        else:
            return self.queue[(self.head+self.num-1) % self.size]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.num == 0
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.num == self.size