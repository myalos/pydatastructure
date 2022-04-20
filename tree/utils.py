# 这个文件里面放着工具函数
import enum
from collections import deque

class IndexType(int, enum.Enum):
    ZEROINDEX = 0
    NONZEROINDEX = 1

def isArrayTree(array, index_type = IndexType.NONZEROINDEX) -> bool:
    """
        array: 待检测的数组
        index_type: 数组的根节点是0还是1
    """
    if not isinstance(array,(list, tuple)):
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
    print(isArrayTree([1,3,4,0,0,2,0], IndexType.ZEROINDEX))


if __name__ == "__main__":
    test()
