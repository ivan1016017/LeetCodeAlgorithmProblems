function maxAscendingSum(nums: number[]): number {

    let tempMax: number = nums[0]
    let minIndex: number = 0
    let maxIndex: number = 0

    for (let i = 1; i < nums.length; i++){
        if (nums[i-1] < nums[i]){
            maxIndex = i
            if ( nums.slice(minIndex, maxIndex+1).reduce((a,b)=> a+b,0) > tempMax){
                tempMax = nums.slice(minIndex, maxIndex+1).reduce((a,b)=> a+b,0) 
            }
        }
        else{
            minIndex = i
            maxIndex = i
        }
    }

    return tempMax

};

console.log(maxAscendingSum([10,20,30,5,10,50]))

console.log(maxAscendingSum([10,20,30,40,50]))

console.log(maxAscendingSum([12,17,15,13,10,11,12]))

console.log(maxAscendingSum([100,10,1]))


console.log([100,1,10].reduce((a,b) => a+b, 0))


