/*Q3. You are given an array of size n-1 containing distinct numbers from 1 to n. 
Find the missing number in the sequence. 
Input Example: 
arr = [1, 2, 4, 5] 
n = 5 
Output Example: 
3 
Hint for Students: 
�
� Use formula: 
[ 
\text{Expected Sum} = \frac{n(n+1)}{2} 
] 
Subtract the actual sum from expected sum. */
import java.util.*;

public class MissingNum {
    public static int findMissing(int[] arr, int n) {
        int expectedSum = n * (n + 1) / 2;
        int actualSum = 0;
        for (int num : arr) {
            actualSum += num;
        }
        return expectedSum - actualSum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n - 1];
        for (int i = 0; i < n - 1; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println(findMissing(arr, n));
    }
}
