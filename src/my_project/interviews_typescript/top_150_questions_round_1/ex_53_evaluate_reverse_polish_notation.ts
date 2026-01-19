function evalRPN(tokens: string[]): number {
    const stack: number[] = [];
    const operators: string[] = ['+', '-', '*', '/'];
    
    for (const token of tokens) {
        if (operators.includes(token)) {
            // Pop two operands (note: order matters for - and /)
            const b = stack.pop()!;
            const a = stack.pop()!;
            
            // Apply operation
            let result: number;
            if (token === '+') {
                result = a + b;
            } else if (token === '-') {
                result = a - b;
            } else if (token === '*') {
                result = a * b;
            } else { // token === '/'
                // Truncate toward zero
                result = Math.trunc(a / b);
            }
            
            stack.push(result);
        } else {
            // It's a number, push to stack
            stack.push(parseInt(token));
        }
    }
    
    // Final result is the only element left in stack
    return stack[0];
}