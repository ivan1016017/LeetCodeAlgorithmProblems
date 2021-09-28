function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
    let flag: boolean = false

    for (let i = 0; i < nums1.length; i++){
        flag = false 
        for (let j = 0; j < nums2.length; j++){
            if (nums1[i] === nums2[j]){
                for (let l = j+1; l < nums2.length; l++){
                    if (nums2[l] > nums1[i]){
                        nums1[i] = nums2[l]
                        flag = true
                        break
                    }
                }
                if (flag === false){
                    nums1[i] = -1
                }
                break
            }
        }
    }
    return nums1
};
// new function to be reverted
function newFunctionToBeReverted(numVariable: number){
    return numVariable
}


console.log(nextGreaterElement([4,1,2], [1,3,4,2]))