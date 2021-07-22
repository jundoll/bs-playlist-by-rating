# load modules
from urllib.request import Request, urlopen
import pandas as pd
import json

# set url info
user_agent = "bs-playlist-by-ranking/1.0.0"
url = "https://cdn.wes.cloud/beatstar/bssb/v2-all.json"

# load json
req = Request(url, headers={'User-Agent': user_agent})
response = urlopen(req).read()
data = json.loads(response)
df = pd.DataFrame.from_dict(data, orient="index")

df.to_csv("dist/all.csv", index=False)
