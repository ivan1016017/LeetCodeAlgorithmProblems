function removePalindromeSub(s: string): number {

    let outputString: string = ''

    for (let word of s){
        outputString = word + outputString
    }
    console.log(outputString)
    if (s === outputString){
        return 1
    }
    else {
        return 2
    }
};

console.log(removePalindromeSub('abcd'))