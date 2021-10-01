class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        answer = True
        letters = "abcdefghijklmnopqrstuvwxyz"

        for letter in letters: 
            if letter not in sentence:
                answer = False 
        

        return answer


solution = Solution()

print(solution.checkIfPangram(sentence = "thequickbrownfoxjumpsoverthelazydog"))