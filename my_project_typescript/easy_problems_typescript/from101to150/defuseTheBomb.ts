function decrypt(code: number[], k: number): number[] {
    let lenCode: number = code.length
    let solution: Array<number> =  []
    let count: number = 0
    code.map((num, index) => {
        solution.push(0)
    })
    if (k > 0){
        for (let i = 0; i < lenCode; i++){
            count = 0
            for (let l = i+1; l < i+1+k; l++ ){
                count += code[l%lenCode]
            }
            solution[i] = count 
        }
    }
    else if (k < 0){
        for (let i = 0; i < lenCode; i++){
            count = 0
            for (let l = i-1; l > i-1+k; l-- ){
                
                if (l%lenCode <0){
                    count += code[lenCode + (l%lenCode)]
                }
                else {
                    count += code[l%lenCode]
                }
                
            }
            solution[i] = count 
        }
    }
    return solution 
};


console.log(decrypt( [5,7,1,4], 3))

console.log(decrypt( [1,2,3,4], 0))

console.log(decrypt([2,4,9,3], -2))
