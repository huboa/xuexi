import xml.etree.ElementTree as ET
tree=ET.parse('a.xml')
root=tree.getroot()
for child in root:
    print('====>',child)
    for i in child:
        print(i.tag,i.attrib,i.text)