from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".",
                       "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---",
                       "k":"-.-", "l":".-..", "m":"--", "n":"-.",
                       "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...",
                       "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-",
                       "y":"-.--", "z":"--.."}

        temp_set = set()
        count: str = ""
        for sentence in words:
            count = ""
            for word in sentence:
                count += morse_codes[word]
            temp_set.add(count)


        return len(temp_set)

solution = Solution()
print(solution.uniqueMorseRepresentations(words = ["gin", "zen", "gig", "msg"]))