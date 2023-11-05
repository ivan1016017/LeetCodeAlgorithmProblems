function reformatDate(date: string): string {

    let tempList = date.split(" ")
    let months: Array<string> = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    let tempDict: any = {}

    for (let i = 0; i < 12; i++){
        tempDict[months[i]] = i+1
    }

    function padLeadingZeros(num:number, size:number): string {
        let s = num.toString() +"";
        while (s.length < size) s = "0" + s;
        return s;
    }


    let answer: string = ""
    let day: string = tempList[0]
    let month: string = tempList[1]
    let year: string = tempList[2]
    
    

    answer = year + "-" + padLeadingZeros(tempDict[month],2) + "-"+  padLeadingZeros(parseInt(day.slice(0,day.length-2)),2)

    return answer 


};


console.log(reformatDate("20th Oct 2052"))

console.log(reformatDate("6th Jun 1933"))

console.log(reformatDate("26th May 1960"))
