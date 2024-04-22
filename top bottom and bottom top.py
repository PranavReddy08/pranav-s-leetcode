class newNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0

def level_order(root, order="TB"):
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
    if order == "TB":
        for lvl in m:
            print(m[lvl], end=" ")
    elif order == "BT":
        for lvl in sorted(m.keys(), reverse=True):  # Corrected the syntax
            print(m[lvl], end=" ")  # Fixed the indentation

root = newNode('A')
root.left = newNode('B')
root.right = newNode('C')
root.left.left = newNode('D')
root.left.right = newNode('E')
root.right.left = newNode('F')
root.right.right = newNode('G')
level_order(root)
level_order(root, "BT")  # Added missing closing parenthesis
