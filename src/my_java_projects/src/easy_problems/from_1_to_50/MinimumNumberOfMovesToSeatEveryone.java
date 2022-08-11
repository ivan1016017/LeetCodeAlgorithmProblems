package easy_problems.from_1_to_50;

import java.util.Arrays;

public class MinimumNumberOfMovesToSeatEveryone  implements Numbers{
    public int minMovesToSeat(int[] seats, int[] students) {
        int solution = 0;

        Arrays.sort(seats);
        Arrays.sort(students);

        for (int i = 0; i < seats.length; i++){
            solution += Math.abs(seats[i] - students[i]);
        }


        return solution;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that return a number that is the minimum movement to allocate each student to a seat without repeating it.");
    }
}
