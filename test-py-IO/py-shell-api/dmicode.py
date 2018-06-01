#!/usr/bin/env  python

"""
file_name: dmi_t.py
"""

from subprocess import Popen, PIPE

def  getData():
    p = Popen(['dmidecode'], stdout=PIPE, stderr=PIPE)
    data = p.stdout.read().split()
    return data

def  parseData(data):
    line_in = False
    lines = []
    for line  in data:
        if line.starswith('System Information'):
            line_in = True
            continue
        if line_in:
            if not line.strip():  #如果遍历到空行，即新的一段信息前，则可以退出循环了
                break
            else:
                lines.append(line)

def  getDmi(lines):
    dmi_dic = {}
    dmi = {}
    dmi_dic = dict([i.strip().split(":")  for i in lines ])
    for k, v in dmi_dic.items():
        dmi_dic[k] = v.strip()

    dmi['Manufacturer'] = dmi_dic['Manufacturer']
    dmi['Product Name'] = dmi_dic['Product Name']
    dmi['Serial Number'] = dmi_dic['Serial Number']

    return dmi

if  __name__ == '__main__':
    data   =  getData()
    lines = parseData(data)
    print getDmi(lines)
