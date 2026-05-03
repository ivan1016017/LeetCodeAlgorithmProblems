function majorityElement(nums: number[]): number {
    const dicAnswer: Map<number, number> = new Map();
    const lenNums = nums.length;

    for (let i = 0; i < lenNums; i++) {
        dicAnswer.set(nums[i], (dicAnswer.get(nums[i]) ?? 0) + 1);

        if (dicAnswer.get(nums[i])! > Math.floor(lenNums / 2)) {
            return nums[i];
        }
    }

    return -1;
};