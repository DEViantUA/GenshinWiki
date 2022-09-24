from GenshinWiki.wiki import WikiAmbr

ambr = WikiAmbr()

avatarInfo = ambr.avatar()

for quote in avatarInfo:
    info = ambr.avatarQuote(avatarId = quote)
    print(info)
    print(f'\n==={info["name"]}===')
    print(f'Description: {info["description"]}')
    print(f'Type: {info["type"]}')
