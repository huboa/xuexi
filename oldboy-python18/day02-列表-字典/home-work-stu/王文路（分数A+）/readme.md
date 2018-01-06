#作业说明
##目录说明
    ├─cart_new.py     购物车程序主文件
    ├─db.txt          存储用户信息文件
    ├─goods.txt       存储商品信息文件
    ├─record.log      购买记录日志
    ├─cart.png        购物车程序流程控制图
    ├─menu.py         三级联动菜单程序主文件
    ├─menu.png        三级联动菜单程序流程控制图
    └─readme.md       程序说明文件
## 运行环境
    Python 3.6.1
## 功能介绍
    1.购物车程序
        * 涉及文件：cart_new.py db.txt goods.txt record.log
        * 运行cart_new.py文件执行程序
        * 程序说明：
            - 本系统共分为五大模块：用户登录模块，购物模块，充值模块，购物车管理模块，结算模块
            - 登录时提供默认两组用户：username:lucy,password:123;username:road,password:321
            - 用户的充值，加入购物车以及结算行为均做了持久化存储并存在购买记录(record.log)
            - 系统中接收的用户数据均做了验证，具体操作可根据提示去做
            - 程序中自定义函数做了简要注释，说明了函数的整体功能
            - 程序小缺陷：结算时购物车里的商品将全部购买，若有修改可到购物车管理模块
    2.三级联动菜单
        * 涉及文件：menu.py 
        * 运行menu.py文件执行程序
        * 根据提示输入相应的省市获取下一级，输入b返回上一级,输入q退出查询      
##博客地址
    [我的博客](https://www.loyous.com/index.php/archives/13/)
    文章地址与上周一样，由于模块相同只在内容上做了补充





