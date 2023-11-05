function matrixReshape(mat: number[][], r: number, c: number): number[][] {

    if (mat.length*mat[0].length !== r*c){
        return mat
    }
    let solutionMatrix: Array<any> = []
    let flatList: Array<number> = []
    

    for (let row of mat){
        for (let num of row){
            flatList.push(num)
        }
    }
    
    let k: number = 0
    for (let i = 0; i <r; i++){
        solutionMatrix.push(flatList.slice(k, k+c))
        k += c
    }
    return solutionMatrix
};


console.log(matrixReshape([[1,2],[3,4]],  1, 4))

console.log(matrixReshape([[1,2],[3,4]], 2,  4))
