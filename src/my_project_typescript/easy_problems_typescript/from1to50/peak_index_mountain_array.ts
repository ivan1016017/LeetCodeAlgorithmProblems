function peakIndexInMountainArray(arr: number[]): number {

    let solution: number = 0;
    let max: number = -1;

    arr.map( (x, index) => {
        if (x > max){
            max = x
            solution = index
        }
    } )

    return solution
};

console.log((peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19])))