function squareIsWhite(coordinates: string): boolean {

    return (coordinates[0].charCodeAt(0) + coordinates[1].charCodeAt(0))%2 !==0
};


console.log(squareIsWhite("a1"))

console.log(squareIsWhite("h3"))

console.log(squareIsWhite("c7"))
