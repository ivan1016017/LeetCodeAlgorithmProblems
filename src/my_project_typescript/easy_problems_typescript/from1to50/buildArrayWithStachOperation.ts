function buildArray(target: number[], n: number): string[] {

    let answer: Array<string> = []

    for (let i = 0; i < target[target.length-1]; i++){
        if (target.includes(i+1)){
            answer.push("Push")
        }
        else {
            answer.push("Push")
            answer.push("Pop")
        }
    }

    return answer

};


console.log(buildArray([1,3],  3))

console.log(buildArray([1,2,3],  3))

console.log(buildArray([1,2], 4))


console.log(buildArray([2,3,4], 4))
