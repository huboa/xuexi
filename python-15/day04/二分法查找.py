#data = [1,3,5,7,12,13,14,15,16,18,20]
data = range(1,1024)
def binary_search(datasets,find_num):
    if len(datasets)>0:

        middle_postion = int(len(datasets)/2)

        if datasets[middle_postion] == find_num:
            ##find num
            print('Find num :',datasets[middle_postion])
        elif datasets[middle_postion] > find_num:
            ##data in left side
            print("going to left side",datasets[0:middle_postion],datasets[middle_postion])
            binary_search(datasets[0:middle_postion],find_num)
        else:####data in right side
            print("going to left side",datasets[middle_postion+1],datasets[middle_postion],find_num)
            binary_search(datasets[middle_postion+1:],find_num)
    else:
        print("connot find the num",find_num)
binary_search(data,500) ##赵胜冲 赵新星，杜凯，李旭锋，代亮 田兴 蔡志亮