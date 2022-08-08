package easy_problems.from_1_to_50;

import java.util.List;

public class CountItemsMatchingRule implements Numbers{
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {

        int tempIndex = -1;
        int solution = 0;

        if (ruleKey.equals("type") ){
            tempIndex = 0;
        }
        else if (ruleKey.equals("color")){
            tempIndex = 1;
        }
        else if (ruleKey.equals("name")){
            tempIndex = 2;
        }

        for (List<String> item: items){

            if (item.get(tempIndex).equals(ruleValue)){
                solution += 1;
            }
        }

        return solution;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that returns the counting number of matches according to a specific criterion");
    }
}
