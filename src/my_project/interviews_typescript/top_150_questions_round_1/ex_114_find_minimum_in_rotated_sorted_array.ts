function findMin(nums: number[]): number {
    let left = 0;
    let right = nums.length - 1;
    
    // If array is not rotated or has only one element
    if (nums[left] <= nums[right]) {
        return nums[left];
    }
    
    while (left < right) {
        const mid = Math.floor(left + (right - left) / 2);
        
        // If mid element is greater than rightmost element,
        // the minimum must be in the right half
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            // The minimum is in the left half (including mid)
            right = mid;
        }
    }
    
    return nums[left];
}