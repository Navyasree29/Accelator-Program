/*Q4. Given an array of integers, print all duplicate elements. 
Input Example: 
arr = [1, 2, 3, 1, 2] 
Output Example: 
Duplicates: 1 2 
Hint for Students: 
�
� Use a HashSet to store seen elements. 
�
� If element already exists in the set → it’s a duplicate. */
import java.util.*;

public class finddupli{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Set<Integer> seen = new HashSet<>();
        Set<Integer> duplicates = new HashSet<>();

        for(int num : arr) {
            if(seen.contains(num)) {
                duplicates.add(num);
            } else {
                seen.add(num);
            }
        }

        System.out.print("Duplicates: ");
        for(int num : duplicates) {
            System.out.print(num + " ");
        }
    }
}
