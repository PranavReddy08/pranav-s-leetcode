class newNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0

def level_order(root):
    if root == None:
        return
    q = [(root, 0)]
    m = dict()
    while len(q):
        node, lvl = q.pop(0)
        if lvl not in m:
            m[lvl] = []
        m[lvl].append(node.data)
        if node.left:
            q.append((node.left, lvl + 1))
        if node.right:
            q.append((node.right, lvl + 1))
    print("Level_Order")
    for lvl in m:
        print(m[lvl], end=" ")

def vertical_order(root):
    m = {}
    q = [(root, 0)]
    while q:
        node, hd = q.pop()
        if hd not in m:
            m[hd] = []
        m[hd].append(node.data)
        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))
    print("\nVertical_order")
    for hd in sorted(m):
        print(m[hd], end=" ")


root = newNode('A')
root.left = newNode('B')
root.right = newNode('C')
root.left.left = newNode('D')
root.left.right = newNode('E')
root.right.left = newNode('F')
root.right.right = newNode('G')

level_order(root)
vertical_order(root)
