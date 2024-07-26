def sortingalgoritm(nums):
    arr = []
    recent = 0
    while len(nums) > 0:
        max = None
        min = None
        for i in range(len(nums)):
            if max == None and min == None:
                max = nums[i]
                min = nums[i]
            elif nums[i] > max:
                max = nums[i]
            elif nums[i] < min:
                min = nums[i]
        if len(nums) > 1:
            nums.remove(max)
            nums.remove(min)
            arr.insert(recent,min)
            arr.insert(recent+1,max)
        elif len(nums) == 1:
            nums.remove(min)
            arr.insert(recent,min)
        recent +=1
    return arr


test_case = [5,6,3,2,7,8,1,0,0]
print(sortingalgoritm(test_case))