import heapq


class Solution:
    # 小根堆求出最大的k个数
    def getLeast1Numbers(self, arr, k):
        if len(arr) <= k:
            return arr
        heap = []
        if k == 0:
            return heap
        for i in range(len(arr)):
            if i < k:
                heap.append(arr[i])
            else:
                heapq.heapify(heap)
                if heap[0] < arr[i]:
                    heapq.heapreplace(heap, arr[i])
        return heap

    # 大根堆求出最小的k个数
    def getLeast2Numbers(self, arr, k):
        if len(arr) <= k:
            return arr
        arr = [-i for i in arr]
        heap = []
        if k == 0:
            return heap
        for i in range(0, len(arr)):
            if i < k:
                heap.append(arr[i])
            else:
                heapq.heapify(heap)
                if heap[0] < arr[i]:
                    heapq.heapreplace(heap, arr[i])
        heap = [-i for i in heap]
        return heap


if __name__ == '__main__':
    s = Solution()
    arr = [0, 0, 0, 2, 0, 5]
    print(s.getLeast1Numbers(arr, 0))
    print(s.getLeast2Numbers(arr, 0))
