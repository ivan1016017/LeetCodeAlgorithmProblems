function smallestEqual(nums: number[]): number {
    let solution: number = -1
    let lenNums: number = nums.length
    for (let i = 0; i < lenNums; i++){
        if (nums[i] === i%10){
            solution = i 
            return solution
        }
    }
    return solution
};


console.log(smallestEqual([0,1,2]))

console.log(smallestEqual([4,3,2,1]))

console.log(smallestEqual([1,2,3,4,5,6,7,8,9,0]))

console.log(smallestEqual([2,1,3,5,2]))
