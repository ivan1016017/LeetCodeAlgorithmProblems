function findOcurrences(text: string, first: string, second: string): string[] {

    let textList: Array<string> = text.split(" ")
    let lenText: number = textList.length
    let answer: Array<string> = []

    for (let i = 0; i < lenText-2; i++){
        if (textList[i] === first && textList[i+1] === second){
            answer.push(textList[i+2])
        }
    }

    return answer 
};



console.log(findOcurrences("alice is a good girl she is a good student",  "a",  "good"))

console.log(findOcurrences("we will we will rock you",  "we", "will"))

console.log(findOcurrences("alice is a good girl she is a good",  "a",  "good"))

