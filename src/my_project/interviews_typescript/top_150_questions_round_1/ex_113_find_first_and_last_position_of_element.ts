function searchRange(nums: number[], target: number): number[] {
    if (nums.length === 0) {
        return [-1, -1];
    }
    
    // Find the leftmost (first) occurrence
    const left = findLeft(nums, target);
    if (left === -1) {
        return [-1, -1];
    }
    
    // Find the rightmost (last) occurrence
    const right = findRight(nums, target);
    
    return [left, right];
}

function findLeft(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;
    let result = -1;
    
    while (left <= right) {
        const mid = Math.floor(left + (right - left) / 2);
        
        if (nums[mid] === target) {
            result = mid;
            right = mid - 1; // Continue searching in the left half
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}

function findRight(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;
    let result = -1;
    
    while (left <= right) {
        const mid = Math.floor(left + (right - left) / 2);
        
        if (nums[mid] === target) {
            result = mid;
            left = mid + 1; // Continue searching in the right half
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}