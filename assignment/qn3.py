def findDistinctOddsumm(n, k):
    # n can be represented as sum of k odds only if 
    # square of k is less than or equal to n and
    # n+k is even(both n and k are even OR both n and k are odd)
    if ((k * k) <= n and (n + k) % 2 == 0):
        print("YES")
    else:
        print("NO")
t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    findDistinctOddsumm(n,k)