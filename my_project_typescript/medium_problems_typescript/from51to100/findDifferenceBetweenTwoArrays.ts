function findDifference(nums1: number[], nums2: number[]): number[][] {

    let arrayOne: Array<number> = []
    let arrayTwo: Array<number> = []


    let solution: Array<Array<number>> = []


    for (let a of nums1){
        if (!nums2.includes(a)){
            arrayOne.push(a)
        }
    }

    for (let a of nums2){
        if (!nums1.includes(a)){
            arrayTwo.push(a)
        }
    }

    solution.push(arrayOne)
    solution.push(arrayTwo)

    return solution

};