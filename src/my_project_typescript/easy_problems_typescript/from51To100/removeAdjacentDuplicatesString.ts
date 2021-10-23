function removeDuplicates(s: string): string {
    let listSolution: Array<string> = []

    for (let letter of s){
        if (listSolution.length ==0){
            listSolution.push(letter)
        }
        else if(listSolution.length > 0 && listSolution[listSolution.length-1] !== letter){
            listSolution.push(letter)
        
        }
        else{
            listSolution.pop()
        }
    }
    return listSolution.join('')
};

console.log(removeDuplicates("abbaca"))

console.log(removeDuplicates("azxxzy"))


