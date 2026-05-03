nums1 = [1,3]
nums2 = [2]
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i] <= nums2[j]:
            nums2.insert(j,nums1[i])
            break
        else:
            nums2.insert(j+1,nums1[i])
print(nums2)
if len(nums2) % 2 == 0:
    median = ((nums2[len(nums2)//2])+(nums2[(len(nums2)//2)-1]))/2
    print("median is :- ",median)
else:
    median = nums2[len(nums2)//2]
    print("median is :- ",median)

# another approach

nums1 = [1,2,3,4,5]
nums2 = [2,3,4,6,8]
nums2 = sorted(nums1 +nums2)
print(nums2,"yes")
if len(nums2) % 2 == 0:
    median = ((nums2[len(nums2)//2])+(nums2[(len(nums2)//2)-1]))/2
    print("median is :- ",median)
else:
    median = nums2[len(nums2)//2]
    print("median is :- ",median)
