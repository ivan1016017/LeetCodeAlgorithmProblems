function judgeCircle(moves: string): boolean {

    let coordinatePosition: any = {'L':-1, 'R':1,'U':1,'D':-1}

    let finalPosition: Array<number> = [0,0]

    for (let move of moves){
        if (move == 'L' || move == 'R'){
            finalPosition[0] += coordinatePosition[move]
        }
        else {
            finalPosition[1] += coordinatePosition[move]

        }
    }

    return finalPosition[0] === 0 && finalPosition[1] == 0

};

console.log(judgeCircle("UD"))

console.log(judgeCircle("LL"))

console.log(judgeCircle("RRDD"))

console.log(judgeCircle( "LDRRLRUULR"))
