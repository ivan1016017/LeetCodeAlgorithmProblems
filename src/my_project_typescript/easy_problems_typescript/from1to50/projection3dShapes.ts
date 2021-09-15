function projectionArea(grid: number[][]): number {

    let projectionXY: number = 0
    let projectionXZ: number = 0
    let projectionYZ: number = 0

    function getColumnMax(grid: number[][], j:number){
        let temp: Array<number> = [];
        for (let i = 0; i< grid.length; i++){
            temp.push(grid[i][j])
        }
        return Math.max.apply(null, temp)
    }

    function getRowMax(grid: number[][], i:number){
        return Math.max.apply(null,grid[i])

    }


    for (let j = 0; j < grid[0].length; j++){
        projectionYZ += getColumnMax(grid,j)
    }

    for (let i = 0; i < grid.length; i++){
        grid[i].map((currentElement) => {
            if (currentElement !== 0){
                projectionXY += 1
            }
        })
        projectionXZ += getRowMax(grid,i)
    }

    return projectionXY + projectionYZ + projectionXZ
};

console.log(projectionArea( [[1,2],[3,4]]))