function numberOfArithmeticSlices(nums: number[]): number {

    let le: number = nums.length
    let l: Array<number> = Array(le).fill(0)

    for (let i = 2; i < le; i++){
        if (nums[i] - nums[i-1] === nums[i-1] - nums[i-2]){
            l[i] = l[i-1] + 1
        }
    }

    return l.reduce((a,b) => a+b,0)

};