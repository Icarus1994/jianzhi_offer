# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        length = len(rotateArray)
        if length == 0:
            return 0
        elif length ==1:
            return rotateArray[0]
        fg = 0
        for i in range(length-1,0,-1):
            if rotateArray[i] < rotateArray[i-1]:
                fg = 1
                break
        if fg:
            return rotateArray[i]
        # 数组未旋转或者数组中所有元素相同时返回第一个元素
        else:
            return rotateArray[0]

list = [3,4,5,1,2]
list1 = [1,2,4,4,6]
solu = Solution()
print(solu.minNumberInRotateArray(list1))

# 题目描述
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0