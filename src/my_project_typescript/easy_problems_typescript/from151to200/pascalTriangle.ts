function generate(numRows: number): number[][] {
    let temp: Array<number> = []

    let solution: number[][] = [[1],[1,1]]

    if (numRows===1){
        return [[1]]
    } 
    else if (numRows===2){
        return [[1],[1,1]]
    }
    else{
        let listPascal: number[] = [1,1]
        let i: number = 3

        while (i<=numRows){
            for (let j = 0; j < i; j++){
                if (j === 0){
                    temp.push(listPascal[0])
                }
                else if (j === (i -1)){
                    temp.push(listPascal[listPascal.length-1])
                }
                else if (j > 0 && j < i-1){
                    temp.push(listPascal[j-1]+listPascal[j])
                }
            }
            i += 1
            listPascal = temp 
            solution.push(listPascal)
            temp = []
        }
        return solution
    }




};