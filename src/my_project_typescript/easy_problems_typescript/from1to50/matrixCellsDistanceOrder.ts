function allCellsDistOrder(rows: number, cols: number, rCenter: number, cCenter: number): number[][] {

    function distance(row:number, col:number): number{
        return Math.abs(row-rCenter) + Math.abs(col-cCenter)
    }

    let answer: number[][] = []
    for (let i = 0; i < rows; i++){
        for (let j = 0; j < cols; j++){
            answer.push([i,j])
        }
    }

    answer = answer.sort((a,b) => distance(a[0],a[1])<= distance(b[0],b[1])?-1:1 )
    
    return answer
};

// This is a new function created in typescript

function myNewFunction(myVariable: number):number{
    return myVariable
}

allCellsDistOrder( 2,  2,  0,  1)
allCellsDistOrder( 2, 3, 1, 2)


