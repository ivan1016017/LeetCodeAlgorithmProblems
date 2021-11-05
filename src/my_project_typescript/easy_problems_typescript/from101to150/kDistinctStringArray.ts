function kthDistinct(arr: string[], k: number): string {
    let countDict: any = {}
    let lenArr: number = arr.length
    let count: number = 0

    for (let i = 0; i< lenArr; i++){
        countDict[arr[i]] = 0
    }

    for (let i = 0; i< lenArr; i++){
        countDict[arr[i]] += 1
    }

    for (let i in countDict){
        
        if (countDict[i] == 1){
            count += 1
            if (count === k){
                return i 
            }
            
        }
    }
    return ""
};


console.log(kthDistinct(["d","b","c","b","c","a"],  2))

console.log(kthDistinct(["aaa","aa","a"],  1))

console.log(kthDistinct(["a","b","a"],  3))


