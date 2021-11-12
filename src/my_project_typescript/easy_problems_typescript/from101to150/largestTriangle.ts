function largestTriangleArea(points: number[][]): number {
    let area: number = 0
    let x1: number = 0
    let x2: number = 0
    let x3: number = 0
    let y1: number = 0
    let y2: number = 0
    let y3: number = 0
    let pointsLength: number = points.length

    for (let i = 0; i < pointsLength; i++){
        x1 = points[i][0]
        y1 = points[i][1]
        for (let j = i+1; j < pointsLength-1; j++){
            x2 = points[j][0]
            y2 = points[j][1]
            for (let k = j + 1; k < pointsLength; k++){
                x3 = points[k][0]
                y3 = points[k][1]
                if (Math.abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))) > area ){
                    area = Math.abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
                }
                        
            }
        }
    }
    return area

};