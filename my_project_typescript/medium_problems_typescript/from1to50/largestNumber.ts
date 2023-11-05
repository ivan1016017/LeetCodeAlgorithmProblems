function largestNumber(nums: number[]): string {
    if(nums.length <= 1) return nums.toString();
    let sorted = nums.map(n => n.toString()).sort((a, b) => 
        (a+b > b+a)?-1:1 )

    if(sorted[0] === "0") return "0";
    
    return sorted.join("");
};