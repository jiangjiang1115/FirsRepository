import re
from datetime import datetime
def extract_numbers_from_string(string):
    numbers = re.findall(r'\d+', string)
    return numbers
def mo_bvt():
    with open('baidu.txt', 'rb') as f:
        data = f.read()
    a1=str(data)

    bytes_text = a1.encode('utf-8')


    # end_index = a1.find('<td>2023-09-06 10:02:32</td>')  379290
    end_index = a1.find('</tbody>')
    end_index2 = a1.find('<td>1241305</td>')

    # a3爬的是时间
    a3=a1[end_index-157:end_index-147]
    print(a3)
    string = a3

    ssss = str(string)
    print(ssss)
    a4 = datetime.now()  # 获取电脑本机时间
    a4z=str(a4)

    if ssss in a4z:
        # a4爬的是bvt号
        a4 = a1[end_index - 270:end_index - 170]
        string = a4
        # print(string)
        numbers = extract_numbers_from_string(string)
        my_list = numbers
        my_tuple = set(my_list)
        my_set = my_tuple
        # my_string就是当天bvt号
        my_string = str(my_set)
        print('bvt已更新',my_string)
        return my_string
    else:
        print('BVT还未更新')
mo_bvt()