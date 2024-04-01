import heapq
def find_cost(wires):
    heapq.heapify(wires)
    tot=0
    while len(wires)>1:
        w1=heapq.heappop(wires)
        w2=heapq.heappop(wires)
        tot +=(w1+w2)
        heapq.heappush(wires,(w1+w2))
        print(wires,tot)
    return tot
wires=list(map(int,input().split()))
ans=find_cost(wires)
print('ans :',ans)
