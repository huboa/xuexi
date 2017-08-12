import xml.etree.ElementTree as ET
tree=ET.parse('a.xml')
# root=tree.getroot()
# for child in root:
#     print('====>',child)
#     for i in child:
#         print(i.tag,i.attrib,i.text)
#
# ##查找 element 元素的三种模式
# years=root.iter('year') #扫描整个xml 找到所有
# for i in years:
#     print(i)
# res=root.find('year')#谁来调，就从下一层开始,只找一个
# print(res)
#
# res=root.findall('country')#谁来调，就从下一层开始,只找一个
# print(res)
#
# for year in years:
#     year.

