from GenshinWiki.wiki import WikiAmbr, WikiDb

ambr = WikiAmbr(lang = "en")

avatarInfo = ambr.avatar()

for avatarNames in avatarInfo:
    info = WikiDb(lang = "en").avatar(avatarName = avatarInfo[avatarNames]["name"])
    print(f'\n==={info["name"]}===')
    print(f'FullName: {info["fullname"]}')
    print(f'Description: {info["description"]}')
    print(f'Element: {info["element"]}')