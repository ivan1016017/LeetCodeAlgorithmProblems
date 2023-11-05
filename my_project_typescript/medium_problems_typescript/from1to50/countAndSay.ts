function countAndSay(n: number): string {
    if (n === 1 ){
        return "1"
    }

    let previous: string = '1'
    let response: string = ''
    let count: number
    for (let i = 1; i < n; i++){
        count = 1
        for (let j = 0; j < previous.length-1; j++){
            if (previous[j] === previous[j+1]){
                count += 1
            }
            else {
                response += String(count) + previous[j]
                count = 1
            }
        }
        response += String(count) + previous[previous.length-1]
        previous = response 
        response = ''

    }

    return previous
};

console.log(countAndSay(6))