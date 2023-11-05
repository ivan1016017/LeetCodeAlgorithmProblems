function kLengthApart(nums: number[], k: number): boolean {
    let index: number = 0
    let count: number = 0
    let lenNums: number = nums.length

    for (let i = 0; i<lenNums; i++){
        if (nums[i] === 1){
            index = i
            break
        }
    }

    nums = nums.slice(index)
    lenNums = nums.length

    for (let i = 0; i < lenNums; i++){
        if (i === 0 && nums[i] === 1){
            continue
        }
        if (nums[i] === 0){
            count += 1
        }
        else{
            if (count < k){
                return false
            }
            else {
                count = 0
            }
        }
    }
    return true 
};


console.log(kLengthApart([1,0,0,0,1,0,0,1], 2))

console.log(kLengthApart([1,0,0,1,0,1], 2))

console.log(kLengthApart([1,1,1,1,1],  0))

console.log(kLengthApart([0,1,0,1], 1))

