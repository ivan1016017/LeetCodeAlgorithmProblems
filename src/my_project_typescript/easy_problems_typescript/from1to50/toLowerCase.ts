function toLowerCase(s: string): string {
    let answer: string = ""
    let temp: string = ""

    for (let letter of s){
        if (letter.charCodeAt(0) <= 90 && letter.charCodeAt(0)>=65){
            temp = String.fromCharCode(letter.charCodeAt(0) + 32)
            answer += temp 
        }
        else{
            answer += letter
        }
        
    }

    return answer 
    
};


console.log(toLowerCase( "Hello"))

console.log(toLowerCase("here"))


console.log(toLowerCase("LOVELY"))
