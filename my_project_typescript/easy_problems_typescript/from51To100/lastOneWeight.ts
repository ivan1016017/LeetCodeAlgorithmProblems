function lastStoneWeight(stones: number[]): number {

    function maxValue(data: Array<number>): number{
        return data.splice(data.indexOf(Math.max.apply(null, data)),1)[0]
    }
    let value: number = 0

    while (stones.length > 1){
        value = Math.abs(maxValue(stones) - maxValue(stones))
        if (value){
            stones.push(value)
        }
    }

    if (stones.length > 0){
        return stones[0] 
    }
    else {
        return 0
    }
};



console.log(lastStoneWeight([2,7,4,1,8,1]))

console.log(lastStoneWeight([1]))

console.log(lastStoneWeight([1,1]))

