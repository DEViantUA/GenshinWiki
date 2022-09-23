from wiki import WikiAmbr, WikiDb


amber =  WikiDb(lang = "ru")
print(amber.avatar(avatarName = "Аяка"))

'''
import requests

url = "https://genshin-db-api.vercel.app/api/"

paramsDb = {"query": "Джинн",
    "matchCategories": "true",
     "dumpResult": "true",
     "resultLanguage": "Russian",
     "queryLanguages": "Russian,jap"
    }

r = requests.get(f"{url}/characters", params = paramsDb)


print(r.json())
'''
