package easy_problems.from_1_to_50;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

public class IntersectionTwoArrays {
    public int[] intersection(int[] nums1, int[] nums2) {

        Set<Integer> set = Arrays.stream(nums1).boxed()
                .collect(Collectors.toSet());
        Set<Integer> intersection = new HashSet();
        for(int n:nums2){
            if(set.contains(n)){
                intersection.add(n);
            }
        }
        return intersection.stream().mapToInt(i->i).toArray();

    }

    public int[] set_intersection(HashSet<Integer> set1, HashSet<Integer> set2) {
        int [] output = new int[set1.size()];
        int idx = 0;
        for (Integer s : set1)
            if (set2.contains(s)) output[idx++] = s;

        return Arrays.copyOf(output, idx);
    }

    public int[] intersectionTwo(int[] nums1, int[] nums2) {
        HashSet<Integer> set1 = new HashSet<Integer>();
        for (Integer n : nums1) set1.add(n);
        HashSet<Integer> set2 = new HashSet<Integer>();
        for (Integer n : nums2) set2.add(n);

        if (set1.size() < set2.size()) return set_intersection(set1, set2);
        else return set_intersection(set2, set1);
    }

}
