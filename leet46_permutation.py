#Credit goes to https://www.youtube.com/watch?v=s7AvT7cGdSo

def permute(nums):
    result = []

    #base case
    if(len(nums) == 1):
        return [nums[:]]
    
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    
    return result

def example():
    list_ = [1,2,3,4,5]
    res = permute(list_)
    print(res)

if __name__ == "__main__":
    example()