function canBeTypedWords(text: string, brokenLetters: string): number {

    let count: number = 0
    let listWords: Array<string> =  text.split(" ")
    for (let word of listWords){
        for (let letter of brokenLetters){
            if (word.includes(letter)){
                count += 1
                break 
            }
        }
    }

    return listWords.length  - count 
};

console.log(canBeTypedWords("hello world", "ad"))

console.log(canBeTypedWords("leet code", "lt"))

console.log(canBeTypedWords("leet code", "e"))
