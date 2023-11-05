package easy_problems.from_1_to_50;

public class ValidPalindrome implements Numbers{
    public ValidPalindrome() {
        System.out.println("This is an instance of the class ValidPalindrome.");
    }

    @Override
    public void returnNumbers() {
        System.out.println("The instance of this class does not return any number");
    }

    public boolean isPalindrome(String s) {

        s=s.toLowerCase().replaceAll("[^a-z0-9]", "");
        return new StringBuilder(s).reverse().toString().equals(s);

    }
}
