package easy_problems.from_1_to_50;

public class ArrayByParity implements Numbers{
    public int[] sortArrayByParityII(int[] nums) {

        int lenNums = nums.length;
        int solution[] = new int[lenNums];

        int evenIndex = 0;
        int oddIndex = 1;

        for (int i = 0; i < lenNums;i++){
            if (nums[i] % 2 == 0){
                solution[evenIndex] = nums[i];
                evenIndex += 2;
            }
            else{
                solution[oddIndex] = nums[i];
                oddIndex += 2;
            }
        }

        return solution;

    }

    public int[] sortArrayByParityIITwo(int[] A) {
        int even = 0, odd = 1;
        while(true){
            while(even < A.length && A[even] % 2 == 0) /*(1)*/
                even += 2;
            while(odd < A.length && A[odd] % 2 != 0) /*(2)*/
                odd += 2;
            if(odd >= A.length || even >= A.length) return A;

            /*(3)*/
            int temp = A[even];
            A[even] = A[odd];
            A[odd] = temp;
        }
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that does not return numbers");
    }
}
