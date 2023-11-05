function checkIfPangram(sentence: string): boolean {
    let answer: boolean = true 
    let letters: string = "abcdefghijklmnopqrstuvwxyz"

    for (let letter of letters){
        if (!sentence.includes(letter)){
            answer = false
        }
    }
    return answer 

};

console.log(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))

console.log(checkIfPangram("leetcode"))
