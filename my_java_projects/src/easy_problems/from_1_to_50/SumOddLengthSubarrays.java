package easy_problems.from_1_to_50;

import java.lang.reflect.Array;

public class SumOddLengthSubarrays implements Numbers{
    public int sumOddLengthSubarrays(int[] arr) {

        int n = arr.length;
        int solution = 0;

        for (int i = 0; i < n; i++){
            solution += Math.floor(((i+1)*(n-i)+1)/2)*arr[i];

        }

        return solution;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of a class that returns numbers");
    }
}
