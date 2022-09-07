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


if __name__ == '__main__':
    sol = Solution()
    root = array2tree('[3,9,20,null,null,15,7]')
    ans = sol.maxDepth(root)
    print(ans)

