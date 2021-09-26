function numJewelsInStones(jewels: string, stones: string): number {
    let count: number = 0
    for (let letter of stones){
        if (jewels.includes(letter)){
            count += 1
        }
    }
    return count 
};

console.log(numJewelsInStones("aA", "aAAbbbb"))

