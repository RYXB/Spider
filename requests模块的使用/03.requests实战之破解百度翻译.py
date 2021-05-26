# 需求：破解百度翻译

# ajax的post请求(携带参数)
# 响应数据是一组json数据
import requests
if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'
    # 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'
    }
    #post请求参数处理(同get请求一致)
    data = {
        'kw':'dog'
    }

    response = requests.post(url=post_url,data=data)