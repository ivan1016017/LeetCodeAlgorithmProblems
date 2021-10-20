function minMovesToSeat(seats: number[], students: number[]): number {

    let answer: number = 0
    seats.sort((x,y) => x<=y?-1:1)
    students.sort((x,y) => x<=y?-1:1)
    let lenSeats: number = seats.length

    for (let i = 0; i < lenSeats; i++){
        answer += Math.abs(seats[i] - students[i])
    }

    return answer 
};


console.log(minMovesToSeat([3,1,5],  [2,7,4]))

console.log(minMovesToSeat([4,1,5,9],  [1,3,2,6]))

console.log(minMovesToSeat([2,2,6,6],  [1,3,2,6]))


// funciton to be removed

function newFunction(num: number){
    return num*7
}
