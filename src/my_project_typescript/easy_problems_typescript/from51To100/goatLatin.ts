function toGoatLatin(sentence: string): string {

    let vowels: Array<string> = ['a','e','i','o','u', 'A','E','I','O','U']
    let listVowels: Array<string> = sentence.split(' ')

    for (let i = 0; i < listVowels.length; i++){
        if (vowels.includes(listVowels[i][0])){
            listVowels[i] += 'ma' + 'a'.repeat(i+1)
        }
        else {
            listVowels[i] = listVowels[i].slice(1) + listVowels[i][0] + 'ma' + 'a'.repeat(i+1)
        }
    }

    return listVowels.join(' ')

};


console.log(toGoatLatin("I speak Goat Latin"))