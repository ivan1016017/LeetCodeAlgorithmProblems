function maxArea(height: number[]): number {

    let l: number = 0
    let r: number = height.length -1 
    let area: number = 0

    while (l < r){
        area = Math.max(area, Math.min(height[l], height[r])*(r-l))

        if (height[l] < height[r]){
            l += 1
        }else {
            r-=1
        }
    }

    return area

};