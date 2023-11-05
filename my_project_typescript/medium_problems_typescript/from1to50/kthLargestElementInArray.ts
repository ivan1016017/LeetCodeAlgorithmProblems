function findKthLargest(nums: number[], k: number): number {

    nums = nums.sort( (a,b) => a>=b?-1:1)

    return nums[k-1]
};