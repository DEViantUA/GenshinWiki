from GenshinWiki.wiki import WikiAmbr, WikiDb

ambr = WikiAmbr(lang = "en")

avatarInfo = ambr.avatar()
db = WikiDb(lang = "en")

for avatarNames in avatarInfo:
    info = db.avatar(avatarName = avatarInfo[avatarNames]["name"])
    print(f'\n==={info["name"]}===')
    print(f'FullName: {info["fullname"]}')
    print(f'Description: {info["description"]}')
    print(f'Element: {info["element"]}')
