class Solution:
    #定义一个参数：number
    #定义一个返回值：返回反转后的数字
    def reverseInteger(self,number):
        h = int (number/100)
        t = int (number%100/10)
        z = int (number%10)
        return (100*z+10*t+h)
#主函数
if __name__ == '__main__':
    solution = Solution()#调用函数
    num = 556#输入对应的3位整数
    ans = solution.reverseInteger(num)
    print("输入：",num)
    print("输出：",ans)