# 这个是二叉树的中序遍历，用的结构也是leetcode 二叉树的结构
#这个是源自于力扣的94题
from utils import *


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.method4(root)
        return self.ans

    def method1(self, root):
        '''
            最基础的方法: 递归
        '''
        if not root:
            return
        self.method1(root.left)
        self.ans.append(root.val)
        self.method1(root.right)

    def method2(self, root):
        '''
            邓公的方法
        '''
        # 将遍历过程分段，第一段是一直遍历左子树到头
        # 第二段是输出最左下子树的父结点然后开始将其右子树的结点作为一个新的epoch
        st = [root]
        while st:
            node = st[-1]
            while node.left:
                st.append(node.left)
                node = node.left
            while st:
                node = st.pop()
                self.ans.append(node.val)
                if node.right:
                    st.append(node.right)
                    break
        return


    def method4(self, root):
        '''
            这是邓公书上的代码
        '''
        st, ans = [], []
        while True:
            if root:
                st.append(root)
                root = root.left
            elif st:
                root = st.pop()
                ans.append(root.val)
                root = root.right
            else:
                break
        self.ans = ans


    def method3(self, root):
        '''
            用堆栈来模拟函数调用，将递归的方法强行转换成迭代的方法
            method3(root.left)
            print(root.val)
            method3(root.right)
        '''
        if not root:
            return
        # 第一个method3 相当于将root压栈
        # print相当于将root 吐出来
        # 第二method3 相当于将root压栈，因为后面root不需要，所以root就直接甩掉就行了
        if not root:
            return
        st = [(root, 0)]
        while st:
            node, times = st.pop()
            # times为0 就是第一次入栈
            if times == 0:
                if node.right:
                    st.append((node.right, 0))
                st.append((node, 1))
                if node.left:
                    st.append((node.left, 1))
            else:
                self.ans.append(node.val)


if __name__ == '__main__':
    sol = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.right = t2
    t2.left  = t3
    ans = sol.inorderTraversal(t1)
    print(ans)
