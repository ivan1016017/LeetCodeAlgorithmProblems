function permuteUnique(nums: number[]): number[][] {
    let results: Array<Array<number>> = []
    function backtrack(comb:Array<number>, counter:{[key:number]: number}):void{
        if (comb.length === nums.length){
            console.log(comb)
            results.push(comb)
            results.push([1])
            return
        }

        for (let num in counter){
            if (counter[num] > 0) {
                comb.push(parseInt(num))
                counter[num] -=1

                backtrack(comb, counter)

                comb.pop()
                counter[num] += 1
            }
            
        }
        
    }

    let temp: {[key:number]: number} = {}
    for (let num of nums){
        temp[num] = 0
    }

    for (let num of nums){
        temp[num] +=1
    }
    // console.log(temp)

    backtrack([],temp)
    return results

};

let sample: Array<Array<number>> = []

sample.push([1,2,3])
console.log(sample)

console.log(permuteUnique([1,1,2]))