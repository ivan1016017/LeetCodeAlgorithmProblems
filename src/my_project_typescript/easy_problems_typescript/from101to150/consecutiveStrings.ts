function maxPower(s: string): number {

    // initialize variables
    let lenS: number = s.length
    let maxNumber: number = 0
    let count: number = 0

    // compute the maximum length of the substring with only one character
    for (let i = 0; i < lenS; i++){
        count = 1
        for (let j = i+1; j < lenS; j++){
            if (s[i] === s[j]){
                count += 1
            }
            else {
                break
            }
        }
        if (count > maxNumber){
            maxNumber = count 
        }
    }

    return maxNumber 

};

console.log(maxPower("leetcode"))

console.log(maxPower("abbcccddddeeeeedcba"))

console.log(maxPower("triplepillooooow"))

console.log(maxPower("hooraaaaaaaaaaay"))

console.log(maxPower("tourist"))
