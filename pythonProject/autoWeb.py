from DrissionPage import ChromiumPage
#解决多个报告查找单个元素的问题
#获取链接
if __name__ == '__main__':
    page = ChromiumPage() # addr_or_opts=co
    page.get("https://perfeye.testplus.cn/case/65a0f95302d8b69cd7972b8b/report?appKey=JX3")
    #   0   6    10    13
    # mov = page.eles('.ant-row',timeout=10)#.eles('.ant-col',timeout=0)
    # print(mov)

    caseName=page.eles(".ant-descriptions-view")[1].eles(".ant-descriptions-item-content")[0].text
    print(caseName)
    CPU=page.ele('#CPU').eles('.ant-col')[6].text
    print(CPU,len(CPU))


    # my_list = [
    #     FPS[0].ele('.ant-statistic-content').text,
    #     FPS[1].ele('.ant-statistic-content').text,
    #     FPS[2].ele('.ant-statistic-content').text,
    #     FPS[3].ele('.ant-statistic-content').text,
    #     FPS[4].ele('.ant-statistic-content').text,
    #     CPU[-2].ele('.ant-statistic-content').text,
    #     Memory[1].ele('.ant-statistic-content').text,
    #     Memory[2].ele('.ant-statistic-content').text,
    #     GPU[0].ele('.ant-statistic-content').text
    # ]

    # df = pd.DataFrame([my_list],
    #                   columns=['AvgFPS', 'Jank(次/10min)', 'BigJank(次/10min)', 'AvgAPP(%)', 'PeakMemory(MB)',
    #                            'AvgApp(%)', 'AvgMemory(MB)', 'PeakMemory(MB)', 'Avg(GPUUsage)[%]'])
    #
    # df.to_excel('my_list.xlsx', index=False)