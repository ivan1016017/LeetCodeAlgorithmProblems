package easy_problems.from_1_to_50;

import java.util.HashMap;

public class RomanToInt {
    public int romanToInt(String s) {
        HashMap<Character,Integer> mapRoman = new HashMap<Character,Integer>();
        mapRoman.put('I',1);
        mapRoman.put('V',5);
        mapRoman.put('X',10);
        mapRoman.put('L',50);
        mapRoman.put('C',100);
        mapRoman.put('D',500);
        mapRoman.put('M',1000);
        int len = s.length(), result = mapRoman.get(s.charAt(len-1));
        for (int i = len-2; i >= 0; i--){
            if (mapRoman.get(s.charAt(i)) >= mapRoman.get(s.charAt(i+1))){
                result += mapRoman.get(s.charAt((i)));
            }
            else{
                result -= mapRoman.get(s.charAt(i));
            }
        }
        return result;

    }

    public int romanToIntTwo(String s) {
        int ans = 0, num = 0;
        for (int i = s.length()-1; i >= 0; i--) {
            switch(s.charAt(i)) {
                case 'I': num = 1; break;
                case 'V': num = 5; break;
                case 'X': num = 10; break;
                case 'L': num = 50; break;
                case 'C': num = 100; break;
                case 'D': num = 500; break;
                case 'M': num = 1000; break;
            }
            if (4 * num < ans) ans -= num;
            else ans += num;
        }
        return ans;
    }
}
