function lengthOfLastWord(s: string): number {

    s = s.trim()
    let temp: number = 0
    for (let i  = 0; i < s.length; i++){
        if (s[i] ===  " "){
            temp = 0
            continue
        }
        temp += 1
    }

    return temp 

};