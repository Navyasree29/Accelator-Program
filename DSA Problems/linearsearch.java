/*Search for an element x in an array using linear search.
 input: arr = [4, 2, 9, 1, 7], x = 9
 output: Element found at index 2
 Hint for Students
 Loop through array and check if any element equals x.
 */
import java.util.*;

public class linearsearch {

    public static void findelement(int a[], int x) {
        int i;
        for (i = 0; i < a.length; i++) {
            if (a[i] == x) {
                System.out.println("Element found at index " + i);
                break;
            }
        }
        if (i == a.length) {
            System.out.println("Element not found");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter array elements separated by space:");
        String[] input = sc.nextLine().split(" ");
        int[] arr = new int[input.length];
        for (int i = 0; i < input.length; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

    
        int x = sc.nextInt();

        findelement(arr, x);
        sc.close();
    }
}
