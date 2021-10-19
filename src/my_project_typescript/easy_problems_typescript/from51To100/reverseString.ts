function reverseString(s: string[]): void {

    let lenS: number = s.length
    let tempLeft: string
    let tempRight: string
    for (let i = 0; i < Math.floor(lenS/2); i++){
        tempLeft = s[i]
        tempRight = s[lenS-1-i]
        s[i] = tempRight
        s[lenS-1-i] = tempLeft
    }
    

};


reverseString(["h","e","l","l","o"])

reverseString(["H","a","n","n","a","h"])


