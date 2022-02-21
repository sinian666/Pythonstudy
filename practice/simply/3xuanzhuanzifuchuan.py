# -*- coding :UTF-8 -*-
# @Time      :2022/2/19 12:33 AM
# @Author    :Si Nian
# @Software  :PyCharm
class Solution:
    def rotateString(self,s,offset):
        if len(s)>0:
            offset = offset % len(s)
        temp =(s+s)[len(s)-offset: 2 * len(s) -offset]
        for i in range (len(temp)):
            s[i] = temp[i]



#主函数
if __name__ == '__main__':
    s = ["a","b","c","d","e","f","g"]
    offset=3
    solution = Solution()
    solution.rotateString (s,offset)
    print("输入：s",["a","b","c","d","e","f","g"],"","offset =",offset)
    print("输入：s =",s)

