function subsets(nums: number[]): number[][] {


    let lenNums: number = nums.length

    let solution: Array<Array<number>> = [[]]

    let temp: Array<Array<number>> = []

    for (let i = 0; i < lenNums; i++){

        temp = []

        for (let item of solution){
            
            temp = temp.concat([item.concat([nums[i]])])
        }
        solution = solution.concat(temp)
    }


    return solution
};

console.log(subsets([1,2,3]))

// let sample: Array<Array<number>> = [[1,2,3]]

// console.log(sample.concat([[7]]))

