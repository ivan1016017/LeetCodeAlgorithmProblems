package easy_problems.from_1_to_50;

import java.util.HashMap;
import java.util.Map;

public class MakeTwoArraysEqualByReversing implements Numbers{
    public boolean canBeEqual(int[] target, int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i:target) map.put(i, map.getOrDefault(i, 0) + 1);
        for(int i:arr) map.put(i, map.getOrDefault(i, 0) - 1);
        for(int key: map.keySet())if (map.get(key) != 0) return false;
        return true;
    }

    public boolean canBeEqualTwo(int[] target, int[] arr) {
        int[] out1 = new int[1001];
        int[] out2 = new int[1001];
        for(int i=0;i<target.length;++i){
            out1[target[i]]++;
            out2[arr[i]]++;
        }
        for(int i=0;i<out1.length;++i){
            if(out1[i]!=out2[i]) return false;
        }
        return true;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of the class that does not return numbers");
    }
}
