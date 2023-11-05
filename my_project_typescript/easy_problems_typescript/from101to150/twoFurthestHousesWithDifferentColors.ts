function maxDistance(colors: number[]): number {
    let max: number = -1
    let lenColors: number = colors.length

    for (let i = 0; i < lenColors; i++){
        for (let j = i+1; j < lenColors; j++){
            if (Math.abs(colors[i]-colors[j]) !== 0){
                if (j-i > max){
                    max = j-i
                }
            }
        }
    }
    return max     
};

console.log(maxDistance([1,1,1,6,1,1,1]))

console.log(maxDistance([1,8,3,8,3]))

console.log(maxDistance([0,1]))
