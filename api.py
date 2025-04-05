import requests
import csv

# 1. API 來源
url = "https://restcountries.com/v3.1/all"

# 2. 發送 GET 請求取得 JSON 資料
response = requests.get(url)

# 3. 將 JSON 資料轉換成 Python list
countries = response.json()

# 4. 建立一個列表來儲存整理後的資料
data_list = []

# 5. 逐一處理每個國家的資訊
for country in countries:
    name = country.get("name", {}).get("common", "N/A")  # 國家名稱
    capital = country.get("capital", ["N/A"])[0]         # 首都（有些國家無首都）
    population = country.get("population", 0)            # 人口數
    area = country.get("area", 0)                        # 面積（平方公里）
    timezones = ", ".join(country.get("timezones", [])) # 時區（多個用逗號分隔）
    flag = country.get("flags", {}).get("png", "N/A")    # 國旗圖片（PNG 格式）

    # 將一筆國家資料加入清單中
    data_list.append({
        "國家": name,
        "首都": capital,
        "人口": population,
        "面積(km²)": area,
        "時區": timezones,
        "國旗圖片": flag
    })

# 6. 寫入 CSV 檔案
with open("api.csv", "w", newline="", encoding="utf-8-sig") as f:
    fieldnames = ["國家", "首都", "人口", "面積(km²)", "時區", "國旗圖片"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_list)

print("✅ 已成功寫入 countries.csv")
