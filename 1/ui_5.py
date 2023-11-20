import requests
import hashlib
import random
import json

def translate(text, from_lang, to_lang):
    app_id = '20231003001835383'  # 替换为你的App ID
    secret_key = 'IKV8aSo3B7K_IRYZOzca'  # 替换为你的Secret Key

    # 生成随机数
    salt = random.randint(32768, 65536)

    # 计算签名
    sign = app_id + text + str(salt) + secret_key
    sign_md5 = hashlib.md5(sign.encode()).hexdigest()

    # 发起请求
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate' ##如果报错应该是没开通服务
    params = {
        'q': text,
        'from': from_lang,
        'to': to_lang,
        'appid': app_id,
        'salt': salt,
        'sign': sign_md5
    }
    # 发送GET请求
    response = requests.get(url, params=params)
    # 解析响应数据
    result = json.loads(response.text)
    try:
        translation = result['trans_result'][0]['dst']
        return translation
    except KeyError:
        # 处理解析错误
        print("Failed to parse response!")
        print(response.text)
        return None


# 调用翻译函数
text = input("请输入要翻译的文本：") #把text换成输出的英文
translated_text = translate(text, 'en', 'zh')
print(translated_text)
