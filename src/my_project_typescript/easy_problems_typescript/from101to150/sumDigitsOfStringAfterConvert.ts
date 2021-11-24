function getLucky(s: string, k: number): number {

    function sumDigits(num: number): number {
        let answer: number = 0
        let quotient: number = 0
        let num_to_string = num.toString()
        let lenNum: number = num_to_string.length

        for (let i = 0; i < lenNum; i++){
            quotient = Math.floor(num / (10**(lenNum -1 -i)))
            answer += quotient
            num = num % (10** (lenNum -1 -i))
        }

        return answer 
    }

    let lenS: number = s.length
    let temp: string = ""
    for (let i = 0; i < lenS; i++){
        temp += (s[i].charCodeAt(0) - 96).toString()
    }

    let answer: number = parseInt(temp)

    for (let l = 0; l < k; l++){
        answer = sumDigits(answer)
    }

    return answer
};


console.log(getLucky("iiii", 1))

console.log(getLucky("leetcode", 2))

console.log(getLucky("zbax", 2))


