def getRemovableIndices(str1, str2):
    if len(str1) != len(str2) + 1:
        return [-1]
    else: 
        indices = []
        
        for i in range(len(str1)):
            if str1[:i] + str1[i+1:] == str2:
                indices.append(i)
        
        return indices if indices else [-1]
