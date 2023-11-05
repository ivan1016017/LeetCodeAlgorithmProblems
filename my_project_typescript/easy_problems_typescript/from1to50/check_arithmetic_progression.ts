function canMakeArithmeticProgression(arr: number[]): boolean {

    arr = arr.sort((x,y) => x <= y ? -1: 1)

    let solution: boolean = true;

    if (arr.length === 1){
        return solution;
    }

    let temp = arr[1] - arr[0]

    for (let i = 0; i < arr.length -1; i++){
        if (arr[i+1] - arr[i] !== temp){
            solution = false;
            return solution;
        }
    }

    return solution;

};

console.log(canMakeArithmeticProgression([3,5,1]))