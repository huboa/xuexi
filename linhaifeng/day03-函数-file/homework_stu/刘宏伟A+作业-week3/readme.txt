一、博客
    http://www.cnblogs.com/liuxiaowei/
二、作业需求
    当然此表你在文件存储时可以这样表示
    1、 1,AlexLi,22,13651054608,IT,2013-04-01
    现需要对这个员工信息文件，实现增删改查操作

        1、可进行模糊查询，语法至少支持下面3种:
    　　2、select name,age from staff_table where age > 22
    　　3、select  * from staff_table where dept = 'IT'
        4、select  * from staff_table where enroll_date like '2013'
    1、查到的信息，打印后，最后面还要显示查到的条数
    2、可创建新员工纪录，以phone做唯一键，staff_id需自增
    3、可删除指定员工信息纪录，输入员工id，即可删除
    4、可修改员工信息，语法如下:
    　　1、update staff_table SET dept='Market' WHERE where dept = 'IT'

三、作业实现
    作业1：
        管理数据操作实现主要运用了函数还有os模块进行文件的删除以及修改名字，以及linecache模块获取文件的最后一行内容，以实现了
        作业中的查、增、更新、删除操作，目前所有条件只能为一个字段条件,程序中主要把每一行转换为字典进行操作
        一、程序中用到的所有语句均为小写且只识别单引号，并且用空格格开
        二、查询功能
            1、支持查询所有字段，有条件和没有条件的形式且语句为小写
            2、条件分为字符条件运算符为=、！=、like
            3、数字类型运算符为=、<、>、=、！=、like
            4、实现了查询出后统计条数功能
            4、查询所有字段没有条件语句示例:
                select * from staff_table
            5、查询所有字段没有条件语句示例 ：
                select * from staff_table where name like 'Ale'
                select  * from staff_table where dept = 'IT'
                select  * from staff_table where enroll_date like '2013'
            6、查询指定字段有条件语句示例 ：
                select staff_id,name,age from staff_table where staff_id = 1
                select name,age from staff_table where age > 22
        三、新增创建功能
            1、目前新增只允许小写，并且只能用values后跟()形式新增，并且必须按字段顺序进行值增加，名字中间不能用空格
            2、完成了如果手机号存在提示无法进行注册功能
            3、完成了id自增功能
            4、语句形式：
                insert into staff_table values('LiuXiaowei',23,123456789,'IT','2014-10-55')
        四、删除功能
            1、可以按字段的的=、<、>、=、！=、like进行删除如下 ：
            2、条件分为字符条件运算符为=、！=、like
                 delete from staff_table where name like 'Jack'
            3、数字类型运算符为=、<、>、=、！=、like
                delete from staff_table where staff_id = 1
                delete from staff_table where age < 30
        五、更新
            1、更新实了对一个字段的条件和一个字段的更新
            1、可以按字段的的=、<、>、=、！=、like进行更新
            2、条件分为字符条件运算符为=、！=、like
                 update staff_table set dept = 'IT' where name like 'Jack'
            3、数字类型运算符为=、<、>、=、！=、like
                update staff_table set dept = 'Market' where age like 30
                update staff_table set dept = 'Market' where dept = 'IT'
                update staff_table set dept = 'IT' where age > 30



        