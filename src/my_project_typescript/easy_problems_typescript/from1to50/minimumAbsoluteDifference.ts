function minimumAbsDifference(arr: number[]): number[][] {
    let answer: any  = []

    arr.sort((a,b) => a <= b?-1:1)

    let minDistance: number = Infinity
    let temp: number = 0

    for (let i = 0; i < arr.length-1; i++){
        if (arr[i+1] - arr[i] <= minDistance){
            minDistance = arr[i+1] - arr[i]
            if (temp > minDistance){
                answer = []
            }
            temp = minDistance
            answer.push([arr[i], arr[i+1]])
        }
    }
    return answer
};

// function to be reverted 
function myFunction(myVariable:  number): number{
    return myVariable*7
}

console.log(minimumAbsDifference([4,2,1,3]))

console.log(minimumAbsDifference([1,3,6,10,15]))


console.log(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
