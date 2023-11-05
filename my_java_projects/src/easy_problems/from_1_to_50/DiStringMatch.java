package easy_problems.from_1_to_50;

public class DiStringMatch implements Numbers{
    public int[] diStringMatch(String s) {
        int n = s.length(), low = 0, high = n;
        int[] solution = new int[n+1];
        for (int i = 0; i < n; i++){
            solution[i] = s.charAt(i) == 'I' ? low++: high--;
        }
        solution[n] = low;
        return solution;
    }

    public int[] diStringMatchTwo(String s) {
        int[] result = new int[s.length() + 1];
        int start = 0, end = result.length - 1;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == 'I') {
                result[i] = start;
                start++;
            } else {
                result[i] = end;
                end--;
            }
        }
        result[result.length - 1] = start;
        return result;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that does not return numbers");
    }
}
