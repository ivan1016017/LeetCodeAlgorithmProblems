function checkZeroOnes(s: string): boolean {
    let countOnes: number = 0
    let countZeroes: number = 0
    let maxOnes: number = 0
    let maxZeroes: number = 0
    let lenS: number = s.length
    let answer: boolean = false 

    if (lenS === 1){
        if (s === "1"){
            answer = true 
            return answer 
        }
        else {
            return answer 
        }
    }

    s = s + 'a'
    lenS += 1

    for (let i = 0; i < lenS; i++){
        if (s[i] === "1"){
            countOnes += 1
            if (s[i+1] === "1"){
                continue
            }
            else{
                if (countOnes > maxOnes){
                    maxOnes = countOnes
                    countOnes = 0
                }
                else {
                    countOnes = 0
                }
            }
        }
        else if (s[i] === "0"){
            countZeroes += 1
            if (s[i+1] === "0"){
                continue
            }
            else {
                if (countZeroes > maxZeroes){
                    maxZeroes = countZeroes
                    countZeroes = 0
                }
                else {
                    countZeroes = 0
                }
            }
        }
    }

    if (maxOnes > maxZeroes){
        answer = true 
    }
    return answer 
};

console.log(checkZeroOnes("1101"))

console.log(checkZeroOnes("111000"))

console.log(checkZeroOnes("110100010"))

