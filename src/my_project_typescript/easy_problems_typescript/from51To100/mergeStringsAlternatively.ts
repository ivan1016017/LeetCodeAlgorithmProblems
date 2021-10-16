function mergeAlternately(word1: string, word2: string): string {
    let answer: string = ''
    let minLength = Math.min(word1.length, word2.length)

    for (let i = 0; i < minLength; i++){
        answer += word1[i] + word2[i]
    }

    if (word1.length < word2.length){
        answer += word2.slice(minLength)
        return answer 
    }
    if (word1.length > word2.length){
        answer += word1.slice(minLength)
        return answer 
    }
    return answer 
};

console.log(mergeAlternately("abc",  "pqr"))

console.log(mergeAlternately("ab", "pqrs"))

console.log(mergeAlternately("abcd", "pq"))
