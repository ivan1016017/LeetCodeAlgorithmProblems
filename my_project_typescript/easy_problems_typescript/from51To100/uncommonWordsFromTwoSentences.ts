function uncommonFromSentences(s1: string, s2: string): string[] {

    let s1Array: Array<string> = []
    let s2Array: Array<string> = []

    s1Array = s1.split(' ')
    s2Array = s2.split(' ')

    let dictionaryOne: any = {}
    let dictionaryTwo: any = {}

    s1Array.map( word => {
        dictionaryOne[word] = 0
    })

    s2Array.map(word => {
        dictionaryTwo[word] = 0
    })

    s1Array.map(word => {
        dictionaryOne[word]+=1
    })

    s2Array.map(word => [
        dictionaryTwo[word] += 1
    ])

    let solutionList: Array<string> = []
    let firstList: Array<string> = []
    let secondList: Array<string> = []

    s1Array.map(word => {
        if (!s2Array.includes(word) && dictionaryOne[word] ==1 ){
            firstList.push(word)
        }
    })

    s2Array.map(word => {
        if (!s1Array.includes(word) && !firstList.includes(word) && dictionaryTwo[word] ==1){
            secondList.push(word)
        }
    })

    firstList.concat(secondList).map(word => {
        solutionList.push(word)
    })

    return solutionList
};

console.log(uncommonFromSentences("this apple is sweet",  "this apple is sour"))

console.log(uncommonFromSentences("apple apple",  "banana"))
