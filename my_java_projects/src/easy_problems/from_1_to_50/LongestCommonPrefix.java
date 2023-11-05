package easy_problems.from_1_to_50;

public class LongestCommonPrefix implements Numbers{

    public LongestCommonPrefix(){
        System.out.println("The instance of the class was called");
    }

    public String longestCommonPrefix(String[] strs){

        if (strs.length == 0) return "";

        String pre = strs[0];
        for (int i = 1; i < strs.length; i++){
            while (strs[i].indexOf(pre) != 0){
                pre = pre.substring(0, pre.length()-1);
            }
        }

        return pre;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This class does not generate numbers");
    }
}
