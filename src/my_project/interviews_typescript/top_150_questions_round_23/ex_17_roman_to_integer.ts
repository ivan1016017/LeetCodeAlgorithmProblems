function romanToInt(s: string): number {

    let roman_to_int_obj: {[key:string]:number} = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    let lenS: number = s.length
    let solution: number = roman_to_int_obj[s[lenS-1]]

    for (let i = 0; i < lenS-1;i++){
        if (roman_to_int_obj[s[lenS-2-i]] < roman_to_int_obj[s[lenS-1-i]]) {
            solution -= roman_to_int_obj[s[lenS-2-i]]
        }
        else{
            solution += roman_to_int_obj[s[lenS-2-i]]
        }
    }

    return solution;

};