#8、在函数中输入3次，如果用户名是dingce密码
# 是123456就返回登录成功不再输入，如果3次都输入错误返回登录失败
def a():
    for i in range(0,3):
        b = input('请输入用户名：')
        c = input('请输入密码：')
        if b=='dingce'and c=='123456':#
            return'登陆成功'
    return'登陆失败'
s=a()
print(s)