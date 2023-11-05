function removeDuplicates(nums: number[]): number {
    let j: number = 0;
    let numsLenght: number = nums.length;
    if (numsLenght === 0 || numsLenght ===1) {
        return numsLenght;
    }
    for (let i = 0; i < numsLenght -1 ; i++ ){
        if (nums[i] !== nums[i+1]){
            nums[j] = nums[i]
            j += 1
        }
    
    }
    nums[j] = nums[numsLenght-1]
    return j+1;
};


console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4]));
console.log(removeDuplicates([1,1,2]));
console.log(removeDuplicates([1,2,3]));