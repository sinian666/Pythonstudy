#导入模块
import unittest
#声明类
class MyUnit(unittest.TestCase):
    # 测试用例方法，方法名必须以test开头
    def testaa(self):
        print("testaa方法")
    def testABC(self):
        print("testABC方法")
    def setUp(self):#每个测试用例方法执行之前调用
        print("setUp方法")
    def tearDown(self):#每个测试用例方法执行之后调用
        print("tearDown方法")

#启动框架
if __name__ == '__main__':  #下划线都是两个下划线
    unittest.main