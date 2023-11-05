function generateMatrix(n: number): number[][] {

    if (!n){
        return []
    }

    let res: Array<Array<number>> = []

    for (let i = 0; i < n; i++){
        res.push(Array(n).fill(0))
    }

    let left: number = 0
    let right: number = n-1 
    let top: number = 0
    let down: number = n-1
    let num: number = 1

    while (left <= right && top <= down){
        for (let i = left; i < right+1; i++){
            res[top][i] = num 
            num += 1
        }
        top += 1
        for (let i = top; i < down+1; i++){
            res[i][right] = num 
            num += 1
        }
        right -= 1
        for (let i = right; i > left-1; i--){
            res[down][i] = num 
            num += 1
        }
        down -= 1
        for (let i = down; i > top-1; i--){
            res[i][left] = num 
            num += 1
        }
        left += 1
    }

    return res

};