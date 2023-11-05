package easy_problems.from_1_to_50;

import java.util.ArrayList;

public class LuckyNumbers {
    public ArrayList<Integer> luckyNumbers (int[][] matrix) {
        var ans = new ArrayList<Integer>();

        for (int[] rows : matrix) {
            var colIndex = 0;

            for (int j = 1; j < rows.length; j++) {
                if (rows[j] < rows[colIndex])
                    colIndex = j;
            }

            var found = false;

            for (int i = 0; i < matrix.length && !found; i++)
                found = matrix[i][colIndex] > rows[colIndex];

            if (!found)
                ans.add(rows[colIndex]);
        }

        return ans;
    }
}
