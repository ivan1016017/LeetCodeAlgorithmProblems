


if __name__ == '__main__':
    class MinStack:

        def __init__(self):
            self.temp_list = list()

        def push(self, val: int) -> None:
            self.temp_list.append(val)


        def pop(self) -> None:
            self.temp_list.pop()

        def top(self) -> int:
            return self.temp_list[-1]

        def getMin(self) -> int:
            return min(self.temp_list)

    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(val)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()