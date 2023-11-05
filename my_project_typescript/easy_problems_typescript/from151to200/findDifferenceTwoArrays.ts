function findDifferenceTwo(nums1: number[], nums2: number[]): number[][] {

    let listOne: number[] = [];
    let listTwo: number[] = [];

    for (let num of nums1){
        if (!nums2.includes(num) && !listOne.includes(num)){
            listOne.push(num)
        }
    }

    for (let num of nums2){
        if (!nums1.includes(num) && !listTwo.includes(num)){
            listTwo.push(num)
        }
    }

    let answer: number[][] = []

    answer.push(listOne)
    answer.push(listTwo)

    return answer 
};


function findDifferenceThree(nums1: number[], nums2: number[]): number[][] {

    let listOne: number[] = [];
    let listTwo: number[] = [];
    let setOne = new Set(nums1)
    let setTwo = new Set(nums2)

    for (let num of setOne){
        if (!nums2.includes(num)){
            listOne.push(num)
        }
    }

    for (let num of setTwo){
        if (!nums1.includes(num)){
            listTwo.push(num)
        }
    }

    return [listOne,listTwo]
};


function findDifferenceFour(nums1: number[], nums2: number[]): number[][] {

    let listOne: number[] = [];
    let listTwo: number[] = [];
    let setOne = new Set(nums1)
    let setTwo = new Set(nums2)

    setOne.forEach(num => {
        if (!nums2.includes(num)){
            listOne.push(num)
        }
    })

    setTwo.forEach(num => {
        if (!nums1.includes(num)){
            listTwo.push(num)
        }
    })

    return [listOne,listTwo]
};

function findDifference(nums1: number[], nums2: number[]): number[][] {
    let s1 = new Set(nums1);
    let s2 = new Set(nums2);
    
    return [[...s1].filter(num => !s2.has(num)), [...s2].filter(num => !s1.has(num))];
};