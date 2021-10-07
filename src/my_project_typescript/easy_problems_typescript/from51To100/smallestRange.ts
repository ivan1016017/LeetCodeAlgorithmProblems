function smallestRangeI(nums: number[], k: number): number {

    let minValue = Math.min.apply(null, nums)
    let maxValue = Math.max.apply(null, nums)


    return Math.max(0, (maxValue-k) - (minValue + k))

};

console.log(smallestRangeI([1], 0))

console.log(smallestRangeI([0,10], 2))

console.log(smallestRangeI([1,3,6], 3))

console.log(smallestRangeI([7,8,8], 5))

console.log(smallestRangeI([3,1,10], 4))

