function numSubarrayProductLessThanK(nums: number[], k: number): number {

    let product: number = 1
    let left: number = 0
    let answer: number = 0

    for (let right = 0; right < nums.length; right++){
        product*=nums[right]

        while (product >= k && right >= left){
            product/=nums[left]
            left+=1
        }
        answer+= right-left+1
    }
    return answer 

};