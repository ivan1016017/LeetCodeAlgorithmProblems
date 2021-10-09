function subsetXORSum(nums: number[]): number {

    function xor_sum(subset:Array<any>, nums: Array<any>): number{
        let xor: number = 0
        if (nums.length == 0){
            xor = 0
            for (let i of subset){
                xor = xor ^ i 
            }
            return xor 
        }
        else {
            return xor_sum(subset.concat([nums[0]]), nums.slice(1)) + xor_sum(subset, nums.slice(1))
        }
    }
    return xor_sum([],nums)

};

console.log(subsetXORSum([5,1,6]))