from typing import List


def rectangleArea(rectangles: List[List[int]]) -> int:
    '''
        function:
            计算平面中所有矩形所覆盖的总面积，返回10**9 + 7后的模
        date:
            2022-09-16
        Args:
            rectangles 每个元素代表一个元素，每个元素包含x1, y1, x2, y2，前面两个点是左下角的坐标，后面两个点是右上角的坐标
        Return:
            覆盖的面积模上10 ** 9 + 7
        Comments:
            这个是第850题，不会做啊
            如果只有一个矩形的话，那么面积好求，两个矩形的话相交的面积也好求，不过3个矩形的话可能需要3个原始面积-3个两两相交的面积+三个相交的面积。当3个以上了复杂度就增加了
    '''
    pass
