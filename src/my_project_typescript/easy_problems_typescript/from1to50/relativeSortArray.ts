function relativeSortArray(arr1: number[], arr2: number[]): number[] {

    let arr:any =  {}
    let leftArray: Array<number> = []
    let rightArray: Array<number> = []
    for (let item of arr2){
        arr[item] = 0
    }
    for (let item of arr1){
        if (arr2.includes(item) ){
            arr[item] += 1
        }
    }
    
    for (let item of arr2){
        for (let i = 0; i < arr[item]; i++){
            leftArray.push(item)
        }
    }

    for (let item of arr1){
        if (!arr2.includes(item)){
            rightArray.push(item)
        }
    }
// thiw is a new comment
let myVariable: number = 0
    rightArray = rightArray.sort((a,b) => a <=b? -1: 1)

    return leftArray.concat(rightArray)
};

console.log(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],  [2,1,4,3,9,6]))