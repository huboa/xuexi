http://www.cnblogs.com/jnbb/p/7388811.html

学生视图：只能注册，选择学校，关联班级，查看

老师视图：可以查看学员，班级，修改学生成绩，查看成绩

管理视图：可以在某个学校里分别创建课程，创建班级，班级绑定课程，创建老师绑定班级

创建学校视图：只创建学校

缺点：学员可以只可以查看成绩，注册，不能修改个人信息（学员模块因为时间的关系，写的比较仓促，其他视图几乎都完成了各个功能）

先创建学校
再进入管理视图创建课程、班级、老师
最后学生注册，绑定班级
老师修改分数
学生查看
初始数据如下：
学校：北京
老师：egon	工资：3000000	班级：['1']
老师：egg	工资：3000000	班级：['2']

班级：1	课程：python
班级：2	课程：linux

课程：python	价格：10000	周期：30周
课程：linux	价格：20000	周期：30周

班级：1	课程：python	学员:['glj']
班级：2	课程：linux	学员:['gelujing']

姓名：glj	年龄：23	分数：90
姓名：gelujing	年龄：22	分数：99

学校：上海
课程：go	价格：40000	周期：30周
班级：1	课程：go
老师：alex	工资：5000000	班级：['1']
班级：1	课程：go	学员:['xmv']
姓名：xmv	年龄：21	分数：98

创建学校：
welcome
	1.学生视图
	2.老师视图
	3.管理视图
	4.创建学校
	q.退出
请输入要选择的视图>>>4
创建的学校北京


管理视图：
welcome
	1.学生视图
	2.老师视图
	3.管理视图
	4.创建学校
	q.退出
请输入要选择的视图>>>3
北京
选择学校>>>北京
==欢迎来到北京校区==
添加课程 add_course
添加班级 add_class
添加老师 add_teacher
查看课程 check_course
查看班级 check_class
查看老师 check_teacher
退出 exit
输入要操作的命令>>>add_course
请输入要添加课程的名称>>>python
请输入要添加课程的价格>>>10000
请输入要添加课程的周期>>>30
创建课程 python 完成
==欢迎来到北京校区==
添加课程 add_course
添加班级 add_class
添加老师 add_teacher
查看课程 check_course
查看班级 check_class
查看老师 check_teacher
退出 exit
输入要操作的命令>>>add_course
请输入要添加课程的名称>>>linux
请输入要添加课程的价格>>>20000
请输入要添加课程的周期>>>40
创建课程 linux 完成
==欢迎来到北京校区==
添加课程 add_course
添加班级 add_class
添加老师 add_teacher
查看课程 check_course
查看班级 check_class
查看老师 check_teacher
退出 exit
输入要操作的命令>>>add_class
请输入要添加班级的名称>>>1
请输入要关联的课程>>>python
创建班级 1 成功，关联课程为 python
==欢迎来到北京校区==
添加课程 add_course
添加班级 add_class
添加老师 add_teacher
查看课程 check_course
查看班级 check_class
查看老师 check_teacher
退出 exit
输入要操作的命令>>>add_class
请输入要添加班级的名称>>>2
请输入要关联的课程>>>linux
创建班级 2 成功，关联课程为 linux
==欢迎来到北京校区==
添加课程 add_course
添加班级 add_class
添加老师 add_teacher
查看课程 check_course
查看班级 check_class
查看老师 check_teacher
退出 exit
输入要操作的命令>>>add_teacher
请输入要添加老师的名字>>>egon
请输入要添加老师的工资>>>3000000
请输入要关联的班级>>>1
创建老师 egon 成功，关联班级为 1
==欢迎来到北京校区==
添加课程 add_course
添加班级 add_class
添加老师 add_teacher
查看课程 check_course
查看班级 check_class
查看老师 check_teacher
退出 exit
输入要操作的命令>>>add_teacher
请输入要添加老师的名字>>>egg
请输入要添加老师的工资>>>300000
请输入要关联的班级>>>2
创建老师 egg 成功，关联班级为 2
==欢迎来到北京校区==
添加课程 add_course
添加班级 add_class
添加老师 add_teacher
查看课程 check_course
查看班级 check_class
查看老师 check_teacher
退出 exit
输入要操作的命令>>>check_course
课程：python	价格：10000	周期：30周
课程：linux	价格：20000	周期：40周
==欢迎来到北京校区==
添加课程 add_course
添加班级 add_class
添加老师 add_teacher
查看课程 check_course
查看班级 check_class
查看老师 check_teacher
退出 exit
输入要操作的命令>>>check_class
班级：1	课程：python
班级：2	课程：linux
==欢迎来到北京校区==
添加课程 add_course
添加班级 add_class
添加老师 add_teacher
查看课程 check_course
查看班级 check_class
查看老师 check_teacher
退出 exit
输入要操作的命令>>>check_teacher
老师：egon	工资：3000000	班级：['1']
老师：egg	工资：300000	班级：['2']
==欢迎来到北京校区==
添加课程 add_course
添加班级 add_class
添加老师 add_teacher
查看课程 check_course
查看班级 check_class
查看老师 check_teacher
退出 exit







学生视图：
welcome
	1.学生视图
	2.老师视图
	3.管理视图
	4.创建学校
	q.退出
请输入要选择的视图>>>1
北京
上海
退出q
选择学校>>>北京
请输入学生姓名>>>glj
请输入学生年龄>>>23
班级：1	课程：python	价格：10000	周期：30月
班级：2	课程：linux	价格：20000	周期：40月
请输入要加入的班级>>>1
请输入要交的学费>>>10000
学生 glj 注册成功
北京
上海
退出q
选择学校>>>北京
请输入学生姓名>>>gelujing
请输入学生年龄>>>23
班级：1	课程：python	价格：10000	周期：30月
班级：2	课程：linux	价格：20000	周期：40月
请输入要加入的班级>>>2
请输入要交的学费>>>20000
学生 gelujing 注册成功
北京
上海
退出q
选择学校>>>北京
请输入学生姓名>>>glj
姓名：glj	年龄：23	分数：90
北京
退出q
选择学校>>>




老师视图
welcome
	1.学生视图
	2.老师视图
	3.管理视图
	4.创建学校
	q.退出
请输入要选择的视图>>>2
北京
上海
选择学校>>>上海
请输入老师姓名>>>egon
请输入正确老师名
北京
上海
选择学校>>>北京
请输入老师姓名>>>egon
查看班级 check_class
修改学生分数 update_score
查看学生分数 check_student_score
退出 exit
输入要操作的命令>>>check_class
班级：1	课程：python	学员:['glj']
查看班级 check_class
修改学生分数 update_score
查看学生分数 check_student_score
退出 exit
输入要操作的命令>>>update_score
请输入班级名>>>1
请输入学生姓名>>>glj
请输入学生分数>>>90
班级：1	学生：glj	分数：90
查看班级 check_class
修改学生分数 update_score
查看学生分数 check_student_score
退出 exit
输入要操作的命令>>>check_student_score
请输入班级名>>>1
请输入学生姓名>>>glj
班级：1	学生：glj	分数：90
查看班级 check_class
修改学生分数 update_score
查看学生分数 check_student_score
退出 exit
输入要操作的命令>>>






