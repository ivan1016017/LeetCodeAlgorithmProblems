/**
 Do not return anything, modify matrix in-place instead.
 */
 function setZeroes(matrix: number[][]): void {

    let m: number = matrix.length
    if (m === 0 ){
        return 
    }
    let n: number = matrix[0].length

    let rowZeroes: boolean = false 
    let columnZeroes: boolean = false 

    for (let i = 0; i < m; i++){
        if (matrix[i][0] === 0){
            rowZeroes = true
            break
        }
    }

    for (let j = 0; j < n; j++){
        if (matrix[0][j] === 0){
            columnZeroes = true
            break
        }
    }

    for (let i = 1; i < m; i++){
        for (let j = 1; j < n; j++){
            if (matrix[i][j] ===0){
                matrix[i][0] = 0
                matrix[0][j] = 0
            }
        }
    }

    for (let i = 1; i < m; i++){
        if (matrix[i][0] === 0){
            for (let j = 1; j < n; j++){
                matrix[i][j] =0
            }
        }
    }

    for (let j = 1; j < n; j++){
        if (matrix[0][j] === 0){
            for (let i = 1; i < m; i++){
                matrix[i][j] = 0
            }
        }
    }



    if (rowZeroes){
        for (let i = 0; i < m; i++){
            matrix[i][0] = 0
        }
    }

    if (columnZeroes){
        for (let j=0; j<n; j++){
            matrix[0][j] = 0
        }
    }
};