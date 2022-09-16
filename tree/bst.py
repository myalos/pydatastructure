# 这个是得到n个不同结点组成的BST有多少个 以及所有的BST
# 还有验证二叉树是BST 98题
# 和原来的BST 换过两个结点之后，还原成BST 99题
# 这是源自于力扣95 和 96两道题
from utils import *


class BST:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        '''
            Args: root 树的根
                  low  要保留的结点值必须大于等于low
                  high 要保留的结点值必须小于等于high
        '''
        def dfs(node, fa):
            # fa是node的父结点
            if not node:
                return
            if node.val < low:
                fa.left = node.right
                dfs(node.right, fa)
            elif node.val > high:
                fa.right = node.left
                dfs(node.left, fa)
            else:
                dfs(node.left, node)
                dfs(node.right, node)

        while root and (root.val < low or root.val > high):
            root = root.right if root.val < low else root.left

        dfs(root, None)
        return root


    def trimBST2(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 这个版本是迭代的来自
        # https://leetcode.cn/problems/trim-a-binary-search-tree/solution/by-ac_oier-help/
        # 迭代法的依据是　根结点的val如果是在low和high之间的，那么根结点的左子树一定全部是小于high的,右边的也全部都是
        # 所以对于根节点的左子树　一次迭代最左边就行了
        while root and (root.val < low or root.val > high):
            root = root.right if root.val < low else root.left
        ans = root
        while root:
            while root.left and root.left.val < low:
                root.left = root.left.right
            root = root.left
        root = ans
        while root:
            while root.right and root.right.val > high:
                root.right = root.right.left
            root = root.right
        return ans


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

    def sortedArrayToBST(self, nums : List[int]) -> Optional[TreeNode]:
        '''
            function:
                将已经是升序的序列转换成一棵高度平衡的二叉搜索树
            date:
                2022-09-12
            Args:
                nums : 已经升序的数组
            Return:
                转换后的二叉搜索树
            Comments:
                可能有多个结果，这个是根据之前从前序和中序还原二叉树的题目的灵感而来的代码
        '''
        n = len(nums)

        def buildBST(left_index, right_index):
            if left_index > right_index:
                return None
            root_index = (left_index + right_index) // 2
            root = TreeNode(nums[root_index])
            root.left = buildBST(left_index, root_index - 1)
            root.right = buildBST(root_index + 1, right_index)
            return root
        return buildBST(0, n - 1)

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        '''
            function:
                将升序的单链表转换成平衡的二叉搜索树
            date:
                2022-09-12
            Args:
                head 升序的单链表
            Return:
                构造出的平衡二叉树
            Comments:
                这个相对于上面一题就是链表不能随机查找，一种方法就是把链表转换成数组然后用上面一题的方法，也可以用快慢指针来找链表的中点
        '''
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        self.sortedArrayToBST(nums)


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
    root = array2tree('[3,0,4,null,2,null,null,null,null,1]')
    sol = BST()
    temp = tree2array(root)
    print(temp)
    ans = sol.trimBST(root, 1, 3)
    print(tree2array(ans))


