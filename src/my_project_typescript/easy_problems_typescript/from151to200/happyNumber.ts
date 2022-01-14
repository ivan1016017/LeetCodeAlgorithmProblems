function isHappy(n: number): boolean {

    function genNext(n:number): number {
        let totalSum: number = 0
        let digit: number 
        while ( n > 0){
            digit = n % 10
            n = Math.floor(n /10)
            totalSum += digit ** 2
        }
        return totalSum
    }

    let seen: Array<number> = []

    while (n !== 1 && !seen.includes(n)){
        seen.push(n)
        n = genNext(n)
    }


    return n === 1

};