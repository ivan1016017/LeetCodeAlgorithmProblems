package easy_problems.from_1_to_50;

import java.util.Stack;

public class ValidParentheses implements Numbers{
    public ValidParentheses() {
        System.out.println("An instance of the ValidParentheses class was called.");
    }

    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (char c : s.toCharArray()) {
            if (c == '(')
                stack.push(')');
            else if (c == '{')
                stack.push('}');
            else if (c == '[')
                stack.push(']');
            else if (stack.isEmpty() || stack.pop() != c)
                return false;
        }
        return stack.isEmpty();
    }

    @Override
    public void returnNumbers() {
        System.out.println("The instance of the class ValidParentheses do not return numbers");
    }
}
