function productExceptSelf(nums: number[]): number[] {

    let output: Array<number> = Array(nums.length).fill(1)

    let leftProduct: number = 1
    for (let i = 1; i < nums.length; i++ ){
        leftProduct *= nums[i-1]
        output[i] = leftProduct
    }


    let rightProduct: number = 1
    for (let i = nums.length-2; i > -1; i--){
        rightProduct *= nums[i+1]
        output[i] *= rightProduct
    }

    return output
};