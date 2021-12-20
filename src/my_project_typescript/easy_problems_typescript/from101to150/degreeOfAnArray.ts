function findShortestSubArray(nums: number[]): number {

    let visited: {[key:string]: number[]} = {}

    nums.forEach( (value, index) => {
        if (value in visited){
            visited[value].push(index)
        }
        else{
            visited[value] = [index]
        }
    })

    let maxLength: number = 0

    for (let k in visited){
        maxLength = Math.max(visited[k].length, maxLength)
    }

    let answer: Array<number> = []
    for (let k in visited){
        if (visited[k].length === maxLength){
            answer.push(visited[k][visited[k].length-1] - visited[k][0])
        }
    }
    

    return answer.reduce((a,b) => {return Math.min(a,b)}) +1

};


console.log(findShortestSubArray([1,2,2,3,1])) 