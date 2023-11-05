function nearestValidPoint(x: number, y: number, points: number[][]): number {

    let answer: Array<any> = []
    let flag: boolean = false 
    answer = Array.from(points)
    answer.reverse()

    for (let item of points){
        if (item[0]===x || item[1]===y){
            flag = true
        }
    }

    if (flag ===false){
        return -1
    }

    function distance_manhattan(point: Array<any>){
        return Math.abs(point[0]-x) + Math.abs(point[1]-y)
    }

    answer = answer.sort((a,b) => distance_manhattan(a) <= distance_manhattan(b) ?-1:1)

    console.log(answer)

    for (let i = 0; i < points.length; i++){
        if (points[i][0] === answer[0][0] && points[i][1] === answer[0][1]){
            return i
        }
        
    }
    return 0
};


console.log(nearestValidPoint(3, 4,  [[1,2],[3,1],[2,4],[2,3],[4,4]]))