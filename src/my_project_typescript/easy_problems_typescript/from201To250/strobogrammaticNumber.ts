function isStrobogrammatic(num: string): boolean {

    let characters: {[key:string]:string} = {'6':'9', '8':'8', '9':'6', '1':'1', '0':'0'}

    let char180 = ''

    for (let s of num){
        if (!(s in characters)){
            return false 
        }
        else{
            char180 += characters[s]
        }
    }

    return [...char180].reverse().join("") === num

};