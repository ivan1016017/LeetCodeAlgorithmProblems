function arrayRankTransform(arr: number[]): number[] {
    let orderedList: Array<number> = []
    let lenArr: number = arr.length
    let tempDict: any = {}

    for (let i = 0; i < lenArr; i++){
        tempDict[arr[i]] = 0
    }

    for (let i in tempDict){
        orderedList.push(parseInt(i))
    }

    orderedList = orderedList.sort((a,b) => a <= b ?-1:1)

    let solutionDict: any = {}
    let valueIndex = 1

    for (let j of orderedList){
        solutionDict[j] = valueIndex
        valueIndex += 1
    }

    for (let j = 0; j < lenArr; j++){
        arr[j] = solutionDict[arr[j]]
    }

    return arr
};


console.log(arrayRankTransform([40,10,20,30]))

console.log(arrayRankTransform([100,100,100]))

console.log(arrayRankTransform([37,12,28,9,100,56,80,5,12]))
