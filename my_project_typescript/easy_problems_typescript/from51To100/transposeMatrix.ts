function transpose(matrix: number[][]): number[][] {

    let flatMatrix: Array<number> = []
    let x: number = matrix.length
    let y: number = matrix[0].length

    for (let j = 0; j < y; j++){
        for (let i = 0; i < x; i++){
            flatMatrix.push(matrix[i][j])
        }
    }

    let transposeMatrix: Array<any> = []

    for (let i = 0; i < y; i++){
        transposeMatrix.push(flatMatrix.slice(i*x, i*x + x))
    }
    return transposeMatrix
};

console.log(transpose([[1,2,3],[4,5,6],[7,8,9]]))

console.log(transpose([[1,2,3],[4,5,6]]))
