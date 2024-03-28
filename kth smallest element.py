import heapq
def ksmall(l,k):
    heapq.heapify(l)
    for i in range(k):
        r=heapq.heappop(l)
    return r
l=list(map(int,input().split()))
k=int(input())
print(ksmall(l,k))
