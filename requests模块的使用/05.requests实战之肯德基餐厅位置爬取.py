# 需求：爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/storelist/index.aspx中指定的地点的餐厅数

import requests
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'
    }

    position = input('enter a position:')
    data = {
        'cname': '',
        'pid': '',
        'keyword':position,
        'pageIndex': '1',
        'pageSize': '10'
    }
    response = requests.post(url=url,data=data, headers=headers)

    page_text = response.text
    fileName = position + '.text'
    fp = open(fileName,'w',encoding='utf-8')
    fp.write(page_text)

    print('over!!!')