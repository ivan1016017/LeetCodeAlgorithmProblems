function findPeakElement(nums: number[]): number {
    let left = 0;
    let right = nums.length - 1;
    
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        
        // If mid element is less than next element, peak must be on the right
        if (nums[mid] < nums[mid + 1]) {
            left = mid + 1;
        } else {
            // Otherwise, peak is on the left (including mid)
            right = mid;
        }
    }
    
    return left;
};