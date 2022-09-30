package easy_problems.from_1_to_50;

import java.util.Arrays;

public class MaxNumberUnitsTruck implements Numbers{
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        int res=0;
        System.out.println(Arrays.deepToString(boxTypes));
        Arrays.sort(boxTypes, (a,b) -> b[1]-a[1]);
        System.out.println(Arrays.deepToString(boxTypes)   );
        for(int i=0;i<boxTypes.length;i++){
            res+=(truckSize >= boxTypes[i][0] ? boxTypes[i][0]*boxTypes[i][1] : truckSize*boxTypes[i][1]);
            truckSize=(boxTypes[i][0]>=truckSize ? 0 : truckSize-boxTypes[i][0]);
            if(truckSize==0) return res;
        }
        return res;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This class does not return numbers");
    }
}
