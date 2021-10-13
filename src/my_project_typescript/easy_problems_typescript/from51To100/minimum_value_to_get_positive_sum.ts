function minStartValue(nums: number[]): number {

    let count: number = 0
    let tempNegative: number = 0

    nums.map(num => {
        count += num 
        // if (count < tempNegative){
        //     tempNegative = count 
        // }
        tempNegative = Math.min(count, tempNegative)
    })
    return Math.abs(tempNegative) + 1
};


console.log(minStartValue([-3,2,-3,4,2]))

console.log(minStartValue([1,2]))

console.log(minStartValue([1,-2,-3]))
