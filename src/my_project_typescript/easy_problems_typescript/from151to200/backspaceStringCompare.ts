function backspaceCompare(s: string, t: string): boolean {

    function returnString(s: string) : string{
        let newString: string = ''
        
        for (let letter of s){
            if (letter === '#'){
                newString = newString.slice(0,newString.length -1)
            }
            else{
                newString += letter
            }
        }
        return newString
    }

    

    return returnString(s) === returnString(t)

};

let sample = 'abcd'
console.log(sample.slice(0,sample.length-1))