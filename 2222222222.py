nums=[1,2,3,4]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]>nums[j]:
          nums[i],nums[j]=nums[j],nums[i]


[7,1,2,4,8]