function isPowerOfThree(n: number): boolean {

    if (n < 1){
        return false
    }
    else if (n === 1){
        return true 
    }

    let temp: number = 1 

    while (temp < n){
        temp = temp*3

        if (temp === n){
            return true
        }
    }

    return false 

};