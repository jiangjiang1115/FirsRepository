text = '''https://perfeye.console.testplus.cn/case/65c2f4ed1bfb5511e9e57541/report?appKey=yizhiban&query=share
https://perfeye.console.testplus.cn/case/65c31a611bfb5511e9e58203/report?appKey=yizhiban&query=share
'''

lists = text.split('\n')
for i in range(0,len(lists)-1,2):
    ida = lists[i].split('/')[-2]
    idb = lists[i+1].split('/')[-2]
    print(fr"https://perfeye.console.testplus.cn/compare/{ida},{idb}?appKey=yizhiban")
    print()