function groupAnagrams(strs: string[]): string[][] {



    let dicitonarySolution: {[key:string]: Array<string>} = {}

    for (let word of strs){
        dicitonarySolution[word.split('').sort().join('')] = []
    }

    for (let word of strs){
        dicitonarySolution[word.split('').sort().join('')].push(word)
    }

    let solution: Array<Array<string>> = []

    for (let value in dicitonarySolution){
        solution.push(dicitonarySolution[value])
    }

    return solution

};


let sample: Array<string> = ['c','b','a']
let sampleTwo: Array<string> = sample.sort()
let a: string = 'dcba'
console.log(a.split(''))

console.log(sampleTwo)

console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))