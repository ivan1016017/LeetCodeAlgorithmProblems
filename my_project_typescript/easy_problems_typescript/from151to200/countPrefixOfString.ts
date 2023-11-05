function countPrefixes(words: string[], s: string): number {

    let arrayS: Array<string> = []
    let target: Boolean = true
    let answer: number = 0

    for (let i = 0; i < s.length; i++){
        arrayS.push(s.slice(0,i+1))
    }

    for (let word of words){
        target = false
        for (let prefix of arrayS){
            if (word === prefix){
                target = true 
                break
            }
        }
        if (target === true){
            answer += 1
        }
    }

  

    return answer 


};

console.log(countPrefixes(["a","b","c","ab","bc","abc"],  "abc"))