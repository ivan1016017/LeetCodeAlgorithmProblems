function shortestDistance(wordsDict: string[], word1: string, word2: string): number {

    let indexOne: number = -1
    let indexTwo: number = -1
    let lenDict: number = wordsDict.length
    let answer: number = lenDict

    for (let i = 0; i < lenDict;i++){
        if (wordsDict[i] === word1){
            indexOne = i 
        }
        else if (wordsDict[i] === word2){
            indexTwo = i 
        }

        if (indexOne !== -1 && indexTwo !== -1 && Math.abs(indexTwo-indexOne) < answer){
            answer  = Math.abs(indexTwo-indexOne)
        }
    }

    return answer

};