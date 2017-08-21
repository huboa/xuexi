###打开文件
import xml.etree.ElementTree as ET
tree=ET.parse('a.xml')

root=tree.getroot()
# print(root.tag,root.attrib,root.text)
###每个信息 包含标签，属性，内容三部分
# for child in root:
#     print('1=============>',child.tag,child.attrib)
#     for i in child:
#         print('2=====>',i.tag,i.attrib,i.text) ###看标签，属性，内容值
#
##查找 element tag元素的三种模式 iter,find,findall
# years=root.iter('year') #扫描整个xml 找到所有
# for i in years:
#     print(i)
# res=root.find('country')#只找一层一个
# print(res)
# # #
# res=root.findall('country3')#找一层全部
# print(res)
###修改 set=等于update
# years=root.iter('year')
# for year in years:
#     print(year.text)
#     year.text=str(int(year.text)+1)
#     year.set('updated','yes')
#     year.set('version','2.0')
# tree.write('a.xml')

##删除 remove 节点
# for county in root.iter('country'):
#     # print(county.tag)
#     rank=county.find('rank')
#     # print(rank.text)
#     if int(rank.text) > 2:
#         county.remove(rank)
#
# tree.write('c.xml')

##添加 节点
for county in root.iter('country'):
    e=ET.Element('zsc')
    e.text='hello'
    e.attrib={'age':'18'}
    county.append(e)
tree.write('d.xml')

