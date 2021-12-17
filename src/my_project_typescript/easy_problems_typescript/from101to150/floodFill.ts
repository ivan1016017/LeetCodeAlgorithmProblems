function floodFill(image: number[][], sr: number, sc: number, newColor: number): number[][] {

    let m: number = image.length
    let n: number = image[0].length
    let oldColor: number = image[sr][sc]
    // visitedCoordinates containes the coordinates of the elements visited 
    let visitedCoordinates: Array<Array<number>> =[]

    function floodFillUntil(image: number[][], x: number, y: number, newColor: number, oldColor: number): number[][]{
        if (!visitedCoordinates.includes([x,y])){
            visitedCoordinates.push([x,y])
        }
        else{
            return image
        }
        if (x <0 || y < 0 || x >= m || y >= n){
            return image
        }
        if (image[x][y] != oldColor){
            return image
        }

        image[x][y] = newColor
        floodFillUntil(image,x-1, y, newColor, oldColor)
        floodFillUntil(image,x+1, y, newColor, oldColor)
        floodFillUntil(image,x, y-1, newColor, oldColor)
        floodFillUntil(image,x, y+1, newColor, oldColor)


        return image
    }

    return floodFillUntil(image, sr,sc,newColor, oldColor)
};

console.log(floodFill([[1,1,1],[1,1,0],[1,0,1]],
    1,
    1,
    2))