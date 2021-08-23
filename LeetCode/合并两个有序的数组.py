def merge(nums1, nums2):
    count = 0
    for i in range(len(nums1) - 1, 0, -1):
        if nums1[i] != 0:
            break
        else:
            count += 1
    nums1 = nums1[0:len(nums1) - count]
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            nums1[i] = nums1[i]
            i += 1
        else:
            nums1.insert(i, nums2[j])
            i += 1
            j += 1

    if j < len(nums2):
        nums1.extend(nums2[j:])
    return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    print(merge(nums1, nums2))
