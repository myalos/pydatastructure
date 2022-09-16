# 这个是二叉树的层序遍历
from utils import *


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        # 这里确保queue里面全是有值的node
        if not root:
            return ans
        q = deque([root])
        while q:
            # 一层的结点放到这里面
            level = []
            cnt = len(q)
            while cnt:
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                cnt -= 1
            ans.append(level)
        return ans

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

if __name__ == '__main__':
    sol = Solution()
    root = array2tree('[3,9,20,null,null,15,7]')
    ans = sol.levelOrder(root)
    print(ans)
