import paramiko

########################华为服务器###########################################
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.199.104.63', port=22, username='admin', password='1234qwer ')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('help')
result = stdout.read()
print(result.decode('utf-8'))
stdin, stdout, stderr = ssh.exec_command('ipmcget -d macaddr')
result = stdout.read()
print(result.decode('utf-8'))
stdin, stdout, stderr = ssh.exec_command('ipmcget -d ipinfo')
# # 获取命令结果
result = stdout.read()
print(result.decode('utf-8'))
# 关闭连接
ssh.close()




########################惠普服务器#############################

# 创建SSH对象
# ssh = paramiko.SSHClient()
# # 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 连接服务器
# ssh.connect(hostname='10.199.104.63', port=22, username='admin', password='')
# # 执行命令
# #stdin, stdout, stderr = ssh.exec_command('show /map1/enetport1/lanendpt1/ipendpt1')
# stdin, stdout, stderr = ssh.exec_command('show ')
#
# # # 获取命令结果
# result = stdout.read()
# print(result.decode('utf-8'))
# # 关闭连接
# ssh.close()


