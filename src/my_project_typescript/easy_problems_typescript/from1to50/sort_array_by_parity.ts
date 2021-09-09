function sortArrayByParityII(nums: number[]): number[] {
    let count: number = 0;

    let solution: Array<number> = [];

    while (nums.length > 0){
        
        for (let item of nums){

            if (item % 2 === 0 && count % 2 ===0){
                var itemIndex = nums.indexOf(item);
                solution.push(item)
                nums.splice(itemIndex, 1)
                break
            }
            if (item % 2 !== 0 && count % 2 !==0){
                var itemIndex = nums.indexOf(item);
                solution.push(item)
                nums.splice(itemIndex, 1)
                break
            }
        }
        count += 1

    }

    return solution


};

console.log(sortArrayByParityII( [4,2,5,7]))
console.log([4,2,5,7].indexOf(7))

// class Solution:
// def sortArrayByParityII(self, nums: List[int]) -> List[int]:

//     count: int = 0
//     solution: list[int] = list()

//     while len(nums) > 0:

//         for item in nums:
//             if item % 2 == 0 and count % 2 == 0:
//                 nums.remove(item)
//                 solution.append(item)
//                 break
//             if item % 2 != 0 and count % 2 != 0:
//                 nums.remove(item)
//                 solution.append(item)
//                 break 
//         count += 1
        
        

//     return solution 