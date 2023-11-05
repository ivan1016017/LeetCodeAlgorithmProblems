function rearrangeArray(nums: number[]): number[] {

    let a: Array<number> = Array(nums.length).fill(0)

    let p: number = 0
    let n: number = 1

    for (let num of nums){
        if (num > 0){
            a[p] = num
            p+=2
        }
        else{
            a[n] = num
            n+=2
        }
    }

    return a

};