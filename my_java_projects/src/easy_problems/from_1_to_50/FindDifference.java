package easy_problems.from_1_to_50;

import java.util.*;
import java.util.stream.Collectors;


public class FindDifference {

    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        HashSet<Integer> set1= new HashSet<>(), set2= new HashSet<>();
        for(int num:nums1) set1.add(num);
        for(int num:nums2) set2.add(num);
        HashSet<Integer> copy1= new HashSet<>(set1);
        set1.removeAll(set2);
        set2.removeAll(copy1);
        return Arrays.asList(new ArrayList<>(set1), new ArrayList<>(set2));
    }

    public List<List<Integer>> findDifferenceTwo(int[] nums1, int[] nums2) {
        Set<Integer> s1 = Arrays.stream(nums1).boxed().collect(Collectors.toSet());
        Set<Integer> s2 = Arrays.stream(nums2).filter(n -> !s1.contains(n)).boxed().collect(Collectors.toSet());
        Arrays.stream(nums2).forEach(s1::remove);
        return Arrays.asList(new ArrayList<>(s1), new ArrayList<>(s2));
    }
}

