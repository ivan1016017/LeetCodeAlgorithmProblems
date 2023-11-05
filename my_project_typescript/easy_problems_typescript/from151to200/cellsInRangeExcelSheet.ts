function cellsInRange(s: string): string[] {

    let answer: Array<string> = []
    let temp: string = ""


    for (let i = s[0].charCodeAt(0); i <= s[3].charCodeAt(0); i++){
        console.log(i)
        for (let j = parseInt(s[1]); j <= parseInt(s[4]); j++){
            temp = String.fromCharCode(i) + j.toString()
            answer.push(temp)
        }
    }

    return answer

};


console.log(cellsInRange("K1:L2"))

console.log("Hi")