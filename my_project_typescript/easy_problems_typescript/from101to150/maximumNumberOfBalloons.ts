function maxNumberOfBalloons(text: string): number {

    // answer 
    let answer: number = 0

    // dictionary to add the total occurrences of each word in text
    let tempDict: any = {}

    let lenText: number = text.length

    // initialize the occurrences of each letter in the word text
    for (let word of "balon"){
        tempDict[word] = 0
    }

    // calculate how many time each word appears in text
    for (let i = 0; i < lenText; i++){
        tempDict[text[i]] = 0
    }

    for (let i = 0; i < lenText; i++){
        tempDict[text[i]] += 1
    }

    // the total amount of occurrences of each letter to form the word balloon
    let ballonOccurrences: Array<number> = []

    ballonOccurrences.push(tempDict['b'])
    ballonOccurrences.push(tempDict['a'])
    ballonOccurrences.push(Math.floor(tempDict['l']/2))
    ballonOccurrences.push(Math.floor(tempDict['o']/2))
    ballonOccurrences.push(tempDict['n'])


    answer = Math.min.apply(null, ballonOccurrences)

    return answer

};


console.log(maxNumberOfBalloons("nlaebolko"))

console.log(maxNumberOfBalloons("loonbalxballpoon"))

console.log(maxNumberOfBalloons("leetcode"))

console.log(maxNumberOfBalloons("lloo"))
