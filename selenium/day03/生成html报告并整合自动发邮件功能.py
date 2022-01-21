from  day3_3.HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

#---------定义发送邮件--------------#
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户/密码
    user = 'beijingzhaoying@163.com'
    password = 'zy12345' #邮箱的授权码

    # 发送邮箱
    sender = 'beijingzhaoying@163.com'
    # 接收邮箱
    receiver = '1937138205@qq.com'

 #   msg = MIMEText(mail_body, 'html', 'utf-8')
    msg = MIMEText(mail_body, _subtype = 'html', _charset = 'utf-8')
    # 发送邮件主题
    subject = '自动化测试报告'
    msg['from'] = sender
    msg['to'] = receiver

    # 编写HTML类型的邮件正文

    msg['Subject'] = Header(subject, 'utf-8')

    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('email has send out!')

# ------------查找测试报告目录，找到最新生成的测试报告文件

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getatime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    #要执行的unittest框架的python文件的目录
    test_dir = 'E:\\py1\\day3_2'
    #测试报告保存的位置
    test_report = 'D:\\'
    #pattern是要执行的unittest框架的python文件名
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='RegLogUnit.py')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况:')

    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)  #发送测试报告

#整个程序的执行过程可以分为三个步骤
#1.通过unittest框架的discover()找到匹配测试用例,由HTMLTestRunner的run()方法执行测试用例并生成最新的测试报告
#2.调用new_report()函数找到测试报告目录（E盘)下最新生成的测试报告，返回测试报告的路径