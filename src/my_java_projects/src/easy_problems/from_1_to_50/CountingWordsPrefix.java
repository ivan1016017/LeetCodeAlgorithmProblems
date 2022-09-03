package easy_problems.from_1_to_50;

public class CountingWordsPrefix implements Numbers{
    public int prefixCount(String[] words, String pref) {

        int solution = 0;

        for (String word: words){
            if (word.indexOf(pref) == 0){
                solution += 1;
            }
        }

        return solution;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This class does return a number");
    }
}
