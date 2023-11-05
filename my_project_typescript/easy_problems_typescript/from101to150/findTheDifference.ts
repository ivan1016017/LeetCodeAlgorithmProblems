function findTheDifference(s: string, t: string): string {

    let lenS: number = s.length
    let lenT: number = t.length

    let dictS: {[key:string]:number} = {}
    let dictT: {[key:string]:number} = {}

    for (let i = 0; i < lenT; i++){
        dictS[t[i]] = 0
        dictT[t[i]] = 0
    }

    for (let i = 0; i < lenS; i++){
        dictS[s[i]] += 1
    }

    for (let i = 0; i < lenT; i++){
        dictT[t[i]] += 1
    }

    for (let key in dictS){
        if (dictS[key] != dictT[key]){
            return key
        }
    }

    return ""

};

console.log(findTheDifference("abcd", "abcde"))

console.log(findTheDifference("", "y"))

console.log(findTheDifference("a", "aa"))

console.log(findTheDifference("ae", "aea"))
