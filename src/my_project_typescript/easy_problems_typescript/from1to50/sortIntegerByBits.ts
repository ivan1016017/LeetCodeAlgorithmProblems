function sortByBits(arr: number[]): number[] {
    arr.sort((a,b) => a>=b?-1:1 )

    function countNumberBits(num: number): number{
        let quotient: number = -1
        let count: number = 0
        let reminder: number = 0
        while (quotient !== 0){
            quotient = Math.floor(num/2)
            reminder = num % 2 
            count += reminder 
            num = quotient
        }
        return count 
    }

    arr.sort((a,b) => countNumberBits(a) <= countNumberBits(b)?-1:1)
    return arr 

};


console.log(sortByBits([0,1,2,3,4,5,6,7,8]))

console.log(sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))

console.log(sortByBits([10000,10000]))

console.log(sortByBits([2,3,5,7,11,13,17,19]))

function countNumberBits(num: number): number{
    let quotient: number = -1
    let count: number = 0
    let reminder: number = 0
    while (quotient !== 0){
        quotient = Math.floor(num/2)
        reminder = num % 2 
        count += reminder 
        num = quotient
    }
    return count
}


let sample: Array<number> = [1,2,3,4,5,6,7]

sample.map(x => console.log(countNumberBits(x)))

