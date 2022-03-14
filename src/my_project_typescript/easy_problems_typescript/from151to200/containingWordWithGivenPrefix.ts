function prefixCount(words: string[], pref: string): number {

    let count: number = 0

    let lenPref: number = pref.length

    for (let word of words){
        if (word.slice(0,lenPref) === pref){
            count += 1
        }
    }

    return count
};