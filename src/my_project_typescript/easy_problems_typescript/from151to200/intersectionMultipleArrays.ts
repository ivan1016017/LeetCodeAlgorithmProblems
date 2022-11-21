function intersection(nums: number[][]): number[] {
    
    if (nums.length === 1) return nums[0].sort((a,b) => a-b)

    let initSet = new Set(nums[0]) // Initialize set 

    for (let i = 1; i < nums.length; i++){
        initSet = new Set(nums[i].filter(x => initSet.has(x)))
    }

    return Array.from(initSet).sort((a,b) => a-b)

};

function intersectionTwo(nums: number[][]): number[] {
    
    if (nums.length === 1) {     // if length is 1, returns the only array inside sorted
        return (nums[0]).sort((n1, n2) => n1 - n2);
    } else {   // otherwise
        
        let intersection = nums[0];    // create a new array with the first element of nums array

        for (let i = 0; i < nums.length; i++) {     // loop through all elements of the array
          if (nums[i + 1] !== undefined) {        // if the next element exists
            intersection = intersection.filter(element => (nums[i + 1]).includes(element));    // find the intersections
          }
        }

        return intersection.sort((n1, n2) => n1 - n2);   // returns the sorted intersection array
    }

};