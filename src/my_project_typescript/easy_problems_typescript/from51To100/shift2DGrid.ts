function shiftGrid(grid: number[][], k: number): number[][] {
    let flatList: Array<number> = []

    let x: number = grid.length
    let y: number = grid[0].length
    let solution: Array<any> = []

    for (let i = 0; i < x; i++){
        for (let j = 0; j < y; j++){
            flatList.push(grid[i][j])
        }
    }
    let temp: any = 0
    for (let i = 0; i < k; i++){
        temp = flatList.pop()
        flatList = [temp].concat(flatList)
    }

    for (let i = 0; i<x; i++){
        solution.push(flatList.slice(i*y, i*y+y))
    }
    return solution
};


console.log(shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4))