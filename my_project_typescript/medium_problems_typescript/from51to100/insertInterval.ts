function insert(intervals: number[][], newInterval: number[]): number[][] {

    intervals.push(newInterval)
    let answer: Array<Array<number>> = []

    intervals.sort( (a,b) => a[0] <= b[0]?-1:1  )

    for (let i of intervals){
        if (answer.length !== 0 && answer[answer.length-1][1] >= i[0]){
            answer[answer.length-1][1] = Math.max(answer[answer.length -1][1],i[1])
        }
        else{
            answer.push(i)
        }

    }



    return answer 

};


console.log(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],  [4,8]))