function isPerfectSquare(num: number): boolean {
    let left: number = 0
    let right: number = num

    let mid: number 

    while (left<=right){
        mid = Math.floor((left+right)/2)

        if(mid**2 == num){
            return true 
        }
        else if (mid**2 < num){
            left=mid+1
        }
        else {
            right=mid-1
        }
    }

    return false

};