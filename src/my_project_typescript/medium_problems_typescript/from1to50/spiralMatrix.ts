function spiralOrder(matrix: number[][]): number[] {


    if (!matrix || !matrix[0]){
        return []
    }

    let ans: Array<number> = []
    let m: number = matrix.length
    let n: number = matrix[0].length
    let u: number = 0
    let d: number = m-1
    let l: number = 0
    let r: number = n-1

    const range = (start:number, end:number) => Array.from({length: (end - start)}, (v, k) => k + start);    

    
    while (l < r && u < d){
        
        ans = ans.concat(range(l,r).map(j => matrix[u][j]))
        ans = ans.concat(range(u,d).map(i => matrix[i][r]))
        ans = ans.concat(range(l+1,r+1).reverse().map(j => matrix[d][j]))
        ans = ans.concat(range(u+1,d+1).reverse().map(i => matrix[i][l]))
        
        u = u+1
        d = d-1
        l = l+1
        r = r-1
    }

    if (l == r){
        ans = ans.concat(range(u,d+1).map(i => matrix[i][r]))
    }
    else if (u == d){
        ans = ans.concat(range(l,r+1).map(j => matrix[u][j]))
    }

    return ans

};

console.log(spiralOrder( [[1,2,3],[4,5,6],[7,8,9]]))