function checkAlmostEquivalent(word1: string, word2: string): boolean {

    let answer: boolean = true 
    let lenWord: number = word1.length
    let alphabet: string = "abcdefghijklmnopqrstuvwxyz"   

    // initialize the dictionaries to count letters
    let dictWord1: any  = {}
    let dictWord2: any = {}

    for (let i = 0; i < 26; i++){
        dictWord1[alphabet[i]] = 0
        dictWord2[alphabet[i]] = 0
    }

    // count the letters in each word
    for (let i = 0; i < lenWord; i++){
        dictWord1[word1[i]] += 1 
        dictWord2[word2[i]] += 1 
    }

    // check the words are almost equivalent
    for (let i = 0; i < lenWord; i++){
        if (Math.abs(dictWord1[word1[i]] - dictWord2[word1[i]]) > 3){
            answer = false 
            return answer 
        }
    }
    
    for (let i = 0; i < lenWord; i++){
        if (Math.abs(dictWord1[word2[i]] - dictWord2[word2[i]]) > 3){
            answer = false 
            return answer 
        }
    }

    return answer 
};


console.log(checkAlmostEquivalent("aaaa", "bccb"))

console.log(checkAlmostEquivalent("abcdeef",  "abaaacc"))

console.log(checkAlmostEquivalent("cccddabba", "babababab"))
