function surfaceArea(grid: number[][]): number {

    let solution: number = 0
    let x: number = grid.length
    let y: number = grid[0].length 
    
    for (let i = 0; i < x; i++){
        for (let j =0; j < y; j++){
            if (grid[i][j] !== 0){
                solution += 2 + grid[i][j]*4
                if (i < x-1){
                    solution -= 2* Math.min(grid[i][j],grid[i+1][j])
                }
                if (j < y-1){
                    solution -= 2* Math.min(grid[i][j],grid[i][j+1])

                }
            }
        }
    }
    return solution 
};

console.log(surfaceArea([[2]]))

console.log(surfaceArea([[1,2],[3,4]]))

console.log(surfaceArea([[1,0],[0,2]]))

console.log(surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))

console.log(surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))
