package easy_problems.from_1_to_50;

import com.mysql.cj.util.StringUtils;

import java.util.ArrayList;
import java.util.Arrays;

public class BaseballGame implements Numbers{
    public int calPoints(String[] operations) {
        int sum = 0;
        int[] arr = new int[operations.length];
        int index = -1;
        for (String s : operations) {
            System.out.println(Arrays.toString(arr));
            switch (s.charAt(0)) {
                case 'C': sum -= arr[index--]; break;
                case 'D': sum += arr[index] * 2; arr[++index] = arr[index - 1] * 2; break;
                case '+': sum += arr[index] + arr[index - 1]; arr[++index] = arr[index - 1] + arr[index - 2]; break;
                default: int n = Integer.parseInt(s); sum += n; arr[++index] = n;
            }
        }
        return sum;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of a class that returns numbers");
    }
}
