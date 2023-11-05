function twoSum(nums: number[], target: number): number[] {

    let temp: {[key: number]: number} = {}

    for (let i = 0; i < nums.length; i++){
        if (target-nums[i] in temp){
            return [temp[target-nums[i]], i]
        }
        temp[nums[i]] = i
    }
    


};