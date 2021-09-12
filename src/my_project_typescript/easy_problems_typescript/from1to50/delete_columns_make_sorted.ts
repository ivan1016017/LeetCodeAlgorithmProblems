function minDeletionSize(strs: string[]): number {

    let temp: string = "";
    let tempList: Array<string> = []
    let tempListOrdered: Array<string> = []
    let tempOrdered: any = null 
    let solution: number = 0
    let listOrdered: Array<string>= []

    for (let i = 0; i < strs[0].length; i++){
        for (let word of strs){
            temp += word[i]
        }
        tempList.push(temp)
        temp = ""  
    }
    
    for (let word of tempList){
        temp = ""
        tempListOrdered = []
        for (let letter of word){
            tempListOrdered.push(letter)
        }
        tempListOrdered.sort((x,y) => x <= y ? -1 : 1)
        for (let letter of tempListOrdered){
            temp += letter
        }
        listOrdered.push(temp)
    }

    for (let i = 0; i < listOrdered.length; i++){
        if (listOrdered[i] !== tempList[i]){
            solution +=1
        }
    }  
    return solution
};

console.log(minDeletionSize(["a","d","g"]))


