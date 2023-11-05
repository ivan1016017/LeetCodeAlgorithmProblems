function romanToInt(s: string): number {

    let lenString: number = s.length

    let result: number = 0

    let tempObj: any = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 };

    result = tempObj[s[lenString - 1]]

    for (let i = 1; i < lenString; i++){
        if (tempObj[s[lenString - i]] > tempObj[s[lenString-i-1]]){
            result -= tempObj[s[lenString-i-1]]
        }
        else {
            result += tempObj[s[lenString-i-1]]
        }
    }
    return result


};