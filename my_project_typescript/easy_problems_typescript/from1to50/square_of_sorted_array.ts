function sortedSquares(nums: number[]): number[] {
    let solution: Array<number> = []

    nums.map( (x) => {
        solution.push(x**2)
    })

    solution = solution.sort((x,y) => x <= y ? -1 : 1);

    return solution

};

console.log(sortedSquares([-4,-1,0,3,10]))