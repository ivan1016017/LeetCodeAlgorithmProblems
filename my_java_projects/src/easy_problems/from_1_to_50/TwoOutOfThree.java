package easy_problems.from_1_to_50;

import java.util.*;

public class TwoOutOfThree implements Numbers{
    public ArrayList<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        ArrayList<Integer> numsArrayOne = new ArrayList<>();
        ArrayList<Integer> numsArrayTwo = new ArrayList<>();
        ArrayList<Integer> numsArrayThree = new ArrayList<>();


        for (int num: nums1){
            if (!numsArrayOne.contains(num))numsArrayOne.add(num);
        }

        for (int num: nums2){
            if (!numsArrayTwo.contains(num))numsArrayTwo.add(num);

        }

        for (int num: nums3){
            if (!numsArrayThree.contains(num))numsArrayThree.add(num);

        }

        HashMap<Integer,Integer> mapCounting = new HashMap<>();

        for (int num: numsArrayOne){
            mapCounting.put(num,0);
        }
        for (int num: numsArrayTwo){
            mapCounting.put(num,0);
        }
        for (int num: numsArrayThree){
            mapCounting.put(num,0);
        }

        for (int num: numsArrayOne){
            mapCounting.put(num,mapCounting.get(num) + 1);
        }

        for (int num: numsArrayTwo){
            mapCounting.put(num,mapCounting.get(num) + 1);
        }
        for (int num: numsArrayThree){
            mapCounting.put(num,mapCounting.get(num) + 1);
        }

        ArrayList<Integer> solution = new ArrayList<>();

        for (int num: mapCounting.keySet()){
            if (mapCounting.get(num) >= 2)solution.add(num);
        }

        return solution;


    }

    public List<Integer> twoOutOfThreeSecond(int[] nums1, int[] nums2, int[] nums3) {
        Set<Integer> set1 = new HashSet<>(), set2 = new HashSet<>(), set3 = new HashSet<>(), set = new HashSet<>();
        for(int i: nums1) { set1.add(i); set.add(i); }
        for(int i: nums2) { set2.add(i); set.add(i); }
        for(int i: nums3) { set3.add(i); set.add(i); }
        List<Integer> result = new ArrayList<>();
        for(int i: set)
            if(set1.contains(i) && set2.contains(i) || set2.contains(i) && set3.contains(i) || set1.contains(i) && set3.contains(i)) result.add(i);
        return result;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that does not return numbers");
    }
}
