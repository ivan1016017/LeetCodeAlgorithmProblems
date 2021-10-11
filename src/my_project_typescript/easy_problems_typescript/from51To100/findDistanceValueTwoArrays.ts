function findTheDistanceValue(arr1: number[], arr2: number[], d: number): number {

    let answer: number = 0
    let flag: boolean = true 

    arr1.map( num1 => {
        flag = true 
        arr2.map( num2 => {
            if (Math.abs(num1 - num2)  <= d){
                flag = false 
            }
        })
        if (flag){
            answer += 1
        }
    })

    return answer 

};


console.log(findTheDistanceValue([4,5,8], [10,9,1,8], 2))

console.log(findTheDistanceValue( [1,4,2,3], [-4,-3,6,10,20,30],  3))

console.log(findTheDistanceValue([2,1,100,3],  [-5,-2,10,-3,7], 6))
