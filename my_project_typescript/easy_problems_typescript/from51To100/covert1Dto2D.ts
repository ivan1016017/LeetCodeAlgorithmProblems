function construct2DArray(original: number[], m: number, n: number): number[][] {
    let lenOriginal: number = original.length
    let solution: Array<any> = []
    let temp: Array<any> = []
    if (lenOriginal !== m*n){
        return solution
    }
    else{
        for (let i = 0; i < m; i++){
            temp = []
            for (let j = 0; j < n; j++){
                temp.push(original[j + i*n])
            }
            solution.push(temp)
        }
        return solution 
    }
    return solution
};

console.log(construct2DArray([1,2,3,4],  2,  2))

console.log(construct2DArray([1,2,3], 1, 3))

console.log(construct2DArray([1,2],  1,  1))

console.log(construct2DArray([3], 1, 2))
