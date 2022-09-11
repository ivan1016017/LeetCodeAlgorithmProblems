package easy_problems.from_1_to_50;

public class NumberStudentsDoingHomework implements Numbers {
    public int busyStudent(int[] startTime, int[] endTime, int queryTime) {

        int solution = 0;

        for (int i = 0; i < startTime.length; i++){
            if (startTime[i] <= queryTime && endTime[i] >= queryTime)solution++;
        }

        return solution;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that returns numbers");
    }
}
