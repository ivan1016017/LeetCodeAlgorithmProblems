function numRookCaptures(board: string[][]): number {



    let coordinateRook: Array<number> = [];
    let numberPawns: number = 0;
    
    for (let i = 0; i< 8; i++){
        for (let j = 0; j<8; j++){
            if (board[i][j]=="R"){
                coordinateRook = [i,j]
            }
        }
    }

    let flag = false;
    for (let i = coordinateRook[0] -1; i > -1; i--){
        if (board[i][coordinateRook[1]] !== "." && board[i][coordinateRook[1]] !== "p"){
            flag = true
        }
        if (flag == false && board[i][coordinateRook[1]] == "p"){
            numberPawns += 1
            flag = true
        }
    }

    flag = false;
    for (let i = coordinateRook[0] +1; i < 8; i++){
        if (board[i][coordinateRook[1]] !== "." && board[i][coordinateRook[1]] !== "p"){
            flag = true
        }
        if (flag == false && board[i][coordinateRook[1]] == "p"){
            numberPawns += 1
            flag = true
        }
    }

    flag = false;
    for (let j = coordinateRook[1] -1; j > -1; j--){
        if (board[coordinateRook[0]][j] !== "." && board[coordinateRook[0]][j] !== "p"){
            flag = true
        }
        if (flag == false && board[coordinateRook[0]][j] == "p"){
            numberPawns += 1
            flag = true
        }
    }

    flag = false;
    for (let j = coordinateRook[1] +1; j < 8; j++){
        if (board[coordinateRook[0]][j] !== "." && board[coordinateRook[0]][j] !== "p"){
            flag = true
        }
        if (flag == false && board[coordinateRook[0]][j] == "p"){
            numberPawns += 1
            flag = true
        }
    }


    return numberPawns
};

console.log(numRookCaptures([[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
console.log(numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))