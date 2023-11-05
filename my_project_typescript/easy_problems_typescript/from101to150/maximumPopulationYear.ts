function maximumPopulation(logs: number[][]): number {
    let firstYearList: Array<number> = []
    let lenLogs: number = logs.length
    let maxNumber: number = -1

    for (let i = 0; i < lenLogs; i++){
        if (!firstYearList.includes(logs[i][0])){
            firstYearList.push(logs[i][0])
        }
    }

    firstYearList = firstYearList.sort((a,b) => a<=b?-1:1)
    lenLogs = firstYearList.length

    let dictMaxRecords: any = {}

    for (let i = 0; i < lenLogs; i++){
        dictMaxRecords[firstYearList[i]] = 0
    }

    for (let i = 0; i < lenLogs; i++){
        for (let interval of logs){
            if (firstYearList[i] >= interval[0] && firstYearList[i] < interval[1]){
                dictMaxRecords[firstYearList[i]] += 1
            }
        }
    }

    let answer = firstYearList[0]

    for (let i = 0; i <lenLogs; i++){
        if (dictMaxRecords[firstYearList[i]]> maxNumber){
            maxNumber = dictMaxRecords[firstYearList[i]]
            answer = firstYearList[i]
        }
    }

    return answer 

};


console.log(maximumPopulation([[1993,1999],[2000,2010]]))

console.log(maximumPopulation([[1950,1961],[1960,1971],[1970,1981]]))

console.log(maximumPopulation([[1966,1968],[1954,2030],[1966,1994],[2030,2044],[1988,2036],[1977,2050],[2036,2046],[1989,2048],[2049,2050],[2008,2019],[2022,2031],[1970,2024],[1957,1996],[1991,2034],[1956,1996],[1959,1969],[2021,2050]]))
