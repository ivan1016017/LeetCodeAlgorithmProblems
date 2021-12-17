from typing import List 

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]
        visited = []
        #visited array keeps a track of visited elements. without this maximum recursion depth 
        #exceeded error might be encountered
        
        def floodfilluntil(image,x,y,newColor,oldColor):
            if (x,y) not in visited:
                visited.append((x,y))
            else:
                return
            if x<0 or y<0 or x>=m or y>=n:
                return
            if image[x][y]!=oldColor:
                return
            
            image[x][y] = newColor
            
            floodfilluntil(image,x+1,y,newColor,oldColor)
            floodfilluntil(image,x-1,y,newColor,oldColor)
            floodfilluntil(image,x,y+1,newColor,oldColor)
            floodfilluntil(image,x,y-1,newColor,oldColor)
            
            return image
        
        return(floodfilluntil(image,sr,sc,newColor,oldColor))
        