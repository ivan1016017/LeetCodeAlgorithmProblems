function convert(s: string, numRows: number): string {

    let lenS: number = s.length

    if (numRows === 1 || numRows >= lenS){
        return s
    }

    let arrayAnswer: Array<string> = Array(lenS).fill('')
    let index: number = 0
    let step: number = 1

    for (let letter of s){
        arrayAnswer[index] += letter 
        if (index === 0){
            step = 1
        }
        else if (index === numRows -1){
            step = -1
        }
        index += step 
    }

    return arrayAnswer.join('')
};