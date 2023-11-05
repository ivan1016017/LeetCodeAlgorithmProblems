function countVowelSubstrings(word: string): number {
    let temp: Array<string> = []
    let answer: number = 0
    let count: number = 0
    let lenWords: number = word.length

    let dictLetters: any = {"a":1, "b":-1,"c":-1, "d":-1,"e":1, "f":-1, "g":-1,
    "h":-1, "i":1,"j":-1, "k":-1,"l":-1, "m":-1,
    "n":-1, "o":1,"p":-1, "q":-1,"r":-1, "s":-1,
    "t":-1, "u":1,"v":-1, "w":-1,"x":-1, "y":-1, "z":-1}

    for (let i = 0; i < lenWords; i++){
        temp = []
        count = 0
        for (let j = i; j < lenWords; j++){
            if (!temp.includes(word[j])){
                if (dictLetters[word[j]] ==1 ){
                    temp.push(word[j])
                    count += 1
                    if (count === 5){
                        answer += 1
                    }
                }
                else{
                    break
                }
            }
            else{
                if (count == 5){
                    answer += 1
                }
            }
        }
    }

    return answer 

};


console.log(countVowelSubstrings("aeiouu"))

console.log(countVowelSubstrings("unicornarihan"))

console.log(countVowelSubstrings("cuaieuouac"))

console.log(countVowelSubstrings("bbaeixoubb"))

console.log(countVowelSubstrings("poazaeuioauoiioaouuouaui"))

