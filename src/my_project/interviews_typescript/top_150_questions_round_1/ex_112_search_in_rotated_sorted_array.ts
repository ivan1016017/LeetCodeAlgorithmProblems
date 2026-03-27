/**
 * Search for target in a rotated sorted array using binary search.
 * 
 * Time Complexity: O(log n)
 * Space Complexity: O(1)
 * 
 * @param nums - Rotated sorted array with distinct values
 * @param target - Target value to search for
 * @returns Index of target if found, -1 otherwise
 */
function search(nums: number[], target: number): number {
    if (!nums || nums.length === 0) {
        return -1;
    }
    
    let left = 0;
    let right = nums.length - 1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        // Found target
        if (nums[mid] === target) {
            return mid;
        }
        
        // Determine which half is sorted
        if (nums[left] <= nums[mid]) {
            // Left half is sorted
            if (nums[left] <= target && target < nums[mid]) {
                // Target is in the sorted left half
                right = mid - 1;
            } else {
                // Target is in the right half
                left = mid + 1;
            }
        } else {
            // Right half is sorted
            if (nums[mid] < target && target <= nums[right]) {
                // Target is in the sorted right half
                left = mid + 1;
            } else {
                // Target is in the left half
                right = mid - 1;
            }
        }
    }
    
    return -1;
}

// Example usage:
// console.log(search([4,5,6,7,0,1,2], 0)); // Output: 4
// console.log(search([4,5,6,7,0,1,2], 3)); // Output: -1
// console.log(search([1], 0)); // Output: -1


