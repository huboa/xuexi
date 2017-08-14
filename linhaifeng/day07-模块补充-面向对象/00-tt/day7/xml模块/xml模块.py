import xml.etree.ElementTree as ET
tree=ET.parse('a.xml')
root=tree.getroot()

# for child in root:
#     print('====>',child.tag)
#     for i in child:
#         print(i.tag,i.attrib,i.text)

#查找element元素的三种方式
# years=root.iter('year') #扫描整个xml文档树，找到所有
# for i in years:
#     print(i)

# res1=root.find('country') #谁来调，就从谁下一层开始找,只找一个
# print(res1)
#
# res2=root.findall('country') #谁来调，就从谁下一层开始找,只找一个
# print(res2)


#修改
# years=root.iter('year') #扫描整个xml文档树，找到所有
# for year in years:
#     year.text=str(int(year.text)+1)
#     year.set('updated','yes')
#     year.set('version','1.0')
# tree.write('a.xml')


#删除
# for county in root.iter('country'):
#     # print(county.tag)
#     rank=county.find('rank')
#     if int(rank.text) > 10:
#         county.remove(rank)
# tree.write('a.xml')

#增加节点
# for county in root.iter('country'):
#     e=ET.Element('egon')
#     e.text='hello'
#     e.attrib={'age':'18'}
#     county.append(e)
#
# tree.write('a.xml')