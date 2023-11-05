package easy_problems.from_1_to_50;

public class PalindromeNumber implements Numbers{
    public PalindromeNumber() {
        System.out.println("An instance of the class Palindrome was built.");
    }

    public boolean isPalindrome(int x) {

        int sum = 0, target = x;

        while (x > 0){

            int temp = x % 10;
            x /= 10;
            sum = sum*10 + temp;
        }

        System.out.println(x);
        System.out.println(target);
        System.out.println(sum);


        return sum == target;
    }

    @Override
    public void returnNumbers(){
        System.out.println("This is a class that returns numbers");
    }
}
