/**
 * Min heap for storing larger half of numbers
 */
class LargeHalf {
    private heap: number[] = [];

    push(val: number): void {
        this.heap.push(val);
        this.bubbleUp(this.heap.length - 1);
    }

    pop(): number {
        if (this.heap.length === 0) return 0;
        if (this.heap.length === 1) return this.heap.pop()!;
        
        const top = this.heap[0];
        this.heap[0] = this.heap.pop()!;
        this.bubbleDown(0);
        return top;
    }

    peek(): number {
        return this.heap[0] || 0;
    }

    size(): number {
        return this.heap.length;
    }

    private bubbleUp(idx: number): void {
        while (idx > 0) {
            const parentIdx = Math.floor((idx - 1) / 2);
            if (this.heap[idx] >= this.heap[parentIdx]) break;
            [this.heap[idx], this.heap[parentIdx]] = [this.heap[parentIdx], this.heap[idx]];
            idx = parentIdx;
        }
    }

    private bubbleDown(idx: number): void {
        while (true) {
            const leftIdx = 2 * idx + 1;
            const rightIdx = 2 * idx + 2;
            let smallest = idx;

            if (leftIdx < this.heap.length && this.heap[leftIdx] < this.heap[smallest]) {
                smallest = leftIdx;
            }
            if (rightIdx < this.heap.length && this.heap[rightIdx] < this.heap[smallest]) {
                smallest = rightIdx;
            }

            if (smallest === idx) break;
            [this.heap[idx], this.heap[smallest]] = [this.heap[smallest], this.heap[idx]];
            idx = smallest;
        }
    }
}

/**
 * Max heap for storing smaller half of numbers
 */
class SmallHalf {
    private heap: number[] = [];

    push(val: number): void {
        this.heap.push(val);
        this.bubbleUp(this.heap.length - 1);
    }

    pop(): number {
        if (this.heap.length === 0) return 0;
        if (this.heap.length === 1) return this.heap.pop()!;
        
        const top = this.heap[0];
        this.heap[0] = this.heap.pop()!;
        this.bubbleDown(0);
        return top;
    }

    peek(): number {
        return this.heap[0] || 0;
    }

    size(): number {
        return this.heap.length;
    }

    private bubbleUp(idx: number): void {
        while (idx > 0) {
            const parentIdx = Math.floor((idx - 1) / 2);
            if (this.heap[idx] <= this.heap[parentIdx]) break;
            [this.heap[idx], this.heap[parentIdx]] = [this.heap[parentIdx], this.heap[idx]];
            idx = parentIdx;
        }
    }

    private bubbleDown(idx: number): void {
        while (true) {
            const leftIdx = 2 * idx + 1;
            const rightIdx = 2 * idx + 2;
            let largest = idx;

            if (leftIdx < this.heap.length && this.heap[leftIdx] > this.heap[largest]) {
                largest = leftIdx;
            }
            if (rightIdx < this.heap.length && this.heap[rightIdx] > this.heap[largest]) {
                largest = rightIdx;
            }

            if (largest === idx) break;
            [this.heap[idx], this.heap[largest]] = [this.heap[largest], this.heap[idx]];
            idx = largest;
        }
    }
}

/**
 * Find median from data stream using two heaps:
 * - maxHeap: stores the smaller half
 * - minHeap: stores the larger half
 * 
 * Invariants:
 * 1. maxHeap size >= minHeap size
 * 2. maxHeap size - minHeap size <= 1
 * 3. All elements in maxHeap <= all elements in minHeap
 */
class MedianFinder {
    private maxHeap: SmallHalf; // smaller half
    private minHeap: LargeHalf; // larger half

    constructor() {
        this.maxHeap = new SmallHalf();
        this.minHeap = new LargeHalf();
    }

    addNum(num: number): void {
        // Always add to maxHeap first
        this.maxHeap.push(num);
        
        // Move the largest from maxHeap to minHeap
        this.minHeap.push(this.maxHeap.pop());
        
        // Balance: maxHeap should have same or 1 more element than minHeap
        if (this.maxHeap.size() < this.minHeap.size()) {
            this.maxHeap.push(this.minHeap.pop());
        }
    }

    findMedian(): number {
        if (this.maxHeap.size() > this.minHeap.size()) {
            return this.maxHeap.peek();
        }
        return (this.maxHeap.peek() + this.minHeap.peek()) / 2.0;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */