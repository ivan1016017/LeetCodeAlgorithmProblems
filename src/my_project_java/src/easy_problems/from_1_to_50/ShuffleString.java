package easy_problems.from_1_to_50;

import java.util.HashMap;

public class ShuffleString implements Numbers{

    public String restoreString(String s, int[] indices) {
        char[] arr = new char[s.length()];
        for (int i = 0; i < indices.length; i++) arr[indices[i]] = s.charAt(i);
        return String.valueOf(arr);
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of a class that does not return numbers.");
    }
}
