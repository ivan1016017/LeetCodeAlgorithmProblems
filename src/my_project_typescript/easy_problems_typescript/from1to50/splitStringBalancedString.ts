function balancedStringSplit(s: string): number {

    let answer: number = 0
    let countR: number = 0
    let countL: number = 0

    for (let word of s){
        if (word === "R"){
            countR += 1
        }
        else {
            countL += 1
        }

        if (countL === countR){
            answer += 1
        }
    }
    return answer 
};

console.log(balancedStringSplit("RLRRLLRLRL"))

console.log(balancedStringSplit("RLLLLRRRLR"))

console.log(balancedStringSplit("LLLLRRRR"))


console.log(balancedStringSplit("RLRRRLLRLL"))
