function findDuplicate(nums: number[]): number {

    let solutionObj: {[key:number]:number} = {}

    for (let item of nums){
        solutionObj[item] = 0
    }

    

    for (let item of nums){
        solutionObj[item] += 1
        if (solutionObj[item] >= 2){
            return item
        }

    }

};