function findPeakElement(nums: number[]): number {

    let low: number = 0
    let high: number = nums.length -1
    let mid: number = 0
    while (low < high){
        mid = Math.floor((low+high)/2)

        if (nums[mid] > nums[mid+1]){
            high = mid 
        }
        else{
            low = mid + 1
        }
    }
    return low
};