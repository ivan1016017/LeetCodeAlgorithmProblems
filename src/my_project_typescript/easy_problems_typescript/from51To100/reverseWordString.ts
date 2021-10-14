function reverseWords(s: string): string {

    let tempList: Array<string> = []
    let tempWord: string = ""
    for (let word of s.split(' ')){
        tempWord = ""
        for (let letter of word){
            tempWord = letter + tempWord
        }
        tempList.push(tempWord)
    }
    
    return tempList.join(' ')
};


console.log(reverseWords("Let's take LeetCode contest"))