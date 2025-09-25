/*Given an array, find the maximum and minimum elements.
 input:
 arr = [10, 5, 20, 8, 2]
 output:
 Min: 2
 Max: 20
 Hint for Students
 Iterate once → keep track of current min and max.
 */ 
import java.util.Scanner;

public class minmaxarray {

    public static void findMinMax(int[] arr) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
            if (arr[i] > max) {
                max = arr[i];
            }
        }

        System.out.println("Min: " + min);
        System.out.println("Max: " + max);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] input = sc.nextLine().split(" ");
        int[] arr = new int[input.length];

        for (int i = 0; i < input.length; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        findMinMax(arr);
    }
}
