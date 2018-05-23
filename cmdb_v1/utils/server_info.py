import paramiko
import subprocess
import shlex

class ssh_connect(object):
    def __init__(self,ip='',port='22',username='',password=''):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password


    def connect_ssh(self,command_line):
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=self.ip,port=self.port, username=self.username, password=self.password)

        # # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command_line)
        result = stdout.read()
        print(result.decode('utf-8'))
        # 关闭连接
        ssh.close()
        return  result
    def get_server_number(self,command_line):
        print(command_line)
        result=self.connect_ssh(command_line)
        print(result)
        # return result

# stdin, stdout, stderr = ssh.exec_command('ipmcget -d macaddr')
# result = stdout.read()
# print(result.decode('utf-8'))
# stdin, stdout, stderr = ssh.exec_command('ipmcget -d ipinfo')
# # # 获取命令结果
# result = stdout.read()
# print(result.decode('utf-8'))
# 关闭连接
# ssh.close()

# ssh.connect(hostname='10.199.104.63', port=22, username='admin', password='1234qwer ')
host_obj=ssh_connect(ip='192.168.50.18',username='root',password='!!feixueliantianshebailu!!=mtime.com')


command_line=shlex.split('ssh %s@%s ip a'%('root',"192.168.51.31"))

print(command_line)
print(host_obj.get_server_number(command_line))

# class Server_Info(object):
#     def __init__(self,ip,conn_methd="ssh"):
#         self.ip=ip
#         self.conn_methd=conn_methd
#
#     def sys_info(self):
#         pass
#     def sn(self):
#         pass
#     def product_name(self):
#         pass
#     def manufacturer(self):
