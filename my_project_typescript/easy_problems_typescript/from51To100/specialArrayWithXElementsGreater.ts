function specialArray(nums: number[]): number {


    nums.sort( (a,b) => a>=b?-1:1)

    let lenNums: number = nums.length

    for (let i =0; i< nums.length; i++){
        if (i+1 <= nums[i]){
            if (i == nums.length -1){
                return i+1
            }
            else{
                if (i+1 <= nums[i+1]){
                    continue
                }
                else{
                    return i+1
                }
            }
        }
    }
    return -1
};


console.log(specialArray([3,5]))

console.log(specialArray([0,0]))

console.log(specialArray([0,4,3,0,4]))

console.log(specialArray([3,6,7,7,0]))
