function largestOddNumber(num: string): string {
    let lenNum: number = num.length
    for (let i = lenNum -1 ; i > -1; i = i -1){
        if (parseInt(num[i])%2 == 1){
            return num.slice(0, i+1)
        }
    }

    return ''

};