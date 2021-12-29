function findAnagrams(s: string, p: string): number[] {

    function areEqualArrays(arr1: Array<number>, arr2:Array<number>): boolean{
        let answer: boolean = true 
        let lenArr1: number = arr1.length
        let lenArr2: number = arr2.length

        if (lenArr1 !== lenArr2){
            answer = false 
            return answer 
        }
        else {
            for (let i = 0; i < lenArr1; i++){
                if (arr1[i] !== arr2[i]){
                    answer = false 
                    return answer 
                }
            }
        }

        return answer
    }
    let answer: Array<number> = []

    let pCounter: Array<number> = new Array<number>(26).fill(0)

    let sCounter: Array<number> = new Array<number>(26).fill(0)

    let lenP: number = p.length
    let lenS: number = s.length

    for (let letter of p){
        pCounter[letter.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
    }

    for (let letter of s.slice(0,lenP-1)){
        sCounter[letter.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
    }

    console.log(sCounter)
    console.log(pCounter)

    for (let i = lenP -1; i < lenS; i++){
        sCounter[s[i].charCodeAt(0) - 'a'.charCodeAt(0)] += 1

        if (areEqualArrays(sCounter, pCounter)){
            answer.push(i-lenP + 1)
        }

        sCounter[s[i-lenP+1].charCodeAt(0) - 'a'.charCodeAt(0)] -= 1
    }


    return answer



};

console.log(findAnagrams("cbaebabacd","abc"))