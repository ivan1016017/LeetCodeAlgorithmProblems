package easy_problems.from_1_to_50;

public class MinDeletionSize {
    public int minDeletionSize(String[] a) {
        if(a.length == 0) return 0;
        int m = a.length, n = a[0].length(), count = 0;
        for(int j=0; j < n; j++){
            int i = 1;
            for(; i < m; i++)
                if(a[i-1].charAt(j) > a[i].charAt(j))
                    break;
            if(i < m)
                ++count;
        }
        return count;
    }
}
