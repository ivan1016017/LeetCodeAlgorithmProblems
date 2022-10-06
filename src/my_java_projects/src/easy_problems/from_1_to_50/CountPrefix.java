package easy_problems.from_1_to_50;

public class CountPrefix implements Numbers {
    public int countPrefixes(String[] words, String s) {
        int solution = 0;

        for (String word: words){
            if (s.indexOf(word) == 0) solution++;
        }

        return solution;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of a class that returns numbers");
    }
}
