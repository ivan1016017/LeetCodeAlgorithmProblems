package easy_problems.from_1_to_50;

import java.util.Arrays;

public class MedianSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int lenNums1 = nums1.length;
        int lenNums2 = nums2.length;
        int[] solution = new int[lenNums1+lenNums2];
        int i = 0;
        int j = 0;
        int k = 0;

        while (i < lenNums1 && j < lenNums2){
            if (nums1[i] <= nums2[j]){
                solution[k] = nums1[i];
                i += 1;
                k += 1;
            }
            else{
                solution[k] = nums2[j];
                j += 1;
                k += 1;
            }
        }

        for (int l = i; l < lenNums1; l++){
            solution[k] = nums1[l];
            k++;

        }
        for (int l = j; l < lenNums2; l++){
            solution[k] = nums2[l];
            k++;

        }

        int lenSolution = lenNums1+lenNums2;

        System.out.println(Arrays.toString(solution));

        if (lenSolution%2 != 0){
            return solution[(int)(lenSolution/2)];
        }
        else {
            return ((double)solution[(int)(lenSolution/2)-1] + (double)solution[(int)(lenSolution/2)])/2;
        }



    }
}
