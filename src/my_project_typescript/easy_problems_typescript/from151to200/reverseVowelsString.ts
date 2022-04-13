function reverseVowels(s: string): string {

    let ind_vec: Array<number> = []
    let vowels: Array<string> = ['a','e','i','o','u','A','E','I','O','U']

    for (let i = 0; i < s.length; i++){
        if (vowels.includes(s[i])){
            ind_vec.push(i)
        }
    }

    let N: number = ind_vec.length

    let s_copy: Array<string> = []

    for (let letter of s){
        s_copy.push(letter)
    }

    for (let i = 0; i < ind_vec.length; i++){
        s_copy[ind_vec[i]] = s[ind_vec[N-1-i]]
    }

    return s_copy.join('')
};