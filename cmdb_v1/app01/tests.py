import re
#简单的匹配给定的字符串是否是ip地址,下面的例子它不是IPv4的地址，但是它满足正则表达式
if re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", "272.168,1,1"):
    print("IP vaild")
else:
    print("IP invaild")
#精确的匹配给定的字符串是否是IP地址
if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", "223.168.1.1"):
    print("IP vaild")
else:
    print("IP invaild")
#简单的从长文本中提取中提取ip地址

string_ip = "os-version (MRO)    : name: CentOS Linux release 7.1.1503 (Core); uname: 3.10.0-229.el7.x86_64; distro: centos; major: 7; minor: 1"

<<<<<<< HEAD
# from utils.md5 import  md5
# print(md5("123456"))

=======
group = re.search(r'name:(.*?)\(Core\);.+?uname:(.*?);',string_ip,re.M)
if group:
	group.group(1)
	group.group(2)

print(group.group(1),group.group(2))

result = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", string_ip)
if result:
    print(result)
else:
    print("re cannot find ip")
>>>>>>> b1cc5598b900d92fbe397df900ac24f95c099074
