function maxScore(s: string): number {

    let lenS: number = s.length;
    let temp: number = 0
    for (let i = 0; i < lenS; i++){
        if (s[i] == '1'){
            temp += 1
        }
    }

    let answer: number = -1

    for (let i = 0; i < (lenS-1); i++){
        if (s[i] == '0'){
            temp += 1
        }
        else {
            temp -= 1
        }
        answer = Math.max(answer, temp)
    }
    return answer 
};

console.log(maxScore("011101"))

console.log(maxScore("00111"))

console.log(maxScore("1111"))
