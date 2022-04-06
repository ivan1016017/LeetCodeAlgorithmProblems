function threeSumMulti(arr: number[], target: number): number {

    let ans: number = 0
    let n: number = arr.length

    let level2: Array<number> = []

    for (let i = 2; i < n; i++){
        for (let j = 0; j < i-1; j++){
            level2[arr[j]+arr[i-1]] = 0
            

        }
        level2[target-arr[i]] = 0
    }

    for (let i = 2; i < n; i++){
        for (let j = 0; j < i-1; j++){
            level2[arr[j]+arr[i-1]] += 1
        }
        ans = ans + level2[target-arr[i]] 
        ans = ans % (10**9  + 7)
    }

    return ans

};