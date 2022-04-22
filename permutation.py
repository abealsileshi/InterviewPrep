def sortString(string):
    #optional is to add .lower() to make all letters lower case
    str = "".join(sorted(string.lower()))
    print("sorted word: ", str)
    return str

def compare(string1, string2):
    s1 = sortString(string1)
    s2 = sortString(string2)
    return True if s1 == s2 else False

def main():
    str1 = "AbealSileshi"
    str2 = "bAlealiSeshi"
    str3 = "ETHIOPIA"
    str4 = "ethiopia"
    answer = compare(str3, str4)
    print("This is our answer Abeal: ", answer)
    print("Never give up on your dreams")


if __name__ == "__main__":
    main()