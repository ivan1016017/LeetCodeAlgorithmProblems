package easy_problems.from_1_to_50;

public class MaximumNumberOfWords implements Numbers{
    public int mostWordsFound(String[] sentences) {

        int solution = 0;

        for (int i = 0; i < sentences.length; i++){
            solution = Math.max(solution, sentences[i].split(" ").length);
        }

        return solution;


    }

    @Override
    public void returnNumbers() {
        System.out.println("This class returns numbers.");
    }
}
