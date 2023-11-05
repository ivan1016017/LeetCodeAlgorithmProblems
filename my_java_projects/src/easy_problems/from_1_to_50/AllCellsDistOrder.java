package easy_problems.from_1_to_50;

import java.util.Arrays;
import java.util.Comparator;

public class AllCellsDistOrder {
    public int[][] allCellsDistOrder(int R, int C, int r0, int c0) {
        int[][] arr = new int[R*C][2];
        for(int k = 0, i = 0; i < R && k < R * C; i++) {
            for(int j = 0; j < C; j++) {
                arr[k++] = new int[]{i, j};
            }
        }
        Arrays.sort(arr, new Comparator<int[]>(){
            @Override
            public int compare(int[] a, int[] b) {
                return Math.abs(a[0] - r0) + Math.abs(a[1] - c0) - (Math.abs(b[0] - r0) + Math.abs(b[1] - c0));
            }
        });
        return arr;
    }
}
