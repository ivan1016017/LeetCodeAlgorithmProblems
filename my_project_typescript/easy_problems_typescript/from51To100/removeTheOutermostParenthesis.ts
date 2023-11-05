function removeOuterParentheses(s: string): string {

    let leftCount: number = 0
    let rightCount: number = 0
    let count: number = 0
    let answer: string = ""

    for (let character of s){
        if (character === "("){
            leftCount += 1
        }
        else if (character === ")"){
            rightCount += 1
        }
        count += 1
        
        if (leftCount === rightCount ){
            answer += s.slice((count - 2*leftCount + 1), count-1)
            leftCount = 0
            rightCount = 0
        }
    }

    return answer 

};


console.log(removeOuterParentheses("(()())(())"))

console.log(removeOuterParentheses("(()())(())(()(()))"))


console.log(removeOuterParentheses("()()"))
