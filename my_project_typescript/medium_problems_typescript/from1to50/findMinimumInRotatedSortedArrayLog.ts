function findMin(nums: number[]): number {

    let low: number = 0
    let high: number = nums.length -1
    let mid: number = 0

    while (low < high){
        mid = Math.floor((low + high)/2)

        if (nums[mid] < nums[mid-1] && nums[mid] < nums[mid+1]){
            return nums[mid]
        }
        else if (nums[mid] <  nums[high]){
            high = mid -1
        }
        else if (nums[mid] > nums[high]){
            low = mid +1
        }
    }
    return nums[low]
};