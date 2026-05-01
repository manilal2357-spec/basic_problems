nums = [0,0,1,1,1,2,3,4,5,5,6]
count = 0
i = 0
print("manilal")

while i < len(nums) - 1:
    if nums[i] == nums[i+1]:
        nums.remove(nums[i])
        nums.insert(i,"_")
        count += 1
        i = i + 1
    else:
        i += 1
print(nums)
print(count)
nums2= []
nums3 =[]
for i in nums:
    if i != "_":
        nums2.append(i)
    else:
        nums3.append(i)
print(nums2 + nums3)








nums3 = [0,0,1,1,1,2,3,4,5,5,6]
i = 0
for j in range(len(nums3)):
    if nums3[j] != nums3[i]:
        i = i+1
        nums3[i]=nums3[j]
m=0
for k in range(i+1,len(nums3)):
    nums3[k] = "_"
    m = m+1
print(nums3)
print(m)



