function divideArray(nums: number[]): boolean {

    let tempObj: {[key:number]: number} = {}

    for (let num of nums){
        tempObj[num] = 0
    }

    for (let num of nums){
        tempObj[num] += 1
    }

    let answer: boolean = true 
    for (let key in tempObj){
        if (tempObj[key] % 2 !==0 ){
            answer = !answer 

            return answer
        }
    }


    return answer

};