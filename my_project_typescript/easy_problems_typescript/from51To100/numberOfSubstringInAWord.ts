function numOfStrings(patterns: string[], word: string): number {

    let count: number = 0

    for (let letter of patterns){
        if (word.includes(letter)){
            count += 1
        }
    }
    return count 

};


console.log(numOfStrings( ["a","abc","bc","d"], "abc"))

console.log(numOfStrings(["a","b","c"], "aaaaabbbbb"))

console.log(numOfStrings(["a","a","a"], "ab"))
