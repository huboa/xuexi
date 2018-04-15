"""
pip install flask
pip3 install flask
"""

from flask import Flask
# 1. 实例化Flask对象
app = Flask('xxxx')

"""
1. 执行 app.route('/index')并获取返回值 xx
2. 
    @xx
    def index():
        return 'Hello World'
3. 执行 index = xx(index)
本质： 
    {
        '/index': index
    }
"""
@app.route('/index')
def index():
    return 'Hello World'

@app.route('/host')
def host():
    return 'Hello World host'


if __name__ == '__main__':
    app.run()
