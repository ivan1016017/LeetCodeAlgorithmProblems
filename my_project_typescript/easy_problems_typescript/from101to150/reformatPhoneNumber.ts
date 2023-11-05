function reformatNumber(number: string): string {

    let reOne = / /gi
    let reTwo = /-/gi
    let temp: string = number.replace(reOne, "") 
    temp = temp.replace(reTwo, '')

    let answer: Array<string> = []
    let count: number = 0

    while (count < temp.length) {
        if (temp.length - count == 4){
            answer.push(temp.slice(count, count+2))
            answer.push(temp.slice(count+2, count+4))
            break
        }
        if (temp.length - count == 3){
            answer.push(temp.slice(count, count+3))
            break
        }
        if (temp.length - count == 2){
            answer.push(temp.slice(count, count+2))
            break
        }
        answer.push(temp.slice(count, count+3))
        count += 3
    }

    return answer.join('-')
};

console.log(reformatNumber("1-23-45 6"))

console.log(reformatNumber("123 4-567"))

console.log(reformatNumber("123 4-5678"))

console.log(reformatNumber("12"))

console.log(reformatNumber("--17-5 229 35-39475 "))