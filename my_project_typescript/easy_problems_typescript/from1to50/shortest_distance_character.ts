function shortestToChar(s: string, c: string): number[] {

    let indexTarget: Array<number> = [];
    let solution: Array<number> = [];
    let temp: any = null;
    let tempArray: Array<number> = [];

    function getArrayMin(array: Array<number>){
        return Math.min.apply(null, array);
     }

    for (let i = 0; i < s.length; i++){
        if (s[i] === c){
            indexTarget.push(i)
        }
    }
    
    for (let i = 0; i <  s.length; i++){
        tempArray = []
        for (let j of indexTarget) {
            tempArray.push(Math.abs(i-j))           
        }

        solution.push(getArrayMin(tempArray))
        
    }

    return solution;

};



console.log(shortestToChar( "loveleetcode", "e"))




