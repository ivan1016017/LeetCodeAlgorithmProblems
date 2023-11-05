function slowestKey(releaseTimes: number[], keysPressed: string): string {

    let lenReleaseTimes: number = releaseTimes.length
    releaseTimes = [0].concat(releaseTimes)
    let timeDuration: Array<number> = []
    let dicTimeDuration: any = {}
    let answer: Array<string> = []

    for (let i = 0; i < lenReleaseTimes; i++){
        dicTimeDuration[releaseTimes[i+1] - releaseTimes[i]] = []
    }

    for (let i = 0; i < lenReleaseTimes; i++){
        timeDuration.push(releaseTimes[i+1] - releaseTimes[i])
        dicTimeDuration[releaseTimes[i+1] - releaseTimes[i]].push(keysPressed[i])
    }

    let maxReleaseTime: number = Math.max.apply(null, timeDuration)

    answer = dicTimeDuration[maxReleaseTime]
    answer.sort((a, b) =>  -a.localeCompare(b))

    return answer[0]
};


console.log(slowestKey([9,29,49,50], "cbcd"))

console.log(slowestKey([12,23,36,46,62], "spuda"))

console.log(slowestKey([19,22,28,29,66,81,93,97] ,"fnfaaxha"))
