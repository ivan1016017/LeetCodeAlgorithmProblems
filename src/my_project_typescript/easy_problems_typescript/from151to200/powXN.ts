function myPow(x: number, n: number): number {

    if (!n){
        return 1
    }
    if (n < 0){
        return 1/myPow(x,-n)
    }
    if (n%2 !== 0){
        return x * myPow(x,n-1)
    }
    return myPow(x*x,n/2)

};