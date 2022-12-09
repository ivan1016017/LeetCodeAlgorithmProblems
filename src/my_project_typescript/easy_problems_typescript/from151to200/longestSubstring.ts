function lengthOfLongestSubstring(s: string): number {

    let objSolution: {[key:string]: number} = {}
    let maxLength: number = 0
    let start: number = 0

    for (let i = 0; i < s.length; i++){
        if (s[i] in objSolution && start <= objSolution[s[i]]){
            start = objSolution[s[i]] + 1
        }
        else {
            maxLength = Math.max(maxLength, i-start+1)
        }

        objSolution[s[i]] = i
    }

    

    return maxLength;

};