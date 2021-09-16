function commonChars(words: string[]): string[] {

    let firstWord: string = words[0]
    let solution: Array<string> = []

    for (let word of words.slice(1)){
        for (let letter of firstWord) {
            if (word.includes(letter)){
                word = word.replace(letter,"")
            }
            else {
                firstWord = firstWord.replace(letter, "")
            }
        }
    }
    console.log(firstWord)
    for (let letter of firstWord){
        solution.push(letter)
    }

    return solution


};

let sample = "abca"
let newSample = sample.replace("a", "")

console.log(newSample)
newSample = newSample.replace("a","")
console.log(newSample)
console.log(commonChars(["cool","lock","cook"]))
