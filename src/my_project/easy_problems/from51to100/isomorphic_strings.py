

class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_map = dict()
        for a, b in zip(s, t):
            if a in dict_map:
                if not dict_map[a]==b:
                    return False
            else:
                if b not in dict_map.values():
                    dict_map[a]=b
                else:
                    return False
        return True


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        temp_dict = dict()
        for entry_s, entry_t in zip(s,t):

            if entry_s in temp_dict:
                if temp_dict[entry_s] != entry_t:
                    return False

            else:
                if entry_t not in temp_dict.values():
                    temp_dict[entry_s] = entry_t
                else:
                    return False
        return True
