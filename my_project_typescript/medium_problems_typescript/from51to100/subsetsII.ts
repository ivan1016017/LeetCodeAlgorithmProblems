function subsetsWithDup(nums: number[]): number[][] {
    // Sort nums to make creating all subsets easier
    const sortedNums = [...nums].sort();
    // Contains all subsets
    let results: number[][] = [[], [sortedNums[0]]];
    /* 
      Contains the current iteration's subsets that will
      be added to results
    */
    let currBatch: number[][] = [[sortedNums[0]]];
  
    /*
      Logic: when we encounter a new number, create the current
      batch of subsets by adding the new number to all the subsets.
      Otherwise, create the current batch of subsets by adding
      the duplicate number to the previous batch of subsets.
      The current batch of subsets is then added to all the subsets.
  
      The following illustrates the logic:
  
      [1, 4, 4, 6]
      results = [[]]
      -----------------------------------------------------------
      currNum = 1
      currBatch = [[1]]
      results = [[], [1]]
      -----------------------------------------------------------
      currNum = 4
      currBatch = [[4], [1,4]]
      results = [[], [1], [4], [1,4]]
      -----------------------------------------------------------
      currNum = 4
      currBatch = [[4,4], [1,4,4]]
      results = [[], [1], [4], [1,4], [4,4], [1,4,4]]
      -----------------------------------------------------------
      currNum = 6
      currBatch = [[6], [1,6], [4,6], [1,4,6], [4,4,6], [1,4,4,6]]
      results = [[], [1], [4], [1,4], [4,4], [1,4,4], [6], [1,6], 
                  [4,6], [1,4,6], [4,4,6], [1,4,4,6]]
    */
    for (let i = 1; i < nums.length; i++) {
      const subsets = sortedNums[i] === sortedNums[i - 1] ? currBatch : results;
      currBatch = subsets.map((subset) => [sortedNums[i], ...subset]);
      results = results.concat(currBatch);
    }
  
    return results;
  }
