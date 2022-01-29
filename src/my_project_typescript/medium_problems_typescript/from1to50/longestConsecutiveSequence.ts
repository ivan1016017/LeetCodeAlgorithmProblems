function longestConsecutive(nums: number[]): number {  
 
    const numSet = new Set<number>(nums);
    let maxSeqCount = 0;
    
    for(let num of numSet.values()) { 
        if(!numSet.has(num - 1)) {
            let curSeqCount = 1, curSeqNum = num;
            while(numSet.has(++curSeqNum)) curSeqCount++;
            
            maxSeqCount = Math.max(maxSeqCount, curSeqCount);
        }
    }
    
    return maxSeqCount;
};