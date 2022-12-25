function checkSubarraySum(nums: number[], k: number): boolean {

    let dicSolution: {[key:number]:number} = {0:-1}

    let sumValue: number = 0

    for (let i = 0; i < nums.length; i++){
        sumValue = (sumValue + nums[i]) % k 

        if (! (sumValue in dicSolution)){
            dicSolution[sumValue] = i 
        }
        else{
            if (i - dicSolution[sumValue] >=2){
                return true
            }
        }
    }

    return false 

};