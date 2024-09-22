import requests

# 일부 기능 프리미엄으로 인한 제한
# API 키 파라미터 수정 필요
url = 'https://www.alphavantage.co/query?function=MACD&symbol=IBM&interval=daily&series_type=open&apikey=demo'
r = requests.get(url)
data = r.json()

# 메타 데이터 출력
print("🔍 MACD 메타 데이터:")
print("  심볼: IBM")
print("  간격: daily\n")

# MACD 데이터를 리스트에 저장
macd_list = []
macd_data = data['Technical Analysis: MACD']

for date, values in sorted(macd_data.items()):
    macd_entry = {
        "날짜": date,
        "MACD": float(values['MACD']),
        "MACD_Signal": float(values['MACD_Signal']),
        "MACD_Hist": float(values['MACD_Hist'])
    }
    macd_list.append(macd_entry)

# 결과 출력
print("📈 저장된 MACD 값:")
for entry in macd_list:
    print(f"  날짜: {entry['날짜']}, MACD: {entry['MACD']:.4f}, MACD_Signal: {entry['MACD_Signal']:.4f}, MACD_Hist: {entry['MACD_Hist']:.4f}")