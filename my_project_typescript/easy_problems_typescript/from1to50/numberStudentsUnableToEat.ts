function countStudents(students: number[], sandwiches: number[]): number {

    let tempFirstItem: number = 0;

    while (students.includes(sandwiches[0])){

        if (students[0] === sandwiches[0]){
            students.shift();
            sandwiches.shift();
            let isEqualArray = students.every((val, index) => val === sandwiches[index])
            if (isEqualArray && students.length  === sandwiches.length){
                return 0
            }
        }
        else {
            tempFirstItem = students[0]
            students = students.slice(1).concat(tempFirstItem)

        }
    }

    return students.length

};

console.log(countStudents( [1,1,0,0], [0,1,0,1]))
console.log(countStudents( [1,1,1,0,0,1], [1,0,0,0,1,1]))


let sampleOne = [1,2,3]
let sampleTwo = [1,2,3,3]

console.log(sampleOne == sampleTwo)
console.log(sampleOne.every((val,index) => val == sampleTwo[index]))
console.log(sampleOne.concat(sampleTwo))