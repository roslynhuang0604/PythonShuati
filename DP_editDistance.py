def sendHealth(costs, startWord, endWord):
    # one of them of both of them are None, return -1
    if startWord is None or endWord is None:
        return -1
    # if they're the same words but in different orders, return cost for anagram
    elif sorted(startWord) == sorted(endWord):
        return costs[3]
    else:
        row = len(startWord) + 1 # row = 7
        col = len(endWord) + 1 # col = 6

        # M[i][j] represents the cost of transforming first i letters of startWord
        # to first j letters of endWord
        M = [[0 for i in range(col)] for j in range(row)]
        interim = [['' for i in range(col)] for j in range(row)]

        # base case: one of the string is empty(WLOG, say s1 is empty), then M[0][i] = i
        for i in range(1, row):
            for j in range(1, col):
                # when ith letter of startWord == jth letter of endWord: do nothing
                # replace ith letter of startWord with jth letter of endWord: M[i][j] = costs[2] + M[i-1][j-1]
                # add a letter to substring i: M[i][j] = costs[0] + M[i][j-1]
                # del a letter from i: M[i][j] = costs[1] + M[i-1][j]
                # print i, j
                if startWord[:i] == endWord[:j]:
                    M[i][j] = M[i - 1][j - 1]
                else:
                    M[i][j] = min(costs[2] + M[i-1][j-1],
                                  costs[0] + M[i][j-1],
                                  costs[1] + M[i-1][j])
                print M[i][j]
                # if M[i][j] == M[i-1][j-1]:
                # interim[i][j]
    return M[row - 1][col - 1]


costs = [1,3,1,5]
print sendHealth(costs, 'HEALTH', 'HANDS') # minimum cost for transfering HEALTH to HANDS
