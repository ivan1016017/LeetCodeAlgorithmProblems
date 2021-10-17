function minTimeToType(word: string): number {
    let answer: number = 0
    let prev: string = 'a'

    for (let letter of word){
        if (Math.abs(letter.charCodeAt(0) - prev.charCodeAt(0)) > 13){
            answer += 26 - Math.abs(letter.charCodeAt(0) - prev.charCodeAt(0)) 
        }
        else{
            answer += Math.abs(letter.charCodeAt(0) - prev.charCodeAt(0)) 
        }
        prev = letter 
        answer += 1
    }

    return answer 
};


console.log(minTimeToType("abc"))

console.log(minTimeToType("bza"))

console.log(minTimeToType("zjpc"))
