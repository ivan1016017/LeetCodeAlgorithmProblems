function reverseOnlyLetters(s: string): string {
    let lenS = s.length
    let tempDict: any = {}
    let tempList: Array<string> = []

    for (let i = 0; i < lenS; i++){
        if (s[i].match(/[^a-zA-Z]/)){
            tempDict[i] = s[i]
        }
    }

    for (let i = 0; i < lenS; i++){
        if (s[i].match(/[a-zA-Z]/)){
            tempList.push(s[i])
        }
    }


    tempList = tempList.reverse()

    for (let i = 0; i < lenS; i++){
        if (i.toString() in tempDict){
            tempList = tempList.slice(0,i).concat([tempDict[i]]).concat(tempList.slice(i))
        }
    }
    return tempList.join("")
};

console.log(reverseOnlyLetters("ab-cd"))

console.log(reverseOnlyLetters("a-bC-dEf-ghIj"))

console.log(reverseOnlyLetters("Test1ng-Leet=code-Q!"))
