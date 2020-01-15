class Mybug(BaseException): # 继承于异常基类BaseException的异常类
    pass


class Yourbug(BaseException):
    pass


try:  # 待执行
    print('Trying.')
    raise Yourbug("Oh ,NO!")
except Mybug as dtl:  # 假如Mybug错误没发生，执行
    print('Exception Mybug!:' + str(dtl))
except:  # 假如其他错误发生，执行
    print('Exception!')
else:  # 假如错误没发生，执行
    print('else.')
    pass
finally:  # 不管错误发没发生，都执行
    print('finally')
    pass
print('other.')  # 正常执行
