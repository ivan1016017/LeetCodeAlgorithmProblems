function calculate(s: string): number {
    const stack: number[] = [];
    let result = 0;
    let currentNum = 0;
    let sign = 1;  // 1 for positive, -1 for negative
    
    for (const char of s) {
        if (char >= '0' && char <= '9') {
            // Build multi-digit number
            currentNum = currentNum * 10 + parseInt(char);
        } else if (char === '+') {
            // Add previous number with its sign
            result += sign * currentNum;
            currentNum = 0;
            sign = 1;
        } else if (char === '-') {
            // Add previous number with its sign
            result += sign * currentNum;
            currentNum = 0;
            sign = -1;
        } else if (char === '(') {
            // Save current result and sign to stack
            stack.push(result);
            stack.push(sign);
            // Reset for new sub-expression
            result = 0;
            sign = 1;
        } else if (char === ')') {
            // Complete current number
            result += sign * currentNum;
            currentNum = 0;
            // Pop sign and previous result from stack
            result *= stack.pop()!;  // Apply sign before parenthesis
            result += stack.pop()!;  // Add previous result
        }
        // Skip spaces
    }
    
    // Add the last number
    result += sign * currentNum;
    
    return result;
}