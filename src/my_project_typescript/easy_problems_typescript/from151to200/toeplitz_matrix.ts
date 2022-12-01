function isToeplitzMatrix(matrix: number[][]): boolean {

    let answer: boolean = true

    let rows: number = matrix.length
    let cols: number = matrix[0].length


    if (matrix.length === 1 || matrix[0].length === 1){
        return answer 
    }

    for (let i = 1; i < rows; i++){
        for (let j = 1; j < cols; j++){
            if (matrix[i][j] !== matrix[i-1][j-1]){
                answer = false 
                return false 
            }
        }
    }

    return answer

};