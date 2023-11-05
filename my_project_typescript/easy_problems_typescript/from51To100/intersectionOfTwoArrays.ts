function intersection(nums1: number[], nums2: number[]): number[] {

    let dictionaryOne: any = {}
    let dictionaryTwo: any = {}
    let answer: Array<number> = []

    for (let num of nums1){
        dictionaryOne[num] = 0
    }

    for (let num of nums2){
        dictionaryTwo[num] = 0
    }

    nums1 = []
    nums2 = []
    for (let num in dictionaryOne){
        nums1.push(parseInt(num))
        
    }   
    for (let num in dictionaryTwo){
        nums2.push(parseInt(num))
        
    }

    for (let num of nums1){
        if (nums2.includes(num)){
            answer.push(num)
        }
    }
    
    return answer
};


console.log(intersection([1,2,2,1], [2,2]))

console.log(intersection([4,9,5], [9,4,9,8,4]))
