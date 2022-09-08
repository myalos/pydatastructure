# 这个是得到n个不同结点组成的BST有多少个 以及所有的BST
# 还有验证二叉树是BST 98题
# 和原来的BST 换过两个结点之后，还原成BST 99题
# 这是源自于力扣95 和 96两道题
from utils import *


class BST:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 这题之前用C++做过，但是C++代码里面要考虑最小int和最大int，我有点忘了，感觉C++的情况可能要复杂一些
        # 一个结点对应一个以该结点为根结点的子树是否为
        # 这个可以用中序的递归遍历，然后在print的那里
        # if node.val <= pre:
        #     return False
        # pre = node.val
        def dfs(node):
            if not node:
                return True, None, None
            ret_flag, ret_value_max, ret_value_min = True, node.val, node.val
            left_flag, left_value_max, left_value_min = dfs(node.left)
            right_flag, right_value_max, right_value_min = dfs(node.right)
            if left_value_max:
                ret_flag = ret_flag and left_flag and left_value_max < node.val
                ret_value_max = max(ret_value_max, left_value_max)
                ret_value_min = min(ret_value_min, left_value_min)
            if right_value_max:
                ret_flag = ret_flag and right_flag and right_value_min > node.val
                ret_value_max = max(ret_value_max, right_value_max)
                ret_value_min = min(ret_value_min, right_value_min)
            return ret_flag, ret_value_max, ret_value_min
        return dfs(root)[0]


    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # 就是有BST中有两个结点的值互换了，要找到这两个互换的结点然后还原
        pass

    def numTrees(self, n: int) -> int:
        # 我印象中这是个递推的问题
        # 数是1--n BST根结点的数字决定左子树和右子树
        # 比如n = 9，根节点是5 那么左子树有4个结点 右边有4个结点
        # dp[i] 表示i个结点的BST个数
        dp = [0] * (1 + n)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # 我感觉这个解题思路和上面差不多
        # 也用dp来存中间结果
        dp = [[] for _ in range(n + 1)]
        dp[0].append(None)
        def copy(node, addition, targetNode):
            # 将node为根的树copy到targetNode为根的树上，targetNode中每个结点的值都是node每个结点的值加上addition
            if node.left:
                targetNode.left = TreeNode(node.left.val + addition)
                copy(node.left, addition, targetNode.left)
            if node.right:
                targetNode.right = TreeNode(node.right.val + addition)
                copy(node.right, addition, targetNode.right)
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                for left_node in dp[j - 1]:
                    for right_node in dp[i - j]:
                        root = TreeNode(j)
                        if left_node:
                            new_left = TreeNode(left_node.val)
                            copy(left_node, 0, new_left)
                            root.left = new_left
                        if right_node:
                            new_right = TreeNode(right_node.val + j)
                            copy(right_node, j, new_right)
                            root.right = new_right
                        dp[i].append(root)
        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numTrees(3))

