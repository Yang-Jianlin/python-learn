def union_array(nums1, nums2):
    for i in range(len(nums1)-1, -1, -1):
        if nums1[i] == 0:
            nums1.pop(i)
        else:
            break
    for i in range(len(nums2)-1, -1, -1):
        if nums2[i] == 0:
            nums2.pop(i)
        else:
            break
    n1 = len(nums1)
    n2 = len(nums2)
    i = 0
    j = 0
    while i < n1 and j < n2:
        if i < n1 and nums1[i] <= nums2[j]:
            i += 1
        if j < n2 and nums1[i] > nums2[j]:
            nums1.insert(i, nums2[j])
            i += 1
            j += 1
    if j < n2:
        nums1.extend(nums2[j:])
    return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    print(union_array(nums1, nums2))
