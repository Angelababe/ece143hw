def get_tree_list(p):
    '''Given a random permutation, generate the corresponding rooted binary tree'''
    assert isinstance(p, list)
    dic = {}
    for val in p:
        assert isinstance(val, int)
        assert not val in dic
        dic[val] = 1
        
    root = Node(val = p[0])
    def placenode(node, v):
        if v>node.val:
            if node.right == None:
                node.right = Node(val = v)
                return
            else:
                placenode(node.right, v)
        else:
            if node.left == None:
                node.left = Node(val = v)
                return
            else:
                placenode(node.left, v)

    for val in p:
        placenode(root, val)

    ret = [0]*len(p)
    ret[root.val] = root.val
    def traverse(node):
        if node.left:
            ret[node.left.val] = node.val
            traverse(node.left)
        if node.right:
            ret[node.right.val] = node.val
            traverse(node.right)
    traverse(root)
    return ret

class Node:
    def __init__(self, val:int=0, left=None, right=None):
        assert isinstance(left,Node) or left is None
        assert isinstance(right,Node) or right is None
        self.val = val
        self.left = left
        self.right = right
