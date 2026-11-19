"""即時美元兌台幣 (USD/TWD) 匯率查詢技能"""
import urllib.request, json

def run(query: str) -> str:
    url = "https://open.er-api.com/v6/latest/USD"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=6) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    twd = data["rates"]["TWD"]
    return f"💱 **即時匯率查詢**\n1 美元 (USD) = **{twd:.3f}** 新台幣 (TWD)"
