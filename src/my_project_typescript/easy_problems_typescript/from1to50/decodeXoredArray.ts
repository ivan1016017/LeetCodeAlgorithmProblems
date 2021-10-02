function decode(encoded: number[], first: number): number[] {

    let output: Array<number> = []
    output.push(first)
    let n: number = encoded.length
    let xor: number = -1
    for (let i = 0; i < n; i++){
        xor = output[i] ^ encoded[i]
        output.push(xor)
    }
    return output 

};


console.log(decode( [1,2,3],  1))


console.log(decode([6,2,7,3], 4))
