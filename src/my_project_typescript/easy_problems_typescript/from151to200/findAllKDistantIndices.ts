function findKDistantIndices(nums: number[], key: number, k: number): number[] {
    let a: Array<number> = []
    for (let i=0; i < nums.length; i++){
        if (nums[i] === key){
            a.push(i)
        }
    }

    let res: Array<number> = []
    let isk: boolean = false
    for (let i=0; i<nums.length;i++){
        isk = false 

        for (let j of a){
            if (Math.abs(i-j) <= k){
                isk = true 
                break 
            }
        }
        if (isk){
            res.push(i)
        }
    }

    return res

};