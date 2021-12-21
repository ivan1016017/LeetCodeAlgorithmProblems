function countPoints(rings: string): number {

    let objectAnswer:  {[key:string]: Array<string>} = {}

    let numbers: string = '0123456789'


    for (let i = 0; i < 10; i++){
        objectAnswer[numbers[i]] = []
    }

    for (let i = 0; i < rings.length; i = i + 2){
        if (!objectAnswer[rings[i+1]].includes(rings[i])){
            objectAnswer[rings[i+1]].push(rings[i])
        }
    }

    let answer: number = 0

    for (let i = 0; i < 10; i++){
        if (objectAnswer[numbers[i]].length === 3){
            answer += 1
        }
    }

    return answer

};