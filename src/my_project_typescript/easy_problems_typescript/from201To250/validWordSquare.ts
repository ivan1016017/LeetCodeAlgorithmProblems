function validWordSquare(words: string[]): boolean {

    for (let i = 0; i < words.length; i++) {
        for (let j = 0; j < words[i].length; j++) {
            let c1 = words[i][j];
            if (j >= words.length || i >= words[j].length) return false;
            let c2 = words[j][i];
            if (c1 != c2) return false;
        }
    }
    
    return true;
};