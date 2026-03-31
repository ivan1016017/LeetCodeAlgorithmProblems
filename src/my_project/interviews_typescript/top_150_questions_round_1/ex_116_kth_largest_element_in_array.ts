function findKthLargest(nums: number[], k: number): number {
    const target = nums.length - k;

    function quickselect(left: number, right: number): number {
        const pivotIndex = left + Math.floor(Math.random() * (right - left + 1));
        const pivot = nums[pivotIndex];

        // 3-way partition (Dutch National Flag)
        let low = left;
        let mid = left;
        let high = right;

        while (mid <= high) {
            if (nums[mid] < pivot) {
                [nums[low], nums[mid]] = [nums[mid], nums[low]];
                low++;
                mid++;
            } else if (nums[mid] > pivot) {
                [nums[mid], nums[high]] = [nums[high], nums[mid]];
                high--;
            } else {
                mid++;
            }
        }

        // All elements equal to pivot are in [low, high]
        if (target < low) {
            return quickselect(left, low - 1);
        } else if (target > high) {
            return quickselect(high + 1, right);
        } else {
            return nums[target];
        }
    }

    return quickselect(0, nums.length - 1);
};