function countKDifference(nums: number[], k: number): number {
    let count: number = 0;

    for (let i = 0; i < nums.length; i++){
        for (let j = i+1; j < nums.length; j++){
            if (Math.abs(nums[i]-nums[j]) === k){
                count += 1
            }
        }
    }
    return count 
};

console.log(countKDifference( [1,2,2,1], 1))

console.log(countKDifference( [1,3], 3))

console.log(countKDifference( [3,2,1,5,4], 2))
