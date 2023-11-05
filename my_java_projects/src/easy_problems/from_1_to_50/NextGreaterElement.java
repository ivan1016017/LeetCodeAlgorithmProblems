package easy_problems.from_1_to_50;

import java.util.ArrayList;

public class NextGreaterElement {
    public static int findIndex(int arr[], int t)
    {
        ArrayList clist = new ArrayList<>();

        for (int i : arr)
            clist.add(i);
        return clist.indexOf(t);
    }
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        boolean pres=false;
        for(int i=0;i<nums1.length;i++)
        {
            for(int j=findIndex(nums2,nums1[i])+1;j<=nums2.length;j++)
            {
                if(j==nums2.length)
                {
                    nums1[i]=-1;
                    break;
                }
                if(nums1[i]<nums2[j])
                {
                    nums1[i]=nums2[j];
                    pres=true;
                    break;
                }
            }
            if(!pres)
            {
                nums1[i]=-1;
            }
        }
        return nums1;
    }
}
