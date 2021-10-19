function findMiddleIndex(nums: number[]): number {

    let lenNums: number = nums.length
    for (let i = 0; i < lenNums; i++){
        if (nums.slice(0,i).reduce((a,b) => a+b,0) === nums.slice(i+1).reduce((a,b) => a+b,0)){
            return i
        }
    }

    if (lenNums === 2){
        return -1
    }
    if (lenNums ===1){
        return 0
    }

    return -1
};

console.log(findMiddleIndex([2,3,-1,8,4]))

console.log(findMiddleIndex([1,-1,4]))

console.log(findMiddleIndex([2,5]))

console.log(findMiddleIndex( [1]))
