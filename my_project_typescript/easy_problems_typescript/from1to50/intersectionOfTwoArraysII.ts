function intersect(nums1: number[], nums2: number[]): number[] {

    let commonList: Array<number> = nums1.concat(nums2)

    let objNums1: {[key:number]: number} = {}
    let objNums2: {[key:number]: number} = {}

    for (let i = 0; i < commonList.length; i++){
        objNums1[commonList[i]] = 0
        objNums2[commonList[i]] = 0
    }

    let lenNums1: number = nums1.length
    let lenNums2: number = nums2.length

    for (let i = 0; i < lenNums1; i++){
        objNums1[nums1[i]] += 1
    }

    for (let i = 0; i < lenNums2; i++){
        objNums2[nums2[i]] += 1
    }

    let answer: Array<number> = []
    
    if (lenNums1 <= lenNums2){
        for (let key in objNums1){
            
            answer = answer.concat(Array(Math.min(objNums1[key],objNums2[key])).fill(key))
        }
    }
    else{
        for (let key in objNums2){
            
            answer = answer.concat(Array(Math.min(objNums1[key],objNums2[key])).fill(key))
        }
    }



    return answer

};

console.log(intersect([1,2,2,1],  [2,2]))

console.log(intersect([4,9,5],  [9,4,9,8,4]))







