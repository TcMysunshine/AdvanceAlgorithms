x=[]
def getDPTable(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    dp = [[0 for col in range(l2 + 1)] for row in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            elif dp[i][j - 1] < dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
    return dp


def traceBack(str1, str2, i, j, lcs_str, dp):
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs_str += str1[i-1]
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            elif dp[i-1][j] < dp[i][j-1]:
                j -= 1
            else:
                traceBack(str1, str2, i-1, j, lcs_str, dp)
                traceBack(str1, str2, i, j-1, lcs_str, dp)
                return
    reverse_str = lcs_str[::-1]
    if reverse_str not in x:
        x.append(reverse_str)

if __name__ == '__main__':
    '''最长公共子序列'''
    # 23G456K 23G45JK
    # str1 = '1A2BD3G4H56JK'
    # str2 = '23EFG4I5J6K7'
    # str1 = 'belong'
    # str2 ='cnblogs'
    # str1 = '13542687'
    # str2 = '148675'
    str1 = input()
    str2 = input()
    # str1 = 'BDCABA'
    # str2 = 'ABCBDAB'
    dp = getDPTable(str1, str2)
    lcs_str = ''
    traceBack(str1, str2, len(str1), len(str2),lcs_str, dp)
    for temp in x:
        print(temp)

