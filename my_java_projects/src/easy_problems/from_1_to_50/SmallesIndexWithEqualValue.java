package easy_problems.from_1_to_50;

public class SmallesIndexWithEqualValue {
    public int smallestEqual(int[] nums) {

        for (int i = 0; i < nums.length;i++){
            if (i % 10 == nums[i]) return i;
        }

        return -1;

    }
}
