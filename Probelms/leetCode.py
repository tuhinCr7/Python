nums = [3, 2, 4]

for i in range(len(nums) - 1):
    if nums[i] + nums[i + 1] == 6:
        print(nums[i], nums[i + 1])