package easy_problems.from_1_to_50;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MinimumAbsoluteDifference {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {

        List<List<Integer>> answer = new ArrayList<>();

        Arrays.sort(arr);

        int min = Integer.MAX_VALUE;

        for (int i = 0; i < arr.length -1; i++){
            int diff = arr[i+1] - arr[i];
            if (diff < min){
                min = diff;
                answer.clear();
                answer.add(Arrays.asList(arr[i],arr[i+1]));

            }
            else if (diff == min){
                answer.add(Arrays.asList(arr[i],arr[i+1]));
            }
        }

        return answer;


    }
}
