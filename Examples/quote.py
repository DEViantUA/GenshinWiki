from GenshinWiki.wiki import WikiAmbr

ambr = WikiAmbr()

avatarInfo = ambr.avatar()

for keyId in avatarInfo:
    info = ambr.avatarQuote(avatarId = keyId)
    print(f'\n==={avatarInfo[keyId]["name"]}===')
    for quote in info:
    	print(f'\nНазаание: {info[quote]["title"]}')
    	print(f'\nТекст: {info[quote]["text"]}')
    break
