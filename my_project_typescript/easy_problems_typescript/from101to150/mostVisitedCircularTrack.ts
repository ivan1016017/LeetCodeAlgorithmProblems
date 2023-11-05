function mostVisited(n: number, rounds: number[]): number[] {

    let lenRounds: number = rounds.length
    if (rounds[0] === rounds[lenRounds-1]){
        return [rounds[0]]
    }

    let answer: Array<number> = []

    if (rounds[0] < rounds[lenRounds-1]){
        for (let i = rounds[0]; i < rounds[lenRounds-1] + 1; i++){
            answer.push(i)
        }
    }
    else{
        for (let i = rounds[0]; i < rounds[lenRounds-1]+1+n; i++){
            if (i == n){
                answer.push(i)
            }
            else{
                answer.push(i%n)
            }
        }
    }
    

    return answer.sort((a,b) => a<=b?-1:1)
};