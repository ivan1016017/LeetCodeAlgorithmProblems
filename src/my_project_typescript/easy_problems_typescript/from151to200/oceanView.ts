function findBuildings(heights: number[]): number[] {
    let answer: number[] = []
    let i: number = heights.length -1 
    let temp: number = 0

    while (i > -1){
        if (heights[i] > temp){
            answer.push(i)
            temp = heights[i]
        }
        i -= 1
    }

    return answer.reverse()

};