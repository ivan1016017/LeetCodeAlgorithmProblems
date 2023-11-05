function findFinalValue(nums: number[], original: number): number {

    nums = nums.sort((a,b) => a<=b ? -1: 1)

    for (let num of nums){
        if (num === original){
            original *= 2
        }
    }

    return original

};