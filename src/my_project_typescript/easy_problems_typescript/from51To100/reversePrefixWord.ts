function reversePrefix(word: string, ch: string): string {

    let leftString: string = ""
    let rightString: string = ""
    let answer: string = ""
    let count: number = 0
    let flag: boolean = false
    
    for (let letter of word){
        count += 1
        if (letter === ch){
            flag = true 
            leftString = word.slice(0, count)
            rightString = word.slice(count)
            break
        }
    }


    if (flag === false){
        return word
    }

    for (let i = leftString.length -1; i > -1; i = i -1){
        answer += leftString[i]
    }

    return answer + rightString
};


console.log(reversePrefix("abcdefd", "d"))

console.log(reversePrefix("xyxzxe", "z"))

console.log(reversePrefix("abcd", "z"))
