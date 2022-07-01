package easy_problems.from_1_to_50;

public class SingleNumber implements Numbers{
    public SingleNumber() {
        System.out.println("This is the instance of the class SingleNumber");
    }

    public int singleNumber(int[] nums){
        int result = 0;
        for (int num: nums){
            result ^= num;
        }
        return result;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that returns the number that appears only one time in an array.");
    }
}
