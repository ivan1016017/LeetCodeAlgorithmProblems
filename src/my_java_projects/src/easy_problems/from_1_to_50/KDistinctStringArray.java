package easy_problems.from_1_to_50;

import java.util.ArrayList;
import java.util.HashMap;

public class KDistinctStringArray {
    public String kthDistinct(String[] arr, int k) {
        HashMap<String, Integer> map = new HashMap<>();
        for(String s:arr) map.put(s, map.getOrDefault(s,0) + 1);
        int i=0, j=0;
        for(;i<arr.length && j<k;i++)
            if(map.get(arr[i]) == 1) j++;
        return j==k ? arr[i-1]: "";
    }

    public String kthDistinctTwo(String[] arr, int k) {
        HashMap<String,Integer>map=new HashMap<>();
        for(String str : arr)map.put(str,map.getOrDefault(str,0)+1);
        for(int i=0;k>0&&i<arr.length;i++){
            if(map.get(arr[i])==1)k--;
            if(k==0)return arr[i];
        }
        return "";
    }
}
