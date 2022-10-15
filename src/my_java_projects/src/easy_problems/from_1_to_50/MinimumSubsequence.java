package easy_problems.from_1_to_50;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;

public class MinimumSubsequence implements  Numbers{

        public ArrayList<Integer> minSubsequence(int[] nums) {

            int lenNums = nums.length;
            int index = 0;
            Arrays.sort(nums);

            System.out.println(Arrays.toString(nums));
            ArrayList<Integer> solution  = new ArrayList<>();

            while (index < lenNums) {
                if (sum(nums,0, lenNums - 1 - index) < sum(nums, lenNums - 1 - index, lenNums)){
                    solution.add(nums[lenNums - 1 - index]);
                    break;
                }else{
                    solution.add(nums[lenNums - 1 - index]);
                    index += 1;
                }

            }

        return solution;


        }

        private int sum(int[] nums, int startIndex, int endIndex){

            int solution = 0;

            for (int i = startIndex; i < endIndex; i++){
                solution += nums[i];
            }

            return solution;
        }


        public ArrayList<Integer> minSubsequenceTwo(int[] nums) {
            int sum = 0, currSum = 0;
            ArrayList<Integer> list = new ArrayList<>();
            int[] count = new int[101];

            for(int num : nums){
                sum += num;
                count[num]++;
            }

            int i=100;
            while(currSum <= sum){
                while(i>1 && count[i]==0){
                    i--;
                }
                if(i>=1){
                    currSum += i;
                    sum -= i;
                    count[i]--;
                    list.add(i);
                }
            }

            return list;
        }

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of the class that does not return numbers");
    }
}

