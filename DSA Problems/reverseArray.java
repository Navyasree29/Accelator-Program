/* Write a program to reverse an array of integers in place.
 input: arr = [1, 2, 3, 4, 5]
 output: [5, 4, 3, 2, 1]
 Hint for Students :
 Use two pointers (start, end) and swap until they meet. */

 
import java.util.*;
public class reverseArray {
    public static void func(int a[]) {
        int start = 0;
        int end = a.length - 1;
        while (start < end) {
            int temp = a[start];
            a[start] = a[end];
            a[end] = temp;

            start++;
            end--;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int[] arr = new int[input.length];
        for (int i = 0; i < input.length; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        func(arr);

        System.out.println(Arrays.toString(arr));
        sc.close();
    }
}
