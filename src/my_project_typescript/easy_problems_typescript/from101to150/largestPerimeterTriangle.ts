function largestPerimeter(nums: number[]): number {
    nums =  nums.sort((a,b) => a>b?-1:1)
    let lenNums: number = nums.length
    let answer:  number = 0

    for (let i = 2; i < lenNums; i++){
        if (nums[i-2] - nums[i-1] < nums[i]){
            answer = nums[i] + nums[i-1] + nums[i-2]
            return answer 
        }
    }
    return answer 
};


console.log(largestPerimeter([2,1,2]))

console.log(largestPerimeter([1,2,1]))

console.log(largestPerimeter([3,2,3,4]))

console.log(largestPerimeter([3,6,2,3]))
