function mostFrequent(nums: number[], key: number): number {

    let dic: {[key:number]:number} = []

    let ans: number = -1000000
    let temp: number = 0
    let lenNums: number = nums.length

    for (let i = 0; i < lenNums; i++){
        dic[nums[i]] = 0
    }

    for (let i = 0; i < lenNums-1; i++){
        if (nums[i] === key){
            dic[nums[i+1]] += 1
            if (temp < dic[nums[i+1]]){
                ans = nums[i+1]
                temp = dic[nums[i+1]]
            }
        }
    }

    return ans

};