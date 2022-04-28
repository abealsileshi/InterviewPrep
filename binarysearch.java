import java.util.ArrayList;

public class binarysearch{
     public static int binarySearch(int [] a, int x, int low, int high){
        if(low > high) return -1;

        int mid = low + ((high - low)/2);
        if(a[mid] < x){
            return binarySearch(a, x, mid +1, high);
        }
        else if (a[mid] > x){
            return binarySearch(a, x, low, mid -1);
        } else{
            return mid;
        }

    }
    public static void main(String[] args) {
        int [] a = {1,2,3,4,5,56,67,78,89,100};

        ArrayList<Integer> arr = new ArrayList<Integer>();
        arr.add(0);
        arr.add(1);
        arr.add(2);
        arr.add(3);
        arr.add(4);
        arr.add(9);
        arr.add(15);
        arr.add(30);
        System.out.println(arr);

        int result;
        result = binarysearch.binarySearch(a, -2, 0, 7);
        System.out.println(result);

    }
}