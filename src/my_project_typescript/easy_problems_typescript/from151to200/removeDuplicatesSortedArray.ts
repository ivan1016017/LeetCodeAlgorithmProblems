function removeDuplicates(nums: number[]): number {

    let lenNums: number = nums.length

    if (lenNums === 0 || lenNums === 1){
        return lenNums
    }

    let k: number = 0
    for (let i = 0; i < lenNums-1 ; i++){
        if (nums[i] !== nums[i+1]){
            nums[k] = nums[i]
            k += 1
        }
    }
    nums[k] = nums[lenNums-1]
    return k+1

};