function findMissingRanges(nums: number[], lower: number, upper: number): string[] {

    let res:any[] = [];
    
    nums = [lower - 1, ...nums, upper + 1];
    
    for (var i = 1; i < nums.length; i++) {
        if (nums[i] === nums[i - 1] + 1) {
            continue;
        }
        
        if (nums[i] === nums[i - 1] + 2 ) {
            res.push('' + (nums[i - 1] + 1));
        } else {
            res.push([nums[i - 1] + 1, nums[i] - 1].join('->'));
        }
    }
    
    return res;


};