function removeElement(nums: number[], val: number): number {
    while (nums.includes(val)){
        const index = nums.indexOf(val);
        nums.splice(index, 1);
    }

    return nums.length;
    
};        

console.log(removeElement([3,2,2,3], 3))