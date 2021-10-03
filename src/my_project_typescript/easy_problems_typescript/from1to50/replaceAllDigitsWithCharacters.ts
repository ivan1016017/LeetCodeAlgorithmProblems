function replaceDigits(s: string): string {

    let temp: string = ""
    let answer: string = ""
    let x: number = 0
    
    for (let i = 1; i < s.length; i = i + 2){
        x = s[i-1].charCodeAt(0)
        temp = String.fromCharCode(x + parseInt(s[i]))
        answer += s[i-1] + temp 
    }

    if (s.length % 2 === 1){
        answer += s[s.length-1]
    }

    return answer

};


console.log(replaceDigits("a1c1e1"))

console.log(replaceDigits("a1b2c3d4e"))
