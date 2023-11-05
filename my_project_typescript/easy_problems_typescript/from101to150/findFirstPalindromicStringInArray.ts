function firstPalindrome(words: string[]): string {
    let answer: string = ""

    function isPalindrome(word: string): boolean{
        let answer: boolean = true 
        let lenWord: number = word.length
        for (let i = 0; i < Math.floor(lenWord/2); i++){
            if (word[i] !== word[lenWord-1-i]){
                answer = false
                return answer
            }
        }
        return answer 
    }

    for (let word of words){
        if (isPalindrome(word)){
            answer = word
            return answer 
        }
    }

    return answer 

};

function isPalindrome(word: string): boolean{
    let answer: boolean = true 
    let lenWord: number = word.length
    for (let i = 0; i < Math.floor(lenWord/2); i++){
        if (word[i] !== word[lenWord-1-i]){
            answer = false
            return answer
        }
    }
    return answer 

}

console.log(isPalindrome("d"))