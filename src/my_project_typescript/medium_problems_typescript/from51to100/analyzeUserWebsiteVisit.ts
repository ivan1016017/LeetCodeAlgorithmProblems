function getPatternsRec(websites: string[], index: number, patterns: string[][]): string[] {
    if(index > websites.length - 1) {
        const ansPattens = patterns.filter(pattern => pattern.length === 3)
        const stringifyPatterns = ansPattens.map(pattern => JSON.stringify(pattern))
        const patternsSet = new Set(stringifyPatterns)
        return Array.from(patternsSet);
    }
    const website = websites[index]
    const patternsToAdd:any = []
    patterns.forEach(pattern => {
        if(pattern.length < 3) {
            patternsToAdd.push([...pattern].concat(website))
        }
    })

    patterns = patterns.concat(patternsToAdd)
    patterns.push([website])
    patterns.push([])

    return getPatternsRec(websites, index + 1, patterns)
}


function getPatterns(websites: string[]): string[] {
    return getPatternsRec(websites, 0, [])
}

function buildUserMap(username: string[], timestamp: number[], website: string[]): Map<string, string[]> {
    const userMap = new Map<string, string[]>()
    const combineArray:any = []
    for (let i=0;i<username.length;i++) {
        combineArray.push([username[i], timestamp[i], website[i]])
    }

    combineArray.sort((record1, record2) => record1[0] - record2[0])
    combineArray.sort((record1, record2) => record1[1] - record2[1])
    const arr = combineArray.map(record => {return {user: record[0], site: record[2]}})

    for(const item of arr) {
        userMap.set(item.user, (userMap.get(item.user) || []).concat(item.site))
    }

    return userMap
}

function mostVisitedPattern(username: string[], timestamp: number[], website: string[]): string[] {
    const userMap: Map<string, string[]> = buildUserMap(username, timestamp, website)
    userMap.forEach((value, key) => {
        // @ts-ignore
        userMap.set(key, getPatterns(value))
    })

    const patternsMap: Map<string, number> = new Map<string, number>()
    userMap.forEach((patterns, key) => {
        for(const pattern of patterns) {
            patternsMap.set(pattern, (patternsMap.get(pattern) || 0) + 1)
        }
    })

    let maxCount = 0
    patternsMap.forEach((count, _) => {
        if(count > maxCount) maxCount = count
    })

    const ans: string[] = []

    patternsMap.forEach((count, pattern) => {
        if(count === maxCount) ans.push(pattern)
    })

    ans.sort((pattern1, pattern2) => pattern1 < pattern2 ? -1 : 1)

    return JSON.parse(ans[0])
};

