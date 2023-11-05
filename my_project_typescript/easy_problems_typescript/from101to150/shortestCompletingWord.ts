function shortestCompletingWord(licensePlate: string, words: string[]): string {

    words = words.reverse()
    words = words.sort( (a,b) => a.length <= b.length ? -1 : 1)

    let stringFiltered = ""
    licensePlate = licensePlate.toLocaleLowerCase()
    let exists: boolean = true

    for (let i = 0; i < licensePlate.length; i++){
        if (licensePlate[i].charCodeAt(0) >= 97 && licensePlate[i].charCodeAt(0) <= 122){
            stringFiltered += licensePlate[i]
        }
    }

   

    function countValues(string1: string, string2: string): number {
        let count:number  = 0
        for (let word of string2){
            if (word == string1){
                count += 1
            }
        }
        return count 
    }

    for (let word of words){
        exists = true 
        for (let char of stringFiltered){
            if(!word.includes(char)){
                exists = false
                break
            }
            else {
                if (countValues(char, word) < countValues(char, stringFiltered)){
                    exists = false 
                    break 
                }
            }

        }
        if (exists){
            return word
        }
    }

    return ""
};

console.log(shortestCompletingWord("1s3 PSt",  ["step","steps","stripe","stepple"]))

console.log(shortestCompletingWord("1s3 456", ["looks","pest","stew","show"]))

console.log(shortestCompletingWord( "Ah71752",  ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]))

console.log(shortestCompletingWord( "OgEu755",  ["enough","these","play","wide","wonder","box","arrive","money","tax","thus"]))



let a = 'sd'

let b = 'sdfhendn'

let count = (b.match(/`${a}`/g) || []).length

console.log(count)