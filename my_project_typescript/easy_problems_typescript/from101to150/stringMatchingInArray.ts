function stringMatching(words: string[]): string[] {

    let lenwords: number = words.length
    let dictWords: any = {}
    let answer:  Array<string> = []

    for (let i = 0; i < lenwords; i++){
        for (let j = 0; j < lenwords; j++){
            if (words[i] !== words[j] && words[j].includes(words[i])){
                dictWords[words[i]] = 1
            }
        }
    }

    for (let word in dictWords){
        answer.push(word)
    }

    return answer 

};


console.log(stringMatching(["mass","as","hero","superhero"]))

console.log(stringMatching( ["leetcode","et","code"]))

console.log(stringMatching(["blue","green","bu"]))
