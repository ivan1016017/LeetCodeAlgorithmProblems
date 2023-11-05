function sortString(s: string): string {
    let vocabulary: string = "abcdefghijklmnopqrstuvwxyz"
    let dict_vocabulary: any = {}

    for (let letter of vocabulary){
        dict_vocabulary[letter] = 0
    }

    for (let i of s){
        dict_vocabulary[i] += 1
    }

    let answer: string = ""

    while (answer.length < s.length){

        for (let i = 0; i < vocabulary.length; i++){
            if (dict_vocabulary[vocabulary[i]] > 0){
                answer += vocabulary[i]
                dict_vocabulary[vocabulary[i]] -= 1
            }
        }

        for (let i = vocabulary.length-1; i > -1; i = i -1){
            if (dict_vocabulary[vocabulary[i]] > 0){
                answer += vocabulary[i]
                dict_vocabulary[vocabulary[i]] -= 1
            }
        }
    }

    return answer 
};

console.log(sortString( "aaaabbbbcccc"))

console.log(sortString( "rat"))

console.log(sortString( "leetcode"))

console.log(sortString("ggggggg"))
