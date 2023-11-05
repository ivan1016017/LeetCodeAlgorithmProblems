package easy_problems.from_1_to_50;

import java.util.HashMap;

public class CountCommonOcurrence implements Numbers{
    public int countWords(String[] words1, String[] words2) {
        HashMap<String,Integer> mapSolution = new HashMap<>();

        int answer = 0;

        for (String s: words1){
            mapSolution.put(s, mapSolution.getOrDefault(s,0)+1);
        }

        for (String s: words2){
            if (mapSolution.containsKey(s)){
                mapSolution.put(s,mapSolution.get(s)+1);
            }
        }

        for (String s: words2){
            if (mapSolution.containsKey(s) && mapSolution.get(s) == 2){
                answer ++;
            }
        }

        return answer;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of the class that return numbers");
    }
}
