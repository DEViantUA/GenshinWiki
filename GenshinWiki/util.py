# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
__all__ = ["langSet", 
    "isin", 
    "isinStr"
    ]
    
from ErrorClass import DGError

langSetting = "ru-ru, ru, en-en, en"

def langSet(lang):
    if lang == "ru-ru" or lang == "ru":
        return "ru", "Russian"
    elif lang == "en-en" or lang == "en":
        return "en", "English"
    else:
        raise DGError(1, f"Using an unsupported lang type, use the following values: {langSetting}")

def isin(id, parameter = "id"):
    if isinstance(id, str):
        try:
            id = int(id)
        except ValueError:
            pass

    if not isinstance(id, int):
        raise DGError(6, f'The id {parameter} must be a number')

    return id

def isinStr(name, parameter = "avatarName"):
    if not isinstance(name, str):
        raise DGError(7, f'The {parameter} parameter must be a string')
    
    return name