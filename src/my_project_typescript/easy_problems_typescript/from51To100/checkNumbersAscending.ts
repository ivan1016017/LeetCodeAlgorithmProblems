function areNumbersAscending(s: string): boolean {

    let listWords: Array<string> = s.split(" ")
    let listNumber: Array<number> = []
    function isNumeric(value: string){
        return /^-?\d+$/.test(value)
    }


    for (let word of listWords){
        if (isNumeric(word)){
            listNumber.push(parseInt(word))
        }
    }

    for (let i = 1; i < listNumber.length; i++){
        if (listNumber[i-1] >= listNumber[i]){
            return false
        }
    }

    
    return true 
};

console.log(areNumbersAscending( "1 box has 3 blue 4 red 6 green and 12 yellow marbles"))

console.log(areNumbersAscending("hello world 5 x 5"))

console.log(areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))

console.log(areNumbersAscending("4 5 11 26"))
