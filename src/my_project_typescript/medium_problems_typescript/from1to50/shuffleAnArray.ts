class Solution {
    arr: Array<number> = []
    nums: Array<number> = []
    constructor(nums: number[]) {
        this.nums = nums
        this.arr = Object.assign([],nums)
    }

    reset(): number[] {
        
        return this.arr

    }

    shuffle(): number[] {
        let ans: Array<number> = this.nums
        this.shuffleArray(ans)
        return ans

    }

    shuffleArray(array: Array<number>):void {
        for (let i = array.length - 1; i > 0; i--) {
            let j = Math.floor(Math.random() * (i + 1));
            let temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }
}