function lengthOfLastWord(s: string): number {
    // define length of the string
    s = s.trim();
    
    let stringLength: number = s.length;

    // initialize solution 
    let solution: number = 0;
    if (stringLength ===0){
        return 0;
    } else {
        stringLength = s.split(" ")[s.split(" ").length -1 ].length
        solution = stringLength
        return solution
    }
};


console.log(lengthOfLastWord("Hello World"));
console.log(lengthOfLastWord(" Hello"));
