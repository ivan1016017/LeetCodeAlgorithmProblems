function validWordAbbreviation(word: string, abbr: string): boolean {

    let i: number = 0, j: number = 0
    let n: number = word.length, m: number = abbr.length

    while (i < n && j < m){
        if (word[i] === abbr[j]){
            i += 1
            j += 1
            
            continue 
        }

        if (!isNumeric(abbr[j]) || abbr[j] === '0'){
            return false
        }

        let start: number = j 

        while ( j < m && isNumeric(abbr[j])){
            j += 1
        }

        let num: number  = parseInt(abbr.slice(start,j))
        i += num 
    }



    return i === n && j === m 

};

function isNumeric(value: string){
    return /^-?\d+$/.test(value)
}