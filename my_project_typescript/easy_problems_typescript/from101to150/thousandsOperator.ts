function thousandSeparator(n: number): string {
    let tempString: string = n.toString()
    tempString = tempString.split("").reverse().join("")

    let lenNumber: number = tempString.length
    let tempList: Array<string> = []
    
    for (let i = 0; i < lenNumber; i = i + 3){
        tempList.push(tempString.slice(i, i+3))
    }

    let answer: string = tempList.join(".")

    

    return answer.split("").reverse().join("")
};

console.log(thousandSeparator(987))

console.log(thousandSeparator(1234))

console.log(thousandSeparator(123456789))

console.log(thousandSeparator(0))
