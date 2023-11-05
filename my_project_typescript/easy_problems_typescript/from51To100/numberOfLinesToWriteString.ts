function numberOfLines(widths: number[], s: string): number[] {

    let count: number = 0
    let numberLines: number = 1 
    for (let letter of s){
        if (count + widths[letter.charCodeAt(0)%97] <= 100){
            count += widths[letter.charCodeAt(0)%97]
        }
        else {
            count = widths[letter.charCodeAt(0)%97]
            numberLines += 1
        }
    }

    let result: Array<number> = [numberLines, count]
    return result 

};


console.log(numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz"))

console.log(numberOfLines( [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],  "bbbcccdddaaa"))
