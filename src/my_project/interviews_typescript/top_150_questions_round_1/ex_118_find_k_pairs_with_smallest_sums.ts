function kSmallestPairs(nums1: number[], nums2: number[], k: number): number[][] {
    const result: number[][] = [];
    const heap: [number, number, number][] = []; // [sum, i, j]

    const heapPush = (item: [number, number, number]) => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const parent = (i - 1) >> 1;
            if (heap[i][0] < heap[parent][0]) {
                [heap[i], heap[parent]] = [heap[parent], heap[i]];
                i = parent;
            } else break;
        }
    };

    const heapPop = (): [number, number, number] | undefined => {
        if (heap.length === 0) return undefined;
        const top = heap[0];
        const last = heap.pop()!;
        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;
            while (true) {
                const left = 2 * i + 1;
                const right = 2 * i + 2;
                let smallest = i;
                if (left < heap.length && heap[left][0] < heap[smallest][0]) smallest = left;
                if (right < heap.length && heap[right][0] < heap[smallest][0]) smallest = right;
                if (smallest === i) break;
                [heap[i], heap[smallest]] = [heap[smallest], heap[i]];
                i = smallest;
            }
        }
        return top;
    };

    // Initialize heap with first element of nums1 paired with first element of nums2
    for (let i = 0; i < Math.min(k, nums1.length); i++) {
        heapPush([nums1[i] + nums2[0], i, 0]);
    }

    while (heap.length > 0 && result.length < k) {
        const item = heapPop();
        if (!item) break;
        const [_, i, j] = item;
        result.push([nums1[i], nums2[j]]);
        
        if (j + 1 < nums2.length) {
            heapPush([nums1[i] + nums2[j + 1], i, j + 1]);
        }
    }

    return result;
}