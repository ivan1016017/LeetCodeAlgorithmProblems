function countCharacters(words: string[], chars: string): number {

    let flag: boolean = false;
    let listSolutionStrings: number = 0
    let dictWord: any 
    let dictChars: any 

    function fromStringsToDict(word: string): any{
        
        let tempDict: any = {}

        for (let letter of word){
            tempDict[letter] = 0
        }

        for (let letter of word){
            tempDict[letter] += 1
        }

        return tempDict
    }

    for (let word of words){
        flag = false;
        dictWord = fromStringsToDict(word)
        dictChars = fromStringsToDict(chars)

        for (let letter of word){

            if (!chars.includes(letter)){
                flag = true 
                break 
            }
            else{
                if (dictWord[letter] > dictChars[letter]){
                    flag = true 
                    break
                }
            }
        }
        if (flag == false){
            listSolutionStrings += word.length
        }
    }



    return listSolutionStrings

};

console.log(countCharacters( ["cat","bt","hat","tree"], "atach"))

console.log(countCharacters( ["hello","world","leetcode"], "welldonehoneyr"))


// function fromStringsToDict(word: string): any{
        
//     let tempDict: any = {}

//     for (let letter of word){
//         tempDict[letter] = 0
//     }

//     for (let letter of word){
//         tempDict[letter] += 1
//     }

//     return tempDict
// }


// console.log(fromStringsToDict("aabc"))