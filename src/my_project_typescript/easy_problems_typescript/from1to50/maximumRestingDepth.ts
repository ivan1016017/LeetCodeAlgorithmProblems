function maxDepth(s: string): number {

    let count: number = 0
    let answer: number = 0
    for (let character of s){
        if (character === "("){
            count += 1
        }
        else if (character === ")"){
            count -= 1
        }
        if (count > answer){
            answer = count
        }
    }

    return answer

};


console.log(maxDepth("(1+(2*3)+((8)/4))+1"))

console.log(maxDepth("(1)+((2))+(((3)))"))


console.log(maxDepth("1+(2*3)/(2-1)"))


console.log(maxDepth( "1"))
