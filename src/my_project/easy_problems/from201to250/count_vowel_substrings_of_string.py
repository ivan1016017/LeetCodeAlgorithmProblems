from typing import List 

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        temp = list()
        
        dict_letters = {"a":1, "b":-1,"c":-1, "d":-1,"e":1, "f":-1, "g":-1,
                        "h":-1, "i":1,"j":-1, "k":-1,"l":-1, "m":-1,
                        "n":-1, "o":1,"p":-1, "q":-1,"r":-1, "s":-1,
                        "t":-1, "u":1,"v":-1, "w":-1,"x":-1, "y":-1, "z":-1}
        
        
        len_words = len(word)
        count = 0
        answer = 0
        
        
        for i in range(len_words):
            temp = []
            count = 0
            
            for j in range(i, len_words):
                if word[j] not in temp:
                    if dict_letters[word[j]] == 1:
                        temp.append(word[j])
                        count += 1
                        if count == 5:
                            answer += 1
                    else: 

                        break 
                else: 
                    if count == 5:
                        answer += 1
                        
        return answer 
    
solution = Solution()

print(solution.countVowelSubstrings(word = "aeiouu"))

print(solution.countVowelSubstrings(word = "unicornarihan"))

print(solution.countVowelSubstrings(word = "cuaieuouac"))

print(solution.countVowelSubstrings(word = "bbaeixoubb"))

print(solution.countVowelSubstrings(word = "poazaeuioauoiioaouuouaui"))



