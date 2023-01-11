function canAttendMeetings(intervals: number[][]): boolean {

    intervals = intervals.sort((a,b) => a[0]<=b[0]?-1:1)

    for (let i = 0; i < intervals.length-1; i++){
        if (intervals[i][1] > intervals[i+1][0]){
            return false
        }
    }

    return true 

};

canAttendMeetings([[7,10],[2,4]])