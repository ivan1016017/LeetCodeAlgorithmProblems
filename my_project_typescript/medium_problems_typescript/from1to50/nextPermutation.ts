function nextPermutation(nums: number[]): void {

    let i: number = nums.length -1 
    let j: number = nums.length -1 

    while (i > 0 && nums[i-1] >= nums[i]){
        i -= 1
    }
    if (i === 0){
        nums.reverse()
        return 
    }
    let k: number = i -1

    while (nums[j] <= nums[k]){
        j -= 1
    }
    let tempOne: number 
    let tempTwo: number 
    tempOne = nums[k]
    tempTwo = nums[j]
    nums[k] = tempTwo 
    nums[j] = tempOne

    let l: number = k+1
    let r: number = nums.length -1 

    while (l < r){
        tempOne = nums[l]
        tempTwo = nums[r]
        nums[l] = tempTwo
        nums[r] = tempOne
        l += 1
        r -= 1
    }
};