import requests

# API 키 파라미터 수정 필요
url = 'https://www.alphavantage.co/query?function=EMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo'
r = requests.get(url)
data = r.json()

# 메타 데이터 출력
meta_data = data['Meta Data']
print("🔍 EMA 메타 데이터:")
print(f"  심볼: {meta_data['1: Symbol']}")
print(f"  지표: {meta_data['2: Indicator']}")
print(f"  가장 최근 갱신: {meta_data['3: Last Refreshed']}")
print(f"  간격: {meta_data['4: Interval']}")
print(f"  기간: {meta_data['5: Time Period']}")
print(f"  시리즈 유형: {meta_data['6: Series Type']}\n")

# EMA 데이터를 리스트에 저장
ema_list = []
ema_data = data['Technical Analysis: EMA']

for date, values in sorted(ema_data.items()):
    ema_entry = {
        "날짜": date,
        "EMA": float(values['EMA'])
    }
    ema_list.append(ema_entry)

# 결과 출력
print("📈 저장된 EMA 값:")
for entry in ema_list:
    print(f"  날짜: {entry['날짜']}, EMA: {entry['EMA']:.4f}")