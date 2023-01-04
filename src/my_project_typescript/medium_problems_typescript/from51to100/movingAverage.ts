class MovingAverage {
    size: number;
    buffer: number[];
    sum: number;
    pointer: number;

    constructor(size: number) {
        this.size = size;
        this.buffer = []
        this.sum = 0;
        this.pointer = 0


    }

    next(val: number): number {
        this.buffer.push(val);
        this.sum += val;
        
        if (this.buffer.length - this.pointer > this.size) {
            this.sum -= this.buffer[this.pointer]
            this.pointer += 1
        }         
        
        return this.sum/(this.buffer.length - this.pointer)

    }
}