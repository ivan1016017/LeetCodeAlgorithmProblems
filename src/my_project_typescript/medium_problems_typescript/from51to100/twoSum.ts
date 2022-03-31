function twoSum(nums: number[], target: number): number[] {

    let tempObj: {[key:number]: number} = {}
    let lenNums: number = nums.length

    for (let i = 0; i < lenNums; i++){
        if (target-nums[i] in tempObj){
            return [tempObj[target-nums[i]],i]
        }
        tempObj[nums[i]] = i
    }
    


};