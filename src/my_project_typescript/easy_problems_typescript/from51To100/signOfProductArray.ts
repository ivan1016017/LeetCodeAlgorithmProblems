function arraySign(nums: number[]): number {

    let answer: number = 0
    let count: number = 1
    for (let num of nums){
        count = count * num
    }

    if (count === 0){
        return  0
    }
    if (count > 0){
        return  1
    }
    if (count < 0){
        return -1
    }

    return answer 

};


console.log(arraySign([-1,-2,-3,-4,3,2,1]))

console.log(arraySign([1,5,0,2,-3]))

console.log(arraySign([-1,1,-1,1,-1]))
