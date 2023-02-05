import requests
from bs4 import BeautifulSoup
import re



print('Вставь свою ссылку:')
url = input()

search = str(re.search('https\://main\.community/u/', url))
links = search

# https://app.main.community/users/425454/posts?limit=&offset=&type=&tagId=
# https://app.main.community/users/{ID}/posts?limit=&offset=&type=&tagId=
# https://main.community/u/Arooj

# ---------------- Функция получения ID пользователя  ----------------------------


def GetId(url):
    try:
        global ID
        response = requests.get(url)
        bs = BeautifulSoup(response.text, "lxml")
        temp = bs.find_all('script')[1]
        List = str(str(temp).split(' '))
        data_html = re.split("[;,:]", str(List))
        Id_Index = data_html.index('openMobileClosed')
        P_ID = Id_Index + 4
        ID = data_html[P_ID]
    except:
        Exec = ('Вы указали неверную ссылку\n'
              'Попробуйте снова\n'
              'Пример ссылки: https://main.community/u/Ваш Никнейм')


if links != 'None':
    GetId(url)
else:
    print('Вы указали неверную ссылку\n'
              'Попробуйте снова\n'
              'Пример ссылки: https://main.community/u/Ваш Никнейм')