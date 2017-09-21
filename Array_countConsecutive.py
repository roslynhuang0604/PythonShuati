def countConsecutive(N):
    count = 0
    L = 1
    while( L * (L + 1) < 2 * N):
        a = (1.0 * N - (L * (L + 1) ) / 2) / (L + 1)
        if ( abs(a - int(a)) == 0.0):
            count += 1
        L += 1
    return count

# Driver code

N = 15
print countConsecutive(N)
# N = 10
# print countConsecutive(N)




