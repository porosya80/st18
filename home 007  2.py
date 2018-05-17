# import reduce

nums = [1, 4, 5, 30, 99]
nums2 = [3, 4, 90, -2]
nums3 = ['some', 1, 'v', 40, '3a', str]

print(list(map(lambda x: x%5, nums)))
print(list(map(lambda x: str(x), nums2)))
print(list(filter(lambda x: not isinstance(x, str), nums3)))
