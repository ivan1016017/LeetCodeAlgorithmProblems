function calPoints(ops: string[]): number {


    let solution: Array<number> = [];
    let count: number = 0

    for (let item of ops){
        if (item === "C"){
            solution.pop()
        }
        else if (item === "D"){
            solution.push(solution[solution.length-1]*2)
        }
        else if (item === "+"){
            solution.push(solution[solution.length-1] + solution[solution.length-2])
        }
        else {
            solution.push(parseInt(item))
        }
    }

    solution.map( (currentElement) => {
        count += currentElement
        return count
    })


    return count
};


console.log(calPoints(["5","2","C","D","+"]))