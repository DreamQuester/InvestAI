import requests
import json
import yaml
from kis_auth import token_manager  # a.py에서 TokenManager 가져오기
from box import Box

with open('API\kis_devlp.yaml', 'r', encoding='UTF8') as f:
    temp = yaml.load(f, Loader=yaml.FullLoader)
    kis_devlp = Box(temp)

TOKEN = token_manager.get_access_token()  # 토큰 가져오기
APP_KEY = kis_devlp.my_app
APP_SECRET = kis_devlp.my_sec
URL_BASE = kis_devlp.prod

headers = {
    "content-type": "application/json; charset=utf-8",
    "authorization": "Bearer " + TOKEN,
    "appkey": APP_KEY,
    "appsecret": APP_SECRET,
    "tr_id": "HHDFS76240000",
}

# 거래소코드(EXCD), 종목코드(SYMB) 확인 / 일,주,월 구분(GUBN) 결정
params = {"AUTH": "", "EXCD": "NAS", "SYMB": "TSLA", "GUBN": 1, "BYMD": "", "MODP": 1}
PATH = "/uapi/overseas-price/v1/quotations/dailyprice"
URL = f"{URL_BASE}/{PATH}"

res = requests.get(URL, headers=headers, params=params)

filtered_data = []
# 응답 상태 코드 확인
if res.status_code == 200:
    # JSON 데이터 출력
    data = res.json()["output2"]
    
    for record in data:
        filtered_record = {
            '날짜': record['xymd'],
            '종가': record['clos'],
            '시가': record['open'],
            '고가': record['high'],
            '저가': record['low'],
            '거래량': record['tvol']
        }
        filtered_data.append(filtered_record)
else:
    print(f'Error: {res.status_code}, Message: {res.text}')

for fd in filtered_data:
    print(fd)