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
    console.log(lenS)
    let temp: string = ""
    for (let i = 0; i < lenS; i++){
        temp += (s[i].charCodeAt(0) - 96).toString()
    }
    console.log(temp)

    let answer: bigint = BigInt(0)

    for (let i = 0; i < temp.length; i++){
        console.log(parseInt(temp[i]))
        answer += BigInt((10**(temp.length-1-i))*parseInt(temp[i]))
    }
    console.log(answer)

    for (let l = 0; l < k; l++){
        answer = BigInt(sumDigits(Number(answer)))
    }

    return Number(answer)
};


// console.log(getLucky("iiii", 1))

// console.log(getLucky("leetcode", 2))

// console.log(getLucky("zbax", 2))

console.log(getLucky("dbvmfhnttvr", 5))




