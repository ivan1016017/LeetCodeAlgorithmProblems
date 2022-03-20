function countElements(nums: number[]): number {

    let maxNum: number = nums.reduce((a,b) => Math.max(a,b))
    let minNum: number = nums.reduce((a,b) => Math.min(a,b))

    let answer: number = 0

    nums.map(a => a > minNum && a < maxNum ? answer += 1:0)

    return answer 

};