function distributeCandies(candyType: number[]): number {
    let count: number = 0
    let listDistinctCandies: Array<number> = []

    candyType.map(candy => {
        if (!listDistinctCandies.includes(candy)){
            listDistinctCandies.push(candy)
            count += 1
        }
    })
    if (count <= candyType.length/2){
        return count
    }
    else{
        return candyType.length/2
    }
};

console.log(distributeCandies([1,1,2,2,3,3]))

console.log(distributeCandies([1,1,2,3]))

console.log(distributeCandies([6,6,6,6]))
