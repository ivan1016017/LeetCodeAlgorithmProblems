function sortEvenOdd(nums: number[]): number[] {

    let result = Array(nums.length).fill(0)

    const even = nums.filter((value,index) => index%2 == 0)
    const odd = nums.filter((value,index) => index%2 !== 0)
    even.sort((a,b) => a<=b?-1:1)
    odd.sort((a,b) => a>=b?-1:1)


    for (let i = 0; i < result.length; i++) {
        if (i % 2 == 0)
            result[i] = even.shift() as number;
        else
            result[i] = odd.shift() as number;
    }
    return result;

};