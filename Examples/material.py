from GenshinWiki.wiki import WikiAmbr

ambr = WikiAmbr(lang = "en")

avatarInfo = ambr.material()

for materialId in avatarInfo:
    info = ambr.material(id = materialId)
    print(f'\n==={info["name"]}===')
    print(f'Description: {info["description"]}')
    print(f'Type: {info["type"]}')