def romanToInt(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = []
    total = 0
    for sym in s:
        nums.append(d[sym])
    # MCMXCIV 1000 100 1000 10 100 1 5
    flag = True
    for i, num in enumerate(nums):
        if i < len(nums) - 1:
            if flag:
                if num >= nums[i + 1]:
                    total += num
                else:
                    total += nums[i + 1] - num
                    flag = False
            else:
                flag = True
        elif i == len(nums) - 1 and flag:
            total += num
    return total

print(romanToInt('III'))
