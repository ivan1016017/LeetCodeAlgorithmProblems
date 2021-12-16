function reformat(s: string): string {

    function isAlpha(x: string):boolean{
        let isUppercase: boolean = x.charCodeAt(0) >= 65 && x.charCodeAt(0) <= 90
        let isLowercase: boolean = x.charCodeAt(0) >= 97 && x.charCodeAt(0) <= 122
        return isUppercase || isLowercase
    }

    function isNumeric(x: string):boolean{
        let isNumeric: boolean = x.charCodeAt(0) >= 48 && x.charCodeAt(0) <= 57
        
        return isNumeric
    }

    let s1: string = ''
    let s2: string = ''
    for (let i = 0 ; i < s.length; i++){
        if (isNumeric(s[i])){
            s2+= s[i]
        }
        else{
            s1+=s[i]
        }
    }

    if (Math.abs(s1.length - s2.length) > 1){
        return ''
    }

    let temp1: string = ''
    let temp2: string = ''

    if (s1.length < s2.length){
        temp1 = s1 
        temp2 = s2 
        s1 = temp2
        s2 = temp1
    }

    let answer: string = ''
    for (let i = 0; i < s2.length; i++){
        answer +=s1[i] + s2[i]
    }

    if (s1.length > s2.length){
        answer += s1[s1.length-1]
    }
    

    return answer 
};


console.log(reformat("a0b1c2"))