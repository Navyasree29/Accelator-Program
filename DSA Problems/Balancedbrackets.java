/*Q2. Given a string of parentheses ()[]{}, check whether it is balanced. 
A string is balanced if every opening bracket has a matching closing bracket in the correct 
order. 
Input Example: 
({[]}) 
Output Example: 
Balanced 
Hint for Students: 
�
� Use a Stack to push opening brackets. 
�
� When a closing bracket comes, check top of stack for its matching pair. 
�
� If mismatch or stack not empty at end → Not Balanced. */
import java.util.*;

public class Balancedbrackets {
    public static boolean isBalanced(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return false;
                char top = stack.pop();
                if ((c == ')' && top != '(') || (c == '}' && top != '{') || (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        if (isBalanced(input)) {
            System.out.println("Balanced");
        } else {
            System.out.println("Not Balanced");
        }
    }
}
