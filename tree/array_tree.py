# 这里用数组来模拟二叉树

# 数组中0表示空，大于0的数表示二叉树节点上的值

# [1, 0, 2] 表示有两个节点的二叉树，其中值为2的节点是值为1的节点的右子数

# 对于以1为根节点索引的二叉树，任意节点x 其左子树节点索引是2x 其右子树节点索引是2x + 1，其父节点索引是x // 2

# 对于以0为根节点索引的二叉树，任意节点x 其左子树节点索引是2(x + 1) - 1 = 2x + 1 其右子树节点索引是 2(x + 1) + 1 - 1 = 2x + 2 其父节点是(x - 1) // 2
from utils import *
from typing import Tuple, List

class ArrayBinaryTree:
    def __init__(self, array : [List, Tuple], arrayType : IndexType):
        if not isArrayTree(array, arrayType):
            raise ValueError("invalid array tree")
        self.data = array
        self.index_type = arrayType

    def __len__(self):
        return self.num

def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    a = ArrayBinaryTree([4, 0, 1, 0, 2, 3], IndexType.ZEROINDEX)


if __name__ == "__main__":
    main()
