function numSpecial(mat: number[][]): number {

    let answer: number = 0
    let sumAlongCol: number = 0
    let colLength: number = mat.length
    let rowLength: number = mat[0].length
    for (let i = 0; i < colLength; i++){
        if (mat[i].reduce((a,b) => a+b,0) !== 1){
            continue
        }
        else {
            for (let j = 0; j < rowLength; j++){
                if (mat[i][j] === 0){
                    continue
                }
                else{
                    sumAlongCol = 0
                    for (let k = 0; k < colLength; k++){
                        sumAlongCol += mat[k][j]
                    }
                    if (sumAlongCol === 1){
                        answer += 1
                    }
                }
            }
        }
    }
    return answer
};

console.log(numSpecial([[1,0,0],
    [0,0,1],
    [1,0,0]]))

// console.log(numSpecial([[1,0,0],
//     [0,1,0],
//     [0,0,1]]))

// console.log(numSpecial([[0,0,0,1],
//     [1,0,0,0],
//     [0,1,1,0],
//     [0,0,0,0]]))
