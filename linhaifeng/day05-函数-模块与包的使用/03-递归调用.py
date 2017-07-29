###递归调用：在调用一个函数过程中，直接或间接地调用函数
def func():
    print('from func')
    yield
    func()

func()