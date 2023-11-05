function findLUSlength(a: string, b: string): number {

    let answer: number = -1 

    if (a !== b){
        answer = Math.max(a.length, b.length)
        return answer
    }
    
    return answer 

};