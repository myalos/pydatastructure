# 这个文件里面放着工具函数
from collections import deque
from IPython import embed
from typing import *
import enum
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    '''
        力扣常用的树的class
    '''

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 因为线段树除了最后一层以外是一个完全二叉树，所以也可以用数组来存线段树的结点，index从1开始，对于index的左子树和右子树，其index分别为2 * index和2 * index + 1
class SegmentTreeNode(TreeNode):
    '''
        线段树的数据结构
    '''
    def __init__(self, val = 0, l = None, r = None, left = None, right = None):
        super().__init__(val, left, right)
        self.l = l
        self.r = r


def isBalanced(root: Optional[TreeNode]) -> bool:
    '''
        function:
            查看二叉树是否是平衡二叉树
        date:
            2022-09-13
        Args:
            root 二叉树的根节点
        Return:
            该二叉树是否是平衡二叉树
        Comments:
            这个是力扣的110题
    '''
    def dfs(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        nonlocal ans
        left = dfs(node.left)
        right = dfs(node.right)
        if abs(left - right) > 1:
            ans = False
        return 1 + max(left, right)
    ans = True
    dfs(root)
    return ans


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    '''
        function:
            判断二叉树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和targetSum
        date:
            2022-09-13
        Args:
            root 二叉树的根节点
            targetSum 目标和
        Return:
            是否存在
        Comments:
            这个是力扣的112题
    '''
    def dfs(node, _sum):
        if not node:
            return False
        tot = node.val + _sum
        if node.left is None and node.right is None:
            return tot == targetSum
        return dfs(node.left, tot) or dfs(node.right, tot)
    return dfs(root, 0)


def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    # 这个是力扣的的113题，2020年做过这道题，那个时候耗时是44ms，现在做是380ms
    from copy import deepcopy
    ans = []
    #　列表作为参数　要小心
    def dfs(node, _sum, path):
        if not node:
            return
        tot = node.val + _sum
        # 如果用new_path = path + [node.val] 而不用deepcopy的话
        # 速度会从380ms变成44ms
        path.append(node.val)
        if node.left is None and node.right is None and targetSum == tot:
            ans.append(path)
            return
        dfs(node.left, tot, deepcopy(path))
        dfs(node.right, tot, deepcopy(path))
    dfs(root, 0, [])
    return ans


def flatten(root: Optional[TreeNode]) -> None:
    '''
        function:
            将二叉树按先序遍历的形式转化成链表
        date:
            2022-09-15
        Args:
            root 二叉树的根结点
        Comments:
            这是力扣114题，需要原地进行转换，链表是以树结点的right来连接的
    '''
    if not root:
        return
    def dfs(node):
        if not node:
            return
        nonlocal head
        head.right = TreeNode(node.val)
        head = head.right
        dfs(node.left)
        dfs(node.right)
    head = TreeNode(0)
    ans = head
    dfs(root)
    # 如果直接root等于ans是不行的，因为函数的实参经过flatten之后还是不变的
    root.left = None
    root.right = ans.right.right


pre = None


def flatten2(root: Optional[TreeNode]) -> None:
    # 这个是原地的版本
    global pre
    if not root:
        return
    flatten2(root.right)
    flatten2(root.left)
    root.left = None
    root.right = pre
    pre = root


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


def buildTreeFromPI(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    '''
        function:
            从先序和中序的序列中还原二叉树
        date:
            2022-09-10
        Args:
            preorder 先序序列
            inorder 中序序列
        Return:
            构造好的二叉树
        Comments:
            这个是来自力扣105题
            找根据结点的时候还要遍历一遍列表
            这个速度比较慢，原因之一是每个结点都会新建4个list和1个set
    '''
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    index = 0
    n = len(inorder)
    while index < n:
        if inorder[index] == preorder[0]:
            break
        index += 1
    left_inorder = inorder[:index]
    lookup = set(left_inorder)
    right_inorder = inorder[index+1:]
    index = 1
    while index < n:
        if preorder[index] not in lookup:
            break
        index += 1
    left_preorder = preorder[1:index]
    right_preorder = preorder[index:]
    root.left = buildTreeFromPI(left_preorder, left_inorder)
    root.right = buildTreeFromPI(right_preorder, right_inorder)
    return root


def buildTreeFromPI2(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # https://leetcode.cn/submissions/detail/361328300/
    # 优点在于没有新建树，也没有用set来确定子树的位置
    def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int) -> Optional[TreeNode]:
        if preorder_left > preorder_right:
            return None
        preorder_root = preorder_left
        inorder_root = lookup[preorder[preorder_root]]
        root = TreeNode(preorder[preorder_root])
        left_subtree_size = inorder_root - inorder_left
        root.left = myBuildTree(preorder_left + 1, preorder_left + left_subtree_size, inorder_left, inorder_root - 1)
        root.right = myBuildTree(preorder_left + 1 + left_subtree_size, preorder_right, inorder_root + 1, inorder_right)
        return root
    n = len(preorder)
    lookup = {inorder[i] : i for i in range(n)}
    return myBuildTree(0, n - 1, 0, n - 1)


def buildTreeFromIP(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    '''
        function:
            从后序和中序的序列中还原二叉树
        date:
            2022-09-10
        Args:
            postorder 后序序列
            inorder 中序序列
        Return:
            构造好的二叉树
        Comments:
            这个是来自力扣106题
            这个就是根据上面的方法写的
            我发现我之前写的C++版本的代码也是用的这个方法
    '''
    def myBuildTree(inorder_left: int, inorder_right: int, postorder_left: int, postorder_right: int) -> Optional[TreeNode]:
        if inorder_left > inorder_right:
            return None
        # 首先先确定根结点的索引
        postorder_root = postorder_right
        inorder_root = lookup[postorder[postorder_root]]
        left_subtree_size = inorder_root - inorder_left
        root = TreeNode(postorder[postorder_root])
        root.left = myBuildTree(inorder_left, inorder_root - 1, postorder_left, postorder_left + left_subtree_size - 1)
        root.right = myBuildTree(inorder_root + 1, inorder_right, postorder_left + left_subtree_size, postorder_root - 1)
        return root
    n = len(inorder)
    lookup = {inorder[i] : i for i in range(n)}
    return myBuildTree(0, n - 1, 0, n - 1)


def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    '''
        function:
            检查p和q的两个二叉树是否是相同的
        date:
            2022-09-10
        Args:
            p 一个二叉树的根结点
            q 另一个二叉树的根结点
        Return:
            p和q是否是相同的二叉树
    '''
    if not p and not q:
        return True
    if p and not q or q and not p:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    '''
        function:
            检查root为根的子节点是否是对称二叉树
        date:
            2022-09-10
        Args:
            root 一个二叉树的根结点
        Return:
            这个二叉树是否是对称二叉树
    '''
    if not root:
        return True
    def checkSymmetric(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return checkSymmetric(p.left, q.right) and checkSymmetric(p.right, q.left)
    return checkSymmetric(root.left, root.right)


# 下面的代码是最早写的,　忘记是哪天写的了
class IndexType(int, enum.Enum):
    ZEROINDEX = 0
    NONZEROINDEX = 1


def isArrayTree(array, index_type = IndexType.NONZEROINDEX) -> bool:
    """
        Args:
            array: 待检测的数组
            index_type: 数组的根节点是0还是1
        Return:
            bool 是否是数组树
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
    root = '[1,2,5,3,4,null,6]'
    root = array2tree(root)
    flatten(root)
