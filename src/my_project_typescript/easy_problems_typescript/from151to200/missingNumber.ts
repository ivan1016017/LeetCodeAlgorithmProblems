function missingNumber(nums: number[]): number {

    let maxNumber: number = Math.max(...nums)

    let tempObj: {[key:number]:number} = {}

    for (let num of nums){
        tempObj[num] = 1
    }

    for (let i = 0; i < maxNumber + 1; i++){
        if (tempObj[i] !== 1) {
            return i;
        }
    }

    return maxNumber + 1

};