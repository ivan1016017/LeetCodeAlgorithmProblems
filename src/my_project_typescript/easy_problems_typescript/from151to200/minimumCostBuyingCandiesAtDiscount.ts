function minimumCost(cost: number[]): number {

    let lenCost: number = cost.length
    let answer: number = 0
    cost.sort((a,b) => a<=b?-1:1)

    for (let i=0; i < lenCost; i++){

        if ((lenCost-i)%3){
            answer+=cost[i]
        }
    }

    return answer
};