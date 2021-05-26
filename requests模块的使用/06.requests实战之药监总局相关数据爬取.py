# 需求：爬取药监总局化妆品的相关数据
# http://scxk.nmpa.gov.cn:81/xk/

import requests
import json
if __name__ == '__main__':
    #批量获取不同企业的id值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'
    }
    id_list = [] #存储企业的id
    all_data_list = []
    #参数的封装
    for page in range(1,10):#按照分页获取1-10页的所有
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        json_ids = requests.post(url=url,headers=headers,data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    #获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id':id
        }
        detail_json = requests.post(url=post_url,headers=headers,data=data).json()
        all_data_list.append(detail_json)

    #持久化存储all_data_list
    fp = open('./all_data.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print('over!!!')