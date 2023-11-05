function canPermutePalindrome(s: string): boolean {


    let answer: {[key:number]:number} = {}

    for (let c of s){
        if (c  in answer){
            answer[c] += 1
        }
        else{
            answer[c] = 1
        }
    }

    let temp = 0
    for (let k in answer){
        temp += answer[k]%2
    }

    return temp === s.length%2
};