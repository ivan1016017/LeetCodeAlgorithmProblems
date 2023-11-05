package easy_problems.from_1_to_50;

public class StrStr implements Numbers{

    public int strStr(String haystack, String needle) {
        for (int i = 0; ; i++) {
            for (int j = 0; ; j++) {
                if (j == needle.length()) return i;
                if (i + j == haystack.length()) return -1;
                if (needle.charAt(j) != haystack.charAt(i + j)) break;
            }
        }
    }

    public int strStrTwo(String haystack, String needle) {
        if (needle.equals(null) || needle.length() == 0) {
            return 0;
        }
        if (haystack.equals(null) || haystack.length() == 0) {
            return -1;
        }
        return haystack.indexOf(needle);
    }

    @Override
    public void returnNumbers() {
        System.out.println("The class StrStr does not return numbers");
    }
}
