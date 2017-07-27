#作业说明
##目录说明
    ├─ pysql.py         // PySQL程序主文件
    ├─ data             // 存储数据的目录
    │  ├─ user          // 存储用户信息文件
    │  └─ user.frm      // 存储用户文件的字段
    ├─ PySQL.png        // PySQL程序流程控制图
    └─ readme.md        // 程序说明文件
## 运行环境
    Python 3.6.1
## 功能介绍
    1.PySQL程序
        * 涉及文件：pysql.py user user.frm
        * 程序暂没做登录操作,可直接运行pysql.py文件执行程序
        * 程序说明：
            - PySQL系统分为增删改查四个模块
            - 提供对应的模拟数据库与数据表文件名称：data.user
            - 程序支持`>` `<` `=` `>=` `<=` 比较运算符, `and` `or` `not`逻辑运算符
            - 实现了与MySQL相同的字段选择性操作、`where`、`like`、`limit`等等，具体操作可参考使用示例
            - 程序暂不支持 '!='运算符 如：`name!=rain` 可用 `not name = rain` 实现
        * 程序使用示例：
            - `insert into data.user values (roll,15,18805475945,CEO,2017-07-19);`
            - `insert into data.user values (roll,15,18805475946,CEO,2017-07-19),(rain,18,13565248795,CTO,2017-07-19);`
            - `delete from data.user where id>4 and not name=rain;`
            - `update data.user set age=16,dept=CTO where id=2;`
            - `select * from data.user;`
            - `select id,name,age from data.user where id>1 and not id=2 or name='lucy' or dept like Python limit 2;`   
##博客地址
    [我的博客](https://www.loyous.com/index.php/archives/16/)





