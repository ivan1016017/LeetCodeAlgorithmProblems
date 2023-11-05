function fizzBuzz(n: number): string[] {
    let solution: Array<string> = []
    for (let i = 1; i <= n; i++){
        solution.push(i.toString())
    }

    for (let i = 0; i < n; i++){
        if ((i+1)%3 === 0 && (i+1)%5 ===0){
            solution[i] = "FizzBuzz"
        }
        else if ( (i+1)%3 === 0){
            solution[i] = "Fizz"
        }
        else if ( (i+1)%5 === 0){
            solution[i] = "Buzz"
        }
    }
    return solution
};

console.log(fizzBuzz(3))

console.log(fizzBuzz(5))

console.log(fizzBuzz(15))
