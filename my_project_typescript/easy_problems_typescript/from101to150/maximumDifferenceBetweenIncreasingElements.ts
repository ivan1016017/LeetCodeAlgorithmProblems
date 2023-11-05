function maximumDifference(nums: number[]): number {
    let answer: number = -1
    let minVal:number = Infinity
    let lenNumber: number = nums.length

    nums.forEach( num => {
        if (num < minVal){
            minVal = num
        }
        else if (num - minVal > 0){
            answer = Math.max(answer, num - minVal)
        }
    })

    return answer 
};

console.log(maximumDifference([7,1,5,4]))

console.log(maximumDifference([9,4,3,2]))

console.log(maximumDifference([1,5,2,10]))
