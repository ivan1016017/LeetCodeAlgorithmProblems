function exist(board: string[][], word: string): boolean {

    for (let i = 0; i < board.length; i++){
        for (let j = 0; j < board[0].length; j++){
            if (backtracking(i,j,board,word)){
                return true 
            }
        }
    }
    
    return false
};


function backtracking(i:number,j:number,board:string[][],word:string):boolean{

    if (word.length === 0){
        return true
    }
    if (i < 0 || i >= board.length || j < 0 || j >= board[0].length){
        return false 
    }
    if (board[i][j]===word[0]){
        board[i][j]="*"
        if (backtracking(i-1,j,board,word.slice(1)) || backtracking(i+1,j,board,word.slice(1)) || backtracking(i,j-1,board,word.slice(1)) || backtracking(i,j+1,board,word.slice(1))){
            return true
        }
        board[i][j]=word[0]
    }

    return false 
}