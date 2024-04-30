# with open('./key.txt','r',encoding='utf-8') as f:
#     dataKey=f.read()
# print(dataKey.split('	'))
data=[]
with open('./res.csv','r',encoding='utf-8') as f:
    for i in f:
        data.append(i[:-1].split(','))
print(data)