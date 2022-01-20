/**
 Do not return anything, modify matrix in-place instead.
 */
 function rotate(matrix: number[][]): void {

    let n: number = matrix.length
    let tempOne: number 
    let tempTwo: number 

    for (let i = 0; i < n; i++){
        for (let j = i+1; j < n; j++ ){
            tempOne = matrix[i][j]
            tempTwo = matrix[j][i]
            matrix[i][j] = tempTwo 
            matrix[j][i] = tempOne
        }
    }

    for (let row of matrix){
        row = row.reverse()
    }

};