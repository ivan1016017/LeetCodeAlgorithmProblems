function trimMean(arr: number[]): number {

    arr.sort( (a,b) => a <= b?-1:1)

    let indexSmallest: number = Math.floor(0.05* arr.length)
    let indexLargest: number =  Math.floor(arr.length  - 0.05* arr.length)
    let newList: Array<number> = arr.slice(indexSmallest, indexLargest)
    console.log(newList)


    return newList.reduce((a,b) => a+b, 0)/newList.length 

};


console.log(trimMean([6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]))