function fact(n:number): number {
    if (n === 0 || n === 1){
        return 1
    }
    else {
        return n*fact(n-1)
    }
}

function uniquePaths(m: number, n: number): number {
    let numerator = fact(n+m-2)
    let denominator = fact(n-1)*fact(m-1)
    return numerator/denominator
};