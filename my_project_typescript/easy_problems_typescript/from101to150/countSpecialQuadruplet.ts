function countQuadruplets(nums: number[]): number {

    let answer: number = 0
    let lenNums: number = nums.length

    for (let i = 0; i < lenNums; i++){
        for (let j = i+1; j < lenNums; j++){
            for (let k = j+1; k < lenNums; k++){
                for (let l = k+1; l < lenNums; l++){
                    if (nums[i] + nums[j] + nums[k] === nums[l]){
                        answer += 1
                    }
                }
            }
        }
    }

    return answer 

};

console.log(countQuadruplets([1,2,3,6]))

console.log(countQuadruplets([3,3,6,4,5]))

console.log(countQuadruplets([1,1,1,3,5]))
