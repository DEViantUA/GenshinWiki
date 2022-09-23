
<p align="center">
 <img src="img/GenshinWikiBanner.png" alt="Баннер"/>
</p>

# GenshinWiki
 Простой пакет Python для облегчения работы с API: [Project Ambert](https://ambr.top/ru) и [genshin-db](https://github.com/theBowja/genshin-db)
 

## Установка:
~~~python
git clone https://github.com/DEViantUA/GenshinWiki
~~~

## Использование:

GenshinWiki может обращаться к двум API, для этого используються классы:
* WikiAmbr - В основном используеться, для получения названий и ID предметов, что бы в дальнейшем использовать их в WikiDb.
* WikiDb - Используеться для получение полной информации о предметах по их имени, которые можно получить в WikiAmbr
* Каждый из классов высше поддерживает два языка: "ru" - русский язык и "en" - Английский язык (ru - по умолчанию)

Пример: 
~~~python
WikiAmbr(lang ="en").elements()
~~~





## Методы пакета:
____
| Класс | Метод | Параметры | Описание |
|-----| ----- | -------- | -------- |
|WikiAmbr| avatarQuote | avatarId | Вернет список цитат персонажа|
|WikiAmbr| avatarStory | avatarId | Вернет список истории персонажа|
|WikiAmbr| material | id | Вернет информацию о материале|
|WikiAmbr| elements | Отсутсвуют | Вернет список элементальных реакций и их описание|
|WikiAmbr| material | Отсутсвует | Вернет список материалов|
|WikiAmbr| food | Отсутсвует | Вернет список еды|
|WikiAmbr| weapon | Отсутсвует | Вернет список Оружия|
|WikiAmbr| reliquary | Отсутсвует | Вернет список Артефактов|
|WikiAmbr| avatar | Отсутсвует | Вернет список Персонажей|
|-----| ----- | -------- | -------- |
|WikiDb| constellations | avatarName | Получить Информацию о созвездии персонажа|
|WikiDb| talents | avatarName | Получить Информацию о талантах персонажа|
|WikiDb| avatar | avatarName | Получить Информацию о Артефакте |
|WikiDb| enemies | enemiesName | Получить Информацию о Врагах |
|WikiDb| weapon | name | Получить Информацию о оружие |
|WikiDb| food | name | Получить Информацию о Блюдах |
|WikiDb| reliquary | name | Получить Информацию о Артефакте |

### Описание параметров:
* avatarId - ID Персонажей
* avatarName - Имя Персонажа/Оружия
* enemiesName - Имя Врага
* name - Название Предмета/Еды/Артефакта
* id - ID материала
* Отсутсвует - Не нужно ничего передавать.


# Пример использования:

~~~python
from GenshinWiki.wiki import WikiAmbr

ambr = WikiAmbr(lang = "en")

avatarInfo = ambr.material()

for materialId in avatarInfo:
    info = ambr.material(id = materialId)
    print(f'\n==={info["name"]}===')
    print(f'Description: {info["description"]}')
    print(f'Type: {info["type"]}')
~~~

Больше тут: [Перейти к примерам](https://github.com/DEViantUA/GenshinWiki/tree/main/Examples).
