"""
利用递归的方式进行全排列
对a,b,c三个字符进行全排列，那么它的全排列有abc,acb,bac,bca,cba,cab这六种可能,
就是当指针指向第一个元素a时，它可以是其本身a(即和自己进行交换)，还可以和b，c进行交换，故有3种可能，
当第一个元素a确定以后，指针移向第二位置，第二个位置可以和其本身b及其后的元素c进行交换，又可以形成两种排列，
当指针指向第三个元素c的时候，这个时候其后没有元素了，此时，则确定了一组排列，输出。
但是每次输出后要把数组恢复为原来的样子。
"""


def permutations(arr, position, end):
    if position == end:
        print(arr)
    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end)
            arr[index], arr[position] = arr[position], arr[index]


# 利用数组进行非递归的全排列
# 一个序列的全排列个数=n！
def permutationN(arr):
    sum = 1

    # 有多少种全排列的组合
    for j in range(len(arr)):
        sum *= (j + 1)

    i = 0
    for k in range(sum):
        arr[i], arr[i+1] = arr[i + 1], arr[i]
        print(arr)
        i += 1
        if i == (len(arr) - 1):
            i = 0


if __name__ == '__main__':
    arr = [1, 2, 3]
    # permutations(arr, 0, len(arr))
    permutationN(arr)
