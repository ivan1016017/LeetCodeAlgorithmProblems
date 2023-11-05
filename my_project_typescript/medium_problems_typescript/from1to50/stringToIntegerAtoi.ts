function myAtoi(s: string): number {
    let MIN: number = -(2**31)
    let MAX: number = (2**31) -1 
    let n: number = 0
    let empty: boolean = true 
    let sign: number = 1 

    for (let i = 0; i < s.length; i++){
        
        
        if (empty){
            if (s[i] === ' '){
                continue 
            }
            else if (s[i] === '-'){
                

                sign = -1
            }
            else if (Number(s[i])){
                
                n = Number(s[i])
            }
            else if (s[i] !== '+'){
                return 0
            }
            empty = false
        }
        else {
            if (Number(s[i])){
                n = n*10 + Number(s[i])
                if (sign*n> MAX){
                    return MAX
                }
                else if (sign*n < MIN){
                    return MIN
                }
            }
            else{
                break
            }
        }
    }

    return sign * n

};

console.log(myAtoi('  -42'))

// let a:string = 'a'

// if (Number(a)){
//     console.log("it works")
// }
// else{
//     console.log("it works for non number")
// }

// console.log('  -42'[4])