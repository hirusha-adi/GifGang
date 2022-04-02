import json as j
import requests as r

x = r.get("https://api.redtube.com/?data=redtube.Tags.getTagList&output=json")
y = j.loads(x.content)
with open("output.json", "w", encoding="utf-8") as f:
    j.dump(y, f, indent=4, ensure_ascii=False)
