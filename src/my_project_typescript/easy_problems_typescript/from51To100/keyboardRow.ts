function findWords(words: string[]): string[] {
    let firstRow: Array<string> = ["q", "w", "e", "r", "t","y","u","i","o","p"]
    let secondRow: Array<string> = ["a", "s", "d", "f", "g","h","j","k","l"]
    let thirdRow: Array<string> = ["z", "x", "c", "v", "b","n","m"]
    let flagFirstRow: boolean = false 
    let flagSecondRow: boolean = false 
    let flagThirdRow: boolean = false 
    let toLowercaseList: Array<string> = []
    let answer: Array<string> = []

    for (let i = 0; i < words.length; i++){
        toLowercaseList.push(words[i].toLowerCase())
    }

    for (let i = 0; i < words.length; i++){
        flagFirstRow = false 
        flagSecondRow = false 
        flagThirdRow = false 

        for (let letter of toLowercaseList[i]){
            if (!firstRow.includes(letter)){
                flagFirstRow = true 
                break
            }
        }

        if (flagFirstRow === false){
            answer.push(words[i])
            continue 
        }

        for (let letter of toLowercaseList[i]){
            if (!secondRow.includes(letter)){
                flagSecondRow = true 
                break
            }
        }

        if (flagSecondRow === false){
            answer.push(words[i])
            continue 
        }

        for (let letter of toLowercaseList[i]){
            if (!thirdRow.includes(letter)){
                flagThirdRow = true 
                break
            }
        }

        if (flagThirdRow === false){
            answer.push(words[i])
            continue 
        }



    }


    return answer
};


console.log(findWords(["Hello","Alaska","Dad","Peace"]))

console.log(findWords(["omk"]))

console.log(findWords(["adsdf","sfd"]))

