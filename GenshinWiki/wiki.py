# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
import requests
from abc import ABCMeta

from .ErrorClass import DGWikiError
from .util import *
from .wiki_api_params import *


class Wiki(metaclass=ABCMeta):
    def __init__(self,lang = "ru-ru"):
        if not isinstance(lang, str):
            raise DGWikiError(5, 'The lang parameter must be a string')
        self.langAmbr, self.lang = langSet(lang)

    #=======ПОЛУЧЕНИЕ ИНФОРМАЦИИ О ОРУЖИЕ=============
    def weapon(self, name = None):
        if name is None:
            return self.send(params = "weapon")
        return self.send(params = isinStr(name,parameter = "name"), categoria = "weapons")

    #=======ПОЛУЧЕНИЕ ИНФОРМАЦИИ О Еде/Ингредиенте=============
    def food(self, name = None):
        if name is None:
            return self.send(params = "food")
        return self.send(params = isinStr(name,parameter = "name"), categoria = "foods")

    #=======ПОЛУЧЕНИЕ ИНФОРМАЦИИ О АРТЕФАКТАХ=============
    def reliquary(self, name = None):
        if name is None:
            return self.send(params = "reliquary")
        return self.send(params = isinStr(name,parameter = "name"), categoria = "artifacts")

    #=======ПОЛУЧЕНИЕ ПЕРСОНАЖЕЙ=============
    def avatar(self, avatarName = None):
        if avatarName is None:
            return self.send(params = "avatar")
        return self.send(params = isinStr(avatarName), categoria = "characters")

class WikiDb(Wiki):
    def send(self,params = None, categoria = None):
        paramsDb["query"] = params
        paramsDb["resultLanguage"] = self.lang
        paramsDb["queryLanguages"] = f"{self.lang},jap"
        r = requests.get(f"{url}/{categoria}", params = paramsDb)
        if r.status_code == 200:
            r = r.json()
            if "result" in r:
                return r["result"]
            else:
                raise DGWikiError(4, f"Check the correctness of the specified parameters.")
        raise DGWikiError(3, f"An error occurred while processing a request to the genshin-db-api")

    #=======ПОЛУЧЕНИЕ ИНФОРМАЦИИ О СОЗВЕЗДИИ=============
    def constellations(self, avatarName = None):
        return self.send(params = isinStr(avatarName), categoria = "constellations")

    #=======ПОЛУЧЕНИЕ ИНФОРМАЦИИ О ТАЛАНТАХ=============
    def talents(self, avatarName = None):
        return self.send(params = isinStr(avatarName), categoria= "talents")

    #=======ПОЛУЧЕНИЕ ПРОТИВНИКОВ=============
    def enemies(self, enemiesName = None):
        return self.send(params = isinStr(enemiesName, parameter = "enemiesName"), categoria = "enemies")
    
class WikiAmbr(Wiki):
    def send(self,params = None):
        r = requests.get(f"{urlAmbr}{self.langAmbr}/{params}?vh=31R3").json()
        if "response" in r:
            if r["response"] == 200:
                if params == "elements":
                    if "info" in r["data"]:
                        return r["data"]
                else:
                    if "items" in r["data"]:
                        return r["data"]["items" ]
                    else:
                        return r["data"]
        raise DGWikiError(2, f"An error occurred while processing a request to the api.ambr")

    #=======ПОЛУЧЕНИЕ ИНФОРМАЦИИ О ЭЛЕМЕНТАХ=============
    def elements(self):
        return self.send(params = "elements")

    #=======ПОЛУЧЕНИЕ ЦИТАТ ПЕРСОНАЖА=============
    def avatarQuote(self, avatarId = 10000069):
        isin(avatarId, parameter = "avatarId")
        return self.send(params = f"avatarFetter/{avatarId}")["quotes"]

    #=======ПОЛУЧЕНИЕ ИСТОРИИ ПЕРСОНАЖА=============
    def avatarStory(self, avatarId = 10000069):
        isin(avatarId, parameter = "avatarId")
        return self.send(params = f"avatarFetter/{avatarId}")["story"]
    
    #=======ПОЛУЧЕНИЕ ИНФОРМАЦИИ О МАТЕРИАЛАХ=============
    def material(self, id = None):
        if id is None:
            return self.send(params = "material")
        else:
            isin(id)
            return self.send(params = f"material/{id}")
