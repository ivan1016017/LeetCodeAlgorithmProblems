function isToeplitzMatrix(matrix: number[][]): boolean {

    let answer: boolean = true 

    if (matrix.length === 1 || matrix[0].length == 1){
        return answer 
    }

    for (let i = 1; i < matrix.length; i++){
        for (let j = 1; j < matrix[0].length; j++){
            if (matrix[i][j] !== matrix[i-1][j-1]){
                answer = false 
                return false 
            }
        }
    }

    return answer 

};

console.log(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))

console.log(isToeplitzMatrix([[1,2],[2,2]]))

console.log(isToeplitzMatrix([[18],[66]]))

console.log(isToeplitzMatrix( [[11,74,0,93],[40,11,74,7]]))
