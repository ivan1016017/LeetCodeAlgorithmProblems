function findSpecialInteger(arr: number[]): number {

    // initialize variables 
    let lenArr: number = arr.length
    let tempDict: any = {}
    let answer: number = -1

    // initialize the dictionary
    for (let i = 0; i < lenArr; i++){
        tempDict[arr[i]] = 0
    }

    // add the frequency in which each element occur
    for (let i = 0; i < lenArr; i++){
        tempDict[arr[i]] += 1/lenArr
    }

    // return the vale that occurs more than 25 percent of the time
    for (let i = 0; i < lenArr; i++){
        if (tempDict[arr[i]] > .25){
            answer = arr[i]
            return answer
        }
    }

    return answer 

};


console.log(findSpecialInteger([1,2,2,6,6,6,6,7,10]))

console.log(findSpecialInteger([1,1]))
