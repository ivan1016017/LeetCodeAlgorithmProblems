function rangeBitwiseAnd(left: number, right: number): number {

    let p: number = 0
    while (left !== right){
        left >>= 1
        right >>= 1
        p += 1
    }
        
    return left << p

};