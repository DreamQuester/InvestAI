import requests
from datetime import datetime, timedelta

def get_bbands_list():
    # API 키 파라미터 수정 필요
    url = 'https://www.alphavantage.co/query?function=BBANDS&symbol=IBM&interval=daily&time_period=20&series_type=close&nbdevup=2&nbdevdn=2&apikey=YOUR_API_KEY'
    r = requests.get(url)
    data = r.json()

    # 오늘 날짜와 2년 전 날짜 계산
    today = datetime.now()
    two_years_ago = today - timedelta(days=730)

    # 데이터 리스트에 저장
    bbands_list = []

    bbands_data = data['Technical Analysis: BBANDS']
    for date, values in sorted(bbands_data.items()):
        entry_date = datetime.strptime(date, '%Y-%m-%d')
        
        # 날짜가 오늘의 2년 전 날짜보다 이전인지 확인
        if entry_date >= two_years_ago:
            bband_entry = {
                "날짜": date,
                "상한선": float(values['Real Upper Band']),
                "중간선": float(values['Real Middle Band']),
                "하한선": float(values['Real Lower Band'])
            }
            bbands_list.append(bband_entry)

    # 날짜 범위 생성 (2년 전부터 오늘까지)
    date_range = [two_years_ago + timedelta(days=i) for i in range((today - two_years_ago).days + 1)]
    final_bbands_list = []

    previous_entry = None

    for date in date_range:
        date_str = date.strftime('%Y-%m-%d')
        found = False
        
        for entry in bbands_list:
            if entry['날짜'] == date_str:
                final_bbands_list.append(entry)
                previous_entry = entry  # 현재 날짜의 값을 이전 값으로 저장
                found = True
                break
        
        # 날짜가 존재하지 않는 경우 이전 값을 추가
        if not found and previous_entry:
            final_bbands_list.append({
                "날짜": date_str,
                "상한선": previous_entry['상한선'],
                "중간선": previous_entry['중간선'],
                "하한선": previous_entry['하한선']
            })

    return final_bbands_list