function destCity(paths: string[][]): string {
    let originList: Array<string> = []
    let destinationList: Array<string> = []


    paths.map( currentElement => {
        originList.push(currentElement[0])
    })

    paths.map(city => {
        if (!originList.includes(city[1])){
            destinationList.push(city[1])
        }
    })

    return destinationList[0]
};

console.log(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))

console.log(destCity([["B","C"],["D","B"],["C","A"]]))

console.log(destCity([["A","Z"]]))
