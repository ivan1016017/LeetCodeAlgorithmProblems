function maxLengthBetweenEqualCharacters(s: string): number {

    let collection: {[key:string]: number[]} = {}
    let lenS: number =  s.length

    let count: number = 0
    for (let i = 0; i < lenS; i++ ){
        collection[s[i]] = []
    }



    for (let i = 0; i < lenS; i++ ){
        collection[s[i]].push(count)
        count += 1
    }

    

    let maxCount: number = -1

    for (let element in collection){
        
        if (collection[element][collection[element].length -1] - collection[element][0] > maxCount){
            maxCount = collection[element][collection[element].length -1] - collection[element][0]
        }
      
    }

    if (maxCount == -1){
        return maxCount
    }
    else{
        return maxCount -1
    }
};

console.log(maxLengthBetweenEqualCharacters("aa"))

console.log(maxLengthBetweenEqualCharacters("abca"))

console.log(maxLengthBetweenEqualCharacters("cbzxy"))

console.log(maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv"))

