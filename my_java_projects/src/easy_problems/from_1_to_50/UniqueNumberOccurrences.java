package easy_problems.from_1_to_50;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;


public class UniqueNumberOccurrences {

    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer,Integer> solutionMap = new HashMap<>();

        for (int number: arr)solutionMap.put(number, solutionMap.getOrDefault(number,0) + 1);

        Set<Integer> set = new HashSet<>(solutionMap.values());

        return set.size() == solutionMap.size();

    }

    public boolean uniqueOccurrencesTwo(int[] arr)
    {
        int[] table = new int[2000];
        for(int i = 0; i < arr.length; i++)
        {
            table[arr[i]+1000] += 1;
        }

        for(int i = 0; i < table.length; i++)
        {
            if(table[i] != 0)
            {
                for(int j = table.length - 1; j > i; j--)
                {
                    if(table[j] != 0 && table[j] == table[i]) return false;
                }
            }
        }
        return true;
    }
}
