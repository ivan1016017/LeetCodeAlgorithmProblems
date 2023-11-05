function longestNiceSubstring(s: string): string {

    function checkNice(s: string): boolean{
        
        let dictAnswer: any = {}
        let answer: boolean = true
        let lenS: number = s.length

        for (let i = 0; i <lenS; i++){
            dictAnswer[s[i]] = 0
            if (s[i].charCodeAt(0) <= 90 && s[i].charCodeAt(0)>= 65) {
                dictAnswer[String.fromCharCode(s[i].charCodeAt(0)+ 32 ) ] = 0
            }
            else {
                dictAnswer[String.fromCharCode(s[i].charCodeAt(0) - 32) ] = 0
            }
        }

        for (let i = 0; i < lenS; i++){
            dictAnswer[s[i]] += 1
        }

        for (let i = 0; i < lenS; i++){
            if (s[i].charCodeAt(0) <= 90 && s[i].charCodeAt(0)>= 65) {
                 if (dictAnswer[String.fromCharCode(s[i].charCodeAt(0)+ 32 ) ] == 0){
                     answer = false 
                     return answer 
                 }
            }
            else {
                if (dictAnswer[String.fromCharCode(s[i].charCodeAt(0) - 32) ] == 0){
                    answer = false 
                    return answer 
                }
            }
        }
        return answer 
    }

    let lenS: number = s.length
    let max: number = -1
    let answer: string = ''

    for (let i = 0; i < lenS; i++){
        for (let j = 0; j < lenS; j++){
            if (checkNice(s.slice(i, j+1)) && ((j - i + 1) > max)){
                answer = s.slice(i, j+1)
                max  = j - i + 1
            }
        }
    }

    return answer
};

console.log(longestNiceSubstring("YazaAay"))

console.log(longestNiceSubstring("Bb"))

console.log(longestNiceSubstring("c"))

console.log(longestNiceSubstring("dDzeE"))

