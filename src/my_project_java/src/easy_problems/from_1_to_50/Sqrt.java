package easy_problems.from_1_to_50;

public class Sqrt implements Numbers{

    public Sqrt() {
        System.out.println("An instance of the class Sqrt was created.");
    }

    @Override
    public void returnNumbers() {
        System.out.println("This class return the int root square of a number.");
    }

    public int mySqrt(int x) {

        int left = 0, right = x, mid = -1;

        while (left<= right){
            mid = (int)((left+right)/2);
            if (Math.pow(mid,2) > x){
                right = mid -1;
            }
            else if (Math.pow(mid,2) < x){
                left = mid + 1;
            }
            else {
                return mid;
            }
        }

        return right;
    }
}
