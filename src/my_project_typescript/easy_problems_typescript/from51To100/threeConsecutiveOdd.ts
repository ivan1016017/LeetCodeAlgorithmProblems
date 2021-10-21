function threeConsecutiveOdds(arr: number[]): boolean {

    let count: number = 0
    for (let num of arr){
        if (num%2 === 0){
            count = 0
        } else {
            count += 1
        }
        if (count >=3){
            
            return true
            
        }
    }

    return false 
};



console.log(threeConsecutiveOdds([2,6,4,1]))

console.log(threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))
