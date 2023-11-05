function maxPoints(points: number[][]): number {
    if (points.length <= 2){
        return points.length
    }

    let d: {[key:string]: number} = {}

    let result: number = 0
    let overlap: number 
    let tempMax: number 
    let dx: number
    let dy: number
    let slope: any
    

    for (let i = 0; i < points.length; i++){
        d = {}
        overlap = 0
        tempMax = 0 
        for (let j = i+1; j<points.length; j++){
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if (dx === 0 && dy === 0){
                overlap +=1
                continue
            }
            if (dx === 0){
                slope = 'infinity'
                if (!d[slope]){
                    d[slope] = 1
                }
                else {
                    d[slope] += 1
                }
            }
            else {
                slope = (dy * 1.0) / dx  
                slope = slope.toString()
                if (!d[slope]){
                    d[slope] = 1
                }
                else {
                    d[slope] += 1
                }     
            }
            
            tempMax = Math.max(tempMax, d[slope])     
        }
        result = Math.max(result, tempMax+overlap+1)

    }

    return result


}


console.log(maxPoints([[1,1],[2,2],[3,3]]))

console.log(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))