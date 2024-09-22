import requests

# API 키 파라미터 수정 필요
url = 'https://www.alphavantage.co/query?function=BBANDS&symbol=IBM&interval=weekly&time_period=5&series_type=close&nbdevup=3&nbdevdn=3&apikey=demo'
r = requests.get(url)
data = r.json()

# 메타 데이터 출력
meta_data = data['Meta Data']
print("🔍 메타 데이터:")
print(f"  심볼: {meta_data['1: Symbol']}")
print(f"  지표: {meta_data['2: Indicator']}")
print(f"  가장 최근 갱신: {meta_data['3: Last Refreshed']}")
print(f"  간격: {meta_data['4: Interval']}")
print(f"  기간: {meta_data['5: Time Period']}")
print(f"  상한선 표준 편차 배수: {meta_data['6.1: Deviation multiplier for upper band']}")
print(f"  하한선 표준 편차 배수: {meta_data['6.2: Deviation multiplier for lower band']}")
print(f"  시리즈 유형: {meta_data['7: Series Type']}\n")

# 데이터 리스트에 저장
bbands_list = []

bbands_data = data['Technical Analysis: BBANDS']
for date, values in sorted(bbands_data.items()):
    bband_entry = {
        "날짜": date,
        "상한선": values['Real Upper Band'],
        "중간선": values['Real Middle Band'],
        "하한선": values['Real Lower Band']
    }
    bbands_list.append(bband_entry)

# 리스트 출력
print("📈 볼린저 밴드 결과:")
for entry in bbands_list:
    print(f"  날짜: {entry['날짜']}")
    print(f"    상한선: {entry['상한선']}")
    print(f"    중간선: {entry['중간선']}")
    print(f"    하한선: {entry['하한선']}")
    print()