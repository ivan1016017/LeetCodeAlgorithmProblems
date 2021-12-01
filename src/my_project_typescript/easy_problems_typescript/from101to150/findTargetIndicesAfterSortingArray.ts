function targetIndices(nums: number[], target: number): number[] {

    nums = nums.sort( (a,b) => a<=b?-1:1)
    let len_nums: number = nums.length
    let answer: Array<number> = []

    for (let i = 0; i < len_nums; i++){
        if (nums[i] === target){
            answer.push(i)
        }
    }

    return answer 
};

console.log(targetIndices([1,2,5,2,3],  2))

console.log(targetIndices([1,2,5,2,3], 3))

console.log(targetIndices([1,2,5,2,3],  5))

console.log(targetIndices([1,2,5,2,3],  4))
