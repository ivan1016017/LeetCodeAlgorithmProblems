function luckyNumbers (matrix: number[][]): number[] {
    let solution: Array<number> = [];

    let getColumnMax = (matrix: number[][], j: number) => {
        let mySlide: Array<number> = [];
        for (let i = 0; i < matrix.length; i++){
            mySlide.push(matrix[i][j])
        }
        return Math.max.apply(null, mySlide)
    }

    let getRowMin = (matrix: number[][], i: number) => {
        let mySlideother: Array<number> = [];
        for (let j = 0; j < matrix[0].length; j++){
            mySlideother.push(matrix[i][j])
        }
        return Math.min.apply(null, mySlideother)
    }

    for (let i = 0; i < matrix.length; i++){
        for (let j = 0; j < matrix[0].length; j++){
            console.log( getRowMin(matrix, i), getColumnMax(matrix,j))
            if (matrix[i][j] === getRowMin(matrix, i) && matrix[i][j] === getColumnMax(matrix,j)){
                solution.push(matrix[i][j])
            }
        }
    }




    return solution

};

console.log(luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))



