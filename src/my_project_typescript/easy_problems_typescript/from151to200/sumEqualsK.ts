function subarraySum(nums: number[], k: number): number {

    let preSum: {[key:number]:number} = {0:1}
    let sum: number = 0
    let answer: number = 0

    for (let num of nums){
        sum += num 
        let diff = sum -k 
        if (diff in preSum){
            answer += preSum[diff]
        }
        if (sum in preSum){
            preSum[sum] += 1
        }
        else{
            preSum[sum] = 1
        }
    }

    return answer
    

};