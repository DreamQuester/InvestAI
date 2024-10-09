import requests

def get_ticker(company_name):
    api_key = 'your_api_key'  # 여기에 본인의 API 키를 입력하세요.
    
    # API 요청 URL 구성
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company_name}&apikey={api_key}'
    
    # GET 요청
    response = requests.get(url)
    data = response.json()
    
    # 데이터에서 종목 코드 추출
    if 'bestMatches' in data:
        matches = data['bestMatches']
        if matches:
            # 첫 번째 결과에서 ticker 반환
            ticker = matches[0]['1. symbol']
            return ticker
        else:
            return "회사를 찾을 수 없습니다."
    else:
        return "API 호출 오류 발생."