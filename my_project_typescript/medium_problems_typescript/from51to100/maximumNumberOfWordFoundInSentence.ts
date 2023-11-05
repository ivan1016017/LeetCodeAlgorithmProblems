function mostWordsFound(sentences: string[]): number {

    let answer: number = 0

    for (let sentence of sentences){
        if (splitAndSum(sentence) > answer){
            answer = splitAndSum(sentence)
        }
    }

    return answer 
};


function splitAndSum(sentence:string): number{
    return sentence.split(" ").length
}