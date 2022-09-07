# 这个文件里面放着工具函数
from collections import deque
from typing import *
import enum
from collections import deque


class TreeNode:
    '''
        力扣常用的树的class
    '''

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree2array(root: Optional[TreeNode]) -> str:
    '''
        Function:   convert tree structure to list
        Args:    root TreeNode object
        Returns: list representing tree structure
    '''
    res = list()
    if not root:
        return res
    # TreeNode 和 这个node的结点标号(根节点的编号是1)
    q = deque([(root, 1)])
    cnt = 1
    while q:
        node, index = q.popleft()
        # 下面的while是补齐两个node之间的null
        while cnt < index:
            res.append('null')
            cnt += 1
        res.append(str(node.val))
        cnt += 1
        if node.left:
            q.append((node.left, 2 * index))
        if node.right:
            q.append((node.right, 2 * index + 1))
    return '[' + ','.join(res) + ']'


def array2tree(arr: str) -> TreeNode:
    '''
        Function: convert tree list to tree structure
        Args: arr tree structre represented by list
        Returns: tree structure
    '''
    if arr == '[]':
        return None
    # 去掉两边的方括号
    data = arr[1:-1]
    nodes = data.split(',')
    n = len(nodes)
    # 这个是以index 0开始 来进行树的构造
    root = TreeNode(int(data[0]))
    q = deque([(root, 0)])
    while q:
        node, node_index = q.popleft()
        if 2 * node_index + 1 < n and nodes[2 * node_index + 1] != 'null':
            node.left = TreeNode(int(nodes[2 * node_index + 1]))
            q.append((node.left, 2 * node_index + 1))
        if 2 * node_index + 2 < n and nodes[2 * node_index + 2] != 'null':
            node.right = TreeNode(int(nodes[2 * node_index + 2]))
            q.append((node.right, 2 * node_index + 2))
    return root


class IndexType(int, enum.Enum):
    ZEROINDEX = 0
    NONZEROINDEX = 1


def isArrayTree(array, index_type = IndexType.NONZEROINDEX) -> bool:
    """
        array: 待检测的数组
        index_type: 数组的根节点是0还是1
    """
    if not isinstance(array, (list, tuple)):
        raise TypeError("the first parameter must be list or tuple")
    if not isinstance(index_type, IndexType):
        raise TypeError("The second parameter must be IndexType")
    num = len(array)
    # valid 数组为1的地方表示这个地方是节点，为0的地方表示这个地方不是节点
    valid = [0] * num
    root_index = int(index_type)
    q = deque()
    q.append(root_index)

    while len(q) > 0:
        index = q.popleft()
        if index < num and array[index] > 0:
            valid[index] = 1
            q.append(2 * index + 1 - root_index)
            q.append(2 * index + 2 - root_index)

    for i in range(num):
        if valid[i] and array[i] == 0:
            return False
        if not valid[i] and array[i] != 0:
            return False
    return True


def test():
    """TODO: Docstring for test.
    :returns: TODO

    """
    print(isArrayTree([1, 3, 4, 0, 0, 2, 0], IndexType.ZEROINDEX))


if __name__ == "__main__":
    t = TreeNode(1)
    t1 = TreeNode(2)
    t.right = t1
    t2 = TreeNode(3)
    t1.right = t2
    t3 = TreeNode(4)
    t2.right = t3
    arr = tree2array(t)
    print(arr)
    new_t = array2tree(arr)
    arr2 = tree2array(new_t)
    print(arr2)
