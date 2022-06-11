package easy_problems.from_1_to_50;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class TwoSum {

    public int[] twoSum(int[] nums, int target){
        int[] result = new int[2];
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        for ( int i = 0; i < nums.length; i++){

            if (map.containsKey(target - nums[i])){
                result[1] = i;
                result[0] = map.get(target - nums[i]);
            }

            map.put(nums[i], i);
        }

        Set set = map.entrySet();
        Iterator itr=set.iterator();
        while(itr.hasNext()){
            //Converting to Map.Entry so that we can get key and value separately
            Map.Entry entry=(Map.Entry)itr.next();
            System.out.println(entry.getKey()+" "+entry.getValue());
        }



        return result;

    }
}
