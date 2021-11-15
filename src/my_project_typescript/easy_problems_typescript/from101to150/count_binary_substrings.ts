function countBinarySubstrings(s: string): number {

    let prevCount: number = 0
    let currentCount: number = 0
    let answer: number = 0
    let prev: string = "-1"
    let lenS: number =  s.length

    for (let i = 0; i < lenS; i++){
        if (s[i] === prev){
            currentCount += 1
        }
        else {
            answer += Math.min(prevCount, currentCount)
            prevCount = currentCount
            currentCount = 1
        }
        prev = s[i]
    }
    answer += Math.min(prevCount, currentCount)

    return answer 

};


console.log(countBinarySubstrings("00110011"))

console.log(countBinarySubstrings("10101"))

