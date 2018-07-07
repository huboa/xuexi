
import ldap3
from  ldap3 import NTLM
"""
   ldapDict=config.objects.get(key="ldap")
            ldapUrl = ldapDict.value
            # ldapUrl="ldap://[图片]10.10.30.206"
            baseDN = "dc=mtime,dc=com"
            searchScope = ldap3.SUBTREE
            # 设置过滤属性，这里只显示cn=test的信息
            searchFilter = "sAMAccountName=" + username
            # 为用户名加上域名
            loginUserName=username
            username = 'mtime\\' + username
            # None表示搜索所有属性，['cn']表示只搜索cn属性
            retrieveAttributes = ["mail","displayName"]
            server=ldap3.Server(ldapUrl,get_info=ldap3.ALL)
            conn=ldap3.Connection(server,username,password,authentication="NTLM",auto_bind=True,receive_timeout=6)
            print 'ldap connect successfully'
        except Exception,error:
            logger.error("{1}--{0}".format(error,"ldap登陆验证错误"))
            return None

"""
server="ldap://10.10.30.206"
baseDN = "dc=mtime,dc=com"
username = "mtime\\shengchong.zhao"
password = "admin2018+"

conn = ldap3.Connection(server, username, password, authentication="NTLM", auto_bind=True, )

# # import class and constants
# from ldap import Server, Connection, ALL
#
#
# # define the server
# s = Server('ldap://10.10.30.206', get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema
#
#
# # define the server
# # s = Server('servername', get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema
#
# # define the connection
# c = Connection(s)  # define an ANONYMOUS connection
#
# # perform the Bind operation
# if not c.bind():
#     print('error in bind', c.result)