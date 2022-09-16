package easy_problems.from_1_to_50;

import java.util.HashMap;

public class sumUniqueElements implements Numbers{
    public int sumOfUnique(int[] nums) {

        HashMap<Integer,Integer> solutionHashMap = new HashMap<>();
        int solution = 0;
        for (int i: nums){
            if (!solutionHashMap.containsKey(i)){
                solutionHashMap.put(i,1);
            } else {
                solutionHashMap.put(i, solutionHashMap.get(i) + 1);
            }
        }

        for (int i: solutionHashMap.keySet()){
            if (solutionHashMap.get(i) == 1){
                solution += i;
            }
        }

        return solution;

    }

    public int sumOfUniqueTwo(int[] nums) {
        int sum = 0;
        int map[] = new int[101];
        for (int num : nums) {
            if (map[num] == 0) {
                sum += num;
            } else if (map[num] == 1) {
                sum -= num;
            }
            map[num] += 1;
        }

        return sum;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that return integers");
    }
}
