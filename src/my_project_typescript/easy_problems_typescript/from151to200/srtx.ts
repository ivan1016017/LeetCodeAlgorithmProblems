function mySqrt(x: number): number {
    let left: number = 0
    let right: number = x 

    let mid: number
    while (left <= right){
        mid = Math.floor((left+right)/2)

        if (mid*mid  > x){
            right = mid -1 
        }
        else if  (mid*mid < x ){
            left = mid + 1
        }
        else {
            return mid 
        }
    }
    return right

};