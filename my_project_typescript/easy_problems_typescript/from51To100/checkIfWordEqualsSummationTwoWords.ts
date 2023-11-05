function isSumEqual(firstWord: string, secondWord: string, targetWord: string): boolean {


    function fromStringToNumber(word: string): number{
        let temp: number = 0
        let lengthWord: number = word.length

        for (let i = word.length-1; i > -1; i = i -1){
            temp += (word[i].charCodeAt(0)%97)*(10**(lengthWord-1-i))
        }
        return temp 
    }

    return fromStringToNumber(firstWord) + fromStringToNumber(secondWord) === fromStringToNumber(targetWord)

};

console.log(isSumEqual("acb", "cba",  "cdb"))

console.log(isSumEqual("aaa",  "a", "aab"))

console.log(isSumEqual("aaa",  "a",  "aaaa"))
