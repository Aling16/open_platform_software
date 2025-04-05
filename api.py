import requests
import csv

def run():
    # 1. 目標 API
    url = "https://holidays-jp.github.io/api/v1/date.json"
    
    # 2. 發送 GET 請求取得 JSON
    response = requests.get(url, timeout=10)
    holidays = response.json()  # 取得回傳的 dict：{日期: 節日名稱}
    
    # 3. 整理為列表（每筆是字典）
    holiday_list = []
    for date, name in holidays.items():
        holiday_list.append({
            "日期": date,
            "節日名稱": name
        })
    
    # 4. 輸出為 CSV 檔案
    with open("jp_holidays.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["日期", "節日名稱"])
        writer.writeheader()
        writer.writerows(holiday_list)
    
    # print("✅ 日本國定假日資料已成功寫入 jp_holidays.csv")

if __name__ == "__main__":
    run()
