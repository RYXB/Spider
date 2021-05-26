# 需求：破解百度翻译

# ajax的post请求(携带参数)
# 响应数据是一组json数据
import requests
import json
if __name__ == '__main__':
    #1.指定URL
    post_url = 'https://fanyi.baidu.com/sug'
    #2.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'
    }
    #3.post请求参数处理(同get请求一致)
    word = input('enter a word:')
    data = {
        'kw':word
    }
    #4.请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    #5.获取响应数据:json()方法返回的是Obj(如果确认响应数据是json类型的，才可以使用json())
    dic_obj = response.json()

    #持久化存储
    fileName = word + '.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)

    print('over!!!')
