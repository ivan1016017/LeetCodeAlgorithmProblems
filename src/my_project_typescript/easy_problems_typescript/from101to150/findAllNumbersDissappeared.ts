function findDisappearedNumbers(nums: number[]): number[] {
    let answer: Array<number> = []
    let lenNums: number = nums.length
    let tempDict: any = {}

    for (let i = 1; i <= lenNums; i++){
        tempDict[i] = 0
    }

    nums.map( num => {
        tempDict[num] += 1
    })

    for (let i = 1; i <= lenNums; i++){
        if (tempDict[i] == 0){
        answer.push(i)
        }
    }

    return answer
};

console.log(findDisappearedNumbers([4,3,2,7,8,2,3,1]))

console.log(findDisappearedNumbers([1,1]))
