import requests
from bs4 import BeautifulSoup
import json
import csv

# 目標網址（台灣銀行匯率）
url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
headers = {"User-Agent": "Mozilla/5.0"}

# 發送請求
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 抓取所有幣別的資料列
rows = soup.select("table.table tbody tr")

data = []

for row in rows:
    # 幣別（含幣名與代碼）
    currency_info = row.select_one("div.visible-phone.print_hide").get_text(strip=True)
    currency_name, currency_code = currency_info.split(" ")

    # 匯率資料
    cash_buy = row.select("td")[1].text.strip()
    cash_sell = row.select("td")[2].text.strip()
    spot_buy = row.select("td")[3].text.strip()
    spot_sell = row.select("td")[4].text.strip()

    data.append({
        "幣別名稱": currency_name,
        "幣別代碼": currency_code,
        "現金買入": cash_buy,
        "現金賣出": cash_sell,
        "即期買入": spot_buy,
        "即期賣出": spot_sell
    })

# 輸出為 JSON
with open("static.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 輸出為 CSV
with open("static.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["幣別名稱", "幣別代碼", "現金買入", "現金賣出", "即期買入", "即期賣出"])
    writer.writeheader()
    writer.writerows(data)

print("✅ 匯率資料已成功輸出到 static.json 和 static.csv")

