class newNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0

def LRview(root, side):
    if root is None:
        return
    q = [(root, 0)]
    res = dict()
    while len(q):
        node, level = q.pop(0)
        if level not in res:
            res[level] = []
        res[level].append(node.data)
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
            
    if side == "L":
        print("\n Left view")
    else:
        print("\n Right View")
    for k in res.keys():
        if side == "L":
            print(res[k][0], end=" ")
        elif side == "R":
            print(res[k][-1], end=" ")

# Driver Code
if __name__ == '__main__':
    root = newNode('A')
    root.left = newNode('B')
    root.right = newNode('C')
    root.left.left = newNode('D')
    root.left.right = newNode('E')
    root.right.left = newNode('F')
    root.right.right = newNode('G')
    LRview(root, "L")
    LRview(root, "R")
