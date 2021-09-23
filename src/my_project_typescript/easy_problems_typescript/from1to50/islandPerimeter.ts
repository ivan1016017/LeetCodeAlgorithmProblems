function islandPerimeter(grid: number[][]): number {

    let perimeter: number = 0;
// this is a new variable that I wont use
let variableOne: number = 1
    for (let i = 0; i < grid.length; i++){
        for (let j = 0; j < grid[0].length; j++){
            if (grid[i][j] ==1){
                perimeter += 4
                if (i > 0 && grid[i-1][j] == 1){
                    perimeter -= 2
                }
                if (j > 0 && grid[i][j-1]){
                    perimeter -= 2
                }
            }
        }
    }
    return perimeter

};

console.log(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))