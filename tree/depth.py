# 2022-09-07 这个是来算二叉树的最大深度
# 源自力扣104题
from utils import *


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return max(left + 1, right + 1)
        return dfs(root)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        '''
            function:
                求一个二叉树的最小深度
            date:
                2022-09-13
            Args:
                root　二叉树的根节点
            Return:
                二叉树最小深度
        '''
        # 下面代码的错误是单右子树　答案应该是结点的个数，而不是1
        # def dfs(node):
        #     if not root:
        #         return 0
        #     left  = dfs(node.left)
        #     right = dfs(node.right)
        #     return 1 + min(left, right)
        # 进行修改，对于只有一个孩子的结点返回其孩子的深度 + 1
        # 最快的方法是用的bfs，当发现第一个没有左孩子也没有右孩子的结点就直接返回
        def dfs(node):
            if not node:
                return 0
            left  = dfs(node.left)
            right = dfs(node.right)
            if not left:
                return 1 + right
            if not right:
                return 1 + left
            return 1 + min(left, right)
        return dfs(root)



if __name__ == '__main__':
    sol = Solution()
    root = array2tree('[3,9,20,null,null,15,7]')
    ans = sol.maxDepth(root)
    print(ans)

