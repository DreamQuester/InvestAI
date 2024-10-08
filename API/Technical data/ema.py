import requests
from datetime import datetime, timedelta

def get_ema_list():
    # API 키 파라미터 수정 필요
    url = 'https://www.alphavantage.co/query?function=EMA&symbol=IBM&interval=daily&time_period=20&series_type=open&apikey=YOUR_API_KEY'
    r = requests.get(url)
    data = r.json()

    # 오늘 날짜와 2년 전 날짜 계산
    today = datetime.now()
    two_years_ago = today - timedelta(days=730)

    # EMA 데이터를 리스트에 저장
    ema_list = []
    ema_data = data['Technical Analysis: EMA']

    for date, values in sorted(ema_data.items()):
        entry_date = datetime.strptime(date, '%Y-%m-%d')
        
        # 날짜가 오늘의 2년 전 날짜보다 이전인지 확인
        if entry_date >= two_years_ago:
            ema_entry = {
                "날짜": date,
                "EMA": float(values['EMA'])
            }
            ema_list.append(ema_entry)

    # 날짜 범위 생성 (2년 전부터 오늘까지)
    date_range = [two_years_ago + timedelta(days=i) for i in range((today - two_years_ago).days + 1)]
    final_ema_list = []

    previous_entry = None

    for date in date_range:
        date_str = date.strftime('%Y-%m-%d')
        found = False
        
        for entry in ema_list:
            if entry['날짜'] == date_str:
                final_ema_list.append(entry)
                previous_entry = entry  # 현재 날짜의 값을 이전 값으로 저장
                found = True
                break
        
        # 날짜가 존재하지 않는 경우 이전 값을 추가
        if not found and previous_entry:
            final_ema_list.append({
                "날짜": date_str,
                "EMA": previous_entry['EMA']
            })
    
    return final_ema_list