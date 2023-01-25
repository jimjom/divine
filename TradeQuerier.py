import json
import requests
import os
from dotenv import load_dotenv

class TradeQuerier:

    def __init__(self):
      load_dotenv()
      self.POESESSID = os.getenv('POE_SESSION_ID')

    def queryTrade(self, query):
      s = requests.session()

      s.cookies.set("_ga", "GA1.2.1716915880.1629409194")
      s.cookies.set("_gid", "GA1.2.92074025.1673491042")
      s.cookies.set("POESESSID", self.POESESSID)
      s.cookies.set("cf_clearance", "BG6MtZG73rTNDCHB4CaJ2wCt5RlkjQSd7WY4cvyg_mA")
      s.cookies.set("stored_data", "1")

      url = "https://www.pathofexile.com/api/trade/search/Sanctum"

      header = {
          "accept": "*/*",
          "accept-language": "en-US,en;q=0.9",
          "content-type": "application/json",
          "path": "api/trade/search/Sanctum",
          "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
          "sec-ch-ua-mobile": "?0",
          "sec-ch-ua-platform": "\"Windows\"",
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76",
          "x-requested-with": "XMLHttpRequest",
          "Referer": "https://www.pathofexile.com/trade/search/Sanctum",
          "Referrer-Policy": "strict-origin-when-cross-origin"
        }

      s.headers.update(header)

      data = json.loads(query)

      r = s.post(url, headers=header, json=data, verify=True)

      s = requests.session()

      output = r.json()

      for i in output['result']:
        url=f"https://www.pathofexile.com/api/trade/fetch/{i}?query={output['id']}"
        break

      r2 = s.get(url, headers=header, verify=True)

      output = r2.json()

      print(json.dumps(output,indent=2))