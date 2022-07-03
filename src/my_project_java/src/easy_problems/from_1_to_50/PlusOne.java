package easy_problems.from_1_to_50;

public class PlusOne implements Numbers{

    public PlusOne() {
        System.out.println("This is a class that returns plus one operation represented in an array");
    }

    public int[] plusOne(int[] digits){
        int n = digits.length;

        for (int i = n-1; i>=0; i--){
            if (digits[i] < 9){
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        int[] newNumber = new int[n+1];
        newNumber[0] = 1;

        return newNumber;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This class returns arrays instead of numbers.");
    }
}
