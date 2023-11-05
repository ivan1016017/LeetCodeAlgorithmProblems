function makeEqual(words: string[]): boolean {

    let answer = true 
    let tempDict: any = {}
    let vocab: string = ""

    for (let word of words){
        vocab = vocab + word
    }

    let lenVocab: number = vocab.length

    for (let i = 0; i < lenVocab; i++){
        tempDict[vocab[i]] = 0
    }

    for (let i = 0; i < lenVocab; i++){
        tempDict[vocab[i]] += 1
    }

    let lenWords: number = words.length

    for (let i = 0; i <lenVocab; i++){
        if (tempDict[vocab[i]] % lenWords !== 0){
            answer = false
            return answer 
        }
    }
    return answer 
};

console.log(makeEqual(["abc","aabc","bc"]))

console.log(makeEqual(["ab","a"]))
