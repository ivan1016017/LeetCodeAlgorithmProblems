function merge(intervals: number[][]): number[][] {

    let out: Array<Array<number>> = []

    intervals = intervals.sort( (a,b) => a[0]<=b[0]?-1:1)

    for (let i of intervals){
        if (out.length > 0 && (i[0] <= out[out.length -1][out[out.length -1].length-1])){
            out[out.length -1][out[out.length -1].length-1] = Math.max(out[out.length -1][out[out.length -1].length-1], i[i.length-1])
        }
        else {
            out = out.concat(Array(i))
        }
    }

    console.log(intervals)

    return out 
};


console.log(merge([[2,6],[8,10],[1,3],[15,18]]))

