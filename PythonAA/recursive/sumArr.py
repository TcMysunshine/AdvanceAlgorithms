def sumArr(n):
    if n<=1:
        return 0
    else:
        return sumArr(n-1)+2
# 0 2 4 6 8
if __name__=='__main__':
    print(sumArr(8))