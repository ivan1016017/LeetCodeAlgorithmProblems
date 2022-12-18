function merge(intervals: number[][]): number[][] {

    let answer: number[][] = []

    intervals = intervals.sort((a,b) => a[0]<=b[0]?-1:1)

    for (let i of intervals){
        
        if (answer.length > 0 && (i[0] <= answer[answer.length-1][1])){
            answer[answer.length-1][1] = Math.max(answer[answer.length-1][1],i[1])
        }
        else{
            answer = answer.concat(Array(i))
        }
    }

    return answer

}