function removeElement(nums: number[], val: number): number {
  let temp: number = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== val) {
      nums[temp] = nums[i];
      temp += 1;
    }
  }
  return temp;
}


console.log(removeElement([0,1,2,2,3,0,4,2],2));