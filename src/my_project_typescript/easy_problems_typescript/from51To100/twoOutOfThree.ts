function twoOutOfThree(nums1: number[], nums2: number[], nums3: number[]): number[] {

    let temp: Array<number> = []


    nums1.map( num => {
        if (!temp.includes(num)){
            temp.push(num)
        }
    })
    nums1 = temp 

    temp = []
    nums2.map( num => {
        if (!temp.includes(num)){
            temp.push(num)
        }
    })
    nums2 = temp 

    temp = []
    nums3.map( num => {
        if (!temp.includes(num)){
            temp.push(num)
        }
    })
    nums3 = temp 

    let tempDict: any = {}

    for (let num of nums1.concat(nums2).concat(nums3)){
        tempDict[num] = 0
    }

    for (let num of nums1.concat(nums2).concat(nums3)){
        tempDict[num] +=1 
    }

    let answer: Array<number> =[]
    for (let key in tempDict){
        if (tempDict[key] >= 2){
            answer.push(parseInt(key))
        }
    }




    return answer
};

console.log(twoOutOfThree([1,1,3,2],  [2,3], [3]))

console.log(twoOutOfThree([3,1],  [2,3],  [1,2]))

console.log(twoOutOfThree([1,2,2],  [4,3,3], [5]))
