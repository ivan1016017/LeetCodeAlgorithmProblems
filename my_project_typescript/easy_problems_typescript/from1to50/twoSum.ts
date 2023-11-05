function twoSum(nums: number[], target: number): number[] {
    let temp: Array<number> = [];
    for (let i = 0; i < nums.length; i++){
        for (let j = i+1; j < nums.length; j++){
            if (nums[i] + nums[j] === target){
                temp.push(i)
                temp.push(j)
            }
        }
    }
    return temp
};

console.log(twoSum([2,7,11,15],9));
console.log(twoSum([3,2,4],6));
console.log(twoSum([3,3],6));