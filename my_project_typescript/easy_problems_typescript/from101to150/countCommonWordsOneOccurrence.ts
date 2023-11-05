function countWords(words1: string[], words2: string[]): number {

    let tempDict: any = {}
    

    for (let word of words1){
        if (!tempDict.hasOwnProperty(word)){
            tempDict[word] = [1,0]
        }
        else {
            tempDict[word][0] += 1
        }
    }
    for (let word of words2){
        if (!tempDict.hasOwnProperty(word)){
            tempDict[word] = [0,1]
        }
        else {
            tempDict[word][1] += 1
        }
    }



    let answer: number = 0

    for (let word in tempDict){
        
        if (tempDict[word][0] === 1 && tempDict[word][1] ===1){
            answer += 1
        }
    }

    return answer 

};

console.log(countWords(["leetcode","is","amazing","as","is"],  ["amazing","leetcode","is"]))

console.log(countWords(["b","bb","bbb"],  ["a","aa","aaa"]))

console.log(countWords(["a","ab"], ["a","a","a","ab"]))


