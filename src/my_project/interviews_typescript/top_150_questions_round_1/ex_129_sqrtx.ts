function mySqrt(x: number): number {
    // Edge cases
    if (x === 0 || x === 1) {
        return x;
    }
    
    // Binary search for the square root
    let left = 1;
    let right = x;
    let result = 0;
    
    while (left <= right) {
        const mid = Math.floor(left + (right - left) / 2);
        const square = mid * mid;
        
        if (square === x) {
            return mid;
        } else if (square < x) {
            // Store the potential answer and search in the right half
            result = mid;
            left = mid + 1;
        } else {
            // square > x, search in the left half
            right = mid - 1;
        }
    }
    
    return result;
};