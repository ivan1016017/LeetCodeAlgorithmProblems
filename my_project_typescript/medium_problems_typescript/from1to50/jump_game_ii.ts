function jump(nums: number[]): number {


    let target: number = nums.length -1 
    let count: number = 0
    let idx: number 
    while (target > 0){
        idx = 0

        while (nums[idx] + idx < target){
            idx += 1
        }
        target = idx
        count += 1
    }
    return count 
};