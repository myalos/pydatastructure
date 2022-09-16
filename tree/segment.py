from utils import *


# 2022-09-16写完
# 这个里面是线段树相关的代码，最初是做了力扣307题想写个线段树的代码
# 有一个数组版本的线段树
# build(p, l, r)
# 是在数组索引p上构造范围是[l, r]的线段树
class SegmentTree:
    def __init__(self, array = [], mode = 'SUM'):
        self.mode = mode
        self.root = None
        self.n = len(array)
        if self.n:
            self.buildSegmentTree(array)


    def buildSegmentTree(self, nums: List[int]):
        '''
            function:
                根据数组nums来构造一个线段树
            date:
                2022-09-16
            Args:
                nums 数组
        '''
        def buildTree(left_index, right_index):
            if left_index == right_index:
                # 只有一个结点的时候
                return SegmentTreeNode(nums[left_index], left_index, right_index)
            mid = (left_index + right_index) // 2
            root = SegmentTreeNode(l = left_index, r = right_index)
            root.left  = buildTree(left_index, mid)
            root.right = buildTree(mid + 1, right_index)
            if self.mode == 'SUM':
                root.val = root.left.val + root.right.val
            return root
        self.root = buildTree(0, self.n - 1)

    def update(self, index: int, val: int) -> None:
        assert 0 <= index <= self.n
        st = [] # 用来装遍历过程中的路径，当更新完叶结点之后就更新从根结点到叶子结点路径上面（除了叶子结点外）所有结点
        p = self.root
        while True:
            if p.l == p.r:
                p.val = val
                break
            mid = (p.l + p.r) // 2
            st.append(p)
            if index <= mid:
                p = p.left
            else:
                p = p.right
        while st:
            node = st.pop()
            if self.mode == 'SUM':
                node.val = node.left.val + node.right.val

    def range(self, left: int, right: int) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if left <= node.l and node.r <= right:
                if self.mode == 'SUM':
                    ans += node.val
                    return
            mid = (node.l + node.r) // 2
            # [node.l, mid] [mid + 1, node.r]
            if left <= mid:
                dfs(node.left)
            if right > mid:
                dfs(node.right)
        dfs(self.root)
        return ans


if __name__ == '__main__':
    nums = [1, 3, 5]
    tree = SegmentTree(nums)
    print(tree.range(0, 2))
    tree.update(1, 2)
    print(tree.range(0, 2))

