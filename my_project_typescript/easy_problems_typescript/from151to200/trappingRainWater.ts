function trap(height: number[]): number {
    let solution: number = 0
    let l: number = 0
    let r: number = height.length
    let i: number 

    while (l < r){
        i = 1

        if (height[l] < height[r]){
            while (height[l] > height[l+i]){
                solution += height[l]-height[l+i]
                i += 1
            }
            l += i 
        }
        else{
            while (height[r] > height[r-i]){
                solution += height[r] - height[r-i]
                i += 1
            }
            r -= i 
        }
    }

    return solution

};