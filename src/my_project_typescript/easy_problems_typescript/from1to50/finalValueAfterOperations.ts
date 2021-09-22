function finalValueAfterOperations(operations: string[]): number {

    let count: number = 0

    for (let item of operations){

        if (item === "X++" || item === "++X" ){
            count += 1
        }
        else {
            count -= 1
        }
    }

    return count

};



console.log(finalValueAfterOperations(["++X","++X","X++"]))