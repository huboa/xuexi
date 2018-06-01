import paramiko
import subprocess
import shlex


class connect_ssh_tb(object):

    def __init__(self,ip='',port='22',username='',password=''):
        '''
        用于使用跳板机获取硬件信息
        :param ip:  跳扳机ip
        :param port:  跳板端口
        :param username: 跳板机用户
        :param password:密码
        '''
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password


    ###连接跳板机
    def ssh_connect(self,command_line):
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=self.ip,port=self.port ,username=self.username, password=self.password)

        # # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command_line)
        result = stdout.readlines()


        # 关闭连接
        ssh.close()
        return  result

    ###获取执行命令
    def command_line(self,user,host,command):
        remote_command=('ssh %s@%s %s' % (user,host,command))
        result=self.ssh_connect(remote_command)
        return result
    ###执行dmidecode
    def get_sys_info(self,user,host):
        data_list = self.command_line(user=user,host=host,command="dmidecode")
        list_info =self.parse_data(data_list)
        dict_info =self.get_dmi(list_info)
        return  dict_info
    #加工decode 获取系统信息
    def parse_data(self,data_list):
        tag = False
        lines = []
        for line in data_list:
            if line.startswith('System Information'): # 如果遍历到System Information 写入新列表
                tag = True
                continue
            if tag:
                if not line.strip():  # 如果遍历到空行，即新的一段信息前，则可以退出循环了
                    break
                else:
                    lines.append(line)
        return lines

    ###将信息转换成字典并返回
    def get_dmi(self,list_info):
        dmi_dic = {}
        dmi = {}
        dmi_dic = dict([i.strip().split(":") for i in list_info])
        for k, v in dmi_dic.items():
            dmi_dic[k] = v.strip()

        dmi['Manufacturer'] = dmi_dic['Manufacturer']
        dmi['Product Name'] = dmi_dic['Product Name']
        dmi['Serial Number'] = dmi_dic['Serial Number']

        return dmi



# ####使用说明创建跳扳机连接实例
# # ssh.connect(hostname='10.199.104.63', port=22, username='admin', password='1234qwer ')
# connect_obj = connect_ssh_tb(ip='192.168.50.18',username='root',password='!!feixueliantianshebailu!!=mtime.com')
#
# ####获取信息
# # print(connect_obj.command_line(user='root',host='192.168.51.31',command='hostname'))
# sys_info_dict = connect_obj.get_sys_info(user='root',host='192.168.50.101',)
# print(sys_info_dict['Manufacturer'])
# print(sys_info_dict['Product Name'])
# print(sys_info_dict['Serial Number'])
