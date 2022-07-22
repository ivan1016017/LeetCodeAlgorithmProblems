package easy_problems.from_1_to_50;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class KidsGreatestNumberCandies {

    class Solution {
        public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {

            int maxCandy = candies[0];
            int candiesLength = candies.length;
            ArrayList<Boolean> solution = new ArrayList<Boolean>();


            for (int i = 0; i <  candiesLength; i++){
                if (maxCandy < candies[i]){
                    maxCandy = candies[i];
                }
            }

            for (int j = 0; j < candiesLength; j++){
                if (candies[j]+extraCandies >= maxCandy){
                    solution.add(true);
                }
                else {
                    solution.add(false);
                }
            }
            return solution;

        }
    }








}



