function findLucky(arr: number[]): number {
    let dictSolution: any = {}
    let listSolution: Array<number> = []

    arr.map(currentElement =>{
        dictSolution[currentElement] = 0
    })

    arr.map(currentElement =>{
        dictSolution[currentElement] += 1
    })

    Object.keys(dictSolution).map(currentElement => {
        if (dictSolution[parseInt(currentElement)] === parseInt(currentElement)){
            listSolution.push(parseInt(currentElement))
            
        }
    })

    if (listSolution.length === 0){
        return -1
    }

    return Math.max.apply(null, listSolution)
};

console.log(findLucky([2,2,3,4]))

console.log(findLucky([1,2,2,3,3,3]))

console.log(findLucky([2,2,2,3,3]))


console.log(findLucky([7,7,7,7,7,7,7]))
