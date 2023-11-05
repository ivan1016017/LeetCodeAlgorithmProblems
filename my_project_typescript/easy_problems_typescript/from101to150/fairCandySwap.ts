function fairCandySwap(aliceSizes: number[], bobSizes: number[]): number[] {

    let sumOne: number = aliceSizes.reduce((a,b) => a+b,0)
    let sumTwo: number = bobSizes.reduce((a,b) => a+b,0)
    let gap: number = 0
    if (sumOne > sumTwo){
        gap = Math.floor((sumOne-sumTwo)/2)
        for (let i = 0; i < aliceSizes.length;i++){
            if (bobSizes.includes( aliceSizes[i] - gap)){
                return [aliceSizes[i],aliceSizes[i]-gap]
            }
        }
    }
    else {
        gap = Math.floor((sumTwo-sumOne)/2)
        for (let i = 0; i < bobSizes.length;i++){
            if (aliceSizes.includes( bobSizes[i] - gap)){
                return [ bobSizes[i]-gap, bobSizes[i]]
            }
        }
    }
    return []
};


console.log(fairCandySwap([1,1], [2,2]))

console.log(fairCandySwap([1,2],  [2,3]))

console.log(fairCandySwap([2], [1,3]))

console.log(fairCandySwap([1,2,5], [2,4]))


