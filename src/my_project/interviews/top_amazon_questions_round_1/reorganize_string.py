from typing import List, Union, Collection, Mapping, Optional

class Solution:
    def reorganizeString(self, s: str) -> str:

        dic_str = dict()
        len_s = len(s)

        for c in s: 
            dic_str[c] = dic_str.get(c, 0) + 1

        print(dic_str)

        lst_s = list(set([c for c in s]))
        lst_s.sort(key=lambda x: dic_str[x], reverse=True)

        solution = [None for s in s]

        if dic_str[lst_s[0]] > (len(s) + 1) // 2:
            return ""        

        i = 0        
        for c in lst_s:
            for _ in range(dic_str[c]):
                if i >= len_s:
                    i = 1                
                solution[i] = c 
                i += 2
                

               

        return ''.join(solution)



