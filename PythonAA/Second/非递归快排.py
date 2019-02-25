def quickSort(nums):
    if len(nums) == 1:
        return nums
    #初始化两个栈
    startStack = [0,]
    endStack = [len(nums)-1,]

    #进入循环，两个栈均为空时，排序结束
    while startStack and endStack:
        #得到本次循环的start 和 end
        start = startStack.pop()
        end = endStack.pop()
        #判断子数组是否有序
        if start>end:
            continue
        i = start
        j = end
        while i < j:
            if nums[i] > nums[j]:
                nums[i], nums[j-1], nums[j] = nums[j-1], nums[j], nums[i]
                j -= 1
            else:
                i += 1
        #将两个子数组的开始和结尾push进栈中
        startStack.append(start)
        endStack.append(i-1)
        startStack.append(i+1)
        endStack.append(end)


if __name__ =='__main__':
    while True:
        try:
            arr = [int(x) for x in input().split(' ')]
            quickSort(arr)
            print(' '.join([str(x) for x in arr]))
        except EOFError:
            break