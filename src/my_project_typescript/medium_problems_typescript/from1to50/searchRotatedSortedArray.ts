function search(nums: number[], target: number): number {

    function binarySearch(nums: number[], left: number, right: number, target:number):number{

        if (left > right){
            return -1 
        }

        let mid: number = Math.floor((left+right)/2)

        if (nums[mid] === target){
            return mid
        }

        if (nums[left] <= nums[mid]){
            if (target>=nums[left] && target<=nums[mid]){
                return binarySearch(nums, left, mid-1, target)
            }
            return binarySearch(nums, mid+1,right, target)
        }

        if (target>=nums[mid] && target<=nums[right]){
            return binarySearch(nums, mid+1, right, target)
        }
        return binarySearch(nums, left, mid-1, target)
    }

    return binarySearch(nums, 0, nums.length-1, target)

};