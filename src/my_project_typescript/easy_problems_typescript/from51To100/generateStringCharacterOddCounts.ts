function generateTheString(n: number): string {

    let firstLetter: string = 'a'
    let secondLetter: string = 'b'
    let answer: string = ''
    if (n%2 == 0){
        answer = firstLetter.repeat(n-1) + secondLetter
    }
    else {
        answer = firstLetter.repeat(n)
    }

    return answer 
};


console.log(generateTheString(4))

console.log(generateTheString(2))

console.log(generateTheString(7))
