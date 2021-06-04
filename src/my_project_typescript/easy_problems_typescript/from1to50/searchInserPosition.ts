function searchInsert(nums: number[], target: number): number {
    let l: number = 0
    let r: number = nums.length-1;
    let mid: number;
    while (l <= r){
        mid = Math.floor((l + r)/2);
        if (nums[mid] === target){
            return mid
        } 
        if (nums[mid] > target){
            r = mid -1
            console.log("flag right", r)
        }
         if (nums[mid] < target) {
            l = mid +1
            console.log("flag left", l)
        }
        
    }
    return l


};

console.log(searchInsert([1,3,5,6], 2));