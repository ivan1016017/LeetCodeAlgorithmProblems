package easy_problems.from_1_to_50;

public class NumberStudentsDoingHomework {
    public int busyStudent(int[] startTime, int[] endTime, int queryTime) {

        int solution = 0;

        for (int i = 0; i < startTime.length; i++){
            if (startTime[i] <= queryTime && endTime[i] >= queryTime)solution++;
        }

        return solution;

    }
}
