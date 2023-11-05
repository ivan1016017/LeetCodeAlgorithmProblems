function areOccurrencesEqual(s: string): boolean {

    let tempDict: any = {}
    let flag: boolean = true 

    for (let letter of s){
        tempDict[letter] = 0
    }

    for (let letter of s){
        tempDict[letter] += 1
    }

    for (let i = 1; i < s.length; i++){
        if (tempDict[s[i-1]] !== tempDict[s[i]]){
            flag = false 
            return flag 
        }
    }
    return flag 
};


console.log(areOccurrencesEqual("abacbc"))

console.log(areOccurrencesEqual("aaabb"))
