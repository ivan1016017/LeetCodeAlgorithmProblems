package easy_problems.from_1_to_50;

public class ReplaceElementsGreatestRight implements Numbers{

        public int[] replaceElements(int[] arr) {

            int maxRight = -1;
            int index = arr.length -1;
            int temp;

            while (index >= 0){
                temp = arr[index];
                arr[index] = maxRight;
                if (temp > maxRight){
                    maxRight = temp;
                }
                index -= 1;
            }

            return arr;

        }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that does not return numbers");
    }
}
