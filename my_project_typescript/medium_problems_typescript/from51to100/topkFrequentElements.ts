// Space O(n)
function topKFrequent(nums: number[], k: number): number[] {
    const freq = new Map<number, number>();
    const buckets = new Array<number[]>(nums.length + 1);
    
    // Construct buckets
    for(let i = 0; i < buckets.length; i++) { 
        buckets[i] = [];
    }
    
    // Count frequencies
    for(let num of nums) {
        if(!freq.has(num)) {
            freq.set(num, 1);
        } else {
            freq.set(num, freq.get(num) + 1);
        }
    }
    
    // Fill buckets
    for(let [num, count] of freq.entries()) {
        buckets[count].push(num);
    }
    
    // Flat buckets
    const flat = buckets.flat();
    
    // Return last k elements of flattened array
    return flat.slice(flat.length - k);
}