package easy_problems.from_1_to_50;

public class IslandPerimeter {
    public int islandPerimeter(int[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        int count = 0;
        for(int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == 1) {
                    count += (i + 1 >= r || grid[i + 1][j] == 0) ? 1 : 0;
                    count += (i - 1 < 0 || grid[i - 1][j] == 0) ? 1 : 0;
                    count += (j + 1 >= c || grid[i][j + 1] == 0) ? 1 : 0;
                    count += (j - 1 < 0 || grid[i][j - 1] == 0) ? 1 : 0;
                }
            }
        }
        return count;
    }
}
