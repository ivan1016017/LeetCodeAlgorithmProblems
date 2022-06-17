package easy_problems.from_1_to_50;

import java.util.HashMap;

public class RomanNumberToInteger implements Numbers{

    public RomanNumberToInteger() {
        System.out.println("An instance of the RomanNumberToInteger class was created");
    }

    public int romanToInt(String s) {

        if (s == null || s.length() == 0) {
            return -1;
        }

        HashMap<Character, Integer> mapRoman = new HashMap<Character, Integer>();
        mapRoman.put('I', 1);
        mapRoman.put('V', 5);
        mapRoman.put('X', 10);
        mapRoman.put('L', 50);
        mapRoman.put('C', 100);
        mapRoman.put('D', 500);
        mapRoman.put('M', 1000);
        int len = s.length(), result = mapRoman.get(s.charAt(len-1));
        for (int i = len-2; i >= 0; i--){
            if (mapRoman.get(s.charAt(i)) >= mapRoman.get(s.charAt(i+1))){
                result += mapRoman.get(s.charAt(i));
            }
            else{
                result -= mapRoman.get(s.charAt(i));
            }
        }
        return result;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This class transform arabic numbers to roman numbers");

    }
}
