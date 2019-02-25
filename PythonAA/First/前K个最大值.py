import heapq
heapTest = heapq
# a = [1, 2, 3, 5, 8]
# print(heapTest.nsmallest(2, a)[-1])

class MyHeap:
    def __init__(self):
        super()

    def BigHeapSort(self, arr):
        self.heap = arr
        length = len(arr)
        i = (length >> 1) - 1
        # 构建大顶椎
        while i >= 0:
            self.heap_adjust(arr, i, length)
            i -= 1
        j = length - 1
        while j > 0:
            arr[0], arr[j] = arr[j], arr[0]
            self.heap_adjust(arr, 0, j)
            j -= 1
        print(arr)

    def heap_adjust(self, arr, i, length):
        temp = arr[i]
        k = (i << 1) + 1
        while k < length:
            if k + 1 < length and arr[k] < arr[k+1]:
                k = k + 1
            if arr[k] > temp:
                arr[i] = arr[k]
                i = k
            else:
                break
            k = (k << 1) + 1
        arr[i] = temp

    def n_small(self, k, arr):
        if k == 1:
            return min(arr)
        length = len(arr)
        # 构建大顶椎
        heapKSmall = arr[0:k]
        self.BigHeap(heapKSmall)
        for i in range(k, length):
            if arr[i] < heapKSmall[0]:
                heapKSmall[0] = arr[i]
                self.BigHeap(heapKSmall)
        print(heapKSmall)
        return heapKSmall[0]

    def BigHeap(self, arr):
        length = len(arr)
        j = (length >> 1) - 1
        # 构建大顶椎
        while j >= 0:
            self.heap_adjust(arr, j, length)
            j -= 1


if __name__ == '__main__':
    arrStr = input()
    arr = [int(x) for x in arrStr.split(" ")]
    arrrange = [int(x) for x in input().split(" ")]
    k = int(input())
    arrK = arr[arrrange[0]-1:arrrange[1]]
    # print(heapTest.nsmallest(k, arrK)[-1])
    myheap = MyHeap()
    # myheap.BigHeapSort(arrK)
    print(myheap.n_small(k, arrK))


