function findMaximizedCapital(k: number, w: number, profits: number[], capital: number[]): number {
    // Pair projects as [capital, profit] and sort by capital requirement
    const projects: [number, number][] = profits.map((p, i) => [capital[i], p]);
    projects.sort((a, b) => a[0] - b[0]);

    // Max-heap of profits for affordable projects (using a simple sorted insert)
    const maxHeap: number[] = [];
    let idx = 0;

    const heapPush = (val: number) => {
        maxHeap.push(val);
        let i = maxHeap.length - 1;
        while (i > 0) {
            const parent = (i - 1) >> 1;
            if (maxHeap[parent] < maxHeap[i]) {
                [maxHeap[parent], maxHeap[i]] = [maxHeap[i], maxHeap[parent]];
                i = parent;
            } else break;
        }
    };

    const heapPop = (): number => {
        const top = maxHeap[0];
        const last = maxHeap.pop()!;
        if (maxHeap.length > 0) {
            maxHeap[0] = last;
            let i = 0;
            while (true) {
                const left = 2 * i + 1;
                const right = 2 * i + 2;
                let largest = i;
                if (left < maxHeap.length && maxHeap[left] > maxHeap[largest]) largest = left;
                if (right < maxHeap.length && maxHeap[right] > maxHeap[largest]) largest = right;
                if (largest === i) break;
                [maxHeap[i], maxHeap[largest]] = [maxHeap[largest], maxHeap[i]];
                i = largest;
            }
        }
        return top;
    };

    for (let i = 0; i < k; i++) {
        // Push all newly affordable projects into the max-heap
        while (idx < projects.length && projects[idx][0] <= w) {
            heapPush(projects[idx][1]);
            idx++;
        }
        if (maxHeap.length === 0) break;
        w += heapPop();
    }

    return w;
}
