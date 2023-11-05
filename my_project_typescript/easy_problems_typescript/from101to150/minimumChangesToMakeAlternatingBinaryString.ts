function minOperations(s: string): number {


    
    let firstDict: {[key:number]: string} = {}
    

    let lenS: number = s.length
    let minCountFirstDict: number = 0
    let minCountSecondDict: number = 0

    for (let i = 0; i < lenS; i++){
        firstDict[i] = ((i+1)%2).toString()
    }

    for (let i = 0; i < lenS; i++){
        if (s[i] === firstDict[i]){
            minCountFirstDict += 1
        }
        else {
            minCountSecondDict += 1
        }
    }

    let answer: number = 
    Math.min(minCountFirstDict,minCountSecondDict)


    return answer 

};

console.log(minOperations("0100"))

console.log(minOperations("10"))

console.log(minOperations("1111"))

console.log(minOperations("10010100"))
