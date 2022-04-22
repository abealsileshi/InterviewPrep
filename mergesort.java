import java.util.*;

public class mergesort{
    static void mergesort(int[] array){

        System.out.println("This is the ORIGINAL array");
        for(int i = 0; i <= array.length - 1; i++){
            System.out.println("Element at index " + i + " : "+ array[i]);
        }

        int[] helper = new int[array.length];
        mergesort(array, helper, 0, array.length - 1);
    }

    static void mergesort(int[] array, int[] helper, int low, int high){
        if(low < high){
            int middle = low + (high - low) / 2;
            mergesort(array, helper, low, middle);
            mergesort(array, helper, middle +1, high);
            merge(array, helper, low, middle, high);
        }
    }

    static void merge(int[] array, int[] helper, int low, int middle, int high){
        for(int i = low; i <= high; i++){
            helper[i] = array[i];
        }

        System.out.println("");
        System.out.println("array before merge function");
        for(int i = 0; i <= array.length - 1; i++){
            System.out.println("Element at index " + i + " : "+ array[i]);
        }
        System.out.println("=================");

        int helperLeft = low;
        int helperRight = middle + 1;
        int current = low;
        System.out.println("This is hL (and low) " +  " : "+ helperLeft);
        System.out.println("This is hR (and middle + 1) " +  " : "+ helperRight);
        System.out.println("This is current (and low) " +  " : "+ current);



        while(helperLeft <= middle && helperRight <= high){
            if(helper[helperLeft] <= helper[helperRight]){ //this means that
                System.out.println("Element at index " + current + " is being filled with value at index " + helperLeft);
                array[current] = helper[helperLeft];
                helperLeft++;

            }
            else{
                System.out.println("Element at index " + current + " is being filled with value at index " + helperRight);
                array[current] = helper[helperRight]; //means the right half is smaller than left half
                helperRight++;
            }
            current++;
        }
        System.out.println("new hR is: " + helperRight);
        System.out.println("new hL is: " + helperLeft);
        System.out.println("new curr: " + current);

        int remaining = middle - helperLeft;
        System.out.println("Remaining is: " + remaining);

        for(int i = 0; i <= remaining; i++){
            array[current + i] = helper[helperLeft + i];
            int temp = current + i;
            System.out.println(helper[helperLeft + i] + " is being placed at index " + temp);

        }
        System.out.println("array AFTER merge function");
        for(int i = 0; i <= array.length - 1; i++){
            System.out.println("Element at index " + i + " : "+ array[i]);
        }
        System.out.println("=================");
    }

    public static void main(String[] args){
        System.out.println("In mergesort.java...");

        int[] arr;
        // allocating memory for 5 integers.
        arr = new int[6];
        arr[0] = 3;
        arr[1] = 4;
        arr[2] = 2;
        arr[3] = 1;
        arr[4] = 6;
        arr[5] = 5;


        mergesort(arr);

        System.out.println("This is the ENDING array");
        for(int i = 0; i <= arr.length - 1; i++){
            System.out.println("Element at index " + i + " : "+ arr[i]);;
        }
    }
}

