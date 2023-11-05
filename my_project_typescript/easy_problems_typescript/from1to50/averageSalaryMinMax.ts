function average(salary: number[]): number {

    let maxNumber: number = Math.max.apply(null, salary);
    let minNumber: number = Math.min.apply(null, salary);


    salary = salary.sort((a,b) => a<=b?-1:1)

    let totalSum: number = 0;

    for (let i = 1; i < salary.length-1; i++){
        totalSum += salary[i]
    }
    
    return totalSum/(salary.length-2)
};


console.log(average([6000,5000,4000,3000,2000,1000]))