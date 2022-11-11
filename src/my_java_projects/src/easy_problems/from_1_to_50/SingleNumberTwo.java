package easy_problems.from_1_to_50;

public class SingleNumberTwo implements Numbers{

    public int singleNumber(int[] nums){
        int result = 0;
        for (int num: nums){
            result ^= num;
        }
        return result;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that return only numbers");
    }
}
