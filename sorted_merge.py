#source code taken from CTCI 6th Edition in Java and reproduced in Python
#Problem: Having 2 sorted arrays one array is exactly both of the arrrays' size
#and in the last n (the size of the smaller array) spots it is empty
#Merge both of the arrays and sort

def merge(arrA, arrB):
    full_index = len(arrA) - 1
    index_b = len(arrB) - 1
    index_a = full_index - index_b - 1

    #starts from the end of both arrays and works to the very beginning
    while(index_b >= 0):
        if(index_a >= 0 & arrA[index_a] > arrB[index_b]):
            arrA[full_index] = arrA[index_a]
            index_a -= 1
        else:
            arrA[full_index] = arrB[index_b]
            index_b -= 1
        full_index -= 1
    return arrA

def main():
    bigarray = [i*2 for i in range(15)] + [0 for i in range(10)]
    arr2 = [i*3 + 1 for i in range(10)]
    # print("bigarray before merge ", bigarray)
    # print("arr2 before merge ", arr2)

    final_array = merge(bigarray, arr2)
    print(final_array)

if __name__ == "__main__":
    main()