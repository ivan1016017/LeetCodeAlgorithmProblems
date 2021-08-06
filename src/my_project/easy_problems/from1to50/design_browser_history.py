from typing import List


class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur_page_index = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.history = self.history[:self.cur_page_index + 1]
        self.history.append(url)
        self.cur_page_index = len(self.history) - 1

    def back(self, steps: int) -> str:
        self.cur_page_index = max(self.cur_page_index - steps, 0)
        return self.history[self.cur_page_index]

    def forward(self, steps: int) -> str:
        if steps + self.cur_page_index >= len(self.history):
            self.cur_page_index = len(self.history) - 1
        else:
            self.cur_page_index += steps
        return self.history[self.cur_page_index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

solution = BrowserHistory("leetcode")
solution.visit("google")
solution.visit("facebook")
solution.visit("youtube")
print(solution.back(1))
print(solution.back(1))
print(solution.forward(1))
solution.visit("linkedin")
print(solution.forward(2))
print(solution.back(2))
print(solution.back(7))