function findMedianSortedArrays(nums1: number[], nums2: number[]): number {

    let solution: number[] = []
    let i = 0;
    let j = 0;
    let lenNums1: number = nums1.length;
    let lenNums2: number = nums2.length

    while (i < lenNums1 && j < lenNums2){
        if (nums1[i] <= nums2[j]){
            solution.push(nums1[i])
            i += 1
        }
        else{
            solution.push(nums2[j])
            j += 1
        }
    }
    solution = solution.concat(nums1.slice(i,lenNums1)).concat(nums2.slice(j,lenNums2))
    let lenSolution: number = lenNums1 + lenNums2
    return lenSolution % 2 !== 0? solution[Math.floor(lenSolution/2)]: (solution[Math.floor(lenSolution/2)]+ solution[Math.floor(lenSolution/2)-1])/2

};