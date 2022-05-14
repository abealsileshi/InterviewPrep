#Problem: Number of ways to go up n stairs
# using 1,2, or 3 steps
#Solution taken from Cracking the Code Interview in Java and turned into Python

def countWays(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return countWays(n-1) + countWays(n-2) + countWays(n-3)


def main():
    num = 4
    res = countWays(num)
    print("The number of ways to climb ",num, " stairs is: ", res )

if __name__ == "__main__":
    main()