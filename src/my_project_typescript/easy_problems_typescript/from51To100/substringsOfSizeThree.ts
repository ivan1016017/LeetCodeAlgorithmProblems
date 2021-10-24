function countGoodSubstrings(s: string): number {

    let count: number = 0
    let tempString: string = ''
    let tempList: Array<string> = []
    for (let i = 2; i < s.length; i++){
        tempString = s.slice(i-2,i+1)
        // console.log(tempString)
        tempList = []
        for (let j of tempString){
            if (!tempList.includes(j)){
                tempList.push(j)
            }
        }
        if (tempList.length === 3){
            count += 1
        }
    }
    return count 

};


console.log(countGoodSubstrings("xyzzaz"))

console.log(countGoodSubstrings("aababcabc"))
