function letterCombinations(digits: string): string[] {
    if (!digits || digits.length === 0) {
        return [];
    }
    
    // Mapping of digits to letters
    const phoneMap: { [key: string]: string } = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    };
    
    const result: string[] = [];
    
    function backtrack(index: number, current: string): void {
        // Base case: if we've processed all digits
        if (index === digits.length) {
            result.push(current);
            return;
        }
        
        // Get the letters for the current digit
        const letters = phoneMap[digits[index]];
        
        // Try each letter and recurse
        for (const letter of letters) {
            backtrack(index + 1, current + letter);
        }
    }
    
    backtrack(0, "");
    return result;
};