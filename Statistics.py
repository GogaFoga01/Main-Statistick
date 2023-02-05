import requests
from bs4 import BeautifulSoup
import re
import GetID

# ---------------- Вычисление индексов каждого показателя ----------------------------
try:
    All_ID = GetID.ID
    Json_Url = f'https://app.main.community/users/{All_ID}/posts?limit=&offset=&type=&tagId='

    response = requests.get(Json_Url)
    bs = BeautifulSoup(response.text, "lxml")
    tmp = bs.find_all('p')
    listing = list(tmp)
    data_base = re.split("[;,:]", str(listing))

    # ---------------- Вычисление индексов каждого показателя ----------------------------

    PC = data_base.index('\"postCount\"') + 1
    Level = data_base.index('\"userLevel\"') + 1
    BAN = data_base.index('\"isBlocked\"') + 1

    Post_count = data_base[PC]
    UserLevel = data_base[Level]

    # ---------------- Показатель блокировки пользователя  ----------------------------

    Blocked = data_base[BAN]
    Blocked_RU = ''
    if Blocked == 'false':
        Blocked_RU = 'Блокировки нет'
    else:
        Blocked_RU = 'Блокировка есть'

    # ---------------- Вычисление индексов каждого показателя ----------------------------

    a1 = f'Количество постов: {Post_count}'
    a2 = f'Уровень пользователя: {UserLevel}'
    a3 = f'Блокировка пользователя: {Blocked_RU}'

    print(f'{a1}\n{a2}\n{a3}')
except:
    pass