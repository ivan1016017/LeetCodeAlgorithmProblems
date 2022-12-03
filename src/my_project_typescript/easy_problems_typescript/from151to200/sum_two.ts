function twoSum(nums: number[], target: number): number[] {

    let hashtable = {}
    let lenNums: number = nums.length

    for (let i = 0; i < lenNums; i++){

        if (nums[i] in hashtable){
            return [i, hashtable[nums[i]]]
        }
        hashtable[target-nums[i]] = i
    }

    return [-1,-1]



};