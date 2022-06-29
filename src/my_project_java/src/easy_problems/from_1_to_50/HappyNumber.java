package easy_problems.from_1_to_50;

import java.util.ArrayList;

public class HappyNumber implements Numbers {

    public HappyNumber() {
        System.out.println("This is a class that checks whether a number is happy or not");
    }

    private int getNext(int n){
        int totalSum = 0;
        int digit;
        while (n > 0){
            digit = n % 10;
            n = (int) n / 10;
            totalSum += Math.pow(digit,2);
        }
        return totalSum;
    }

    public boolean isHappy(int n) {

        ArrayList<Integer> seen = new ArrayList<Integer>();


        while (n != 0 && !seen.contains(n)){

            seen.add(n);
            n = this.getNext(n);

        }

        return n == 1;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This class does not return numbers. It returns booleans instead.");
    }
}
