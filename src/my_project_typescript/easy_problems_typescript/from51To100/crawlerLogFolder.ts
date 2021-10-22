function minOperations(logs: string[]): number {

    let count: number = 0
    logs.map( currentElement =>{
        if (currentElement === "./"){
            count += 0
        }
        else if (currentElement === "../"){
            if (count === 0){
                count = 0
            }
            else {
                count -= 1
            }
        }
        else {
            count += 1
        }
    })
    return count 
};

console.log(minOperations(["d1/","d2/","../","d21/","./"]))

console.log(minOperations(["d1/","d2/","./","d3/","../","d31/"]))

console.log(minOperations(["d1/","../","../","../"]))

console.log(minOperations(["./","wz4/","../","mj2/","../","../","ik0/","il7/"]))
