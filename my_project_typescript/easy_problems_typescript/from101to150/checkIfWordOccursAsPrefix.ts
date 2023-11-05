function isPrefixOfWord(sentence: string, searchWord: string): number {
    let listSentence: Array<String> = sentence.split(" ")
    let lenSentence: number = listSentence.length
    let lenSearchWord: number = searchWord.length
    let flag: boolean = false 

    for (let i = 0; i < lenSentence; i++){
        flag = false 
        for (let j = 0;  j < lenSearchWord; j++){
            if (lenSearchWord <= listSentence[i].length){
                if (searchWord[j] !== listSentence[i][j]){
                    flag = true 
                    continue 
                }
            }
            else{
                flag = true 
                continue
            }   
        }
        if (flag === false){
            return i + 1
        }
    }

    return -1
};


console.log(isPrefixOfWord("i love eating burger",  "burg"))

console.log(isPrefixOfWord("this problem is an easy problem",  "pro"))

console.log(isPrefixOfWord("i am tired",  "you"))

console.log(isPrefixOfWord("i use triple pillow",  "pill"))

console.log(isPrefixOfWord("hello from the other side",  "they"))

