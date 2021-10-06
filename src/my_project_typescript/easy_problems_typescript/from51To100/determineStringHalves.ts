function halvesAreAlike(s: string): boolean {
    let leftS: string = s.slice(0, Math.floor(s.length /2))
    let rightS: string = s.slice(Math.floor(s.length /2))
    let countLeft: number = 0
    let countRight: number = 0

    let vowels: Array<string> =  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for (let i = 0; i < Math.floor(s.length /2); i++){
        if (vowels.includes(leftS[i])){
            countLeft += 1
        }
        if (vowels.includes(rightS[i])){
            countRight += 1
        }
    }
    if (countLeft !== countRight){
        return false 
    }
    else{
        return true 
    }
    

};


console.log(halvesAreAlike( "book"))

console.log(halvesAreAlike("textbook"))

console.log(halvesAreAlike("MerryChristmas"))

console.log(halvesAreAlike("AbCdEfGh"))
