function searchRange(nums: number[], target: number): number[] {

    let lenNums: number = nums.length

    function first(nums: Array<number>, target: number): number {

        let low: number = 0
        let high: number = lenNums -1
        let answer: number = -1
        let mid: number = 0

        while(low <= high) {
            mid = Math.floor((low + high)/2)
            if (nums[mid] > target){
                high = mid -1
            }
            else if (nums[mid] < target){
                low = mid + 1
            }
            else {
                answer = mid 
                high = mid - 1
            }
        }
        return answer
    }

    function second(nums: Array<number>, target: number): number {

        let low: number = 0
        let high: number = lenNums -1
        let answer: number = -1
        let mid: number = 0

        while(low <= high) {
            mid = Math.floor((low + high)/2)
            if (nums[mid] > target){
                high = mid -1
            }
            else if (nums[mid] < target){
                low = mid + 1
            }
            else {
                answer = mid 
                low = mid + 1
            }
        }
        return answer
    }
    return [first(nums, target), second(nums, target)]
};