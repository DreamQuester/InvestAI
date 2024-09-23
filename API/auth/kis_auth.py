import requests
import json
import yaml
from box import Box
import time

class TokenManager:
    def __init__(self):
        self.access_token = None
        self.token_expiry = 0
        self.last_request_time = 0  # 마지막 요청 시간

    def get_access_token(self):
        current_time = time.time()

        # 1분 이내에 요청한 경우 기존 토큰 사용
        if self.access_token and current_time < self.token_expiry:
            return self.access_token
        
        # 1분 이내에 요청한 경우
        if current_time - self.last_request_time < 60:
            print("토큰 요청 제한으로 기존 토큰을 사용합니다.")
            return self.access_token  # 기존 토큰 반환, 오류 발생하지 않음
        
        # 토큰 요청
        with open('API/auth/kis_devlp.yaml', 'r', encoding='UTF8') as f:
            temp = yaml.load(f, Loader=yaml.FullLoader)
            kis_devlp = Box(temp)
        
        APP_KEY = kis_devlp.my_app
        APP_SECRET = kis_devlp.my_sec
        URL_BASE = kis_devlp.prod

        headers = {"content-type": "application/json"}
        body = {
            "grant_type": "client_credentials",
            "appkey": APP_KEY,
            "appsecret": APP_SECRET
        }
        PATH = "oauth2/tokenP"
        URL = f"{URL_BASE}/{PATH}"

        res = requests.post(URL, headers=headers, data=json.dumps(body))

        if res.status_code == 200:
            self.access_token = res.json()["access_token"]
            self.token_expiry = current_time + 24 * 3600  # 24시간 후 만료
            self.last_request_time = current_time  # 마지막 요청 시간 업데이트
            return self.access_token
        else:
            print("토큰 발급 실패, 1분 후 재시도합니다.")
            time.sleep(60)  # 1분 대기
            return self.get_access_token()  # 재귀적으로 다시 시도

token_manager = TokenManager()

if __name__ == "__main__":
    try:
        token = token_manager.get_access_token()
        print(token)
    except Exception as e:
        print(e)