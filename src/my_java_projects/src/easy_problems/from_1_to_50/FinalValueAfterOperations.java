package easy_problems.from_1_to_50;

public class FinalValueAfterOperations implements Numbers{

    public int finalValueAfterOperations(String[] operations) {

        int solution = 0;

        for (String value: operations){
            if (value.charAt(1) == '+'){
                solution++;
            }
            else{
                solution--;
            }
        }

        return solution;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This class actually returns numeric values.");
    }
}
