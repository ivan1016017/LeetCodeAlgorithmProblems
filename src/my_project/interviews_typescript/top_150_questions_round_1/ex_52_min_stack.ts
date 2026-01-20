class MinStack {

    private stack: number[]
    private minStack: number[]

    constructor() {
        this.stack = [];
        this.minStack = [];
        
    }

    push(val: number): void {
        this.stack.push(val)
        if (this.minStack.length === 0){
            this.minStack.push(val)
        }else{
            this.minStack.push(Math.min(val, this.minStack[this.minStack.length - 1]))
        }        
    }

    pop(): void {
        this.stack.pop()
        this.minStack.pop()
    }

    top(): number {
        return this.stack[this.stack.length - 1]
    }

    getMin(): number {
        return this.minStack[this.minStack.length - 1]
    }
}