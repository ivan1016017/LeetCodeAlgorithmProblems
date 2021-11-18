function getMinDistance(nums: number[], target: number, start: number): number {
    let indexList: Array<number> = []
    let lenNums: number = nums.length

    for (let i = 0; i < lenNums; i++){
        if (nums[i] === target){
            indexList.push(i)
        }
    }

    indexList = indexList.sort( (a,b) => Math.abs(a-start) <= Math.abs(b-start) ?-1:1 )
            
    return Math.abs(indexList[0] - start)
};


console.log(getMinDistance([1,2,3,4,5],  5,  3))

console.log(getMinDistance([1], 1,  0))

console.log(getMinDistance( [1,1,1,1,1,1,1,1,1,1],  1,  0))
