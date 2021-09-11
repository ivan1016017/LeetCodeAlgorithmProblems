function minCostToMoveChips(position: number[]): number {

    let evenCount: number = 0;
    let oddCount: number = 0;

    position.map((currentElement) => {
        if (currentElement % 2 === 0){
            evenCount += 1
        }
        else {
            oddCount += 1
        }
    })

    return Math.min(evenCount, oddCount)

};


console.log(minCostToMoveChips([2,2,2,3,3]))