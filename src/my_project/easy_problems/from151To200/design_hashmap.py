from typing import List 

class MyHashMap(object):

    def __init__(self):
        self.hashMap = []
        

    def put(self, key, value):
        flag = False
        for i in range(len(self.hashMap)):
            if self.hashMap[i][0] == key:
                self.hashMap[i][1] = value
                flag = True
        if flag == False: 
            self.hashMap.append([key,value])
        return None 
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        

    def get(self, key):
        for i in range(len(self.hashMap)):
            if self.hashMap[i][0] == key:
                return self.hashMap[i][1]
        else:
            return -1
        """
        :type key: int
        :rtype: int
        """
        

    def remove(self, key):
        for i in range(len(self.hashMap)):
            if self.hashMap[i][0] == key:
                self.hashMap = self.hashMap[0:i] + self.hashMap[i+1:]
                break
        return None 
        """
        :type key: int
        :rtype: None
        """
