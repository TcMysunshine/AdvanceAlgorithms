from collections import deque
def logestSubSeries(str1,str2):
    return True

def getLIS(arr):
    # arr = [0, 2, 4, 6, 5, 7, 8, 10]
    # arr = [0, 2, 4, 6, 5, 7,-1, 12, 10]
    l2 = len(arr)
    # q = deque()
    LIS=[]
    lengthLIS=[]
    first = arr[0]
    LIS.append([first])
    lengthLIS.append(1)
    for i in range(1, l2):
        temp = [arr[i]]
        print(arr[i])
        maxLength = 0
        for x in LIS:
            if arr[i] >= x[-1]:
               temp = x + temp
               print(temp)
               LIS.append(temp)
               temp = [arr[i]]
    for x in LIS:
        if len(x) > 1:
            print(x)


if __name__ == '__main__':
    arr = [4,6,7,7]
    getLIS(arr)
    # 23G456K 23G45JK
    # str1 = '1A2BD3G4H56JK'
    # str2 = '23EFG4I5J6K7'
    # # str1 = 'belong'
    # # str2 ='cnblogs'
    # l1 = len(str1)
    # l2 = len(str2)
    # p = deque()
    # q1 = deque()
    # q2 = deque()
    # index = 0
    # for i in range(l1):
    #     for j in range(l2):
    #         if str1[i] == str2[j]:
    #             p.append(str1[i])
    #             q1.append(i)
    #             q2.append(j)
    # print(p)
    # print(q1)
    # print(q2)
